# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Debugging XML structure of: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        # Let's see all element names in the document
        Write-Host "`nCollecting all unique element names..."
        $elementNames = @()
        foreach($node in $xml.SelectNodes("//*")) {
            if ($node.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                if (-not ($elementNames -contains $node.Name)) {
                    $elementNames += $node.Name
                }
            }
        }
        Write-Host "Found $($elementNames.Count) unique element names:"
        foreach($name in $elementNames | Sort-Object) {
            Write-Host "  $name"
        }

        # Let's look specifically for elements that contain our target text
        Write-Host "`nFinding elements containing 'F1_ETAPA1_CONTEXTO_v02'..."
        $matches = $xml.SelectNodes("//*[contains(text(), 'F1_ETAPA1_CONTEXTO_v02')]")
        Write-Host "Found $($matches.Count) matching elements:"
        for($i=0; $i -lt $matches.Count; $i++) {
            $elem = $matches[$i]
            Write-Host ("  {0}: Name='{1}', InnerText length={2}" -f $i, $elem.Name, $elem.InnerText.Length)
            if ($elem.InnerText.Length -lt 200) {
                Write-Host ("     Content: {0}" -f $elem.InnerText)
            } else {
                Write-Host ("     Content starts with: {0}" -f $elem.InnerText.Substring(0, 100))
            }

            # Show parent info
            if ($elem.ParentNode) {
                Write-Host ("     Parent: {0}" -f $elem.ParentNode.Name)
                # Show parent's attributes
                if ($elem.ParentNode.Attributes.Count -gt 0) {
                    Write-Host ("     Parent attributes:")
                    foreach($attr in $elem.ParentNode.Attributes) {
                        Write-Host ("       {0} = {1}" -f $attr.Name, $attr.Value)
                    }
                }
            }
        }

        # Let's check if there's a namespace issue
        Write-Host "`nChecking for namespaces..."
        if ($xml.DocumentElement.NamespaceURI) {
            Write-Host ("Document element namespace: {0}" -f $xml.DocumentElement.NamespaceURI)
            Write-Host ("Document element prefix: {0}" -f $xml.DocumentElement.Prefix)
        } else {
            Write-Host "No namespace on document element."
        }

        # Try to get namespace manager
        $nsMgr = New-Object System.Xml.XmlNamespaceManager($xml.NameTable)
        if ($xml.DocumentElement.NamespaceURI) {
            $nsMgr.AddNamespace("ns", $xml.DocumentElement.NamespaceURI)
            Write-Host "Added namespace 'ns' for URI: $($xml.DocumentElement.NamespaceURI)"

            # Try selecting with namespace
            $codeInputNs = $xml.SelectNodes("//ns:CodeInput", $nsMgr)
            Write-Host ("Found {0} CodeInput elements with namespace" -f $codeInputNs.Count)

            # Try selecting all elements with local name CodeInput
            $allCodeInput = $xml.SelectNodes("//*[local-name()='CodeInput']")
            Write-Host ("Found {0} elements with local-name 'CodeInput'" -f $allCodeInput.Count)
        }

    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}