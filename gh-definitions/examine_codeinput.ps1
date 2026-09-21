# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Examining CodeInput elements in: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        # Find all CodeInput elements
        $codeInputs = $xml.SelectNodes("//CodeInput")
        Write-Host "Found $($codeInputs.Count) CodeInput elements."

        # Look for the specific one we want
        $targetFound = $false
        for($i=0; $i -lt $codeInputs.Count; $i++) {
            $codeInput = $codeInputs[$i]
            if ($codeInput.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                Write-Host "`n=== Found target CodeInput at index $i ==="
                Write-Host "Parent element: $($codeInput.ParentNode.Name)"

                # Let's examine the parent hierarchy
                $parent = $codeInput.ParentNode
                $level = 0
                while($parent -and $level -lt 5) {
                    Write-Host ("  Level {0}: {1}" -f $level, $parent.Name)
                    if ($parent.Attributes.Count -gt 0) {
                        foreach($attr in $parent.Attributes) {
                            Write-Host ("    {0} = {1}" -f $attr.Name, $attr.Value)
                        }
                    }
                    $parent = $parent.ParentNode
                    $level++
                }

                # Look for NickName or similar identifiers in siblings or ancestors
                Write-Host "`nChecking for NickName or identifier elements..."
                $ancestor = $codeInput.ParentNode
                while($ancestor -and $level -lt 10) {
                    // Look for NickName, Name, or similar elements
                    $nickName = $ancestor.SelectSingleNode(".//NickName")
                    if ($nickName) {
                        Write-Host ("Found NickName at ancestor level {0}: '{1}'" -f $level, $nickName.InnerText)
                        $targetFound = $true
                        break
                    }
                    $nameElem = $ancestor.SelectSingleNode(".//Name")
                    if ($nameElem) {
                        Write-Host ("Found Name at ancestor level {0}: '{1}'" -f $level, $nameElem.InnerText)
                    }
                    $ancestor = $ancestor.ParentNode
                    $level++
                }

                if (-not $targetFound) {
                    Write-Host "No NickName or Name elements found in ancestors."

                    // Let's see what elements ARE present in the immediate parent
                    Write-Host "`nElements in immediate parent:"
                    foreach($child in $codeInput.ParentNode.ChildNodes) {
                        if ($child.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                            Write-Host ("  {0} (inner text length: {1})" -f $child.Name, $child.InnerText.Length)
                        }
                    }
                }

                // Show a preview of the code
                Write-Host "`nCode preview (first 200 chars):"
                $preview = $codeInput.InnerText.Substring(0, [Math]::Min(200, $codeInput.InnerText.Length))
                Write-Host $preview

                break
            }
        }

        if (-not $targetFound) {
            Write-Host "Target CodeInput not found."
        }

    } catch {
        Write-Host "Failed to load XML: $_"
    }
} else {
    Write-Host "File does not exist."
}