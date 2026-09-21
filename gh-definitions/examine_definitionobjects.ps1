# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Examining DefinitionObjects chunk in: $path"
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

        # Look at the items inside DefinitionObjects
        $definitionObjectsItems = $definitionObjectsChunk.SelectSingleNode("items")
        if ($definitionObjectsItems) {
            Write-Host ("DefinitionObjects has {0} items:" -f $definitionObjectsItems.GetAttribute('count'))
        } else {
            Write-Host "DefinitionObjects has no items node."
        }

        # Look at the chunks inside DefinitionObjects
        $definitionObjectsChunks = $definitionObjectsChunk.SelectSingleNode("chunks")
        if ($definitionObjectsChunks) {
            Write-Host ("DefinitionObjects has {0} chunks:" -f $definitionObjectsChunks.ChildNodes.Count)
            for($i=0; $i -lt $definitionObjectsChunks.ChildNodes.Count; $i++) {
                $chunk = $definitionObjectsChunks.ChildNodes[$i]
                if ($chunk.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                    Write-Host ("  Chunk {0}: {1}" -f $i, $chunk.GetAttribute('name'))
                }
            }
        } else {
            Write-Host "DefinitionObjects has no chunks node."
        }

        # Now let's look for Object elements anywhere in DefinitionObjects
        Write-Host "`nSearching for Object elements in DefinitionObjects..."
        $objectsInDefinitionObjects = $definitionObjectsChunk.SelectNodes(".//Object")
        Write-Host ("Found {0} Object elements in DefinitionObjects." -f $objectsInDefinitionObjects.Count)

        if ($objectsInDefinitionObjects.Count -gt 0) {
            Write-Host "Examining Object elements:"
            for($j=0; $j -lt $objectsInDefinitionObjects.Count; $j++) {
                $obj = $objectsInDefinitionObjects[$j]
                Write-Host ("`nObject {0}:" -f $j)
                Write-Host ("  Name: {0}" -f $obj.Name)

                # Look for identifying elements
                $nickName = $obj.SelectSingleNode(".//NickName")
                if ($nickName) {
                    Write-Host ("  NickName: {0}" -f $nickName.InnerText)
                }

                $name = $obj.SelectSingleNode(".//Name")
                if ($name) {
                    Write-Host ("  Name: {0}" -f $name.InnerText)
                }

                $instanceGuid = $obj.SelectSingleNode(".//InstanceGuid")
                if ($instanceGuid) {
                    Write-Host ("  InstanceGuid: {0}" -f $instanceGuid.InnerText)
                }

                # Look for CodeInput
                $codeInput = $obj.SelectSingleNode(".//CodeInput")
                if ($codeInput) {
                    Write-Host ("  CodeInput: {0} chars" -f $codeInput.InnerText.Length)
                    if ($codeInput.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                        Write-Host "  *** THIS IS THE TARGET COMPONENT! ***"

                        # Show preview
                        $preview = $codeInput.InnerText.Substring(0, [Math]::Min(200, $codeInput.InnerText.Length))
                        Write-Host ("  Preview: {0}" -f $preview)
                    }
                }
            }
        } else {
            Write-Host "No Object elements found in DefinitionObjects."
        }

        # Let's also check if there are any elements with our target string in DefinitionObjects
        Write-Host "`nSearching for target string in DefinitionObjects elements..."
        $targetMatches = $definitionObjectsChunk.SelectNodes(".//*[contains(text(), 'F1_ETAPA1_CONTEXTO_v02')]")
        Write-Host ("Found {0} elements containing target string in DefinitionObjects." -f $targetMatches.Count)
        for($i=0; $i -lt $targetMatches.Count; $i++) {
            $elem = $targetMatches[$i]
            Write-Host ("  Match {0}: {1}" -f $i, $elem.Name)
            if ($elem.InnerText.Length -lt 200) {
                Write-Host ("     Content: {0}" -f $elem.InnerText)
            } else {
                Write-Host ("     Content starts with: {0}" -f $elem.InnerText.Substring(0, 100))
            }

            # Show parent info
            if ($elem.ParentNode) {
                Write-Host ("     Parent: {0}" -f $elem.ParentNode.Name)
                # Check if parent is an Object
                if ($elem.ParentNode.Name -eq "Object") {
                    Write-Host ("     *** PARENT IS AN OBJECT! ***")
                    # Look for NickName in this object
                    $objNickName = $elem.ParentNode.SelectSingleNode(".//NickName")
                    if ($objNickName) {
                        Write-Host ("     Object NickName: {0}" -f $objNickName.InnerText)
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