# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Finding target component in: $path"
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

        Write-Host "Found items element with count attribute: $($itemsElement.GetAttribute('count'))"
        Write-Host "Number of child elements in items: $($itemsElement.ChildNodes.Count)"

        # Look through each child of items to find the one with CodeInput containing our target
        $targetIndex = -1
        $targetCodeInput = $null
        $targetDescription = $null

        for($i=0; $i -lt $itemsElement.ChildNodes.Count; $i++) {
            $child = $itemsElement.ChildNodes[$i]
            if ($child.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                # Check if this child has a CodeInput element containing our target string
                $codeInput = $child.SelectSingleNode(".//CodeInput")
                if ($codeInput -and $codeInput.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                    $targetIndex = $i
                    $targetCodeInput = $codeInput
                    Write-Host "`nFound target CodeInput at items index $i:"
                    Write-Host "  Element name: $($child.Name)"

                    # Also get the Description if it exists
                    $targetDescription = $child.SelectSingleNode(".//Description")
                    if ($targetDescription) {
                        Write-Host "  Description length: $($targetDescription.InnerText.Length) chars"
                        # Show first 200 chars of description
                        $descPreview = $targetDescription.InnerText.Substring(0, [Math]::Min(200, $targetDescription.InnerText.Length))
                        Write-Host "  Description preview: $descPreview"
                    }

                    break
                }
            }
        }

        if ($targetIndex -ge 0) {
            Write-Host "`nExamining all elements at items index $targetIndex:"
            $targetElement = $itemsElement.ChildNodes[$targetIndex]
            if ($targetElement.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                Write-Host "  Element name: $($targetElement.Name)"

                # Show all child elements of this target element
                Write-Host "  Child elements:"
                for($j=0; $j -lt $targetElement.ChildNodes.Count; $j++) {
                    $grandChild = $targetElement.ChildNodes[$j]
                    if ($grandChild.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                        $textLength = $grandChild.InnerText.Length
                        Write-Host ("    [{0}] {1} (text length: {2})" -f $j, $grandChild.Name, $textLength)
                        if ($textLength -lt 100) {
                            Write-Host ("        Content: '{0}'" -f $grandChild.InnerText)
                        }
                    }
                }

                # Now look for NickName specifically
                Write-Host "`nLooking for NickName in target element..."
                $nickNameElement = $targetElement.SelectSingleNode(".//NickName")
                if ($nickNameElement) {
                    Write-Host ("Found NickName: '{0}'" -f $nickNameElement.InnerText)
                } else {
                    Write-Host "No NickName element found."

                    # Let's see what OTHER identifying elements we have
                    Write-Host "Checking for Name element..."
                    $nameElement = $targetElement.SelectSingleNode(".//Name")
                    if ($nameElement) {
                        Write-Host ("Found Name: '{0}'" -f $nameElement.InnerText)
                    } else {
                        Write-Host "No Name element found either."
                    }

                    # Let's check InstanceGuid
                    Write-Host "Checking for InstanceGuid..."
                    $instanceGuidElement = $targetElement.SelectSingleNode(".//InstanceGuid")
                    if ($instanceGuidElement) {
                        Write-Host ("Found InstanceGuid: '{0}'" -f $instanceGuidElement.InnerText)
                    }
                }

                # Show the CodeInput content preview
                Write-Host "`nCodeInput content preview (first 300 chars):"
                $codePreview = $targetCodeInput.InnerText.Substring(0, [Math]::Min(300, $targetCodeInput.InnerText.Length))
                Write-Host $codePreview
            }
        } else {
            Write-Host "ERROR: Could not find target CodeInput in items element"
        }

    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}