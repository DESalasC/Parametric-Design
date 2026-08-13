# Fix-Ghx.ps1
# Converts simplified GHX format to proper GH_IO format
param(
    [string]$InputPath = "D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v07.ghx",
    [string]$OutputPath = ""
)

if (-not $OutputPath) {
    $OutputPath = $InputPath -replace '\.ghx$', '_fixed.ghx'
}

$ErrorActionPreference = "Stop"

Write-Host "Loading GH_IO..." -ForegroundColor Cyan
Add-Type -Path "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"

Write-Host "Reading simplified GHX: $InputPath"
[xml]$doc = Get-Content $InputPath -Encoding UTF8

$archiveRoot = $doc.Archive
$docObj = $archiveRoot.Object

if (-not $docObj) {
    Write-Error "No <Object> under <Archive>"
    exit 1
}

$docName = if ($docObj.name) { $docObj.name } else { "Unknown" }

Write-Host "Creating GH_Archive..."

# Create archive using reflection
$asm = [System.Reflection.Assembly]::LoadFrom("C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll")
$archiveType = $asm.GetType("GH_IO.Serialization.GH_Archive")
$chunkType = $asm.GetType("GH_IO.Serialization.GH_Chunk")

$archive = [Activator]::CreateInstance($archiveType)

# Helper functions
function Set-ChunkString($chunk, $name, $value) {
    $chunk.GetType().GetMethod("SetString").Invoke($chunk, @($name, $value))
}

function Set-ChunkBoolean($chunk, $name, $value) {
    $chunk.GetType().GetMethod("SetBoolean").Invoke($chunk, @($name, $value))
}

function Set-ChunkInt32($chunk, $name, $value) {
    $chunk.GetType().GetMethod("SetInt32").Invoke($chunk, @($name, $value))
}

function Set-ChunkGuid($chunk, $name, $guid) {
    $chunk.GetType().GetMethod("SetGuid").Invoke($chunk, @($name, $guid))
}

function Set-ChunkGuidIndex($chunk, $name, $index, $guid) {
    $chunk.GetType().GetMethod("SetGuid", @([string], [int], [Guid])).Invoke($chunk, @($name, $index, $guid))
}

function New-Chunk($parent, $name) {
    $parent.GetType().GetMethod("CreateChunk", @([string])).Invoke($parent, @($name))
}

function New-ChunkIndex($parent, $name, $index) {
    $parent.GetType().GetMethod("CreateChunk", @([string], [int])).Invoke($parent, @($name, $index))
}

function New-GuidFromString($input) {
    $md5 = [System.Security.Cryptography.MD5]::Create()
    $bytes = $md5.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($input))
    $bytes[6] = ($bytes[6] -band 0x0F) -bor 0x30
    $bytes[8] = ($bytes[8] -band 0x3F) -bor 0x80
    return [Guid]::new($bytes)
}

# Create Definition chunk
$defChunk = New-Chunk $archive "Definition"

# DefinitionProperties
$defProps = New-Chunk $defChunk "DefinitionProperties"
$defName = if ($docObj.Name) { $docObj.Name } else { $docName }
Set-ChunkString $defProps "Name" $defName
$defDesc = if ($docObj.Description) { $docObj.Description } else { "" }
Set-ChunkString $defProps "Description" $defDesc

# DefinitionObjects
$objectsNode = $docObj.Objects
if ($objectsNode -and $objectsNode.Object) {
    $defObjs = New-Chunk $defChunk "DefinitionObjects"
    $objList = @($objectsNode.Object)
    Set-ChunkInt32 $defObjs "ObjectCount" $objList.Count

    for ($i = 0; $i -lt $objList.Count; $i++) {
        $obj = $objList[$i]
        Write-Host "  Processing object $($i+1)/$($objList.Count): $($obj.name)" 
        
        $objChunk = New-ChunkIndex $defObjs "Object" $i
        
        # Object basic info
        $objName = if ($obj.Name) { $obj.Name } elseif ($obj.name) { $obj.name } else { "Object" }
        $objId = if ($obj.ID) { $obj.ID } else { "" }
        $objNick = if ($obj.Nickname) { $obj.Nickname } else { $objName }
        $objDesc = if ($obj.Description) { $obj.Description } else { "" }
        
        $objGuid = if ($objId) { New-GuidFromString $objId } else { [Guid]::NewGuid() }
        
        Set-ChunkGuid $objChunk "GUID" $objGuid
        Set-ChunkString $objChunk "Name" $objName
        Set-ChunkString $objChunk "NickName" $objNick
        Set-ChunkString $objChunk "Description" $objDesc
        
        # Container
        $container = New-Chunk $objChunk "Container"
        
        # Transfer extra leaf elements
        foreach ($child in $obj.ChildNodes) {
            if ($child.NodeType -ne [System.Xml.XmlNodeType]::Element) { continue }
            $tag = $child.Name
            $text = $child.InnerText.Trim()
            if (-not $text) { continue }
            
            if ($tag -in @('Name','ID','Nickname','Description','Inputs','Outputs',
                           'OptionalParams','Code','Attributes','Wires')) { continue }
            
            Set-ChunkString $container $tag $text
        }
        
        # Python code
        if ($obj.Code) {
            $codeText = $obj.Code.InnerText.Trim()
            if ($codeText) {
                Set-ChunkString $container "CodeInput" $codeText
            }
        }
        
        # ParameterData with Inputs/Outputs
        $inputsNode = $obj.Inputs
        $outputsNode = $obj.Outputs
        
        $inputCount = 0
        $outputCount = 0
        $inputElements = @()
        $outputElements = @()
        
        if ($inputsNode -and $inputsNode.Input) {
            $inputElements = @($inputsNode.Input)
            $inputCount = $inputElements.Count
        }
        
        if ($outputsNode -and $outputsNode.Output) {
            $outputElements = @($outputsNode.Output)
            $outputCount = $outputElements.Count
        }
        
        if ($inputCount -gt 0 -or $outputCount -gt 0) {
            $paramData = New-Chunk $container "ParameterData"
            
            for ($j = 0; $j -lt $inputCount; $j++) {
                $inp = $inputElements[$j]
                $inpName = if ($inp.name) { $inp.name } else { "Input$j" }
                $inpId = New-GuidFromString "$objName`_$inpName"
                
                Set-ChunkInt32 $paramData "InputCount" $inputCount
                Set-ChunkGuidIndex $paramData "InputId" $j $inpId
                
                $inpParam = New-ChunkIndex $paramData "InputParam" $j
                Set-ChunkString $inpParam "Name" $inpName
                Set-ChunkString $inpParam "NickName" $inpName
                Set-ChunkString $inpParam "Description" "Script input $inpName."
                Set-ChunkBoolean $inpParam "Optional" $true
                Set-ChunkBoolean $inpParam "AllowTreeAccess" $true
                Set-ChunkBoolean $inpParam "ShowTypeHints" $true
                Set-ChunkInt32 $inpParam "ScriptParamAccess" 0
                Set-ChunkInt32 $inpParam "SourceCount" 0
                Set-ChunkGuid $inpParam "InstanceGuid" $inpId
                Set-ChunkGuid $inpParam "TypeHintID" ([Guid]"d60527f5-b5af-4ef6-8970-5f96fe412559")
            }
            
            for ($j = 0; $j -lt $outputCount; $j++) {
                $outp = $outputElements[$j]
                $outName = if ($outp.name) { $outp.name } else { "Output$j" }
                $outNick = if ($outp.nickname) { $outp.nickname } else { $outName }
                $outId = New-GuidFromString "$objName`_out_$outName"
                
                Set-ChunkInt32 $paramData "OutputCount" $outputCount
                Set-ChunkGuidIndex $paramData "OutputId" $j $outId
                
                $outParam = New-ChunkIndex $paramData "OutputParam" $j
                Set-ChunkString $outParam "Name" $outName
                Set-ChunkString $outParam "NickName" $outNick
                Set-ChunkGuid $outParam "InstanceGuid" $outId
            }
        }
    }
}

Write-Host "Writing GH_IO format: $OutputPath"
$writeMethod = $archiveType.GetMethod("WriteToFile")
$result = $writeMethod.Invoke($archive, @($OutputPath, $false, $false, $null))

if ($result) {
    Write-Host "SUCCESS: File written to $OutputPath" -ForegroundColor Green
} else {
    Write-Host "FAILED to write file" -ForegroundColor Red
}
