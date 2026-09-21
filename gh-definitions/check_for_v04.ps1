# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Checking for F1_ETAPA1_CONTEXTO_v04 in CodeInput elements in: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        $codeInputItems = $xml.SelectNodes("//item[@name='CodeInput']")
        Write-Host ("Found {0} CodeInput item nodes." -f $codeInputItems.Count)

        $foundCount = 0
        for($i=0; $i -lt $codeInputItems.Count; $i++) {
            $item = $codeInputItems[$i]
            $text = $item.InnerText

            # Check if it contains our target string (the new version)
            if ($text -like "*F1_ETAPA1_CONTEXTO_v04*") {
                Write-Host ("Found F1_ETAPA1_CONTEXTO_v04 in CodeInput item {0}" -f $i)
                $foundCount++
            }
        }

        if ($foundCount -gt 0) {
            Write-Host "SUCCESS: Found F1_ETAPA1_CONTEXTO_v04 in {0} CodeInput item(s)" -f $foundCount
        } else {
            Write-Host "Did not find F1_ETAPA1_CONTEXTO_v04 in any CodeInput items"
        }
    } catch {
        Write-Host "Error: $($_.Exception.Message)"
    }
} else {
    Write-Host "File does not exist."
}