# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Checking nested items elements in: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        # Find all items elements in the document
        $itemsElements = $xml.SelectNodes("//items")
        Write-Host ("Found {0} items elements in document." -f $itemsElements.Count)

        for($i=0; $i -lt $itemsElements.Count; $i++) {
            $itemsElement = $itemsElements[$i]
            Write-Host ("`nItems element {0}:" -f $i)
            Write-Host ("  Parent element: {0}" -f $itemsElement.ParentNode.Name)
            Write-Host ("  Count attribute: {0}" -f $itemsElement.GetAttribute('count'))
            Write-Host ("  Number of child elements: {0}" -f $itemsElement.ChildNodes.Count)

            # Examine each child of this items element
            for($j=0; $j -lt $itemsElement.ChildNodes.Count; $j++) {
                $child = $itemsElement.ChildNodes[$j]
                if ($child.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                    Write-Host ("    Child {0}:" -f $j)
                    Write-Host ("      Name: {0}" -f $child.Name)

                    # Show attributes
                    if ($child.Attributes.Count -gt 0) {
                        Write-Host "      Attributes:"
                        foreach($attr in $child.Attributes) {
                            Write-Host ("        {0} = {1}" -f $attr.Name, $attr.Value)
                        }
                    }

                    # Look for Object elements
                    $objects = $child.SelectNodes(".//Object")
                    Write-Host ("      Found {0} Object elements." -f $objects.Count)

                    if ($objects.Count -gt 0) {
                        Write-Host "      Examining Object elements:"
                        for($k=0; $k -lt $objects.Count; $k++) {
                            $obj = $objects[$k]
                            Write-Host ("        Object {0}:" -f $k)
                            Write-Host ("          Name: {0}" -f $obj.Name)

                            # Look for NickName
                            $nickName = $obj.SelectSingleNode(".//NickName")
                            if ($nickName) {
                                Write-Host ("          NickName: {0}" -f $nickName.InnerText)
                            }

                            # Look for Name
                            $name = $obj.SelectSingleNode(".//Name")
                            if ($name) {
                                Write-Host ("          Name: {0}" -f $name.InnerText)
                            }

                            # Look for InstanceGuid
                            $instanceGuid = $obj.SelectSingleNode(".//InstanceGuid")
                            if ($instanceGuid) {
                                Write-Host ("          InstanceGuid: {0}" -f $instanceGuid.InnerText)
                            }

                            # Look for CodeInput
                            $codeInput = $obj.SelectSingleNode(".//CodeInput")
                            if ($codeInput) {
                                Write-Host ("          CodeInput: {0} chars" -f $codeInput.InnerText.Length)
                                if ($codeInput.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                                    Write-Host "          *** THIS IS THE TARGET COMPONENT! ***"
                                    # Show preview
                                    $preview = $codeInput.InnerText.Substring(0, [Math]::Min(200, $codeInput.InnerText.Length))
                                    Write-Host ("          Preview: {0}" -f $preview)
                                }
                            }
                        }
                    }

                    # If no Object elements, let's see what ELSE we can find
                    if ($objects.Count -eq 0) {
                        # Look for other interesting elements
                        $interestingNames = @("DefinitionObjects", "Objects", "Component", "Components", "GH_Object", "GH_Document")
                        foreach($name in $interestingNames) {
                            $elements = $child.SelectNodes(".//$name")
                            if ($elements.Count -gt 0) {
                                Write-Host ("      Found {0} {1} elements." -f $elements.Count, $name)
                            }
                        }

                        # Let's look at what element names we DO have
                        $elementNames = @()
                        foreach($grandChild in $child.ChildNodes) {
                            if ($grandChild.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                                if (-not ($elementNames -contains $grandChild.Name)) {
                                    $elementNames += $grandChild.Name
                                }
                            }
                        }
                        if ($elementNames.Count -gt 0) {
                            Write-Host ("      Element names found: {0}" -f ($elementNames -join ', '))
                        }

                        # Let's check the Description element since we know it's there
                        $description = $child.SelectSingleNode(".//Description")
                        if ($description) {
                            Write-Host ("      Description element found (length: {0})" -f $description.InnerText.Length)
                            if ($description.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                                Write-Host "      *** DESCRIPTION CONTAINS TARGET STRING! ***"
                            }
                        }

                        # Let's check the CodeInput element since we know it's there
                        $codeInput = $child.SelectSingleNode(".//CodeInput")
                        if ($codeInput) {
                            Write-Host ("      CodeInput element found (length: {0})" -f $codeInput.InnerText.Length)
                            if ($codeInput.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                                Write-Host "      *** CODEINPUT CONTAINS TARGET STRING! ***"
                                # Show preview
                                $preview = $codeInput.InnerText.Substring(0, [Math]::Min(200, $codeInput.InnerText.Length))
                                Write-Host ("      Preview: {0}" -f $preview)
                            }
                        }
                    }
                }
            }
        }

    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}