# M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveTagArtist

﻿ GH\_Canvas.RemoveTagArtist Method (IGH\_TagArtist)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Canvas Class](../html/T_Grasshopper_GUI_Canvas_GH_Canvas.htm "GH_Canvas Class")

[GH\_Canvas Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Canvas.htm "GH_Canvas Methods")

[RemoveTagArtist Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Canvas_RemoveTagArtist.htm "RemoveTagArtist Method ")

[RemoveTagArtist Method (Guid)](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveTagArtist_1.htm "RemoveTagArtist Method (Guid)")

[RemoveTagArtist Method (IGH\_TagArtist)](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveTagArtist.htm "RemoveTagArtist Method (IGH_TagArtist)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CanvasAddLanguageSpecificTextSet("LSTD5F1D812\_0?cpp=::|nu=.");RemoveTagArtist Method (IGH\_TagArtist) |

Remove a specific tag artist from this canvas.
If the instance occurs multiple times in the TagArtist list,
all instances will be removed.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int RemoveTagArtist(
	IGH_TagArtist artist
)
```

```
Public Function RemoveTagArtist ( 
	artist As IGH_TagArtist
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

artist
:   Type: [Grasshopper.GUI.Canvas.TagArtistsAddLanguageSpecificTextSet("LSTD5F1D812\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_TagArtist](T_Grasshopper_GUI_Canvas_TagArtists_IGH_TagArtist.htm)  
    TagArtist to remove.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
The number of IGH\_TagArtist instances removed.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Canvas Class](T_Grasshopper_GUI_Canvas_GH_Canvas.htm)

[RemoveTagArtist Overload](Overload_Grasshopper_GUI_Canvas_GH_Canvas_RemoveTagArtist.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)