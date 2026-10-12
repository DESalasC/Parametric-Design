# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Examining Object chunk structure in: $path"
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

        Write-Host "Found DefinitionObjects chunk with {0} chunks." -f $definitionObjectsChunk.SelectSingleNode("chunks").ChildNodes.Count

        # Let's examine a few chunks to understand the structure
        $allChunks = $definitionObjectsChunk.SelectSingleNode("chunks")
        for($chunkIndex=0; $chunkIndex -lt [Math]::Min(10, $allChunks.ChildNodes.Count); $chunkIndex++) {
            $chunk = $allChunks.ChildNodes[$chunkIndex]
            if ($chunk.NodeType -eq [System.Xml.XmlNodeType]::Element -and $chunk.Name -eq "chunk") {
                Write-Host ("`n=== Examining chunk {0} (name: {1}) ===" -f $chunkIndex, $chunk.GetAttribute('name'))

                # Look at items in this chunk
                $items = $chunk.SelectSingleNode("items")
                if ($items) {
                    Write-Host ("  Items count: {0}" -f $items.GetAttribute('count'))

                    # Look for GUID and Name elements
                    $guidElement = $items.SelectSingleNode(".//GUID")
                    $nameElement = $items.SelectSingleNode(".//Name")

                    if ($guidElement) {
                        Write-Host ("  GUID: {0}" -f $guidElement.InnerText)
                    }
                    if ($nameElement) {
                        Write-Host ("  Name: {0}" -f $nameElement.InnerText)
                    }

                    # Look for CodeInput element
                    $codeInputElement = $items.SelectSingleNode(".//CodeInput")
                    if ($codeInputElement) {
                        Write-Host ("  CodeInput found (length: {0})" -f $codeInputElement.InnerText.Length)
                        if ($codeInputElement.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                            Write-Host "  *** THIS IS OUR TARGET COMPONENT! ***"

                            # Show identifying information
                            if ($guidElement) {
                                Write-Host ("  Component GUID: {0}" -f $guidElement.InnerText)
                            }
                            if ($nameElement) {
                                Write-Host ("  Component Name: {0}" -f $nameElement.InnerText)
                            }

                            # Show preview of the code
                            $preview = $codeInputElement.InnerText.Substring(0, [Math]::Min(200, $codeInputElement.InnerText.Length))
                            Write-Host ("  Code preview: {0}" -f $preview)

                            # We found it! Let's stop searching
                            Write-Host "`nTarget component found at chunk index {0}!" -f $chunkIndex
                            return
                        }
                    } else {
                        Write-Host "  No CodeInput element found."
                    }
                } else {
                    Write-Host "  No items element found."
                }
            }
        }

        Write-Host "`nTarget component not found in first 10 chunks."

    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}