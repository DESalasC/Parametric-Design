# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Checking Description elements in: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        # Find all Description elements
        $descriptionElements = $xml.SelectNodes("//Description")
        Write-Host "Found {0} Description elements." -f $descriptionElements.Count

        for($i=0; $i -lt $descriptionElements.Count; $i++) {
            $desc = $descriptionElements[$i]
            Write-Host ("`nDescription {0}:" -f $i)
            Write-Host ("  Parent element: {0}" -f $desc.ParentNode.Name)
            Write-Host ("  Text length: {0}" -f $desc.InnerText.Length)

            # Show first 200 characters
            $preview = $desc.InnerText.Substring(0, [Math]::Min(200, $desc.InnerText.Length))
            Write-Host ("  Preview: {0}" -f $preview)

            # Check if it contains our target string
            if ($desc.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                Write-Host "  *** CONTAINS TARGET STRING! ***"
            }

            # Check if it contains F1_ETAPA2_NORMATIVA (which we saw earlier)
            if ($desc.InnerText -like "*F1_ETAPA2_NORMATIVA*") {
                Write-Host "  *** CONTAINS F1_ETAPA2_NORMATIVA! ***"
            }
        }

    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}