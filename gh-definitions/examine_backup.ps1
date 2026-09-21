# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx.bak-2026-09-17-1732'
$resolvedPath = Resolve-Path -Path $wildcardPath
$backupPath = $resolvedPath.Path

Write-Host "Examining backup: $backupPath"
if (Test-Path $backupPath) {
    Write-Host "File exists."
    try {
        [xml]$xml = Get-Content -Path $backupPath
        Write-Host "Loaded XML successfully."

        # Let's see what the root element is
        Write-Host "Root element: $($xml.Name)"

        # Let's see what child elements the root has
        Write-Host "`nRoot child elements:"
        foreach($child in $xml.ChildNodes) {
            Write-Host "  $($child.Name)"
        }

        # Let's look for Object elements specifically
        Write-Host "`nLooking for Object elements..."
        $objects = $xml.SelectNodes("//Object")
        Write-Host "Found $($objects.Count) Object elements."

        if ($objects.Count -gt 0) {
            Write-Host "First Object element:"
            $firstObj = $objects[0]
            Write-Host "  Name: $($firstObj.Name)"
            foreach($child in $firstObj.ChildNodes) {
                Write-Host "    $($child.Name): $($child.InnerText)"
            }
        }

        # Let's look for any elements that contain text
        Write-Host "`nLooking for elements with text content..."
        $textElements = $xml.SelectNodes("//*[text()]", [System.Xml.XmlNamespaceManager]::new($xml.NameTable))
        Write-Host "Found $($textElements.Count) elements with text content."
        if ($textElements.Count -gt 0) {
            Write-Host "First 5 text elements:"
            for($i=0; $i -lt [Math]::Min(5, $textElements.Count); $i++) {
                $elem = $textElements[$i]
                Write-Host "  $($elem.Name): '$($elem.InnerText)'"
            }
        }

        # Let's also check the current (non-backup) file for comparison
        Write-Host "`n=== COMPARISON WITH CURRENT FILE ==="
        $currentPath = $backupPath -Replace '\.bak-\d{4}-\d{2}-\d{2}-\d{4}', ''
        Write-Host "Current file: $currentPath"
        if (Test-Path $currentPath) {
            [xml]$currentXml = Get-Content -Path $currentPath
            Write-Host "Loaded current XML successfully."
            $currentObjects = $currentXml.SelectNodes("//Object")
            Write-Host "Current file has $($currentObjects.Count) Object elements."
            $currentNickNames = $currentXml.SelectNodes("//NickName")
            Write-Host "Current file has $($currentNickNames.Count) NickName elements."
            if ($currentNickNames.Count -gt 0) {
                $values = @()
                foreach($node in $currentNickNames) {
                    $values += $node.InnerText
                }
                Write-Host "Current file NickName values (first 10): $($values[0..[Math]::Min(9, $values.Count-1)] -join ', ')"
            }
        } else {
            Write-Host "Current file does not exist."
        }
    } catch {
        Write-Error "Failed to load XML: $_"
    }
} else {
    Write-Host "Backup file does not exist."
}