# Inventario del canvas — F1_CONTEXTO_v13.5 (2026-10-11 22:18)

Generado por `scripts/utilities/inventario-canvas.py`. Estado: **inventario vivo** (se actualiza a medida que avanza el canvas; no implica limpieza — punto 8 reformulado 2026-10-11).

## Resumen

| Clasificacion | Cuenta |
|---|---|
| Grupo | 134 |
| Informativo (Panel) | 95 |
| Entrada (UI) | 44 |
| LC -> ArchiCAD | 40 |
| Soporte (util) | 39 |
| Logica (script) | 19 |
| Otro | 6 |
| **TOTAL** | **377** |

### Cambios vs 2026-10-09 (noche)

- Nuevos: dd1fc9ba #242-Zone, e9607073 #241-Zone Settings, 828c34ab #236-Boolean Toggle, b2484541 #230-Layer, f8f36bf8 #232-Line Type, 380e0aa5 #233-Pen, 10532c0d #231-2D Viewpoint, e5ef868b #234-Number Slider, f6e78136 #235-Number Slider, 921141e7 #156-Panel, c51b3e5c , bcabde6b Ocupaciones por piso, 4444cede , 62e64c98 Ocupaciones por piso, b5256602 Ocupaciones por piso, dcca63ed F1_ETAPA2_NORMATIVA_v10.py, a0d539fd Base normativa · límites para distribución, d4aa2e48 #157-Panel, ad1f7c90 #160-Panel, 66c3f7a4 GhPython Script, 1fc65c1e GhPython Script, 95085a1d GhPython Script, a77cc3a0 GhPython Script, 24d07532 File Path, 653ba5b1 2D Polyline, ac31b9be Layer, d23bb2c0 Line Type, 7fe40b57 Polyline Settings, dc39e94d Pen, e39fbfbb 2D Viewpoint, 4b900851 Relay, c74b7a94 2D Polyline, 80319fd1 Layer, 656db93c Line Type, dade3cd9 Polyline Settings, 084be978 Pen, 8edbf330 2D Viewpoint, b74fc9b4 Merge, cfcd060c 2D Polyline, ea19d3ee Layer, ee8b1809 Line Type, c2a2815f Polyline Settings, ea1aaf6f Pen, f0f06b7e 2D Viewpoint, c4d653b3 Relay, 11b98876 GhPython Script, b658a37e GhPython Script, 4126f986 GhPython Script, fbdcec7f GhPython Script, f2a60e3a Relay, aec8eb51 Area, 604a0309 Value List, 4870ebe5 Value List, 5f84844c Addition, 32858c60 GhPython Script, 7d6ed153 GhPython Script, 86df9c01 Relay, 4c2febf1 Value List, e2365733 Curve, d830771b Curve, 327e5b72 Curve, 7b786066 Deconstruct 2D Polyline, 9e23cc66 Deconstruct 2D Polyline, 7468089c Relay, 1d39d7be Deconstruct 2D Polyline, b385f0bd Relay, 3b0c13d7 Relay, b2d84cc8 Deconstruct 2D Polyline, f9850dd2 Discontinuity, 58bebead GhPython Script, db41cf38 Text Join, 0f0dd9c3 Merge, f62705a6 File Path, 0307009e Text Join, 6804758d Merge, d605a481 Deconstruct 2D Polyline, 43bad581 Text Join, 5df11558 Merge, 5e4574ae GhPython Script, bdaf80ce Merge, 9d399dd1 File Path, 48a10705 Text Join, 43de239b Morph Solid, 8597969f Bifocals, e10ae037 Polyline Settings, 3df2f94b Curve, 739aad43 2D Polyline, 72109838 Layer, f6dca2d9 2D Viewpoint, 28a8f8f0 Line Type, b274f661 Pen, 7a3598ea Merge, f210e566 Mesh, b54076d8 Relay, 691f6795 Mesh, 7d62e125 CreateMeshes, 4744dbec MeshSkirtTypes, 05a5d042 MeshRidgeTypes, 55ce2018 Deconstruct Mesh, bf2a992c Relay, 905a123a Relay, d986fa47 Relay, 5eb1b0d7 Deconstruct 2D Polyline, bda3fcdb 2D Curve, f6a2508e PolylineDetails, a173df40 End Points, 82a62dbb Relay, 03f30d6a File Path, bc74d728 GhPython Script, 50bb986e GhPython Script, 39d55583 GhPython Script, d6e38120 GhPython Script, f380bfb9 GhPython Script, 4b5a4d6f GhPython Script, 6fbe85e5 Merge, 52305f84 Merge, 35e56cd0 Text Join, 7184e7d3 Text Join, 759cecb7 Relay, 47f99169 Merge, 156f20b0 Text Join, d98de3cb Value List, 6a18beb3 Value List, 04b339dd Merge, c5e85644 Text Join, f60b9736 Zone, 4cc7c8d7 Zone Settings, 259aa7b9 Layer, a884cb60 Line Type, d785abe5 Pen, f76e9b10 2D Viewpoint, 86a44bef Python 3 Script
- Renombrados: 0d986a36: #72-F1_ETAPA1_CONTEXTO_v04.4.1.py -> #79-F1_ETAPA1_CONTEXTO_v04.4.1.py; d4aab682: #154-F1_ETAPA2_NORMATIVA_v09.1.py -> #124-F1_ETAPA2_NORMATIVA_v09.1.py; d3bed17b: #161-F1_ETAPA2_PATIO_v03.py -> #78-F1_ETAPA2_PATIO_v03.py; 03edc848: #151-F1_ETAPA2_LADOS_v06.py -> #71-F1_ETAPA2_LADOS_v06.py; 35bd28f4: #23-File Path -> #39-File Path; 6a8732f5: #2-Panel -> #4-Panel; 15733227: #90-Panel -> #86-Panel; 28b87fd9: #82-Panel -> #84-Panel; 8b17987d: #134-Boolean Toggle -> #112-Boolean Toggle; 84453b10: #152-Panel -> #122-Panel; dd604d67: #212-2D Polyline -> #206-2D Polyline; 849a322b: #187-Boolean Toggle -> #171-Boolean Toggle; 0bb86424: #193-Layer -> #178-Layer; 34cdf701: #191-Line Type -> #176-Line Type; 760e4765: #209-Polyline Settings -> #201-Polyline Settings; 4db3f174: #192-Pen -> #177-Pen; e5825223: #190-2D Viewpoint -> #175-2D Viewpoint; 89201549: #194-Number Slider -> #179-Number Slider; 04aec516: #195-Number Slider -> #180-Number Slider; 772379fe: #177-Panel -> #130-Panel; 0830dd93: #178-Panel -> #131-Panel; 63e69fd5: #32-Panel -> #55-Panel; 42b993db: #94-Relay -> #62-Relay; 380f39b7: #214-2D Polyline -> #208-2D Polyline; 7e2f27a2: #189-Boolean Toggle -> #174-Boolean Toggle; 3e5d0ca6: #205-Layer -> #190-Layer; 72e819a2: #203-Line Type -> #188-Line Type; 311eb66f: #211-Polyline Settings -> #203-Polyline Settings; 901e3b63: #204-Pen -> #189-Pen; 0cbe0c13: #202-2D Viewpoint -> #187-2D Viewpoint; 8ea22cc0: #206-Number Slider -> #191-Number Slider; 40a99b07: #207-Number Slider -> #192-Number Slider; f14aed47: #85-Merge -> #56-Merge; d14425f9: #213-2D Polyline -> #207-2D Polyline; 6ab82bef: #188-Boolean Toggle -> #173-Boolean Toggle; f0d50526: #199-Layer -> #184-Layer; 3839b024: #197-Line Type -> #182-Line Type; b81b4596: #210-Polyline Settings -> #202-Polyline Settings; e7cc4cd8: #198-Pen -> #183-Pen; 6d22157d: #196-2D Viewpoint -> #181-2D Viewpoint; 123c4142: #200-Number Slider -> #185-Number Slider; 1a1b6e8a: #201-Number Slider -> #186-Number Slider; 1840c52e: #3-Panel -> #6-Panel; c4f84ab6: #165-Panel -> #80-Panel; d2bbbe59: #91-Relay -> #83-Relay; f4f06e09: #130-Number Slider -> #99-Number Slider; 64ac3a17: #160-Panel -> #140-Panel; c7c2bc5b: #180-Panel -> #146-Panel; 880d9e49: #146-F1_LAYERS_XML_v02.py -> #116-F1_LAYERS_XML_v02.py; 1fd35183: #169-Panel -> #82-Panel; b439301d: #173-Panel -> #81-Panel; ad270c61: #29-F1_CONTEXTO50_BUILD_v01.2.py -> #47-F1_CONTEXTO50_BUILD_v01.2.py; f7f1bd10: #28-F0_LOAD_PROYECTO_v01.py -> #51-F0_LOAD_PROYECTO_v01.py; 6c6470af: #179-Relay -> #145-Relay; 92829854: #216-Area -> #214-Area; b4dfe4e3: #186-Panel -> #152-Panel; fb742b15: #132-Boolean Toggle -> #102-Boolean Toggle; e07db6bf: #217-Value List -> #213-Value List; c8d88565: #131-Number Slider -> #101-Number Slider; 90cd998a: #155-Panel -> #128-Panel; 45f34d3c: #166-Panel -> #133-Panel; ed129f1a: #167-Panel -> #134-Panel; d1f1c084: #168-Panel -> #135-Panel; ec511a85: #171-Panel -> #136-Panel; 702eccf6: #175-Panel -> #138-Panel; d23735c9: #176-Panel -> #139-Panel; d99cc805: #172-Panel -> #137-Panel; c16825c6: #136-Value List -> #104-Value List; 08dbd128: #124-Panel -> #127-Panel; 357fa72a: #119-Addition -> #121-Addition; d836b34f: #113-Number Slider -> #117-Number Slider; cec00a6d: #215-Boolean Toggle -> #210-Boolean Toggle; 4d6fba96: #225-F1_EXPORTAR_GFA_v02.4.py -> #229-F1_EXPORTAR_GFA_v02.4.py; 7f12bc12: #219-Panel -> #223-Panel; 57232634: #222-Panel -> #226-Panel; 758487fe: #221-Panel -> #225-Panel; 55030132: #223-Panel -> #228-Panel; eb315550: #224-Panel -> #227-Panel; 317814cc: #220-Panel -> #224-Panel; 27de6944: #226-Panel -> #237-Panel; b903fe07: #183-Panel -> #149-Panel; e661bc13: #184-Panel -> #150-Panel; 8f44a013: #185-Panel -> #151-Panel; 38323b45: #181-Panel -> #147-Panel; ff0fcdd4: #182-Panel -> #148-Panel; 41d42d82: #147-Panel -> #132-Panel; a3134bb0: #163-Panel -> #143-Panel; 0d1eca32: #52-Relay -> #61-Relay; 57bb3157: #89-Panel -> #85-Panel; 9233109c: #227-Panel -> #238-Panel; 59fbebbf: #228-Panel -> #239-Panel; f64dbcbb: #229-Panel -> #240-Panel; 1d4f3d63: #170-Panel -> #74-Panel; 0cce8b8c: #158-Panel -> #73-Panel; be3562fe: #100-Panel -> #87-Panel; eaf82dd6: #73-Panel -> #45-Panel; aa101248: #137-Value List -> #105-Value List; 37716694: #148-Number Slider -> #129-Number Slider; 2134c72c: #127-Number Slider -> #100-Number Slider; 934649b8: #128-Number Slider -> #98-Number Slider; c1892186: #156-Panel -> #126-Panel; 2dc76614: #164-Panel -> #77-Panel; 2e914f70: #59-Panel -> #28-Panel; 7a432820: #62-Panel -> #34-Panel; 5a318d6c: #65-Panel -> #41-Panel; bcc3ada7: #79-Curve -> #50-Curve; 904b6c1d: #77-Curve -> #49-Curve; 3f88648e: #78-Curve -> #48-Curve; d7be7a0e: #122-Number Slider -> #64-Number Slider; 1e6dc444: #123-Number Slider -> #65-Number Slider; 478712be: #41-Deconstruct 2D Polyline -> #12-Deconstruct 2D Polyline; ac47b487: #42-Deconstruct 2D Polyline -> #9-Deconstruct 2D Polyline; f2cd77e4: #53-Relay -> #22-Relay; 1438c1ca: #39-Deconstruct 2D Polyline -> #10-Deconstruct 2D Polyline; ebb20caa: #54-Relay -> #20-Relay; 267eaecc: #55-Relay -> #21-Relay; b2c63b70: #40-Deconstruct 2D Polyline -> #8-Deconstruct 2D Polyline; 0eb19658: #57-Discontinuity -> #27-Discontinuity; f19513b3: #33-Panel -> #57-Panel; 6d2eeba1: #6-GhPython Script -> #7-GhPython Script; 78b9fd6b: #15-Text Join -> #29-Text Join; e59eb879: #12-Merge -> #19-Merge; b3af946a: #35-File Path -> #58-File Path; fd3423b1: #26-Panel -> #46-Panel; 0865d8d8: #24-Text Join -> #40-Text Join; 60af5a5b: #17-Merge -> #32-Merge; d0e3739a: #43-Deconstruct 2D Polyline -> #11-Deconstruct 2D Polyline; 27cc6af6: #14-Panel -> #24-Panel; b0236142: #1-Panel -> #5-Panel; 1a4544c5: #16-Text Join -> #30-Text Join; 9f1e1586: #11-Merge -> #17-Merge; 1d751cb9: #19-Panel -> #36-Panel; 749104c7: #30-Panel -> #52-Panel; c7b05cf9: #5-Panel -> #1-Panel; a5c82623: #7-GhPython Script -> #3-GhPython Script; ced222ac: #13-Merge -> #16-Merge; c63b5578: #25-File Path -> #35-File Path; 66c173d7: #18-Text Join -> #26-Text Join; 6449298a: #27-Panel -> #44-Panel; 3f45df55: #20-Boolean Toggle -> #33-Boolean Toggle; 4f0b0d0c: #31-Panel -> #53-Panel; e327a458: #37-Morph Solid -> #59-Morph Solid; 88c456d6: #34-Boolean Toggle -> #54-Boolean Toggle; 0c26a207: #21-Boolean Toggle -> #31-Boolean Toggle; a3e18872: #10-Bifocals -> #14-Bifocals; 087871a4: #4-Boolean Toggle -> #2-Boolean Toggle; 5301ad37: #22-Panel -> #43-Panel; 1ee725c5: #9-Panel -> #13-Panel; 6a30edd7: #120-Boolean Toggle -> #110-Boolean Toggle; 82bb1e2a: #126-Panel -> #114-Panel; f6c9b51e: #109-Panel -> #93-Panel; 3ec247b1: #116-Polyline Settings -> #106-Polyline Settings; a384ca19: #117-Curve -> #107-Curve; ca49279b: #138-2D Polyline -> #115-2D Polyline; 7df02852: #112-Layer -> #97-Layer; ff8a3228: #118-2D Viewpoint -> #108-2D Viewpoint; 592bb6c9: #108-Line Type -> #92-Line Type; 60a0c532: #110-Pen -> #94-Pen; baa9b444: #107-Merge -> #91-Merge; 22f9b32e: #143-Number Slider -> #72-Number Slider; 0eafeb92: #106-Mesh -> #103-Mesh; dbc95c73: #101-Relay -> #89-Relay; dca4a6c3: #103-Mesh -> #90-Mesh; 6dd340ab: #121-CreateMeshes -> #118-CreateMeshes; 6a375270: #114-MeshSkirtTypes -> #111-MeshSkirtTypes; 27647d89: #115-MeshRidgeTypes -> #113-MeshRidgeTypes; 062194a4: #141-Panel -> #125-Panel; 8c5cf5c0: #140-Panel -> #123-Panel; 0bf3fa7e: #105-Deconstruct Mesh -> #96-Deconstruct Mesh; 9e33e757: #104-Boolean Toggle -> #95-Boolean Toggle; 7a26ae98: #111-Boolean Toggle -> #109-Boolean Toggle; 08455ae4: #8-Relay -> #18-Relay; 1ea7de8d: #208-Relay -> #153-Relay; 01e5d387: #102-Relay -> #63-Relay; b9b52851: #95-Panel -> #67-Panel; 0233a1ba: #149-Deconstruct 2D Polyline -> #25-Deconstruct 2D Polyline; 5b50f44c: #153-Panel -> #42-Panel; ac209233: #133-2D Curve -> #15-2D Curve; 19f5d71c: #145-PolylineDetails -> #38-PolylineDetails; fb06952e: #139-End Points -> #23-End Points; b33704fa: #50-Panel -> #37-Panel; dc9c2e53: #129-Number Slider -> #119-Number Slider; 20218518: #159-Panel -> #76-Panel; eb4f42e5: #125-Panel -> #66-Panel; fb511c0d: #36-Panel -> #60-Panel; 468c4fcf: #142-Relay -> #69-Relay; 75a255b0: #150-Panel -> #70-Panel; 33fedb5f: #144-File Path -> #68-File Path; eda71746: #135-Boolean Toggle -> #120-Boolean Toggle; 6eaf2956: #76-F3_DISTRIBUCION_v03.py -> #200-F3_DISTRIBUCION_v03.8.py; 9ee561bd: #88-Panel -> #212-Panel; 15d034b9: #157-Panel -> #75-Panel; 37bf9948: #92-F3_UNIDADES_TIPOLOGIAS_v02.py -> #216-F3_UNIDADES_TIPOLOGIAS_v02.py; 8c7e8133: #75-F3_VOLUM_GENERADOR_v08.py -> #197-F3_VOLUM_GENERADOR_v08.py; 8eaf3a60: #86-F3_MORPH_ATRIBUTOS_v02.py -> #211-F3_MORPH_ATRIBUTOS_v02.py; 768ebdc8: #93-F3_ACCESOS_INTEGRADOR_v02.py -> #217-F3_ACCESOS_INTEGRADOR_v02.py; 60a9e98b: #48-Boolean Toggle -> #163-Boolean Toggle; cfab7031: #49-Boolean Toggle -> #164-Boolean Toggle; e05f8f43: #46-Panel -> #165-Panel; ba6ed6bc: #51-Panel -> #166-Panel; ab3a9f4c: #44-GhPython Script -> #161-GhPython Script; c7cced40: #61-Merge -> #169-Merge; 70baf962: #45-Panel -> #162-Panel; 775cbddc: #56-Merge -> #168-Merge; 795fbf2a: #66-Panel -> #193-Panel; ab4b44cb: #67-Panel -> #194-Panel; e0fd46b4: #63-Text Join -> #172-Text Join; 6f68e9f5: #64-Text Join -> #170-Text Join; ccf3dd73: #38-Relay -> #155-Relay; d29dc15b: #58-Panel -> #88-Panel; 11b314e3: #60-Panel -> #154-Panel; 59b9cfe2: #68-Merge -> #158-Merge; 8bb53d04: #80-Text Join -> #159-Text Join; 1503dde0: #70-Value List -> #195-Value List; 36a640db: #69-Value List -> #196-Value List; 6126aaea: #71-Panel -> #198-Panel; 6c5ba3b4: #81-Merge -> #204-Merge; f0e16fe8: #87-Text Join -> #209-Text Join; 5fe99180: #83-Panel -> #205-Panel; 3cd964a7: #174-Panel -> #144-Panel; 61d0c4e5: #98-Panel -> #222-Panel; a1c435d3: #99-Panel -> #219-Panel; 2d024429: #162-Panel -> #141-Panel; 4bb706ab: #96-Panel -> #220-Panel; 75a2e5ab: #97-Panel -> #221-Panel; 7f22c946: #47-Panel -> #167-Panel; 3c58edf4: #84-Panel -> #215-Panel; bd2ac736: #74-Panel -> #199-Panel
- Desaparecidos: 04e1f0c9 GhPython Script, 0ff2ec6e GhPython Script, 13dcfdc0 GhPython Script, 854321db GhPython Script, 7210c172 File Path, a6d25b61 2D Polyline, de570cd0 Layer, fe9ac21d Line Type, 5fabec5a Polyline Settings, c5e8e974 Pen, eaf3da0f 2D Viewpoint, 24ab23c8 Relay, 05955997 2D Polyline, c48e491e Layer, 07ac5fa4 Line Type, 784db856 Polyline Settings, 1b4a1593 Pen, 67eb43fd 2D Viewpoint, b93cbafd Merge, 2c92ac98 2D Polyline, 34c0816a Layer, 66ad23f1 Line Type, d3f9e26f Polyline Settings, d351b289 Pen, 8a603bfe 2D Viewpoint, 90ac5cc0 Relay, 80a4a2ae GhPython Script, 35e6cd1b GhPython Script, 6a223535 GhPython Script, 74d4dc03 GhPython Script, dd129d74 Relay, 7f5a6180 Area, ae660eec Value List, ef73a481 Value List, ba09db31 Addition, dd5bb666 GhPython Script, 0b7ca7cc GhPython Script, 178d1e14 Relay, 57821ae4 Value List, 593bb411 Curve, 0ca699e7 Curve, 01b505ed Curve, a056d0f7 Deconstruct 2D Polyline, d500dc96 Deconstruct 2D Polyline, 940d739c Relay, 63d80378 Deconstruct 2D Polyline, 225c223a Relay, 7f1082b2 Relay, 67fd6079 Deconstruct 2D Polyline, 7addc591 Discontinuity, 4a95b2f3 GhPython Script, d0201f0c Text Join, e823f036 Merge, ff224a86 File Path, e3bd89ee Text Join, 11f895e5 Merge, 01ccac90 Deconstruct 2D Polyline, e8d7b22a Text Join, b5e399be Merge, 5ddb89da GhPython Script, faf57450 Merge, d9fbc5b1 File Path, 7add00d8 Text Join, 914296c6 Morph Solid, 3ee37a4e Curve, 841c6e9a 2D Polyline, c953d9fa Layer, 863ae40b 2D Viewpoint, 320643cc Line Type, 4a454ef7 Pen, 86a6926b Merge, ea2c4657 Mesh, 8e10cad0 Relay, c0127624 Mesh, dd1baa01 CreateMeshes, d99d8c90 MeshSkirtTypes, d27b2747 MeshRidgeTypes, 19410e42 Deconstruct Mesh, 47b395ca Relay, 0a6ba313 Relay, 6593870e Relay, 26766254 Deconstruct 2D Polyline, cf3d289c 2D Curve, eaf9edfa PolylineDetails, 034ae182 End Points, 9af88422 Relay, 6908b4d0 File Path, 3f15d96f GhPython Script, cc8168c2 GhPython Script, 8a9b6a74 GhPython Script, ce260e73 GhPython Script, 58123948 GhPython Script, a429fcc5 GhPython Script, 66a36248 Merge, 802be7b5 Merge, 9d97b580 Text Join, 608d1eb8 Text Join, c95ebeac Relay, b259a9c7 Merge, 7bed14b4 Text Join, 2260e877 Value List, 9fe273f2 Value List, 4774171f Merge, ee2ffe93 Text Join, 95b22b48 GhPython Script, ffca3285 GhPython Script, 27941a3c GhPython Script, 8d7db3f7 GhPython Script, de650baa File Path, fc9c06ac 2D Polyline, eb85af25 Layer, f5ca0fa6 Line Type, 3acef643 Polyline Settings, 0793438d Pen, 1bffb172 2D Viewpoint, c5c106fa Relay, 2b3ae5f1 2D Polyline, f851445a Layer, 7636c316 Line Type, ff41bd06 Polyline Settings, 186981b1 Pen, 2ef1fdbf 2D Viewpoint, 898e4f39 Merge, 757f1f70 2D Polyline, bcba20f2 Layer, ec2d95ec Line Type, 87962d0f Polyline Settings, e061322c Pen, 9845b9e8 2D Viewpoint, b218c0cc Relay, 6f16bd35 GhPython Script, 1c5100c3 GhPython Script, 0c00d724 GhPython Script, 7e8a4075 GhPython Script, afb46ba3 Relay, 3dafd005 Area, c9a4658a Value List, 4d8eb07e Value List, 06883356 Addition, 260383c9 GhPython Script, b81bad1e GhPython Script, 50d912d4 Relay, 003860fc Value List, 44274470 Curve, 74ad0fd2 Curve, dc1f030c Curve, 06609cba Deconstruct 2D Polyline, 62473532 Deconstruct 2D Polyline, 14e88d1c Relay, 308d4180 Deconstruct 2D Polyline, c0e9d004 Relay, 0d40038a Relay, c6e032bc Deconstruct 2D Polyline, d65a87a5 Discontinuity, 1a962b6d GhPython Script, 47327045 Text Join, 157a3b34 Merge, 6fe38d64 File Path, 380592fd Text Join, 04d50c79 Merge, 2dd3ed56 Deconstruct 2D Polyline, 702c8f4a Text Join, d560fd7b Merge, 13ea2ea8 GhPython Script, f9ea68e8 Merge, 28b7efb6 File Path, b666cfae Text Join, ecbd97b2 Morph Solid, 9f0056b1 Bifocals, 419a5f07 Polyline Settings, d7408177 Curve, 7864a8b1 2D Polyline, f70651f6 Layer, 2a2c77f0 2D Viewpoint, a4ee375d Line Type, 7a178bc8 Pen, 409f7eab Merge, 3172af6f Mesh, 73ef2e86 Relay, 93559852 Mesh, 3c41c11e CreateMeshes, 368d3c3c MeshSkirtTypes, 808bfec4 MeshRidgeTypes, 78401059 Deconstruct Mesh, d6e14791 Relay, 727c9bca Relay, 896aae13 Relay, 28b6fd1f Deconstruct 2D Polyline, c2bbec76 2D Curve, 5111c217 PolylineDetails, 2ce44155 End Points, 40b46e5d Relay, cb22f137 File Path, 2cbb19f5 GhPython Script, 8904d819 GhPython Script, 6bdecb3f GhPython Script, 00589c89 GhPython Script, f15ea4ca GhPython Script, 7f711cc8 GhPython Script, 52a7bc4e Merge, a9071ebd Merge, efa4b55c Text Join, 4788e571 Text Join, b7b9b5c9 Relay, 8ec1d6ed Merge, 74688161 Text Join, 2ca2a5a7 Value List, 7fa2838c Value List, 46c3d302 Merge, b38d45b8 Text Join

## Componentes

| # | Nick / nombre | GUID | Tipo | Conexiones | Clasificacion | Nota |
|---|---|---|---|---|---|---|
| 1 | #1-Panel | `c7b05cf9-cc04-4c3a-a9ff-c34aa1a7910f` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 2 | #2-Boolean Toggle | `087871a4-6ec3-4389-b33f-b8703fd8bacb` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 3 | #3-GhPython Script | `a5c82623-3079-475a-9837-66871b700f79` | GhPython Script | in 0 / out 1 | Logica (script) | codigo 251 chars |
| 4 | #4-Panel | `6a8732f5-d48d-465a-8d94-d57ca928f322` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 5 | #5-Panel | `b0236142-1719-40f4-abf8-76c39e6a3e88` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 6 | #6-Panel | `1840c52e-a9cc-4222-8b40-dea520b25ad2` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 7 | #7-GhPython Script | `6d2eeba1-3621-4525-a927-d50a79898068` | GhPython Script | in 0 / out 0 | Logica (script) | codigo 251 chars; SIN consumidores (salida no usada) |
| 8 | #8-Deconstruct 2D Polyline | `b2c63b70-56a6-4355-bd5a-2d2004cb4dcb` | Deconstruct 2D Polyline | in 0 / out 0 | Otro |  |
| 9 | #9-Deconstruct 2D Polyline | `ac47b487-ba18-4ea9-8d63-d9b916ff6e26` | Deconstruct 2D Polyline | in 0 / out 0 | Otro |  |
| 10 | #10-Deconstruct 2D Polyline | `1438c1ca-389d-489c-b673-efa9baabc494` | Deconstruct 2D Polyline | in 0 / out 0 | Otro |  |
| 11 | #11-Deconstruct 2D Polyline | `d0e3739a-c694-4a56-9261-95e0a498b6ac` | Deconstruct 2D Polyline | in 0 / out 1 | Otro |  |
| 12 | #12-Deconstruct 2D Polyline | `478712be-5815-489c-997e-cbd8bf9c606d` | Deconstruct 2D Polyline | in 0 / out 1 | Otro |  |
| 13 | #13-Panel | `1ee725c5-6ed5-4f3e-a6c2-2f536cc6c6f7` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 14 | #14-Bifocals | `a3e18872-7fab-403a-90b0-3221f1885768` | Bifocals | in 0 / out 0 | Soporte (util) |  |
| 15 | #15-2D Curve | `ac209233-807c-44aa-b509-0d057290f8ea` | 2D Curve | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 16 | #16-Merge | `ced222ac-dd75-44dc-b94c-6f75e4902917` | Merge | in 2 / out 1 | Soporte (util) |  |
| 17 | #17-Merge | `9f1e1586-3a52-4367-88ad-2961cf9e0658` | Merge | in 2 / out 1 | Soporte (util) |  |
| 18 | #18-Relay | `08455ae4-5d60-49cf-9f63-34479c9e9109` | Relay | in 0 / out 0 | Soporte (util) |  |
| 19 | #19-Merge | `e59eb879-013c-4118-b70c-acc0c04f3698` | Merge | in 2 / out 1 | Soporte (util) |  |
| 20 | #20-Relay | `ebb20caa-158a-4e94-a4be-40e9e030cf83` | Relay | in 0 / out 0 | Soporte (util) |  |
| 21 | #21-Relay | `267eaecc-557b-4336-a976-21f4a751efed` | Relay | in 0 / out 0 | Soporte (util) |  |
| 22 | #22-Relay | `f2cd77e4-f7c1-4845-9def-85a9d94be25b` | Relay | in 0 / out 0 | Soporte (util) |  |
| 23 | #23-End Points | `fb06952e-d1bf-41dd-b786-c80004dbc678` | End Points | in 1 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 24 | #24-Panel | `27cc6af6-372a-4bed-931b-24755c7ef4d1` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 25 | #25-Deconstruct 2D Polyline | `0233a1ba-e22d-43c5-82d8-2271070e92b2` | Deconstruct 2D Polyline | in 1 / out 0 | Otro |  |
| 26 | #26-Text Join | `66c173d7-31b3-4a22-9acd-468486fb09ee` | Text Join | in 1 / out 0 | Soporte (util) |  |
| 27 | #27-Discontinuity | `0eb19658-f906-4321-bce0-0d2c071c81a5` | Discontinuity | in 1 / out 1 | Soporte (util) |  |
| 28 | #28-Panel | `2e914f70-6eb8-411a-972c-363e484bceea` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 29 | #29-Text Join | `78b9fd6b-ffb9-4ff9-8601-6596080b9ca0` | Text Join | in 1 / out 0 | Soporte (util) |  |
| 30 | #30-Text Join | `1a4544c5-6e27-4dad-993c-2e224f626bc9` | Text Join | in 1 / out 1 | Soporte (util) |  |
| 31 | #31-Boolean Toggle | `0c26a207-9856-43a6-84dc-ba4cdb9820ae` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 32 | #32-Merge | `60af5a5b-eae0-4812-9d98-777c610edcc8` | Merge | in 2 / out 1 | Soporte (util) |  |
| 33 | #33-Boolean Toggle | `3f45df55-582b-48e8-98b1-992b6a0321d8` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 34 | #34-Panel | `7a432820-bfc3-4f64-a540-014698dd6436` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 35 | #35-File Path | `c63b5578-7f1a-481b-8280-a33991b57c4e` | File Path | in 0 / out 0 | Entrada (UI) |  |
| 36 | #36-Panel | `1d751cb9-293f-4e51-8a9d-be47ef2e4352` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 37 | #37-Panel | `b33704fa-c3c1-447e-a9e1-ff5e6182551a` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 38 | #38-PolylineDetails | `19f5d71c-566b-4eb8-9ad8-3b347359dee2` | PolylineDetails | in 1 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 39 | #39-File Path | `35bd28f4-53a8-4e21-bf88-ed6dc6173a8c` | File Path | in 0 / out 0 | Entrada (UI) |  |
| 40 | #40-Text Join | `0865d8d8-1b01-446f-a93d-ed55c872ac8d` | Text Join | in 1 / out 0 | Soporte (util) |  |
| 41 | #41-Panel | `5a318d6c-64e2-4b89-8314-b880615266ef` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 42 | #42-Panel | `5b50f44c-2241-4d9f-8170-3c37d9c1bd13` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 43 | #43-Panel | `5301ad37-cf0a-4260-869d-5bb8004c78a0` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 44 | #44-Panel | `6449298a-b31a-496e-8884-e1a35cc25bba` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 45 | #45-Panel | `eaf82dd6-6ede-43ce-95bb-a62e537bc753` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 46 | #46-Panel | `fd3423b1-8746-4269-9e48-d3b90c0d31e6` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 47 | #47-F1_CONTEXTO50_BUILD_v01.2.py | `ad270c61-3268-4dcc-b9e8-dd6e9711f5c8` | GhPython Script | in 3 / out 1 | Logica (script) | codigo 25676 chars |
| 48 | #48-Curve | `3f88648e-3885-41eb-9fd0-ef923dfa34af` | Curve | in 0 / out 0 | Soporte (util) |  |
| 49 | #49-Curve | `904b6c1d-25c3-43ca-9764-c890793a79fe` | Curve | in 0 / out 0 | Soporte (util) |  |
| 50 | #50-Curve | `bcc3ada7-773e-4c7f-81b7-bc9996c57149` | Curve | in 0 / out 0 | Soporte (util) |  |
| 51 | #51-F0_LOAD_PROYECTO_v01.py | `f7f1bd10-32ba-4501-9dda-ebe9486e179b` | GhPython Script | in 1 / out 0 | Logica (script) | codigo 13803 chars; SIN consumidores (salida no usada) |
| 52 | #52-Panel | `749104c7-6f20-479f-93d6-d4c4ae9db733` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 53 | #53-Panel | `4f0b0d0c-c758-49ba-b757-3423422932ad` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 54 | #54-Boolean Toggle | `88c456d6-2341-4157-bbe4-4a51090eb4cd` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 55 | #55-Panel | `63e69fd5-d297-4dc8-8c71-867541849e60` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 56 | #56-Merge | `f14aed47-9d88-4b2c-9ca0-7a42204505a3` | Merge | in 3 / out 0 | Soporte (util) |  |
| 57 | #57-Panel | `f19513b3-7722-473c-8e74-20971cb106da` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 58 | #58-File Path | `b3af946a-c564-4209-9294-fa89a6976d29` | File Path | in 0 / out 0 | Entrada (UI) |  |
| 59 | #59-Morph Solid | `e327a458-1571-457b-8185-b7b162da62bc` | Morph Solid | in 2 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 60 | #60-Panel | `fb511c0d-1457-4d60-9213-03867c6c236a` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 61 | #61-Relay | `0d1eca32-e997-4907-a772-a9166aa1c7a9` | Relay | in 0 / out 0 | Soporte (util) |  |
| 62 | #62-Relay | `42b993db-8865-48f2-a456-ac01c6bd34d7` | Relay | in 0 / out 0 | Soporte (util) |  |
| 63 | #63-Relay | `01e5d387-3575-453f-a5c8-b445f08b6fc7` | Relay | in 0 / out 0 | Soporte (util) |  |
| 64 | #64-Number Slider | `d7be7a0e-8698-4399-ba5c-c653546bb97a` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 65 | #65-Number Slider | `1e6dc444-0c34-430f-9148-4240875941d0` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 66 | #66-Panel | `eb4f42e5-e1df-4a4c-9064-1297d6cf9c32` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 67 | #67-Panel | `b9b52851-151c-441f-a62b-e945739fe023` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 68 | #68-File Path | `33fedb5f-5245-4518-b1bc-eae6c982d553` | File Path | in 0 / out 0 | Entrada (UI) |  |
| 69 | #69-Relay | `468c4fcf-187b-44a4-945c-ff45409d1919` | Relay | in 0 / out 0 | Soporte (util) |  |
| 70 | #70-Panel | `75a255b0-88f8-416f-b41b-511ccbc8f256` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 71 | #71-F1_ETAPA2_LADOS_v06.py | `03edc848-3a7f-4fa4-b2a6-bf736d5414f5` | GhPython Script | in 10 / out 13 | Logica (script) | codigo 58801 chars |
| 72 | #72-Number Slider | `22f9b32e-6510-473e-a8c2-de1cc56ebaf1` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 73 | #73-Panel | `0cce8b8c-fd80-43e0-8a31-c6c895e21057` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 74 | #74-Panel | `1d4f3d63-4e93-4557-a029-b9cd443004b2` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 75 | #75-Panel | `15d034b9-e099-49b9-916a-f6b8b219adfe` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 76 | #76-Panel | `20218518-41dc-4537-b434-762666ca75f0` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 77 | #77-Panel | `2dc76614-d1cc-444c-b35e-e98d87e80ca9` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 78 | #78-F1_ETAPA2_PATIO_v03.py | `d3bed17b-1b6b-4e89-8761-1985327b292b` | GhPython Script | in 4 / out 2 | Logica (script) | codigo 37658 chars |
| 79 | #79-F1_ETAPA1_CONTEXTO_v04.4.1.py | `0d986a36-a41a-429c-8f29-9e2658659e25` | GhPython Script | in 1 / out 12 | Logica (script) | codigo 22616 chars |
| 80 | #80-Panel | `c4f84ab6-92ca-4ada-88e2-786201fc80a4` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 81 | #81-Panel | `b439301d-b0be-41a2-928f-41da4f18c987` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 82 | #82-Panel | `1fd35183-777a-41fb-8537-bc45b054ef4b` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 83 | #83-Relay | `d2bbbe59-0e4c-4e4c-979b-3945ce82b179` | Relay | in 0 / out 0 | Soporte (util) |  |
| 84 | #84-Panel | `28b87fd9-301d-4d71-b78b-b054159df54a` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 85 | #85-Panel | `57bb3157-6032-45ae-8e93-6fd413f437b3` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 86 | #86-Panel | `15733227-041e-45e8-b1f7-d84eb95f0eb4` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 87 | #87-Panel | `be3562fe-86e5-4802-9481-87c0a2260585` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 88 | #88-Panel | `d29dc15b-8be3-42e4-a462-b9646bc8247d` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 89 | #89-Relay | `dbc95c73-4eba-46be-ad1b-f645cf419845` | Relay | in 0 / out 0 | Soporte (util) |  |
| 90 | #90-Mesh | `dca4a6c3-5024-4a66-a020-6e5884373d5c` | Mesh | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 91 | #91-Merge | `baa9b444-c899-4d4b-9ec8-aeedb84d218e` | Merge | in 5 / out 0 | Soporte (util) |  |
| 92 | #92-Line Type | `592bb6c9-9b5b-4527-9174-17c4d8fb276c` | Line Type | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 93 | #93-Panel | `f6c9b51e-32d1-4ca9-a55b-110c414109e1` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 94 | #94-Pen | `60a0c532-9603-4d52-a6b2-f1ccad351d07` | Pen | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 95 | #95-Boolean Toggle | `9e33e757-ad0d-4345-a368-ac6c1847533d` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 96 | #96-Deconstruct Mesh | `0bf3fa7e-4f67-43f7-9069-cf6fe3b096f7` | Deconstruct Mesh | in 1 / out 2 | LC -> ArchiCAD | destino ArchiCAD |
| 97 | #97-Layer | `7df02852-4711-4513-86da-eb9e622c9440` | Layer | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 98 | #98-Number Slider | `934649b8-f30e-4e0d-9946-44b39a418994` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 99 | #99-Number Slider | `f4f06e09-bd63-48c9-aacf-ebb1a18798f2` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 100 | #100-Number Slider | `2134c72c-86b1-44ff-b1dc-5cbc480c8e14` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 101 | #101-Number Slider | `c8d88565-ae8d-4127-aea2-80cad521e413` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 102 | #102-Boolean Toggle | `fb742b15-3bde-4c9c-87bc-d7c26fc84df3` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 103 | #103-Mesh | `0eafeb92-ec9c-4e0a-a3ed-1ad7caba58d2` | Mesh | in 2 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 104 | #104-Value List | `c16825c6-468b-42ab-8d89-5bb3a3e6b000` | Value List | in 0 / out 0 | Entrada (UI) |  |
| 105 | #105-Value List | `aa101248-4f97-41cb-b4cb-e64c44676e8b` | Value List | in 0 / out 0 | Entrada (UI) |  |
| 106 | #106-Polyline Settings | `3ec247b1-4020-4595-8829-14a200c74eac` | Polyline Settings | in 3 / out 1 | LC -> ArchiCAD | destino ArchiCAD |
| 107 | #107-Curve | `a384ca19-1fae-44d6-b049-2bfe1bb5ea0e` | Curve | in 0 / out 0 | Soporte (util) |  |
| 108 | #108-2D Viewpoint | `ff8a3228-87d5-480f-ae45-ac461b9ceebf` | 2D Viewpoint | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 109 | #109-Boolean Toggle | `7a26ae98-b331-40bc-afb7-656afaf2e88a` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 110 | #110-Boolean Toggle | `6a30edd7-ad55-4bb5-b655-4661491037b8` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 111 | #111-MeshSkirtTypes | `6a375270-ab81-445a-a42b-687ae6596bc9` | MeshSkirtTypes | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 112 | #112-Boolean Toggle | `8b17987d-da61-41b7-9712-57b50a21f998` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 113 | #113-MeshRidgeTypes | `27647d89-c0fd-45b7-9c0d-4e0d18ed990a` | MeshRidgeTypes | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 114 | #114-Panel | `82bb1e2a-4481-4265-b7e6-1811fa3ce562` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 115 | #115-2D Polyline | `ca49279b-7297-4a65-a232-1ac1b99bb74f` | 2D Polyline | in 4 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 116 | #116-F1_LAYERS_XML_v02.py | `880d9e49-9938-4d31-a0bc-35d297a2ab28` | GhPython Script | in 3 / out 0 | Logica (script) | codigo 9498 chars; SIN consumidores (salida no usada) |
| 117 | #117-Number Slider | `d836b34f-5419-465d-a84d-e8230ac289b4` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 118 | #118-CreateMeshes | `6dd340ab-a7f7-43dc-8298-39a7faf0074d` | CreateMeshes | in 4 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 119 | #119-Number Slider | `dc9c2e53-9427-480d-8c47-e0694a6c0454` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 120 | #120-Boolean Toggle | `eda71746-c5a8-4b99-aa50-07c1dc5afe3d` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 121 | #121-Addition | `357fa72a-93e4-4425-b31c-e01dd408b3aa` | Addition | in 2 / out 2 | Soporte (util) |  |
| 122 | #122-Panel | `84453b10-964e-4389-9951-fdbf34e7e957` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 123 | #123-Panel | `8c5cf5c0-6d4c-46ab-ab09-8e706ffcb0d3` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 124 | #124-F1_ETAPA2_NORMATIVA_v09.1.py | `d4aab682-ad94-40e9-a5b5-eaf20b3350c7` | GhPython Script | in 19 / out 13 | Logica (script) | codigo 55149 chars |
| 125 | #125-Panel | `062194a4-bb25-4e36-93f1-4e717c28c9d0` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 126 | #126-Panel | `c1892186-c813-41cb-bec2-21c8067218b1` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 127 | #127-Panel | `08dbd128-35a6-435b-9ea7-79402a2b00b8` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 128 | #128-Panel | `90cd998a-cf3d-4d66-bad7-6ebb9c8d5fa8` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 129 | #129-Number Slider | `37716694-f7a2-4bf9-a6f3-57820c4a26e0` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 130 | #130-Panel | `772379fe-bfb9-4a3b-8c09-36f1ae73e39b` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 131 | #131-Panel | `0830dd93-5b15-49a0-9808-688e1ce4b74b` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 132 | #132-Panel | `41d42d82-93b7-4037-b79a-d3fbf11d8059` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 133 | #133-Panel | `45f34d3c-d6dd-4c2c-a205-81ac308016ea` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 134 | #134-Panel | `ed129f1a-f0ce-42fd-a8f8-d59ffe2660f4` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 135 | #135-Panel | `d1f1c084-9663-45e0-ab5b-10ab6ca1e023` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 136 | #136-Panel | `ec511a85-a91c-4b9f-b257-e0d7da451d23` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 137 | #137-Panel | `d99cc805-befe-4c30-b61a-5541f0f841a2` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 138 | #138-Panel | `702eccf6-3076-42af-bff8-18788a45f560` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 139 | #139-Panel | `d23735c9-60d8-4295-9583-e9547a66670e` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 140 | #140-Panel | `64ac3a17-bd64-4985-9dcb-559a9acefde0` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 141 | #141-Panel | `2d024429-600f-4112-84a3-369f7f8c03df` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 143 | #143-Panel | `a3134bb0-55c8-49f3-896f-9c46998931ae` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 144 | #144-Panel | `3cd964a7-8e94-4ad4-8e77-c66dadd1075c` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 145 | #145-Relay | `6c6470af-070b-40fb-8ce0-708b1bc4c36d` | Relay | in 0 / out 0 | Soporte (util) |  |
| 146 | #146-Panel | `c7c2bc5b-4052-4ce7-ae0a-42a7909799f8` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 147 | #147-Panel | `38323b45-34cc-42b3-a539-e2e9745e78b6` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 148 | #148-Panel | `ff0fcdd4-f859-442b-b594-8fd671b949a6` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 149 | #149-Panel | `b903fe07-7be3-4c39-8df8-b0122ce9aba2` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 150 | #150-Panel | `e661bc13-5085-492c-8011-fa8f822e2e49` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 151 | #151-Panel | `8f44a013-cd50-4112-9820-2e7279c7a41b` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 152 | #152-Panel | `b4dfe4e3-b87b-4b62-b84c-98d829ff0c09` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 153 | #153-Relay | `1ea7de8d-5f61-4bef-b2e3-68f8880c34aa` | Relay | in 0 / out 0 | Soporte (util) |  |
| 154 | #154-Panel | `11b314e3-5540-4150-a6a5-461705ea4949` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 155 | #155-Relay | `ccf3dd73-b7a4-45d5-80c8-f98614002345` | Relay | in 0 / out 0 | Soporte (util) |  |
| 156 | #156-Panel | `921141e7-7912-458e-9ce3-ce457dac0dc6` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 157 | #157-Panel | `d4aa2e48-30b6-47e2-a220-a896adebef23` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 158 | #158-Merge | `59b9cfe2-481b-40b3-9f8e-f563767809ec` | Merge | in 2 / out 1 | Soporte (util) |  |
| 159 | #159-Text Join | `8bb53d04-fd9d-4913-8f71-17bec5845638` | Text Join | in 1 / out 1 | Soporte (util) |  |
| 160 | #160-Panel | `ad1f7c90-dd0b-46dd-96d5-3867b8c64f2a` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 161 | #161-GhPython Script | `ab3a9f4c-26ae-4553-bf95-018a7d42dfb0` | GhPython Script | in 0 / out 4 | Logica (script) | codigo 251 chars |
| 162 | #162-Panel | `70baf962-5d0f-4c48-bede-7b6df39d3dcf` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 163 | #163-Boolean Toggle | `60a9e98b-3ca0-4e63-b965-3fe65ae06804` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 164 | #164-Boolean Toggle | `cfab7031-f2f0-402b-99ba-753561e80287` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 165 | #165-Panel | `e05f8f43-2ae2-4256-98e0-bb28d60a523a` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 166 | #166-Panel | `ba6ed6bc-1040-4af2-9b38-42041de28f71` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 167 | #167-Panel | `7f22c946-9443-4808-8b4e-c254bd94077d` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 168 | #168-Merge | `775cbddc-136b-42d8-b9a1-954acf3de7ba` | Merge | in 2 / out 1 | Soporte (util) |  |
| 169 | #169-Merge | `c7cced40-8223-4be6-867d-053b5538733d` | Merge | in 2 / out 1 | Soporte (util) |  |
| 170 | #170-Text Join | `6f68e9f5-9abf-4aee-956b-3a4f8f6a6655` | Text Join | in 1 / out 1 | Soporte (util) |  |
| 171 | #171-Boolean Toggle | `849a322b-7d33-4c1e-8633-9dfe37af1f59` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 172 | #172-Text Join | `e0fd46b4-4845-4efe-aec7-f3258241a68e` | Text Join | in 1 / out 0 | Soporte (util) |  |
| 173 | #173-Boolean Toggle | `6ab82bef-54d9-44c1-b5b3-6d6805086423` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 174 | #174-Boolean Toggle | `7e2f27a2-c765-4f44-94f8-5fa04eae9f82` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 175 | #175-2D Viewpoint | `e5825223-1365-42ed-9490-ae707a7a09cb` | 2D Viewpoint | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 176 | #176-Line Type | `34cdf701-7cf8-4955-8975-75329121639e` | Line Type | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 177 | #177-Pen | `4db3f174-8a42-436d-aced-a70672391d3e` | Pen | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 178 | #178-Layer | `0bb86424-168b-4a23-8729-b34cf8f4f464` | Layer | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 179 | #179-Number Slider | `89201549-7937-4bb2-864f-a95e4aa35b60` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 180 | #180-Number Slider | `04aec516-6fc6-4810-89ad-4c7c3d602b6a` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 181 | #181-2D Viewpoint | `6d22157d-e41b-47c8-a535-4c6f3c667b4a` | 2D Viewpoint | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 182 | #182-Line Type | `3839b024-127d-43e7-9b54-7ece590f14cd` | Line Type | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 183 | #183-Pen | `e7cc4cd8-cbf8-4e60-b0d1-7c48b2466df9` | Pen | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 184 | #184-Layer | `f0d50526-09ee-4826-8b39-40bcad7df949` | Layer | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 185 | #185-Number Slider | `123c4142-1f99-46ce-9864-1138d1abcf0c` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 186 | #186-Number Slider | `1a1b6e8a-bec4-42f5-bbd4-1c42663229d0` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 187 | #187-2D Viewpoint | `0cbe0c13-8ec1-4281-a9a1-4807586739e4` | 2D Viewpoint | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 188 | #188-Line Type | `72e819a2-0155-4315-8d76-015ce69f4657` | Line Type | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 189 | #189-Pen | `901e3b63-3fea-4dd9-80fe-95e3cf5ab767` | Pen | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 190 | #190-Layer | `3e5d0ca6-fbe0-4e00-be8e-560007d4d928` | Layer | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 191 | #191-Number Slider | `8ea22cc0-d729-43e5-926c-5d052ab9f5fe` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 192 | #192-Number Slider | `40a99b07-e22d-4256-9862-b2fcd8dc6bbb` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 193 | #193-Panel | `795fbf2a-6e1e-452b-8e7f-867a082f4294` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 194 | #194-Panel | `ab4b44cb-5c73-4c73-85fe-1eae77abbea7` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 195 | #195-Value List | `1503dde0-93b6-4798-927f-aea7d47a3801` | Value List | in 0 / out 0 | Entrada (UI) |  |
| 196 | #196-Value List | `36a640db-ef17-4bdf-9cfa-9186deef18b4` | Value List | in 0 / out 0 | Entrada (UI) |  |
| 197 | #197-F3_VOLUM_GENERADOR_v08.py | `8c7e8133-0bbe-401d-9fa0-6c4b761bbc5d` | GhPython Script | in 9 / out 8 | Logica (script) | codigo 70055 chars |
| 198 | #198-Panel | `6126aaea-a05d-42ad-8847-11e1bcd482fd` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 199 | #199-Panel | `bd2ac736-15e3-4060-9b6b-46789821dedc` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 200 | #200-F3_DISTRIBUCION_v03.8.py | `6eaf2956-f649-4540-a900-4b32a10deee4` | GhPython Script | in 5 / out 4 | Logica (script) | codigo 63603 chars |
| 201 | #201-Polyline Settings | `760e4765-8728-46dc-8ef3-5deee88006dd` | Polyline Settings | in 5 / out 1 | LC -> ArchiCAD | destino ArchiCAD |
| 202 | #202-Polyline Settings | `b81b4596-0469-4755-b504-296ddd5890fb` | Polyline Settings | in 5 / out 1 | LC -> ArchiCAD | destino ArchiCAD |
| 203 | #203-Polyline Settings | `311eb66f-fd9b-453f-9d93-be217b5f3deb` | Polyline Settings | in 5 / out 1 | LC -> ArchiCAD | destino ArchiCAD |
| 204 | #204-Merge | `6c5ba3b4-f736-4d6c-8a27-b3982adfbe53` | Merge | in 2 / out 1 | Soporte (util) |  |
| 205 | #205-Panel | `5fe99180-4ef7-4a27-b2b4-7309dd83d812` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 206 | #206-2D Polyline | `dd604d67-9b5f-416e-9fbb-0819263b68e9` | 2D Polyline | in 4 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 207 | #207-2D Polyline | `d14425f9-533d-419f-91e1-1a1d962a3186` | 2D Polyline | in 4 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 208 | #208-2D Polyline | `380f39b7-9873-421a-af11-ed44574b9418` | 2D Polyline | in 4 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 209 | #209-Text Join | `f0e16fe8-e47f-4b33-97b0-863471c94bdc` | Text Join | in 1 / out 1 | Soporte (util) |  |
| 210 | #210-Boolean Toggle | `cec00a6d-b355-4ca1-9659-7362d5f52ae2` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 211 | #211-F3_MORPH_ATRIBUTOS_v02.py | `8eaf3a60-de2a-4e86-891a-92be4b05be59` | GhPython Script | in 7 / out 0 | Logica (script) | codigo 13603 chars; SIN consumidores (salida no usada) |
| 212 | #212-Panel | `9ee561bd-c38a-471e-b202-52fed1276b48` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 213 | #213-Value List | `e07db6bf-212d-4d7e-a2c9-da85f3cfd502` | Value List | in 0 / out 0 | Entrada (UI) |  |
| 214 | #214-Area | `92829854-3405-4203-b1dd-701411597671` | Area | in 1 / out 1 | Soporte (util) |  |
| 215 | #215-Panel | `3c58edf4-f463-43d5-995d-c033e34e16cb` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 216 | #216-F3_UNIDADES_TIPOLOGIAS_v02.py | `37bf9948-065e-4814-a36d-b49f7427dbb6` | GhPython Script | in 6 / out 1 | Logica (script) | codigo 32915 chars |
| 217 | #217-F3_ACCESOS_INTEGRADOR_v02.py | `768ebdc8-7e53-4541-b511-72408af73c32` | GhPython Script | in 3 / out 0 | Logica (script) | codigo 21277 chars; SIN consumidores (salida no usada) |
| 218 | #218-F1_OVERRIDE_USO_v01.py | `7aadd219-4308-492c-8d2b-c73d8041a9ef` | GhPython Script | in 2 / out 0 | Logica (script) | codigo 5360 chars; SIN consumidores (salida no usada) |
| 219 | #219-Panel | `a1c435d3-ee7e-416f-96bb-82f435afbc96` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 220 | #220-Panel | `4bb706ab-34fb-42de-b48d-bd164f045b0c` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 221 | #221-Panel | `75a2e5ab-b2f0-4563-8013-545833bd6b5a` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 222 | #222-Panel | `61d0c4e5-ea2a-46a3-ab18-21b1bb9de70a` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 223 | #223-Panel | `7f12bc12-850d-4bd3-928a-43c850272731` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 224 | #224-Panel | `317814cc-ff32-43ef-8565-fc611857b8df` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 225 | #225-Panel | `758487fe-61fb-4919-88c5-1c98d94d6725` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 226 | #226-Panel | `57232634-8272-4117-b257-37f79f02c366` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 227 | #227-Panel | `eb315550-d746-4cac-8aa7-afe18c78f761` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 228 | #228-Panel | `55030132-8f2b-45c2-856c-cfd3424bfb4f` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 229 | #229-F1_EXPORTAR_GFA_v02.4.py | `4d6fba96-1d12-4029-9683-b92d8c021e55` | GhPython Script | in 12 / out 0 | Logica (script) | codigo 10046 chars; SIN consumidores (salida no usada) |
| 230 | #230-Layer | `b2484541-d4e3-40d9-b622-b5bc904f545c` | Layer | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 231 | #231-2D Viewpoint | `10532c0d-7f87-4efb-8cc6-91ca21347225` | 2D Viewpoint | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 232 | #232-Line Type | `f8f36bf8-e511-4c4f-8203-6f386b7ad911` | Line Type | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 233 | #233-Pen | `380e0aa5-31ad-4108-9d94-ecb58bca326d` | Pen | in 0 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| 234 | #234-Number Slider | `e5ef868b-df0a-4d86-8bbf-11b08d795808` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 235 | #235-Number Slider | `f6e78136-37be-4b0c-8955-25177d5c659e` | Number Slider | in 0 / out 0 | Entrada (UI) |  |
| 236 | #236-Boolean Toggle | `828c34ab-5f7b-499e-bc03-a60ebcc8dce4` | Boolean Toggle | in 0 / out 0 | Entrada (UI) |  |
| 237 | #237-Panel | `27de6944-de5a-480c-9636-b21af4a9ec7d` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 238 | #238-Panel | `9233109c-fbb0-4ddb-b43c-bc7069417ad9` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 239 | #239-Panel | `59fbebbf-1edf-441c-9604-860d364fcba4` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 240 | #240-Panel | `f64dbcbb-eedb-433a-a177-8d65d8095f62` | Panel | in 0 / out 0 | Informativo (Panel) |  |
| 241 | #241-Zone Settings | `e9607073-1a60-4270-ada0-68ac9d7240f8` | Zone Settings | in 4 / out 1 | LC -> ArchiCAD | destino ArchiCAD |
| 242 | #242-Zone | `dd1fc9ba-7c58-436a-b866-92ffbe01f837` | Zone | in 4 / out 0 | LC -> ArchiCAD | destino ArchiCAD; SIN consumidores (salida no usada) |
| — | Group | `c51b3e5c-d0e7-4cd4-97c6-1153940d7608` | Group | in 0 / out 0 | Grupo |  |
| — | Group | `4444cede-7b3a-4bdc-ac22-644cf5ab24d8` | Group | in 0 / out 0 | Grupo |  |
| — | 01 / Entrada JSON y Contexto Urbano | `d0d0789f-a7d6-4c5a-96f5-9ab64e6d39dd` | Group | in 0 / out 0 | Grupo |  |
| — | 02 / Capas Archicad (XML / API) | `f55b4e66-2095-4e4d-bd50-3b107b353abc` | Group | in 0 / out 0 | Grupo |  |
| — | 03 / Clasificación Linderos y Patios | `9ebc95fc-13c5-42db-80d5-f79c660b7b39` | Group | in 0 / out 0 | Grupo |  |
| — | 04 / Normativa y Alturas Urbanas | `cb6fdc2d-12be-4d1f-8006-e15c13657eb4` | Group | in 0 / out 0 | Grupo |  |
| — | 05 / Rutas y Configuración JSON | `1dee5c9a-02b6-4b1b-828d-82a9880dc848` | Group | in 0 / out 0 | Grupo |  |
| — | 06 / Exportación GFA a JSON | `6e99f404-cea9-421d-9c51-c2b89878d1ed` | Group | in 0 / out 0 | Grupo |  |
| — | 07 / Dibujo 2D en Archicad (Tapir) | `ea1b9473-3536-4ade-9b4b-fcbaf5b7f9d6` | Group | in 0 / out 0 | Grupo |  |
| — | 08 / Contexto 3D / Morph Solid | `bdbe0d15-9943-4176-9847-9b28ccb0b83b` | Group | in 0 / out 0 | Grupo |  |
| — | 09 / Terreno y Mallas Archicad | `08bc3460-41b1-49b5-a61d-6cabc1464c5b` | Group | in 0 / out 0 | Grupo |  |
| — | 10 / Utilidades y Diagnóstico | `bba83612-eff3-4cc4-b451-ed16d784b74b` | Group | in 0 / out 0 | Grupo |  |
| — | 2D Curve | `bda3fcdb-b6ea-418b-9348-eed9e17e5f51` | Group | in 0 / out 0 | Grupo |  |
| — | 2D Polyline | `653ba5b1-cb93-490d-9ab2-50a59fd0dfa6` | Group | in 0 / out 0 | Grupo |  |
| — | 2D Polyline | `c74b7a94-748c-4b5d-987f-31e9fe9e7415` | Group | in 0 / out 0 | Grupo |  |
| — | 2D Polyline | `cfcd060c-db46-4cd4-9401-c71aac722bee` | Group | in 0 / out 0 | Grupo |  |
| — | 2D Polyline | `739aad43-11f7-42ec-84a4-8083989da73d` | Group | in 0 / out 0 | Grupo |  |
| — | 2D Viewpoint | `e39fbfbb-aff0-4edc-ae63-be8f1543f8aa` | Group | in 0 / out 0 | Grupo |  |
| — | 2D Viewpoint | `8edbf330-c75a-4e61-981e-4e04884a9143` | Group | in 0 / out 0 | Grupo |  |
| — | 2D Viewpoint | `f0f06b7e-16f1-4f38-b2f8-ee748df8ad0d` | Group | in 0 / out 0 | Grupo |  |
| — | 2D Viewpoint | `f6dca2d9-bf99-4afd-9d43-168369c42626` | Group | in 0 / out 0 | Grupo |  |
| — | 2D Viewpoint | `f76e9b10-9007-4090-97ad-ff28fbe0d7d5` | Group | in 0 / out 0 | Grupo |  |
| — | Addition | `5f84844c-4bac-4f49-b8ef-8398109ee455` | Group | in 0 / out 0 | Grupo |  |
| — | Area | `aec8eb51-e605-493e-84b1-4647de327ef2` | Group | in 0 / out 0 | Grupo |  |
| — | Base normativa · límites para distribución | `a0d539fd-cfa4-40a3-bcc1-a12a03606794` | Group | in 0 / out 0 | Grupo |  |
| — | Bifocals | `8597969f-4fb0-4f55-a67d-a51c7484af51` | Group | in 0 / out 0 | Grupo |  |
| — | CreateMeshes | `7d62e125-6115-44ce-b346-1ee99a5129e5` | Group | in 0 / out 0 | Grupo |  |
| — | Curve | `e2365733-260c-4ba3-8db4-3452c4d485ae` | Group | in 0 / out 0 | Grupo |  |
| — | Curve | `d830771b-88f0-4404-914c-f2a39c60e44a` | Group | in 0 / out 0 | Grupo |  |
| — | Curve | `327e5b72-4a27-4a57-94a3-070beb30257f` | Group | in 0 / out 0 | Grupo |  |
| — | Curve | `3df2f94b-7ba3-4f0e-b840-2993f3c21f1d` | Group | in 0 / out 0 | Grupo |  |
| — | Datos ArchiCAD | `48f3fa48-29d2-41ba-b405-053ff73fd733` | Group | in 0 / out 0 | Grupo |  |
| — | Deconstruct 2D Polyline | `7b786066-0f88-41be-890c-469f0123e4c7` | Group | in 0 / out 0 | Grupo |  |
| — | Deconstruct 2D Polyline | `9e23cc66-233c-4d45-91ed-0f117d32f113` | Group | in 0 / out 0 | Grupo |  |
| — | Deconstruct 2D Polyline | `1d39d7be-e89a-4ea1-a9b1-f7202debc4c4` | Group | in 0 / out 0 | Grupo |  |
| — | Deconstruct 2D Polyline | `b2d84cc8-3fd8-4ad1-8084-5fbf5e80a104` | Group | in 0 / out 0 | Grupo |  |
| — | Deconstruct 2D Polyline | `d605a481-56b3-4b17-9a5c-7a389ba0aa61` | Group | in 0 / out 0 | Grupo |  |
| — | Deconstruct 2D Polyline | `5eb1b0d7-1848-47af-a7ea-392faa183ea3` | Group | in 0 / out 0 | Grupo |  |
| — | Deconstruct Mesh | `55ce2018-68c3-4009-9b37-c91ac4a8f36a` | Group | in 0 / out 0 | Grupo |  |
| — | Determinación altura ejes | `8e92ae56-55dc-484e-9d6d-80133e013c5c` | Group | in 0 / out 0 | Grupo |  |
| — | Dibujo Raw en ArchiCAD | `8c839f38-130b-4f1f-9a96-bef0ed55d6f5` | Group | in 0 / out 0 | Grupo |  |
| — | Discontinuity | `f9850dd2-f269-4e53-9ffd-c4fcffe12430` | Group | in 0 / out 0 | Grupo |  |
| — | End Points | `a173df40-0a09-45e6-88c0-d71e21130631` | Group | in 0 / out 0 | Grupo |  |
| — | F1_ETAPA2_NORMATIVA_v10.py | `dcca63ed-f231-4d9d-ad06-6b5cfa34ed1c` | Python 3 Script | in 18 / out 2 | Logica (script) | codigo 0 chars |
| — | Fancy Names | `6189090f-7bd9-40a2-9efd-da6728321f62` | GhPython Script | in 1 / out 0 | Logica (script) | codigo 2958 chars; SIN consumidores (salida no usada) |
| — | Fase 3 - Creacion Volumenes | `83d4a3cc-a5bc-4fa8-99f1-105d0765d1d6` | Group | in 0 / out 0 | Grupo |  |
| — | File Path | `24d07532-eaf3-4536-8f97-a87f946fddcb` | Group | in 0 / out 0 | Grupo |  |
| — | File Path | `f62705a6-8098-47f0-b13d-9c8cb3c255ea` | Group | in 0 / out 0 | Grupo |  |
| — | File Path | `9d399dd1-4f09-462b-8105-0853ea9afe1d` | Group | in 0 / out 0 | Grupo |  |
| — | File Path | `03f30d6a-6faf-49cb-b7e3-2ee177c19532` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `48c48d04-9a53-4fed-a77d-b1acd3fc016e` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `66c3f7a4-544f-4a2f-bcfc-71fd774e6858` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `1fc65c1e-504d-4901-8408-3828fc3b8cb1` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `95085a1d-6f0e-4097-868f-ded4f997cffc` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `a77cc3a0-20b5-4ba9-8b88-d44aded5d57a` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `11b98876-7bfe-4441-9679-a0e223262090` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `b658a37e-1076-46be-9681-c0710779cd6f` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `4126f986-18c5-4276-a9e3-5b7b55d5a09f` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `fbdcec7f-87f9-4423-a559-6e14d1515d7d` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `32858c60-b343-4f3f-ae60-b5de904d3137` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `7d6ed153-a7e4-4d69-87fc-d548a5258463` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `58bebead-5414-4ec1-9703-1520dcbb5f28` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `5e4574ae-b93f-40c3-9367-9ca6435b58ad` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `bc74d728-a4b8-48c3-9992-2b20b212e781` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `50bb986e-9632-4fed-91d2-3af20f4fa870` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `39d55583-92f5-44b6-9f04-74071a1968b7` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `d6e38120-9472-4777-bc40-8f50b0145b58` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `f380bfb9-29eb-419f-97d8-159bfcd9a8eb` | Group | in 0 / out 0 | Grupo |  |
| — | GhPython Script | `4b5a4d6f-1c0b-4e0d-9d18-b55f71e64518` | Group | in 0 / out 0 | Grupo |  |
| — | Layer | `ac31b9be-a555-46f6-9105-1a1234c5609c` | Group | in 0 / out 0 | Grupo |  |
| — | Layer | `80319fd1-4c95-4d74-926f-f6b3c35d35e2` | Group | in 0 / out 0 | Grupo |  |
| — | Layer | `ea19d3ee-d4e3-47dc-a92c-e6bb5f3a5474` | Group | in 0 / out 0 | Grupo |  |
| — | Layer | `72109838-309b-438e-a5ef-86fbe4e32f4f` | Group | in 0 / out 0 | Grupo |  |
| — | Layer | `259aa7b9-930f-4131-81be-0f7c590b2f51` | Group | in 0 / out 0 | Grupo |  |
| — | Line Type | `d23bb2c0-42a6-425b-be14-58b649654fd6` | Group | in 0 / out 0 | Grupo |  |
| — | Line Type | `656db93c-beab-4404-a0ff-9195c4a440d8` | Group | in 0 / out 0 | Grupo |  |
| — | Line Type | `ee8b1809-25f6-4600-a694-117852391d8a` | Group | in 0 / out 0 | Grupo |  |
| — | Line Type | `28a8f8f0-4ad7-4dfb-9d82-9f52b725bb33` | Group | in 0 / out 0 | Grupo |  |
| — | Line Type | `a884cb60-0ed7-4b06-8d04-3775154a413e` | Group | in 0 / out 0 | Grupo |  |
| — | Merge | `b74fc9b4-f8ea-4991-9652-1d1c3c5c63b4` | Group | in 0 / out 0 | Grupo |  |
| — | Merge | `0f0dd9c3-13b8-43c1-b5db-e1fdad5f6517` | Group | in 0 / out 0 | Grupo |  |
| — | Merge | `6804758d-b05a-4073-b195-eb975d43bb72` | Group | in 0 / out 0 | Grupo |  |
| — | Merge | `5df11558-1569-4779-8be4-c45a0f293859` | Group | in 0 / out 0 | Grupo |  |
| — | Merge | `bdaf80ce-4b7f-4bb8-bed7-1faf61d26255` | Group | in 0 / out 0 | Grupo |  |
| — | Merge | `7a3598ea-79fc-4191-ab4d-939851d71de3` | Group | in 0 / out 0 | Grupo |  |
| — | Merge | `6fbe85e5-c097-4573-ba62-a146755f3b17` | Group | in 0 / out 0 | Grupo |  |
| — | Merge | `52305f84-6489-4e1d-8556-9c1a9c121491` | Group | in 0 / out 0 | Grupo |  |
| — | Merge | `47f99169-095e-4421-a550-53e7bd898a06` | Group | in 0 / out 0 | Grupo |  |
| — | Merge | `04b339dd-319e-49ca-9a6f-a102167031c2` | Group | in 0 / out 0 | Grupo |  |
| — | Mesh | `f210e566-7683-44c1-b59e-fa0f0bb6e743` | Group | in 0 / out 0 | Grupo |  |
| — | Mesh | `691f6795-6926-4ea5-afd9-76fcbdf9102a` | Group | in 0 / out 0 | Grupo |  |
| — | MeshRidgeTypes | `05a5d042-561f-4d6d-8fa8-fd7b50cfcf5d` | Group | in 0 / out 0 | Grupo |  |
| — | MeshSkirtTypes | `4744dbec-c0a8-4af8-85e7-37e79c0c72f1` | Group | in 0 / out 0 | Grupo |  |
| — | Morph Solid | `43de239b-3381-44be-8947-39da36da4b89` | Group | in 0 / out 0 | Grupo |  |
| — | Ocupaciones por piso | `bcabde6b-32bf-446b-85b5-c4d9318df319` | Group | in 0 / out 0 | Grupo |  |
| — | Ocupaciones por piso | `62e64c98-2145-4126-b833-d8e698330fb1` | Group | in 0 / out 0 | Grupo |  |
| — | Ocupaciones por piso | `b5256602-2ac9-4170-8537-1b532811f746` | Group | in 0 / out 0 | Grupo |  |
| — | Pen | `dc39e94d-59b9-405e-8270-2f22b218aae6` | Group | in 0 / out 0 | Grupo |  |
| — | Pen | `084be978-0ae2-4fee-9012-e37669cacf4f` | Group | in 0 / out 0 | Grupo |  |
| — | Pen | `ea1aaf6f-f6f5-4c95-9273-147860969df1` | Group | in 0 / out 0 | Grupo |  |
| — | Pen | `b274f661-da84-4159-85fb-bedf680d6437` | Group | in 0 / out 0 | Grupo |  |
| — | Pen | `d785abe5-494e-4dc3-921e-7c8541089ff4` | Group | in 0 / out 0 | Grupo |  |
| — | Polyline Settings | `7fe40b57-95d0-4a2c-ad09-1c48a45aa427` | Group | in 0 / out 0 | Grupo |  |
| — | Polyline Settings | `dade3cd9-a9db-4ccb-a5ca-33d14f9629e7` | Group | in 0 / out 0 | Grupo |  |
| — | Polyline Settings | `c2a2815f-3609-4da3-9612-7b2f43704a79` | Group | in 0 / out 0 | Grupo |  |
| — | Polyline Settings | `e10ae037-bd24-462d-a3a1-0f7500394a09` | Group | in 0 / out 0 | Grupo |  |
| — | PolylineDetails | `f6a2508e-264b-4940-a051-72ba3dd29883` | Group | in 0 / out 0 | Grupo |  |
| — | Python 3 Script | `86a44bef-ebcb-4a56-b24a-8c9549cbbfad` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `4b900851-e75a-48f1-ba0d-8cf4ea00e76e` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `c4d653b3-3196-4aa6-847b-44ad74646da4` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `f2a60e3a-a707-41f6-a37c-5eb516168a06` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `86df9c01-fc44-43ca-b375-afab9cd66fea` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `7468089c-1dd3-457d-9884-5fbc912cfee8` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `b385f0bd-f435-4e30-a05b-103ec688a5bb` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `3b0c13d7-e04c-4247-8134-ff796efb9cfc` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `b54076d8-4057-4457-b061-91a3af524cd7` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `bf2a992c-058a-4c4b-b11d-6521716b5180` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `905a123a-b0d1-42a8-9740-0043640d7924` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `d986fa47-b098-48b8-873e-6c31d06795d1` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `82a62dbb-a2a0-4de2-a1a8-730564c6daba` | Group | in 0 / out 0 | Grupo |  |
| — | Relay | `759cecb7-c70c-4fe7-93b0-996d2b605dd5` | Group | in 0 / out 0 | Grupo |  |
| — | Text Join | `db41cf38-208a-43c1-a4da-f8c064375398` | Group | in 0 / out 0 | Grupo |  |
| — | Text Join | `0307009e-6072-4f4f-ab06-b60d5e5c5747` | Group | in 0 / out 0 | Grupo |  |
| — | Text Join | `43bad581-c6dd-48a3-b57a-577ccd5fb624` | Group | in 0 / out 0 | Grupo |  |
| — | Text Join | `48a10705-dec0-4646-9dd3-67d4324d3715` | Group | in 0 / out 0 | Grupo |  |
| — | Text Join | `35e56cd0-c11e-4cf4-9f9f-d3b7a52bbd6b` | Group | in 0 / out 0 | Grupo |  |
| — | Text Join | `7184e7d3-c7c1-4f71-88ec-552ebff923ad` | Group | in 0 / out 0 | Grupo |  |
| — | Text Join | `156f20b0-e8e9-4db9-8df4-2dd572456924` | Group | in 0 / out 0 | Grupo |  |
| — | Text Join | `c5e85644-0b7a-44d2-9f73-0815100c1677` | Group | in 0 / out 0 | Grupo |  |
| — | Value List | `604a0309-5dd2-448d-a31b-16be5868dc2a` | Group | in 0 / out 0 | Grupo |  |
| — | Value List | `4870ebe5-f432-4c8f-8915-a2f58d3ae21d` | Group | in 0 / out 0 | Grupo |  |
| — | Value List | `4c2febf1-3cdf-4197-8e54-9c57ceb9b24b` | Group | in 0 / out 0 | Grupo |  |
| — | Value List | `d98de3cb-c4b3-4cb7-aaf8-98ee6bc2da08` | Group | in 0 / out 0 | Grupo |  |
| — | Value List | `6a18beb3-6ffb-4668-8963-10c1e9ff1ee4` | Group | in 0 / out 0 | Grupo |  |
| — | Zone | `f60b9736-2e9c-4ed7-9330-175e5efe08a6` | Group | in 0 / out 0 | Grupo |  |
| — | Zone Settings | `4cc7c8d7-057b-4735-bf21-9e207393cbe2` | Group | in 0 / out 0 | Grupo |  |

## Cableado clave (zonas / implantacion / stories)

```
#197-F3_VOLUM_GENERADOR_v08.py.zonas_alturas -> #241-Zone Settings.Height
#197-F3_VOLUM_GENERADOR_v08.py.zonas_centroides -> #242-Zone.Stamp Position
#197-F3_VOLUM_GENERADOR_v08.py.zonas_nombres -> #241-Zone Settings.Name
#197-F3_VOLUM_GENERADOR_v08.py.zonas_perimetros -> #242-Zone.Polygon
#197-F3_VOLUM_GENERADOR_v08.py.zonas_pisos -> #241-Zone Settings.Number
#200-F3_DISTRIBUCION_v03.8.py.barras_json -> #124-F1_ETAPA2_NORMATIVA_v09.1.py.barras_json
#200-F3_DISTRIBUCION_v03.8.py.barras_json -> #197-F3_VOLUM_GENERADOR_v08.py.barras_implantadas_json
#200-F3_DISTRIBUCION_v03.8.py.layout_espacial_json -> #197-F3_VOLUM_GENERADOR_v08.py.layout_usos_json
#241-Zone Settings.Zone Settings -> #242-Zone.Zone Settings
<828c34ab> -> #242-Zone.Synchronize
<d4aa2e48> -> #200-F3_DISTRIBUCION_v03.8.py.n_barras_objetivo
<e5ef868b> -> #241-Zone Settings.Renovation Status
```

## Leyenda

- **Grupo**: contenedor organizativo. No borrar sin revisar.
- **Informativo (Panel)**: solo muestra texto; no participa en el calculo.
- **LC -> ArchiCAD**: componente de la Live Connection (destino).
- **Logica (script)**: GhPython/Python3; indispensable si tiene consumidores.
- **Entrada (UI)**: sliders/toggles/listas: parametros del operador.
- **Soporte (util)**: merges/relays/joins/curvas: utilidades de cableado.
- **Otro**: revisar caso a caso.