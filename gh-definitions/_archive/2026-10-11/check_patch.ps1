# Load GH_IO.dll
$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Write-Host ("Loading GH_IO.dll from: {0}" -f $ghioPath)
try {
    Add-Type -Path $ghioPath
    Write-Host "GH_IO.dll loaded successfully."
} catch {
    Write-Host "Failed to load GH_IO.dll: $_" -ForegroundColor Red
    exit 1
}

# Use wildcard to avoid encoding issues with special characters
$ghxPath = 'D:\Work\PROJECTS\Dise*\gh-definitions\F1_CONTEXTO_v11.ghx'
Write-Host ("Checking GHX file (wildcard): {0}" -f $ghxPath)
if(-not (Test-Path $ghxPath)) {
    Write-Host "File not found with wildcard!" -ForegroundColor Red
    exit 1
}
Write-Host "File found with wildcard."

# Get the actual resolved path
$resolvedPath = Resolve-Path $ghxPath
Write-Host ("Resolved path: {0}" -f $resolvedPath)

# Try to load the GHX file
$doc = $null
try {
    $doc = New-Object Grasshopper.IO.GH_Archive
    Write-Host "GH_Archive object created."
    $doc.Read($resolvedPath.Path)
    Write-Host "File loaded successfully."

    # Check components
    $objects = $doc.GetObjectIterator()
    $v02Count = 0
    $v04Count = 0
    while($objects.MoveNext()) {
        $obj = $objects.Current
        if($obj.Type -eq 'Component' -and $obj.NickName -like '*F1_ETAPA1_CONTEXTO*') {
            $code = $obj.CodeInput
            $v02Refs = ($code -split 'v02' | Measure-Object).Count - 1
            $v04Refs = ($code -split 'v04' | Measure-Object).Count - 1
            if($v02Refs -gt 0) { $v02Count++ }
            if($v04Refs -gt 0) { $v04Count++ }
            Write-Host ("Component: {0} (GUID: {1})" -f $obj.NickName, $obj.InstanceGuid)
            Write-Host ("  v02 refs: {0}, v04 refs: {1}" -f $v02Refs, $v04Refs)
        }
    }
    Write-Host ("SUMMARY: v02={0}, v04={1}" -f $v02Count, $v04Count)

    if($v02Count -eq 0 -and $v04Count -gt 0) {
        Write-Host "SUCCESS: All F1_ETAPA1_CONTEXTO components have been updated to v04!" -ForegroundColor Green
    } elseif($v02Count -gt 0) {
        Write-Host "WARNING: Found $v02Count components still referencing v02" -ForegroundColor Yellow
    } else {
        Write-Host "INFO: No F1_ETAPA1_CONTEXTO components found" -ForegroundColor Yellow
    }
} catch {
    Write-Host "Error loading GHX file: $_" -ForegroundColor Red
} finally {
    if($doc) { $doc.Dispose() }
}