# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Sampling XML content from: $path"
if (Test-Path $path) {
    try {
        # Get first 5000 characters to see the structure
        $content = Get-Content -Path $path -Raw
        $length = $content.Length
        Write-Host ("File length: {0} characters" -f $length)

        $sampleLength = [Math]::Min(5000, $length)
        $sample = $content.Substring(0, $sampleLength)
        Write-Host ("`nFirst {0} characters:" -f $sampleLength)
        Write-Host $sample

        # Look for where our target string appears
        $targetPos = $content.IndexOf("F1_ETAPA1_CONTEXTO_v02")
        if ($targetPos -ge 0) {
            Write-Host ("`nTarget string found at position: {0}" -f $targetPos)
            $start = [Math]::Max(0, $targetPos - 200)
            $end = [Math]::Min($length, $targetPos + 200)
            $context = $content.Substring($start, $end - $start)
            Write-Host ("Context around target:")
            Write-Host $context
        } else {
            Write-Host "`nTarget string NOT found in file."
        }

    } catch {
        Write-Host "Failed to read file: $_"
    }
} else {
    Write-Host "File does not exist."
}