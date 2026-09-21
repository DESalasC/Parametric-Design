# Resolve the path first to handle special characters
$wildcardPath = 'D:\Work\PROJECTS\Dise*/gh-definitions/F1_CONTEXTO_v11.ghx'
$resolvedPath = Resolve-Path -Path $wildcardPath
$path = $resolvedPath.Path

Write-Host "Using resolved path: $path"

# Get lines around the matches
$lines = [System.IO.File]::ReadAllLines($path)
Write-Host "Total lines: $($lines.Length)"

# Function to show context
function Show-Context($lineNumber, $contextLines) {
    $start = [Math]::Max(0, $lineNumber - $contextLines - 1) # zero-based index
    $end = [Math]::Min($lines.Length, $lineNumber + $contextLines) # exclusive
    Write-Host "`n--- Context around line $lineNumber ---"
    for($i=$start; $i -lt $end; $i++) {
        $prefix = if($i+1 -eq $lineNumber) { "> " } else { "  " }
        Write-Host "$prefix$($i+1): $($lines[$i])"
    }
}

Show-Context -lineNumber 1375 -contextLines 10
Show-Context -lineNumber 2581 -contextLines 10