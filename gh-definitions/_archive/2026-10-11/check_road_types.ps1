$files = Get-ChildItem -Path 'D:\Work\PROJECTS\Dise*\data\pot-cache' -Filter '*-contexto.json'
foreach ($file in $files) {
    try {
        $data = Get-Content $file.FullName -Raw | ConvertFrom-Json
        $chip = $data.metadata.chip
        $viasOf = if ($data.'vias_oficiales') { $data.'vias_oficiales'.Length } else { 0 }
        $viasSec = if ($data.'vias_secundarias') { $data.'vias_secundarias'.Length } else { 0 }
        $viasTer = if ($data.'vias_terciarias') { $data.'vias_terciarias'.Length } else { 0 }
        $peatonales = if ($data.peatonales) { $data.peatonales.Length } else { 0 }

        if ($viasSec -gt 0 -or $viasTer -gt 0 -or $peatonales -gt 0) {
            Write-Host ("{0}: OF={1} SEC={2} TER={3} PEAT={4}" -f $chip, $viasOf, $viasSec, $viasTer, $peatonales)
        }
    } catch {
        Write-Host ("Error processing {0}: {1}" -f $($file.Name), $_) -ForegroundColor Red
    }
}