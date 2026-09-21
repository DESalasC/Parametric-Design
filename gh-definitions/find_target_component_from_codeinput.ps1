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
        $current = $targetItem.ParentNode  # This should be the items element
        $levelsUp = 0
        while($current -and $levelsUp -lt 10) {
            Write-Host ("  Level {0} up: {1}" -f $levelsUp, $current.Name)
            if ($current.Name -eq "items") {
                # Go up one more to see if it's a chunk
                $chunkCandidate = $current.ParentNode
                if ($chunkCandidate -and $chunkCandidate.Name -eq "chunk") {
                    Write-Host ("    Parent chunk name: {0}" -f $chunkCandidate.GetAttribute('name'))
                    if ($chunkCandidate.GetAttribute('name') -eq "Object") {
                        Write-Host ("    *** FOUND OBJECT CHUNK! ***")
                        # Now we have the Object chunk, let's get its identifying information
                        $objectItems = $chunkCandidate.SelectSingleNode("items")
                        if ($objectItems) {
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
                        }
                        break
                    }
                }
            }
            $current = $current.ParentNode
            $levelsUp++
        }
    } else {
        Write-Host "Target string not found in any CodeInput item."
    }

} catch {
    Write-Host "An error occurred:"
    Write-Host $_.Exception.Message
}