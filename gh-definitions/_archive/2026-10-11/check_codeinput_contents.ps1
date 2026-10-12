# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Checking CodeInput contents in: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        $codeInputItems = $xml.SelectNodes("//item[@name='CodeInput']")
        Write-Host ("Found {0} CodeInput item nodes." -f $codeInputItems.Count)

        for($i=0; $i -lt $codeInputItems.Count; $i++) {
            $item = $codeInputItems[$i]
            $text = $item.InnerText
            $length = $text.Length
            Write-Host ("Item {0}: length = {1}" -f $i, $length)

            # Check if it contains our target string
            if ($text -like "*F1_ETAPA1_CONTEXTO_v02*") {
                Write-Host "  --> CONTAINS TARGET STRING!"
            }

            # Show first 100 chars
            $previewLength = [Math]::Min(100, $length)
            $preview = $text.Substring(0, $previewLength)
            Write-Host ("  Preview: {0}" -f $preview)
            Write-Host ""
        }
    } catch {
        Write-Host "Error: $($_.Exception.Message)"
    }
} else {
    Write-Host "File does not exist."
}