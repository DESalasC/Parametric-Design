$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

try {
    [xml]$xml = Get-Content -Path $path
    Write-Host "Loaded XML successfully."

    # Let's try to get the CodeInput element by its full path
    # From the raw check, we saw it's in an item with name="CodeInput"
    $codeInputNode = $xml.SelectSingleNode("//item[@name='CodeInput']")
    if ($codeInputNode) {
        Write-Host "Found CodeInput node by attribute."
        Write-Host ("  Inner text length: {0}" -f $codeInputNode.InnerText.Length)
        if ($codeInputNode.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
            Write-Host "  Contains target string."
        } else {
            Write-Host "  Does NOT contain target string."
            # Show first 100 chars
            Write-Host ("  First 100 chars: {0}" -f $codeInputNode.InnerText.Substring(0, [Math]::Min(100, $codeInputNode.InnerText.Length)))
        }
    } else {
        Write-Host "CodeInput node NOT found by attribute."
    }

    # Let's also try to get all item nodes and see their names
    $itemNodes = $xml.SelectNodes("//item")
    Write-Host ("Found {0} item nodes." -f $itemNodes.Count)
    $codeInputItems = @()
    foreach($item in $itemNodes) {
        if ($item.GetAttribute('name') -eq 'CodeInput') {
            $codeInputItems += $item
        }
    }
    Write-Host ("Found {0} item nodes with name='CodeInput'." -f $codeInputItems.Count)
    for($i=0; $i -lt $codeInputItems.Count; $i++) {
        $item = $codeInputItems[$i]
        Write-Host ("  Item {0}: inner text length {1}" -f $i, $item.InnerText.Length)
        if ($item.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
            Write-Host "    Contains target string."
        }
    }

} catch {
    Write-Host "An error occurred:"
    Write-Host $_.Exception.Message
}