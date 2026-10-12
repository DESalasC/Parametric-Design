$files = Get-ChildItem -Path 'D:\Work\PROJECTS\Dise*\data\pot-cache' -Filter '*-contexto.json'
foreach ($file in $files) {
    try {
        $data = Get-Content $file.FullName -Raw | ConvertFrom-Json
        $chip = $data.metadata.chip

        $viasOfCount = if ($data.'vias_oficiales') { $data.'vias_oficiales'.Length } else { 0 }
        $viasSecCount = if ($data.'vias_secundarias') { $data.'vias_secundarias'.Length } else { 0 }
        $viasTerCount = if ($data.'vias_terciarias') { $data.'vias_terciarias'.Length } else { 0 }
        $peatonalesCount = if ($data.peatonales) { $data.peatonales.Length } else { 0 }

        Write-Host ("{0}: OF={1} SEC={2} TER={3} PEAT={4}" -f $chip, $viasOfCount, $viasSecCount, $viasTerCount, $peatonalesCount)
    } catch {
        Write-Host ("Error processing {0}: {1}" -f $($file.Name), $_) -ForegroundColor Red
    }
}