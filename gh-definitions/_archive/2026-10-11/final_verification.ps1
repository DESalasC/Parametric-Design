# Final verification script using correct GH_Archive type
$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'

try {
    Add-Type -Path $ghioPath
} catch {
    "Failed to load GH_IO.dll"
    exit 1
}

$ghxPath = 'D:\Work\PROJECTS\Dise*\gh-definitions\F1_CONTEXTO_v11.ghx'

if(-not (Test-Path $ghxPath)) {
    "File not found with wildcard"
    exit 1
}

$resolvedPath = Resolve-Path $ghxPath

try {
    $asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
           Where-Object { $_.FullName -like 'GH_IO,*' } |
           Select-Object -First 1

    $type = $asm.GetType('Grasshopper.IO.Serialization.GH_Archive')
    if(-not $type) {
        "Could not find Grasshopper.IO.Serialization.GH_Archive type"
        exit 1
    }

    $doc = $type.GetConstructor(@()).Invoke(@($null))
    $doc.Read($resolvedPath.Path)

    $objects = $doc.GetObjectIterator()
    $v02Count = 0
    $v04Count = 0
    $componentCount = 0

    while($objects.MoveNext()) {
        $obj = $objects.Current
        if($obj.Type -eq 'Component' -and $obj.NickName -like '*F1_ETAPA1_CONTEXTO*') {
            $componentCount++
            $code = $obj.CodeInput
            $v02Refs = ($code -split 'v02' | Measure-Object).Count - 1
            $v04Refs = ($code -split 'v04' | Measure-Object).Count - 1
            if($v02Refs -gt 0) { $v02Count++ }
            if($v04Refs -gt 0) { $v04Count++ }
        }
    }

    "SUMMARY: Found {0} F1_ETAPA1_CONTEXTO components" -f $componentCount
    "SUMMARY: v02 references in {0} components, v04 references in {1} components" -f $v02Count, $v04Count

    if($v02Count -eq 0 -and $v04Count -gt 0) {
        "SUCCESS: All F1_ETAPA1_CONTEXTO components have been updated to v04!"
        exit 0
    } elseif($v02Count -gt 0) {
        "WARNING: Found {0} components still referencing v02" -f $v02Count
        exit 1
    } elseif($v04Count -eq 0) {
        "ERROR: No components found with v04 references"
        exit 1
    } else {
        "INFO: Mixed v02/v04 references found"
        exit 1
    }
} catch {
    "Error: $($_.Exception.Message)"
    exit 1
} finally {
    if($doc) { $doc.Dispose() }
}