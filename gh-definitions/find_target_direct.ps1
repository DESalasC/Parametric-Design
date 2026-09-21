# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Directly searching for target component in: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        # Find the Description element that contains our target string
        Write-Host "`nSearching for Description element containing target string..."
        $descriptionMatches = $xml.SelectNodes("//Description[contains(text(), 'F1_ETAPA1_CONTEXTO_v02')]")
        Write-Host ("Found {0} Description elements with target string." -f $descriptionMatches.Count)

        if ($descriptionMatches.Count -gt 0) {
            $descriptionElem = $descriptionMatches[0]
            Write-Host ("Description element found at: {0}" -f $descriptionElem.ParentNode.Path)
            Write-Host ("Parent element name: {0}" -f $descriptionElem.ParentNode.Name)

            # Now let's see if this parent element also contains a CodeInput with our target
            $codeInputInParent = $descriptionElem.ParentNode.SelectSingleNode(".//CodeInput[contains(text(), 'F1_ETAPA1_CONTEXTO_v02')]")
            if ($codeInputInParent) {
                Write-Host "*** FOUND TARGET CODEINPUT IN SAME PARENT AS DESCRIPTION! ***"
                Write-Host ("CodeInput text length: {0}" -f $codeInputInParent.InnerText.Length)

                # Now let's examine this parent element thoroughly
                $targetElement = $descriptionElem.ParentNode
                Write-Host ("`nTarget element name: {0}" -f $targetElement.Name)

                # Show attributes
                if ($targetElement.Attributes.Count -gt 0) {
                    Write-Host "Attributes:"
                    foreach($attr in $targetElement.Attributes) {
                        Write-Host ("  {0} = {1}" -f $attr.Name, $attr.Value)
                    }
                }

                # List all child elements
                Write-Host ("Child elements count: {0}" -f $targetElement.ChildNodes.Count)
                for($i=0; $i -lt $targetElement.ChildNodes.Count; $i++) {
                    $child = $targetElement.ChildNodes[$i]
                    if ($child.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                        $textLen = $child.InnerText.Length
                        Write-Host ("  [{0}] {1} (length: {2})" -f $i, $child.Name, $textLen)
                        if ($textLen -lt 100) {
                            Write-Host ("      Content: '{0}'" -f $child.InnerText)
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
                $codePreview = $codeInputInParent.InnerText.Substring(0, [Math]::Min(300, $codeInputInParent.InnerText.Length))
                Write-Host $codePreview

            } else {
                Write-Host "Description element found but no matching CodeInput in same parent."

                # Let's look upwards for a container that might have both
                $current = $descriptionElem.ParentNode
                $level = 0
                while($current -and $level -lt 5) {
                    Write-Host ("Level {0}: {1}" -f $level, $current.Name)
                    $codeInputHere = $current.SelectSingleNode(".//CodeInput[contains(text(), 'F1_ETAPA1_CONTEXTO_v02')]")
                    if ($codeInputHere) {
                        Write-Host ("*** FOUND TARGET CODEINPUT IN ANCESTOR LEVEL {0}! ***" -f $level)
                        $targetElement = $current
                        break
                    }
                    $current = $current.ParentNode
                    $level++
                }
            }
        } else {
            Write-Host "No Description element found containing target string."
        }

    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}