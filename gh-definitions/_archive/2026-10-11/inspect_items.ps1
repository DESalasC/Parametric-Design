# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Inspecting items element in: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        # Find the items element
        $itemsElement = $xml.SelectSingleNode("//items")
        if (-not $itemsElement) {
            Write-Host "ERROR: Could not find items element"
            exit
        }

        Write-Host ("Found items element with count attribute: {0}" -f $itemsElement.GetAttribute('count'))
        Write-Host ("Number of child elements in items: {0}" -f $itemsElement.ChildNodes.Count)

        # Examine each child of items
        for($i=0; $i -lt $itemsElement.ChildNodes.Count; $i++) {
            $child = $itemsElement.ChildNodes[$i]
            if ($child.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                Write-Host ("`nChild {0}:" -f $i)
                Write-Host ("  Name: {0}" -f $child.Name)

                # Show attributes
                if ($child.Attributes.Count -gt 0) {
                    Write-Host "  Attributes:"
                    foreach($attr in $child.Attributes) {
                        Write-Host ("    {0} = {1}" -f $attr.Name, $attr.Value)
                    }
                }

                # Show child elements count
                Write-Host ("  Number of child elements: {0}" -f $child.ChildNodes.Count)

                # List child element names
                $childNames = @()
                foreach($grandChild in $child.ChildNodes) {
                    if ($grandChild.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                        if (-not ($childNames -contains $grandChild.Name)) {
                            $childNames += $grandChild.Name
                        }
                    }
                }
                if ($childNames.Count -gt 0) {
                    Write-Host ("  Child element names: {0}" -f ($childNames -join ', '))
                }

                # Check for CodeInput
                $codeInput = $child.SelectSingleNode(".//CodeInput")
                if ($codeInput) {
                    Write-Host ("  Found CodeInput element (text length: {0})" -f $codeInput.InnerText.Length)
                    if ($codeInput.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                        Write-Host "  *** THIS IS THE TARGET CODEINPUT! ***"
                    }
                }

                # Check for Description
                $description = $child.SelectSingleNode(".//Description")
                if ($description) {
                    Write-Host ("  Found Description element (text length: {0})" -f $description.InnerText.Length)
                    if ($description.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                        Write-Host "  *** DESCRIPTION CONTAINS TARGET STRING! ***"
                    }
                }

                # Check for NickName
                $nickName = $child.SelectSingleNode(".//NickName")
                if ($nickName) {
                    Write-Host ("  Found NickName element: '{0}'" -f $nickName.InnerText)
                }

                # Check for Name
                $name = $child.SelectSingleNode(".//Name")
                if ($name) {
                    Write-Host ("  Found Name element: '{0}'" -f $name.InnerText)
                }

                # Check for InstanceGuid
                $instanceGuid = $child.SelectSingleNode(".//InstanceGuid")
                if ($instanceGuid) {
                    Write-Host ("  Found InstanceGuid element: '{0}'" -f $instanceGuid.InnerText)
                }

                # Show a sample of inner text if it's small
                if ($child.InnerText.Length -lt 200) {
                    Write-Host ("  Inner text: '{0}'" -f $child.InnerText)
                } elseif ($child.InnerText.Length -gt 0) {
                    Write-Host ("  Inner text starts with: '{0}'" -f $child.InnerText.Substring(0, 100))
                }
            }
        }

    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}