[xml]$xml = Get-Content gh-definitions\F1_CONTEXTO_v13.5.ghx
$objects = $xml.SelectNodes('//chunk[@name="Object"]')
foreach ($obj in $objects) {
    $guid = $obj.GetAttribute('instanceGuid')
    if ($guid -eq "6eaf2956-f649-4540-a900-4b32a10deee4") {
        $nick = $obj.GetAttribute('nickName')
        Write-Host "Found Object: NickName='$nick', GUID=$guid"
        $scriptFile = $obj.SelectSingleNode('.//chunk[@name="ScriptFile"]')
        if ($scriptFile) {
            $script = $scriptFile.SelectSingleNode('.//chunk[@name="script"]')
            if ($script -and $script.FirstChild) {
                $text = $script.FirstChild.InnerText
                Write-Host "Script length: $($text.Length)"
                $lines = $text.Split("`n")
                Write-Host "First 5 lines:"
                for ($i=0; $i -lt [Math]::Min(5, $lines.Length); $i++) {
                    Write-Host "  $($lines[$i])"
                }
                Write-Host "Last 5 lines:"
                for ($i=[Math]::Max(0, $lines.Length-5); $i -lt $lines.Length; $i++) {
                    Write-Host "  $($lines[$i])"
                }
            }
        }
    }
}