# M_Grasshopper_GUI_Gradient_GH_Gradient_MouseUp

﻿ GH\_Gradient.MouseUp Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Gradient](../html/N_Grasshopper_GUI_Gradient.htm "Grasshopper.GUI.Gradient")

[GH\_Gradient Class](../html/T_Grasshopper_GUI_Gradient_GH_Gradient.htm "GH_Gradient Class")

[GH\_Gradient Methods](../html/Methods_T_Grasshopper_GUI_Gradient_GH_Gradient.htm "GH_Gradient Methods")

[AddGrip Method](../html/Overload_Grasshopper_GUI_Gradient_GH_Gradient_AddGrip.htm "AddGrip Method ")

[ColourAt Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_ColourAt.htm "ColourAt Method ")

[DeleteGripRegion Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_DeleteGripRegion.htm "DeleteGripRegion Method ")

[DisplayGradientEditor Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_DisplayGradientEditor.htm "DisplayGradientEditor Method ")

[DisplayGripColourPicker Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_DisplayGripColourPicker.htm "DisplayGripColourPicker Method ")

[EarthlyBrown Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_EarthlyBrown.htm "EarthlyBrown Method ")

[Forest Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Forest.htm "Forest Method ")

[GreyScale Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_GreyScale.htm "GreyScale Method ")

[Heat Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Heat.htm "Heat Method ")

[MouseDown Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_MouseDown.htm "MouseDown Method ")

[MouseDragAbort Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_MouseDragAbort.htm "MouseDragAbort Method ")

[MouseMove Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_MouseMove.htm "MouseMove Method ")

[MouseUp Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_MouseUp.htm "MouseUp Method ")

[NearestGrip Method](../html/Overload_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip.htm "NearestGrip Method ")

[NewGripRegion Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_NewGripRegion.htm "NewGripRegion Method ")

[NormalizeGrips Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_NormalizeGrips.htm "NormalizeGrips Method ")

[OnGradientChanged Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_OnGradientChanged.htm "OnGradientChanged Method ")

[OnGradientChangedIntermediate Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_OnGradientChangedIntermediate.htm "OnGradientChangedIntermediate Method ")

[OnSelectionChanged Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_OnSelectionChanged.htm "OnSelectionChanged Method ")

[Read Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Read.htm "Read Method ")

[RemoveGrip Method](../html/Overload_Grasshopper_GUI_Gradient_GH_Gradient_RemoveGrip.htm "RemoveGrip Method ")

[Render\_Background Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Render_Background.htm "Render_Background Method ")

[Render\_Gradient Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Render_Gradient.htm "Render_Gradient Method ")

[Render\_Grips Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Render_Grips.htm "Render_Grips Method ")

[SoGay Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_SoGay.htm "SoGay Method ")

[Spectrum Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Spectrum.htm "Spectrum Method ")

[Traffic Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Traffic.htm "Traffic Method ")

[Write Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Write.htm "Write Method ")

[Zebra Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Zebra.htm "Zebra Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GradientAddLanguageSpecificTextSet("LST358D5948\_0?cpp=::|nu=.");MouseUp Method |

Terminate grip drag.

**Namespace:**
 [Grasshopper.GUI.Gradient](N_Grasshopper_GUI_Gradient.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool MouseUp(
	RectangleF dest,
	PointF pt,
	bool deselect
)
```

```
Public Function MouseUp ( 
	dest As RectangleF,
	pt As PointF,
	deselect As Boolean
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

dest
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST358D5948\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Destination rectangle of gradient

pt
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST358D5948\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Mouse location in destination coordinates

deselect
:   Type: [SystemAddLanguageSpecificTextSet("LST358D5948\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

#### Implements

IGradient.MouseUp(RectangleF, PointF, Boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Gradient Class](T_Grasshopper_GUI_Gradient_GH_Gradient.htm)

[Grasshopper.GUI.Gradient Namespace](N_Grasshopper_GUI_Gradient.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)