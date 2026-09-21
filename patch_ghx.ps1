param(
    [string]$ghxPath,
    [string]$nickname,
    [string]$pythonScriptPath,
    [switch]$NoBackup,
    [switch]$RegenerateGH
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
} catch {
    Write-Error "Failed to load GHX document: $_"
    exit 1
}

# Find component by NickName
$target = $doc.Objects | Where-Object { $_.NickName -eq $nickname }
if (-Not $target) {
    Write-Error "Component with NickName '$nickname' not found."
    exit 1
}
Write-Host "Found component: $($target.NickName)"

# Read new Python code
try {
    $newCode = Get-Content -Path $pythonScriptPath -Raw
} catch {
    Write-Error "Failed to read Python script: $_"
    exit 1
}

# Replace CodeInput
# We need to find the CodeInput field/property in the object.
# Let's look for a field or property named "CodeInput" or "ScriptContent" that we can set.
$fields = $target.GetType().GetFields([System.Reflection.BindingFlags]'Instance,NonPublic,Public') | Where-Object { $_.Name -match 'CodeInput|ScriptContent' }
if ($fields) {
    foreach ($field in $fields) {
        Write-Host "Found field: $($field.Name)"
        $field.SetValue($target, $newCode)
        Write-Host "Set $($field.Name) to new code."
    }
} else {
    Write-Warning "Could not find CodeInput/ScriptContent field. Attempting to set via property..."
    # Try to find a property with setter
    $props = $target.GetType().GetProperties([System.Reflection.BindingFlags]'Instance,NonPublic,Public') | Where-Object { $_.Name -match 'CodeInput|ScriptContent' -and $_.CanWrite }
    if ($props) {
        foreach ($prop in $props) {
            $prop.SetValue($target, $newCode)
            Write-Host "Set property $($prop.Name) to new code."
        }
    } else {
        Write-Error "No suitable field/property found to set script content."
        exit 1
    }
}

# Backup original unless -NoBackup
if (-Not $NoBackup) {
    Backup-File -Path $ghxPath
}

# Save the modified document back to GHX
try {
    $doc.WriteToFile($ghxPath, $true, $true)  # overwrite, allow file sharing?
    Write-Host "Saved GHX via WriteToFile."
} catch {
    Write-Error "Failed to save GHX document: $_"
    exit 1
}

# Regenerate GH binary if requested
if ($RegenerateGH) {
    $ghPath = [System.IO.Path]::ChangeExtension($ghxPath, ".gh")
    try {
        # Try to write binary archive
        $doc.WriteToFile($ghPath, $true, $false)  # IsBinary? We want binary for .gh
        Write-Host "Generated GH binary at $ghPath"
    } catch {
        Write-Warning "Failed to generate GH binary: $_"
    }
}

Write-Host "Patch completed successfully."