# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx.bak-2026-09-17-1732'
$resolvedPath = Resolve-Path -Path $wildcardPath
$backupPath = $resolvedPath.Path

Write-Host "Checking backup: $backupPath"
if (Test-Path $backupPath) {
    Write-Host "File exists."
    try {
        [xml]$xml = Get-Content -Path $backupPath
        Write-Host "Loaded XML successfully."
        $nickNameNodes = $xml.SelectNodes("//NickName")
        Write-Host "Found $($nickNameNodes.Count) NickName elements."
        if ($nickNameNodes.Count -gt 0) {
            $values = @()
            foreach($node in $nickNameNodes) {
                $values += $node.InnerText
            }
            Write-Host "NickName values: $($values -join ', ')"
        } else {
            Write-Host "No NickName elements found."
        }
    } catch {
        Write-Error "Failed to load XML: $_"
    }
} else {
    Write-Host "Backup file does not exist."
}