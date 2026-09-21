# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

try {
    [xml]$xml = Get-Content -Path $path
    Write-Host "Loaded XML successfully."

    # Find all elements with local name CodeInput
    $codeInputs = $xml.SelectNodes("//*[local-name()='CodeInput']")
    Write-Host ("Found {0} elements with local-name CodeInput." -f $codeInputs.Count)

    $found = $false
    for($i=0; $i -lt $codeInputs.Count; $i++) {
        $ci = $codeInputs[$i]
        if ($ci.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
            Write-Host ("*** FOUND TARGET IN CODEINPUT INDEX {0} ***" -f $i)
            Write-Host ("  Element name: {0}" -f $ci.Name)
            Write-Host ("  CodeInput length: {0}" -f $ci.InnerText.Length)
            $found = $true
            # Traverse up to find the Object element
            $current = $ci.ParentNode
            $level = 0
            while($current -and $level -lt 20) {
                Write-Host ("  Level {0} up: {1}" -f $level, $current.Name)
                if ($current.Name -eq "Object") {
                    Write-Host ("  FOUND OBJECT ELEMENT {0} LEVELS UP" -f $level)
                    # Show identifying information
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
                    $guid = $current.SelectSingleNode(".//GUID")
                    if ($guid) {
                        Write-Host ("    GUID: {0}" -f $guid.InnerText)
                    } else {
                        Write-Host "    No GUID found."
                    }
                    break
                }
                $current = $current.ParentNode
                $level++
            }
            break
        }
    }

    if (-not $found) {
        Write-Host "Target string not found in any CodeInput element."
        # Let's see what the first few such elements contain
        for($i=0; $i -lt [Math]::Min(5, $codeInputs.Count); $i++) {
            $ci = $codeInputs[$i]
            Write-Host ("Element {0} name: {1}, length: {2}" -f $i, $ci.Name, $ci.InnerText.Length)
            if ($ci.InnerText.Length -lt 100) {
                Write-Host ("  Content: {0}" -f $ci.InnerText)
            } else {
                Write-Host ("  Starts with: {0}" -f $ci.InnerText.Substring(0, 50))
            }
        }
    }

} catch {
    Write-Host "An error occurred:"
    Write-Host $_.Exception.Message
}