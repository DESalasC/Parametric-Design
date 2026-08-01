# M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseDoubleClick

﻿ IGH\_ResponsiveObject.RespondToMouseDoubleClick Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[IGH\_ResponsiveObject Interface](../html/T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm "IGH_ResponsiveObject Interface")

[IGH\_ResponsiveObject Methods](../html/Methods_T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm "IGH_ResponsiveObject Methods")

[RespondToKeyDown Method](../html/M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToKeyDown.htm "RespondToKeyDown Method ")

[RespondToKeyUp Method](../html/M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToKeyUp.htm "RespondToKeyUp Method ")

[RespondToMouseDoubleClick Method](../html/M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseDoubleClick.htm "RespondToMouseDoubleClick Method ")

[RespondToMouseDown Method](../html/M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseDown.htm "RespondToMouseDown Method ")

[RespondToMouseMove Method](../html/M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseMove.htm "RespondToMouseMove Method ")

[RespondToMouseUp Method](../html/M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseUp.htm "RespondToMouseUp Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ResponsiveObjectAddLanguageSpecificTextSet("LSTC251BBD8\_0?cpp=::|nu=.");RespondToMouseDoubleClick Method |

This function will be called whenever the left button is double-clicked over the canvas.
If you are active, you will be the only object who gets called.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
GH_ObjectResponse RespondToMouseDoubleClick(
	GH_Canvas sender,
	GH_CanvasMouseEvent e
)
```

```
Function RespondToMouseDoubleClick ( 
	sender As GH_Canvas,
	e As GH_CanvasMouseEvent
) As GH_ObjectResponse
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

sender
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LSTC251BBD8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Canvas](T_Grasshopper_GUI_Canvas_GH_Canvas.htm)  
    Base canvas.

e
:   Type: [Grasshopper.GUIAddLanguageSpecificTextSet("LSTC251BBD8\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CanvasMouseEvent](T_Grasshopper_GUI_GH_CanvasMouseEvent.htm)  
    Mouse event arguments.

#### Return Value

Type: [GH\_ObjectResponse](T_Grasshopper_GUI_Canvas_GH_ObjectResponse.htm)  
All Response flags are valid.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_ResponsiveObject Interface](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)