# M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedStyle_1

﻿ GH\_CapsuleRenderEngine.GetImpliedStyle Method (GH\_Palette, Boolean, Boolean, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_CapsuleRenderEngine Class](../html/T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm "GH_CapsuleRenderEngine Class")

[GH\_CapsuleRenderEngine Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm "GH_CapsuleRenderEngine Methods")

[GetImpliedStyle Method](../html/Overload_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedStyle.htm "GetImpliedStyle Method ")

[GetImpliedStyle Method (GH\_Palette, IGH\_Attributes)](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedStyle.htm "GetImpliedStyle Method (GH_Palette, IGH_Attributes)")

[GetImpliedStyle Method (GH\_Palette, Boolean, Boolean, Boolean)](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedStyle_1.htm "GetImpliedStyle Method (GH_Palette, Boolean, Boolean, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CapsuleRenderEngineAddLanguageSpecificTextSet("LST947B6505\_0?cpp=::|nu=.");GetImpliedStyle Method (GH\_Palette, Boolean, Boolean, Boolean) |

Static (Shared in VB) method for solving which palette style is implied by the properties.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_PaletteStyle GetImpliedStyle(
	GH_Palette palette,
	bool selected,
	bool locked,
	bool hidden
)
```

```
Public Shared Function GetImpliedStyle ( 
	palette As GH_Palette,
	selected As Boolean,
	locked As Boolean,
	hidden As Boolean
) As GH_PaletteStyle
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

palette
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST947B6505\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Palette](T_Grasshopper_GUI_Canvas_GH_Palette.htm)  
    Palette hint.

selected
:   Type: [SystemAddLanguageSpecificTextSet("LST947B6505\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    Specifies whether the *selected* flavour of a palette needs to be returned.

locked
:   Type: [SystemAddLanguageSpecificTextSet("LST947B6505\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, the returned palette style is always **Locked**.

hidden
:   Type: [SystemAddLanguageSpecificTextSet("LST947B6505\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, the returned palette style is always **Hidden**.

#### Return Value

Type: [GH\_PaletteStyle](T_Grasshopper_GUI_Canvas_GH_PaletteStyle.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_CapsuleRenderEngine Class](T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm)

[GetImpliedStyle Overload](Overload_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedStyle.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)