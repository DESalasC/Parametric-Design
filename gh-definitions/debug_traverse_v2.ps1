$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

try {
    [xml]$xml = Get-Content -Path $path
    Write-Host "Loaded XML successfully."

    # Get the target CodeInput item (we know it's index 1 from previous run)
    $codeInputItems = $xml.SelectNodes("//item[@name='CodeInput']")
    $targetItem = $codeInputItems[1]
    Write-Host ("Target CodeInput item inner text length: {0}" -f $targetItem.InnerText.Length)

    # Traverse up and record the chain
    $chain = @()
    $current = $targetItem
    $levelsUp = 0
    while($current -and $levelsUp -lt 20) {
        $nodeInfo = "{0}: {1}" -f $levelsUp, $current.Name
        if ($current -is [System.Xml.XmlElement]) {
            $nameAttr = $current.GetAttribute('name')
            if ($nameAttr) {
                $nodeInfo += " (name='{0}')" -f $nameAttr
            }
        }
        $chain += $nodeInfo
        $current = $current.ParentNode
        $levelsUp++
    }

    Write-Host ("Chain of {0} nodes:" -f $chain.Count)
    $chain | ForEach-Object { Write-Host "  $_" }

    // Now look for Object chunk in the chain
    $objectChunkFound = $false
    foreach($link in $chain) {
        if ($link -like "*name='Object'*" -and $link -like "*chunk*") {
            Write-Host "Found Object chunk in chain: {0}" -f $link
            $objectChunkFound = $true
            break
        }
    }
    if (-not $objectChunkFound) {
        Write-Host "Object chunk NOT found in chain."
    }

} catch {
    Write-Host "An error occurred:"
    Write-Host $_.Exception.Message
}