$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

try {
    [xml]$xml = Get-Content -Path $path
    Write-Host "Loaded XML successfully."

    # Get all CodeInput item nodes
    $codeInputItems = $xml.SelectNodes("//item[@name='CodeInput']")
    Write-Host ("Found {0} CodeInput item nodes." -f $codeInputItems.Count)

    $targetIndex = -1
    for($i=0; $i -lt $codeInputItems.Count; $i++) {
        $item = $codeInputItems[$i]
        if ($item.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
            $targetIndex = $i
            Write-Host ("*** FOUND TARGET IN CODEINPUT ITEM INDEX {0} ***" -f $i)
            break
        }
    }

    if ($targetIndex -ge 0) {
        $targetItem = $codeInputItems[$targetIndex]
        Write-Host ("Target CodeInput item inner text length: {0}" -f $targetItem.InnerText.Length)

        # Now traverse up to find the Object chunk
        $current = $targetItem
        $levelsUp = 0
        $objectChunk = $null
        while($current -and $levelsUp -lt 20) {
            # Check if current is a chunk with name="Object"
            if ($current.Name -eq "chunk" -and $current.GetAttribute('name') -eq "Object") {
                $objectChunk = $current
                Write-Host ("  Found Object chunk at level {0} up." -f $levelsUp)
                break
            }
            $current = $current.ParentNode
            $levelsUp++
        }

        if ($objectChunk) {
            Write-Host ("  Object chunk name: {0}" -f $objectChunk.GetAttribute('name'))
            # Now get the items element of this Object chunk
            $objectItems = $objectChunk.SelectSingleNode("items")
            if ($objectItems) {
                Write-Host ("  Object items count: {0}" -f $objectItems.GetAttribute('count'))

                # Look for GUID, Name, NickName
                $guidItem = $objectItems.SelectSingleNode(".//item[@name='GUID']")
                $nameItem = $objectItems.SelectSingleNode(".//item[@name='Name']")
                $nickNameItem = $objectItems.SelectSingleNode(".//item[@name='NickName']")

                Write-Host ("  Identifying information:")
                if ($guidItem) {
                    Write-Host ("    GUID: {0}" -f $guidItem.InnerText)
                } else {
                    Write-Host "    No GUID item found."
                }
                if ($nameItem) {
                    Write-Host ("    Name: {0}" -f $nameItem.InnerText)
                } else {
                    Write-Host "    No Name item found."
                }
                if ($nickNameItem) {
                    Write-Host ("    NickName: {0}" -f $nickNameItem.InnerText)
                } else {
                    Write-Host "    No NickName item found."
                }

                # Also, let's verify that the CodeInput we found is indeed in this Object's items
                $codeInputInObject = $objectItems.SelectSingleNode(".//item[@name='CodeInput']")
                if ($codeInputInObject) {
                    Write-Host ("  CodeInput in Object: length {0}" -f $codeInputInObject.InnerText.Length)
                    if ($codeInputInObject.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                        Write-Host "    Contains target string."
                    }
                }
            } else {
                Write-Host "  No items element found in Object chunk."
            }
        } else {
            Write-Host "  Could not find Object chunk by traversing up."
        }
    } else {
        Write-Host "Target string not found in any CodeInput item."
    }

} catch {
    Write-Host "An error occurred:"
    Write-Host $_.Exception.Message
}