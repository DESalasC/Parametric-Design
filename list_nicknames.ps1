Add-Type -Path "C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"
$doc = New-Object GH_IO.Serialization.GH_Archive
$doc.ReadFromFile(".\gh-definitions\F1_CONTEXTO_v11.ghx")
$doc.Objects | ForEach-Object { $_.NickName }
