# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Understanding chunk structure in DefinitionObjects: $path"
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

        # Examine the first few chunks to understand the structure
        $allChunks = $definitionObjectsChunk.SelectSingleNode("chunks")
        Write-Host ("Total chunks: {0}" -f $allChunks.ChildNodes.Count)

        # Look at first 5 chunks
        for($chunkIndex=0; $chunkIndex -lt [Math]::Min(5, $allChunks.ChildNodes.Count); $chunkIndex++) {
            $chunk = $allChunks.ChildNodes[$chunkIndex]
            if ($chunk.NodeType -eq [System.Xml.XmlNodeType]::Element -and $chunk.Name -eq "chunk") {
                Write-Host ("`n=== Chunk {0} ===" -f $chunkIndex)
                Write-Host ("  Name: {0}" -f $chunk.GetAttribute('name'))

                # Look at items in this chunk
                $items = $chunk.SelectSingleNode("items")
                if ($items) {
                    Write-Host ("  Items count: {0}" -f $items.GetAttribute('count'))

                    # List all element names in items
                    $elementNames = @()
                    foreach($child in $items.ChildNodes) {
                        if ($child.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                            if (-not ($elementNames -contains $child.Name)) {
                                $elementNames += $child.Name
                            }
                        }
                    }
                    Write-Host ("  Element names in items: {0}" -f ($elementNames -join ', '))

                    # Show first few elements with their content length
                    $displayCount = 0
                    foreach($child in $items.ChildNodes) {
                        if ($child.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                            Write-Host ("    {0}: {1} chars" -f $child.Name, $child.InnerText.Length)
                            $displayCount++
                            if ($displayCount -ge 3) { break }
                        }
                    }
                } else {
                    Write-Host "  No items element found."
                }

                # Look for any Object elements directly in this chunk
                $directObjects = $chunk.SelectNodes(".//Object")
                Write-Host ("  Direct Object elements: {0}" -f $directObjects.Count)

                # Look for Object elements in items
                $itemsObjects = $chunk.SelectNodes("items//Object")
                Write-Host ("  Object elements in items: {0}" -f $itemsObjects.Count)
            }
        }

        # Now let's search for our target string in a different way
        Write-Host "`nSearching for target string in all CodeInput elements..."
        $allCodeInputs = $xml.SelectNodes("//CodeInput")
        Write-Host ("Found {0} CodeInput elements total." -f $allCodeInputs.Count)

        $targetCodeInputIndex = -1
        for($i=0; $i -lt $allCodeInputs.Count; $i++) {
            $codeInput = $allCodeInputs[$i]
            if ($codeInput.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                $targetCodeInputIndex = $i
                Write-Host ("*** FOUND TARGET IN CODEINPUT INDEX {0} ***" -f $i)

                # Traverse up to find the Object element
                $current = $codeInput.ParentNode
                $levelsUp = 0
                while($current -and $levelsUp -lt 10) {
                    Write-Host ("  Level {0} up: {1}" -f $levelsUp, $current.Name)
                    if ($current.Name -eq "Object") {
                        Write-Host ("  *** FOUND OBJECT ELEMENT {0} LEVELS UP ***" -f $levelsUp)

                        # Show Object identifying information
                        $nickName = $current.SelectSingleNode(".//NickName")
                        if ($nickName) {
                            Write-Host ("    NickName: {0}" -f $nickName.InnerText)
                        } else {
                            Write-Host "    No NickName found."
                        }

                        $name = $current.SelectSingleNode(".//Name")
                        if ($name) {
                            Write-Host ("    Name: {0}" -f $name.InnerText)
                        } else {
                            Write-Host "    No Name found."
                        }

                        break
                    }
                    $current = $current.ParentNode
                    $levelsUp++
                }

                break
            }
        }

        if ($targetCodeInputIndex -lt 0) {
            Write-Host "Target string not found in any CodeInput element."
        }

    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}