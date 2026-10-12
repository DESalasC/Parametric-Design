# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Examining first Object chunk in DefinitionObjects: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        # Find the DefinitionObjects chunk
        $definitionObjectsChunk = $xml.SelectSingleNode("//chunk[@name='DefinitionObjects']")
        if (-not $definitionObjectsChunk) {
            Write-Host "ERROR: Could not find DefinitionObjects chunk"
            exit
        }

        Write-Host "Found DefinitionObjects chunk."

        # Get the first chunk (index 0) which should be an Object
        $firstObjectChunk = $definitionObjectsChunk.SelectSingleNode("chunks/chunk[1]")  # First chunk
        if (-not $firstObjectChunk) {
            Write-Host "ERROR: Could not find first chunk in DefinitionObjects"
            exit
        }

        Write-Host ("First chunk name: {0}" -f $firstObjectChunk.GetAttribute('name'))

        # Look for items inside this chunk
        $itemsInFirstObject = $firstObjectChunk.SelectSingleNode("items")
        if ($itemsInFirstObject) {
            Write-Host ("First chunk has {0} items:" -f $itemsInFirstObject.GetAttribute('count'))

            # Look for Object element in these items
            $objectElement = $itemsInFirstObject.SelectSingleNode(".//Object")
            if ($objectElement) {
                Write-Host "Found Object element in first chunk!"
                Write-Host ("  Object Name: {0}" -f $objectElement.Name)

                # Look for identifying elements in this Object
                $nickName = $objectElement.SelectSingleNode(".//NickName")
                if ($nickName) {
                    Write-Host ("  NickName: {0}" -f $nickName.InnerText)
                } else {
                    Write-Host "  No NickName found."
                }

                $name = $objectElement.SelectSingleNode(".//Name")
                if ($name) {
                    Write-Host ("  Name: {0}" -f $name.InnerText)
                } else {
                    Write-Host "  No Name found."
                }

                $instanceGuid = $objectElement.SelectSingleNode(".//InstanceGuid")
                if ($instanceGuid) {
                    Write-Host ("  InstanceGuid: {0}" -f $instanceGuid.InnerText)
                } else {
                    Write-Host "  No InstanceGuid found."
                }

                # Look for CodeInput
                $codeInput = $objectElement.SelectSingleNode(".//CodeInput")
                if ($codeInput) {
                    Write-Host ("  CodeInput: {0} chars" -f $codeInput.InnerText.Length)
                    if ($codeInput.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                        Write-Host "  *** THIS IS THE TARGET COMPONENT! ***"

                        # Show preview
                        $preview = $codeInput.InnerText.Substring(0, [Math]::Min(200, $codeInput.InnerText.Length))
                        Write-Host ("  Preview: {0}" -f $preview)
                    } else {
                        Write-Host "  CodeInput does not contain target string."
                    }
                } else {
                    Write-Host "  No CodeInput found."
                }
            } else {
                Write-Host "No Object element found in first chunk's items."

                # Let's see what elements ARE in the items
                Write-Host "Elements in first chunk's items:"
                foreach($child in $itemsInFirstObject.ChildNodes) {
                    if ($child.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                        Write-Host ("  {0}" -f $child.Name)
                    }
                }
            }
        } else {
            Write-Host "No items element found in first chunk."
        }

        # Now let's search through ALL chunks in DefinitionObjects for our target
        Write-Host ("`nSearching through all {0} chunks in DefinitionObjects for target..." -f $definitionObjectsChunk.SelectSingleNode("chunks").ChildNodes.Count)

        $targetFound = $false
        $targetChunkIndex = -1

        $allChunks = $definitionObjectsChunk.SelectSingleNode("chunks")
        for($i=0; $i -lt $allChunks.ChildNodes.Count; $i++) {
            $chunk = $allChunks.ChildNodes[$i]
            if ($chunk.NodeType -eq [System.Xml.XmlNodeType]::Element -and $chunk.Name -eq "chunk") {
                # Look for Object element in this chunk's items
                $itemsInChunk = $chunk.SelectSingleNode("items")
                if ($itemsInChunk) {
                    $objectElement = $itemsInChunk.SelectSingleNode(".//Object")
                    if ($objectElement) {
                        $codeInput = $objectElement.SelectSingleNode(".//CodeInput")
                        if ($codeInput -and $codeInput.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                            $targetFound = $true
                            $targetChunkIndex = $i
                            Write-Host ("*** FOUND TARGET IN CHUNK INDEX {0} ***" -f $i)

                            # Show identifying information
                            $nickName = $objectElement.SelectSingleNode(".//NickName")
                            if ($nickName) {
                                Write-Host ("  NickName: {0}" -f $nickName.InnerText)
                            } else {
                                Write-Host "  No NickName found."
                            }

                            $name = $objectElement.SelectSingleNode(".//Name")
                            if ($name) {
                                Write-Host ("  Name: {0}" -f $name.InnerText)
                            } else {
                                Write-Host "  No Name found."
                            }

                            break
                        }
                    }
                }
            }
        }

        if (-not $targetFound) {
            Write-Host "Target component not found in any chunk."
        } else {
            Write-Host ("Target found at chunk index: {0}" -f $targetChunkIndex)
        }

    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}