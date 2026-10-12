$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

try {
    [xml]$xml = Get-Content -Path $path
    Write-Host "Loaded XML successfully."

    # Get the target CodeInput item (we know it's index 1 from previous runs)
    $codeInputItems = $xml.SelectNodes("//item[@name='CodeInput']")
    $targetItem = $codeInputItems[1]
    Write-Host ("Target CodeInput item inner text length: {0}" -f $targetItem.InnerText.Length)
    Write-Host ("Target CodeInput item type: {0}" -f $targetItem.GetType().Name)
    Write-Host ("Target CodeInput item name: {0}" -f $targetItem.Name)

    # Traverse up and examine each level
    $current = $targetItem
    $levelsUp = 0
    while($current -and $levelsUp -lt 10) {
        Write-Host ("Level {0}:" -f $levelsUp)
        Write-Host ("  Type: {0}" -f $current.GetType().Name)
        Write-Host ("  Name: {0}" -f $current.Name)
        if ($current -is [System.Xml.XmlElement]) {
            $nameAttr = $current.GetAttribute('name')
            if ($nameAttr) {
                Write-Host ("  Attribute 'name': {0}" -f $nameAttr)
                if ($nameAttr -eq "Object") {
                    Write-Host ("  *** THIS IS AN OBJECT CHUNK! ***")
                }
            }
        }
        Write-Host ""
        $current = $current.ParentNode
        $levelsUp++
    }

} catch {
    Write-Host "An error occurred:"
    Write-Host $_.Exception.Message
}