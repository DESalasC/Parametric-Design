# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Checking chunks element in: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        # Find the chunks element
        $chunksElement = $xml.SelectSingleNode("//chunks")
        if (-not $chunksElement) {
            Write-Host "ERROR: Could not find chunks element"
            exit
        }

        Write-Host ("Found chunks element with count attribute: {0}" -f $chunksElement.GetAttribute('count'))
        Write-Host ("Number of child elements in chunks: {0}" -f $chunksElement.ChildNodes.Count)

        # Examine each child of chunks
        for($i=0; $i -lt $chunksElement.ChildNodes.Count; $i++) {
            $child = $chunksElement.ChildNodes[$i]
            if ($child.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                Write-Host ("`nChunk {0}:" -f $i)
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

                # Look for Object elements in this chunk
                $objects = $child.SelectNodes(".//Object")
                Write-Host ("  Found {0} Object elements." -f $objects.Count)

                if ($objects.Count -gt 0) {
                    Write-Host "  Examining Object elements:"
                    for($j=0; $j -lt $objects.Count; $j++) {
                        $obj = $objects[$j]
                        Write-Host ("    Object {0}:" -f $j)
                        Write-Host ("      Name: {0}" -f $obj.Name)

                        # Look for NickName
                        $nickName = $obj.SelectSingleNode(".//NickName")
                        if ($nickName) {
                            Write-Host ("      NickName: {0}" -f $nickName.InnerText)
                        }

                        # Look for Name
                        $name = $obj.SelectSingleNode(".//Name")
                        if ($name) {
                            Write-Host ("      Name: {0}" -f $name.InnerText)
                        }

                        # Look for InstanceGuid
                        $instanceGuid = $obj.SelectSingleNode(".//InstanceGuid")
                        if ($instanceGuid) {
                            Write-Host ("      InstanceGuid: {0}" -f $instanceGuid.InnerText)
                        }

                        # Look for CodeInput
                        $codeInput = $obj.SelectSingleNode(".//CodeInput")
                        if ($codeInput) {
                            Write-Host ("      CodeInput: {0} chars" -f $codeInput.InnerText.Length)
                            if ($codeInput.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                                Write-Host "      *** THIS IS THE TARGET COMPONENT! ***"
                                # Show preview
                                $preview = $codeInput.InnerText.Substring(0, [Math]::Min(200, $codeInput.InnerText.Length))
                                Write-Host ("      Preview: {0}" -f $preview)
                            }
                        }
                    }
                }

                # If no Object elements, let's see what IS in this chunk
                if ($objects.Count -eq 0) {
                    Write-Host "  No Object elements found. Checking what's inside..."
                    # Show first few element names
                    $elementNames = @()
                    $count = 0
                    foreach($grandChild in $child.ChildNodes) {
                        if ($grandChild.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                            if (-not ($elementNames -contains $grandChild.Name)) {
                                $elementNames += $grandChild.Name
                            }
                            $count++
                            if ($count -ge 10) { break }
                        }
                    }
                    if ($elementNames.Count -gt 0) {
                        Write-Host ("  First few element names: {0}" -f ($elementNames -join ', '))
                    }
                }
            }
        }

        # Also, let's search the entire document for Object elements
        Write-Host "`nSearching entire document for Object elements..."
        $allObjects = $xml.SelectNodes("//Object")
        Write-Host ("Found {0} Object elements in entire document." -f $allObjects.Count)

        if ($allObjects.Count -gt 0) {
            Write-Host "Examining all Object elements for target:"
            for($i=0; $i -lt $allObjects.Count; $i++) {
                $obj = $allObjects[$i]
                # Look for CodeInput
                $codeInput = $obj.SelectSingleNode(".//CodeInput")
                if ($codeInput -and $codeInput.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                    Write-Host ("Found target in Object {0}:" -f $i)
                    Write-Host ("  Object Name: {0}" -f $obj.Name)

                    # Look for NickName
                    $nickName = $obj.SelectSingleNode(".//NickName")
                    if ($nickName) {
                        Write-Host ("  NickName: {0}" -f $nickName.InnerText)
                    } else {
                        Write-Host "  No NickName found."
                    }

                    # Look for Name
                    $name = $obj.SelectSingleNode(".//Name")
                    if ($name) {
                        Write-Host ("  Name: {0}" -f $name.InnerText)
                    } else {
                        Write-Host "  No Name found."
                    }

                    break
                }
            }
        }

    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}