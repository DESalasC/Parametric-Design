# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Examining ValueTable chunk in: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        # Find the ValueTable chunk
        $valueTable = $xml.SelectSingleNode("//chunk[@name='ValueTable']")
        if (-not $valueTable) {
            Write-Host "ERROR: Could not find ValueTable chunk"
            exit
        }

        Write-Host "Found ValueTable chunk."
        Write-Host ("  items count: {0}" -f $valueTable.SelectSingleNode("items").GetAttribute('count'))
        Write-Host ("  chunks count: {0}" -f $valueTable.SelectSingleNode("chunks").GetAttribute('count'))

        # Look at the chunks inside ValueTable
        $valueTableChunks = $valueTable.SelectSingleNode("chunks")
        if ($valueTableChunks) {
            Write-Host ("ValueTable has {0} chunks:" -f $valueTableChunks.ChildNodes.Count)
            for($i=0; $i -lt $valueTableChunks.ChildNodes.Count; $i++) {
                $chunk = $valueTableChunks.ChildNodes[$i]
                if ($chunk.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                    Write-Host ("  Chunk {0}: {1}" -f $i, $chunk.GetAttribute('name'))
                }
            }
        }

        # Now let's look for Object elements anywhere in ValueTable
        Write-Host "`nSearching for Object elements in ValueTable..."
        $objectsInValueTable = $valueTable.SelectNodes(".//Object")
        Write-Host ("Found {0} Object elements in ValueTable." -f $objectsInValueTable.Count)

        if ($objectsInValueTable.Count -gt 0) {
            Write-Host "Examining Object elements:"
            for($j=0; $j -lt $objectsInValueTable.Count; $j++) {
                $obj = $objectsInValueTable[$j]
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
            Write-Host "No Object elements found in ValueTable."
        }

        # Let's also check if there are any elements with our target string in ValueTable
        Write-Host "`nSearching for target string in ValueTable elements..."
        $targetMatches = $valueTable.SelectNodes(".//*[contains(text(), 'F1_ETAPA1_CONTEXTO_v02')]")
        Write-Host ("Found {0} elements containing target string in ValueTable." -f $targetMatches.Count)
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