# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Examining structure of: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        # Let's see what the root element is
        Write-Host "Root element: " + $xml.Name

        # Let's see what child elements the root has
        Write-Host "`nRoot child elements:"
        foreach($child in $xml.ChildNodes) {
            if ($child.Name -ne 'xml') {  # Skip the xml declaration
                Write-Host "  " + $child.Name
                # Show attributes of this element
                if ($child.Attributes.Count -gt 0) {
                    Write-Host "    Attributes:"
                    foreach($attr in $child.Attributes) {
                        Write-Host "      " + $attr.Name + " = " + $attr.Value
                    }
                }
                # Show first few child elements
                $count = 0
                foreach($grandChild in $child.ChildNodes) {
                    if ($grandChild.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                        Write-Host "    Element: " + $grandChild.Name
                        $count++
                        if ($count -ge 5) { break }
                    }
                }
            }
        }

        # Let's look for any elements that might contain objects or components
        Write-Host "`nSearching for common Grasshopper element names..."
        $commonNames = @('Object', 'Objects', 'Component', 'Components', 'GH_Document', 'GH_Object')
        foreach($name in $commonNames) {
            $elements = $xml.SelectNodes("//$name")
            Write-Host ("  {0}: {1} elements" -f $name, $elements.Count)
        }

        # Let's look at the actual structure by examining a path
        Write-Host "`nExamining Archive/Root/... path..."
        $archiveNodes = $xml.SelectNodes("//Archive")
        Write-Host ("Found {0} Archive nodes." -f $archiveNodes.Count)
        if ($archiveNodes.Count -gt 0) {
            $archive = $archiveNodes[0]
            Write-Host ("Archive node name: {0}" -f $archive.Name)
            Write-Host ("Archive child elements count: {0}" -f $archive.ChildNodes.Count)
            # Look for Objects or similar
            foreach($child in $archive.ChildNodes) {
                if ($child.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                    Write-Host ("  Archive child: {0}" -f $child.Name)
                }
            }
        }

        # Let's search for the specific string we know is in the file
        Write-Host "`nSearching for 'F1_ETAPA1_CONTEXTO_v02' in element text..."
        $matches = $xml.SelectNodes("//*[contains(text(), 'F1_ETAPA1_CONTEXTO_v02')]")
        Write-Host ("Found {0} elements containing the string." -f $matches.Count)
        if ($matches.Count -gt 0) {
            for($i=0; $i -lt [Math]::Min(3, $matches.Count); $i++) {
                $elem = $matches[$i]
                Write-Host ("  Match {0}: {1} = '{2}'" -f $i, $elem.Name, $elem.InnerText)
                # Show parent element
                if ($elem.ParentNode) {
                    Write-Host ("    Parent: {0}" -f $elem.ParentNode.Name)
                }
            }
        }

        # Let's look at what the actual Objects collection might be called in GH_IO
        Write-Host "`nChecking what GH_IO.Serialization.GH_Archive actually has for Objects..."
        # We'll do this via PowerShell reflection later if needed

    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}