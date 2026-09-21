# Script to patch a GHPython component in a GHX file by CodeInput content
# Usage: .\patch_component_by_content.ps1 <ghx_path> <target_string> <new_code_path> [--no-backup]

param(
    [Parameter(Mandatory=$true)]
    [string]$ghxPath,

    [Parameter(Mandatory=$true)]
    [string]$targetString,

    [Parameter(Mandatory=$true)]
    [string]$newCodePath,

    [switch]$noBackup
)

try {
    Write-Host "Loading GHX file: $ghxPath"
    [xml]$xml = Get-Content -Path $ghxPath
    Write-Host "Loaded XML successfully."

    # Create backup unless --no-backup is specified
    if (-not $noBackup) {
        $backupPath = "$ghxPath.bak-$(Get-Date -Format 'yyyy-MM-dd-HHmmss')"
        Copy-Item -Path $ghxPath -Destination $backupPath
        Write-Host "Created backup: $backupPath"
    }

    # Load the new code
    Write-Host "Loading new code from: $newCodePath"
    $newCode = Get-Content -Path $newCodePath -Raw
    Write-Host ("New code length: {0} characters" -f $newCode.Length)

    # Find all CodeInput item nodes
    $codeInputItems = $xml.SelectNodes("//item[@name='CodeInput']")
    Write-Host ("Found {0} CodeInput item nodes." -f $codeInputItems.Count)

    $patchedCount = 0
    for($i=0; $i -lt $codeInputItems.Count; $i++) {
        $item = $codeInputItems[$i]
        if ($item.InnerText -like "*$targetString*") {
            Write-Host ("*** FOUND TARGET IN CODEINPUT ITEM INDEX {0} ***" -f $i)
            Write-Host ("  Current CodeInput length: {0}" -f $item.InnerText.Length)

            # Replace the content
            $item.InnerText = $newCode
            Write-Host ("  Replaced with new code of length: {0}" -f $newCode.Length)
            $patchedCount++
        }
    }

    if ($patchedCount -eq 0) {
        Write-Warning "No CodeInput items found containing the target string."
        exit 1
    } else {
        Write-Host ("Successfully patched {0} CodeInput item(s)." -f $patchedCount)
    }

    # Save the modified XML
    Write-Host "Saving modified GHX file..."
    $xml.Save($ghxPath)
    Write-Host "GHX file saved successfully."

} catch {
    Write-Host "An error occurred:"
    Write-Host $_.Exception.Message
    exit 1
}