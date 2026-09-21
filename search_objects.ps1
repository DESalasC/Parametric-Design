# Resolve the path first to handle special characters
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Using resolved path: $path"

# Read the file as text
$content = [System.IO.File]::ReadAllText($path)
Write-Host ("File length: {0} characters" -f $content.Length)

# Search for Objects section
if ($content -match '<Objects>.*?</Objects>') {
    $objectsSection = $matches[0]
    Write-Host "Found Objects section:"
    Write-Host $objectsSection

    # Extract all NickName values
    if ($objectsSection -match '<NickName>(.*?)</NickName>') {
        $matches = [regex]::Matches($objectsSection, '<NickName>(.*?)</NickName>')
        Write-Host ("Found {0} NickName entries:" -f $matches.Count)
        for($i=0; $i -lt $matches.Count; $i++) {
            Write-Host ("  {0}: {1}" -f ($i+1), $matches[$i].Groups[1].Value)
        }
    }
} else {
    Write-Host "No Objects section found with regex"

    # Try to find Object elements
    if ($content -match '<Object.*?</Object>') {
        $matches = [regex]::Matches($content, '<Object.*?</Object>', [System.Text.RegularExpressions.RegexOptions]::Singleline)
        Write-Host ("Found {0} Object elements:" -f $matches.Count)
        for($i=0; $i -lt [Math]::Min($matches.Count, 10); $i++) {
            $obj = $matches[$i].Value
            if ($obj -match '<NickName>(.*?)</NickName>') {
                Write-Host ("  Object {0}: NickName = {1}" -f ($i+1), $matches[0].Groups[1].Value)
            }
        }
    }
}

// Also let's look for the specific nickname we're looking for
if ($content -match 'F1_ETAPA1_CONTEXTO_v02') {
    Write-Host "Found 'F1_ETAPA1_CONTEXTO_v02' in the file"
    # Show context around the match
    $index = $content.IndexOf('F1_ETAPA1_CONTEXTO_v02')
    $start = [Math]::Max(0, $index - 100)
    $length = [Math]::Min(200, $content.Length - $start)
    $context = $content.Substring($start, $length)
    Write-Host "Context: ...$context..."
} else {
    Write-Host "'F1_ETAPA1_CONTEXTO_v02' NOT found in the file"
}