# Load GH_IO.dll
$ghioPath = 'C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll'
Write-Host "Loading GH_IO.dll from: $ghioPath"
try {
    Add-Type -Path $ghioPath
    Write-Host "GH_IO.dll loaded successfully."
} catch {
    Write-Host "Failed to load GH_IO.dll: $_" -ForegroundColor Red
    exit 1
}

# Use wildcard to avoid encoding issues with special characters
$ghxPath = 'D:\Work\PROJECTS\Dise*\gh-definitions\F1_CONTEXTO_v11.ghx'
Write-Host "Checking GHX file (wildcard): $ghxPath"
if(-not (Test-Path $ghxPath)) {
    Write-Host "File not found with wildcard!" -ForegroundColor Red
    exit 1
}
Write-Host "File found with wildcard."

# Get the actual resolved path
$resolvedPath = Resolve-Path $ghxPath
Write-Host "Resolved path: $($resolvedPath.Path)"

# Try to load the GHX file using reflection to get the type
$doc = $null
try {
    $asm = [System.AppDomain]::CurrentDomain.GetAssemblies() |
           Where-Object { $_.FullName -like 'GH_IO,*' } |
           Select-Object -First 1

    if(-not $asm) {
        Write-Host "Could not find GH_IO assembly" -ForegroundColor Red
        exit 1
    }

    $type = $asm.GetType("Grasshopper.IO.Serialization.GH_Archive")
    if(-not $type) {
        Write-Host "Could not find Grasshopper.IO.Serialization.GH_Archive type" -ForegroundColor Red
        exit 1
    }

    Write-Host "Found GH_Archive type: $($type.FullName)"
    $doc = $type.GetConstructor(@()).Invoke(@($null))
    Write-Host "GH_Archive object created."
    $doc.Read($resolvedPath.Path)
    Write-Host "File loaded successfully."

    # Check components
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
            Write-Host ("Component {0}: {1} (GUID: {2})" -f $componentCount, $obj.NickName, $obj.InstanceGuid)
            Write-Host ("  v02 refs: {0}, v04 refs: {1}" -f $v02Refs, $v04Refs)
            # Show first 150 chars of code input for verification
            if($code.Length -gt 150) {
                $preview = $code.Substring(0,150) -replace "[`r`n]", " "
                Write-Host ("  Code preview: {0}..." -f $preview)
            } else {
                Write-Host ("  Code: {0}" -f $code)
            }
            Write-Host("")
        }
    }
    Write-Host ("SUMMARY: Found {0} F1_ETAPA1_CONTEXTO components" -f $componentCount)
    Write-Host ("SUMMARY: v02 references in {0} components, v04 references in {1} components" -f $v02Count, $v04Count)

    if($v02Count -eq 0 -and $v04Count -gt 0) {
        Write-Host "SUCCESS: All F1_ETAPA1_CONTEXTO components have been updated to v04!" -ForegroundColor Green
    } elseif($v02Count -gt 0) {
        Write-Host "WARNING: Found $v02Count components still referencing v02" -ForegroundColor Yellow
    } elseif($v04Count -eq 0) {
        Write-Host "ERROR: No components found with v04 references" -ForegroundColor Red
    } else {
        Write-Host "INFO: Mixed v02/v04 references found" -ForegroundColor Yellow
    }
} catch {
    Write-Host "Error loading GHX file: $($_.Exception.Message)" -ForegroundColor Red
} finally {
    if($doc) { $doc.Dispose() }
}