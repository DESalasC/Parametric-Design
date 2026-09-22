$file = 'D:\Work\PROJECTS\Dise*\data\pot-cache\AAA0030JKOE-contexto.json'
$data = Get-Content $file -Raw | ConvertFrom-Json
Write-Host ("Chip: {0}" -f $data.metadata.chip)

$viasOfCount = if ($data.'vias_oficiales') { $data.'vias_oficiales'.Length } else { 0 }
Write-Host ("Vias oficiales: {0}" -f $viasOfCount)

$viasSecCount = if ($data.'vias_secundarias') { $data.'vias_secundarias'.Length } else { 0 }
Write-Host ("Vias secundarias: {0}" -f $viasSecCount)

$viasTerCount = if ($data.'vias_terciarias') { $data.'vias_terciarias'.Length } else { 0 }
Write-Host ("Vias terciarias: {0}" -f $viasTerCount)

$peatonalesCount = if ($data.peatonales) { $data.peatonales.Length } else { 0 }
Write-Host ("Peatonales: {0}" -f $peatonalesCount)