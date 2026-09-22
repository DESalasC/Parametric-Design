$ghioPath = "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
if (-Not (Test-Path $ghioPath)) {
    Write-Error "GH_IO.dll not found at $ghioPath"
    exit 1
}
Add-Type -Path $ghioPath

$root = $env:DISENO_PARAMETRICO_ROOT
if (-not $root) {
    Write-Error "Environment variable DISENO_PARAMETRICO_ROOT is not set"
    exit 1
}
$ghxPath = Join-Path $root "gh-definitions\F1_CONTEXTO_v11.ghx"
Write-Host "Path: $ghxPath"
Write-Host "Test-Path: $(Test-Path $ghxPath)"
if (-Not (Test-Path $ghxPath)) {
    Write-Error "File does not exist"
    exit 1
}
try {
    $doc = New-Object GH_IO.Serialization.GH_Archive
    $doc.ReadFromFile($ghxPath)
    $objects = $doc.Objects
    Write-Output ("Total objects: {0}" -f $objects.Count)
    foreach ($obj in $objects) {
        if ($obj.TypeName -like '*Python*') {
            Write-Output ("Python: NickName: {0}, TypeName: {1}" -f $obj.NickName, $obj.TypeName)
        }
    }
} catch {
    Write-Host "Error: $_"
}
