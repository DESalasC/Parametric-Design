# Use wildcard to handle special characters in directory name
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Exploring GHX structure in: $path"
if (Test-Path $path) {
    try {
        [xml]$xml = Get-Content -Path $path
        Write-Host "Loaded XML successfully."

        # Let's look for Definition or DefinitionObjects elements
        Write-Host "`nLooking for Definition/DefinitionObjects elements..."
        $defObj = $xml.SelectSingleNode("//DefinitionObjects")
        if ($defObj) {
            Write-Host "Found DefinitionObjects element."
            Write-Host ("  Name: {0}" -f $defObj.Name)
            Write-Host ("  Number of child elements: {0}" -f $defObj.ChildNodes.Count)

            # Look for Object elements within DefinitionObjects
            $objects = $defObj.SelectNodes(".//Object")
            Write-Host ("  Found {0} Object elements." -f $objects.Count)

            if ($objects.Count -gt 0) {
                Write-Host "  Examining first few Object elements:"
                for($i=0; $i -lt [Math]::Min(3, $objects.Count); $i++) {
                    $obj = $objects[$i]
                    Write-Host ("    Object {0}:" -f $i)
                    Write-Host ("      Name: {0}" -f $obj.Name)

                    # Look for NickName
                    $nickName = $obj.SelectSingleNode(".//NickName")
                    if ($nickName) {
                        Write-Host ("      NickName: {0}" -f $nickName.InnerText)
                    }

                    # Look for Name
                    $name = $obj.SelectSingleNode(".//Name")
                    if ($name) {
                        Write-Host ("      Name: {0}" -f $name.InnerText)
                    }

                    # Look for InstanceGuid
                    $instanceGuid = $obj.SelectSingleNode(".//InstanceGuid")
                    if ($instanceGuid) {
                        Write-Host ("      InstanceGuid: {0}" -f $instanceGuid.InnerText)
                    }

                    # Look for CodeInput
                    $codeInput = $obj.SelectSingleNode(".//CodeInput")
                    if ($codeInput) {
                        Write-Host ("      CodeInput: {0} chars" -f $codeInput.InnerText.Length)
                        if ($codeInput.InnerText -like "*F1_ETAPA1_CONTEXTO_v02*") {
                            Write-Host "      *** THIS IS THE TARGET COMPONENT! ***"
                        }
                    }
                }
            }
        } else {
            Write-Host "DefinitionObjects element not found."
        }

        # Also look for Definition element
        Write-Host "`nLooking for Definition element..."
        $definition = $xml.SelectSingleNode("//Definition")
        if ($definition) {
            Write-Host "Found Definition element."
            Write-Host ("  Name: {0}" -f $definition.Name)
            Write-Host ("  Number of child elements: {0}" -f $definition.ChildNodes.Count)

            # Look for Objects within Definition
            $defObjects = $definition.SelectNodes(".//Object")
            Write-Host ("  Found {0} Object elements in Definition." -f $defObjects.Count)
        }

        # Let's also check if there are any elements with our target string in their attributes
        Write-Host "`nSearching for target string in element attributes..."
        $attrMatches = $xml.SelectNodes("//*[@*[contains(., 'F1_ETAPA1_CONTEXTO_v02')]]")
        Write-Host ("Found {0} elements with attributes containing target string." -f $attrMatches.Count)
        for($i=0; $i -lt $attrMatches.Count; $i++) {
            $elem = $attrMatches[$i]
            Write-Host ("  Element: {0}" -f $elem.Name)
            foreach($attr in $elem.Attributes) {
                if ($attr.Value -like "*F1_ETAPA1_CONTEXTO_v02*") {
                    Write-Host ("    Attribute {0} = {1}" -f $attr.Name, $attr.Value)
                }
            }
        }

        # Let's check what the root element contains directly
        Write-Host "`nExamining root element children..."
        $root = $xml.DocumentElement
        Write-Host ("Root element: {0}" -f $root.Name)
        Write-Host ("Root child elements count: {0}" -f $root.ChildNodes.Count)

        foreach($child in $root.ChildNodes) {
            if ($child.NodeType -eq [System.Xml.XmlNodeType]::Element) {
                Write-Host ("  Child: {0}" -f $child.Name)
                if ($child.Attributes.Count -gt 0) {
                    Write-Host "    Attributes:"
                    foreach($attr in $child.Attributes) {
                        Write-Host ("      {0} = {1}" -f $attr.Name, $attr.Value)
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