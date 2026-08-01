# M_Grasshopper_GUI_Canvas_TagArtists_GH_TagArtist_Paint

﻿ GH\_TagArtist.Paint Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas.TagArtists](../html/N_Grasshopper_GUI_Canvas_TagArtists.htm "Grasshopper.GUI.Canvas.TagArtists")

[GH\_TagArtist Class](../html/T_Grasshopper_GUI_Canvas_TagArtists_GH_TagArtist.htm "GH_TagArtist Class")

[GH\_TagArtist Methods](../html/Methods_T_Grasshopper_GUI_Canvas_TagArtists_GH_TagArtist.htm "GH_TagArtist Methods")

[Paint Method](../html/M_Grasshopper_GUI_Canvas_TagArtists_GH_TagArtist_Paint.htm "Paint Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TagArtistAddLanguageSpecificTextSet("LST2D12300B\_0?cpp=::|nu=.");Paint Method |

This method is called whenever a Canvas channel is painted

**Namespace:**
 [Grasshopper.GUI.Canvas.TagArtists](N_Grasshopper_GUI_Canvas_TagArtists.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract void Paint(
	GH_Canvas canvas,
	GH_CanvasChannel channel
)
```

```
Public MustOverride Sub Paint ( 
	canvas As GH_Canvas,
	channel As GH_CanvasChannel
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

canvas
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST2D12300B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Canvas](T_Grasshopper_GUI_Canvas_GH_Canvas.htm)  
    Canvas that is currently painting.

channel
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST2D12300B\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CanvasChannel](T_Grasshopper_GUI_Canvas_GH_CanvasChannel.htm)  
    Channel that is currently being painted.

#### Implements

[IGH\_TagArtistAddLanguageSpecificTextSet("LST2D12300B\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Paint(GH\_Canvas, GH\_CanvasChannel)](M_Grasshopper_GUI_Canvas_TagArtists_IGH_TagArtist_Paint.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TagArtist Class](T_Grasshopper_GUI_Canvas_TagArtists_GH_TagArtist.htm)

[Grasshopper.GUI.Canvas.TagArtists Namespace](N_Grasshopper_GUI_Canvas_TagArtists.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)