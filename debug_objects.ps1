param(
    [string]$ghxPath = "D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v11.ghx"
)

function Backup-File {
    param([string]$Path)
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $backup = "$Path.$timestamp.bak"
    Copy-Item -Path $Path -Destination $backup
    Write-Host "Backup created: $backup"
}

# Load GH_IO.dll
$ghioPath = "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
if (-Not (Test-Path $ghioPath)) {
    Write-Error "GH_IO.dll not found at $ghioPath"
    exit 1
}
Add-Type -Path $ghioPath

# Load the GHX document
try {
    $doc = New-Object GH_IO.Serialization.GH_Archive
    $doc.ReadFromFile($ghxPath)
    Write-Host "Successfully loaded GHX file"
} catch {
    Write-Error "Failed to load GHX document: $_"
    exit 1
}

# List all objects by NickName
$objects = $doc.Objects
Write-Host ("Found {0} objects:" -f $objects.Count)
if($objects.Count -gt 0) {
    for($i=0; $i -lt $objects.Count; $i++) {
        $obj = $objects[$i]
        Write-Host ("  [{0}] NickName: {1}, TypeName: {2}" -f $i, $obj.NickName, $obj.TypeName)
    }
} else {
    Write-Host "No objects found"
}