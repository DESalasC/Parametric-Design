# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Verifying patch in: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        $codeInputItems = $xml.SelectNodes("//item[@name='CodeInput']")
        Write-Host ("Found {0} CodeInput item nodes." -f $codeInputItems.Count)

        $v02Count = 0
        $v04Count = 0

        for($i=0; $i -lt $codeInputItems.Count; $i++) {
            $item = $codeInputItems[$i]
            $text = $item.InnerText

            if ($text -like "*F1_ETAPA1_CONTEXTO_v02*") {
                $v02Count++
                Write-Host ("Item {0}: Contains v02" -f $i)
            }
            if ($text -like "*F1_ETAPA1_CONTEXTO_v04*") {
                $v04Count++
                Write-Host ("Item {0}: Contains v04" -f $i)
            }
        }

        Write-Host ("Summary: v02 found {0} times, v04 found {1} times" -f $v02Count, $v04Count)

        if ($v02Count -eq 0 -and $v04Count -gt 0) {
            Write-Host "SUCCESS: Patch completed - v02 replaced with v04"
        } elseif ($v02Count -gt 0) {
            Write-Host "ERROR: Patch incomplete - v02 still present"
        } else {
            Write-Host "WARNING: No v02 or v04 found - unexpected state"
        }
    } catch {
        Write-Host "Error: $($_.Exception.Message)"
    }
} else {
    Write-Host "File does not exist."
}