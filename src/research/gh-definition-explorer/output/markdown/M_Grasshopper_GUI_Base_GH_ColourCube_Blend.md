# M_Grasshopper_GUI_Base_GH_ColourCube_Blend

﻿ GH\_ColourCube.Blend Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_ColourCube Class](../html/T_Grasshopper_GUI_Base_GH_ColourCube.htm "GH_ColourCube Class")

[GH\_ColourCube Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_ColourCube.htm "GH_ColourCube Methods")

[Average Method](../html/Overload_Grasshopper_GUI_Base_GH_ColourCube_Average.htm "Average Method ")

[Blend Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_Blend.htm "Blend Method ")

[ColorAtRail Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_ColorAtRail.htm "ColorAtRail Method ")

[ColorAtSlice Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_ColorAtSlice.htm "ColorAtSlice Method ")

[RenderAll Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderAll.htm "RenderAll Method ")

[RenderBackEdges Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderBackEdges.htm "RenderBackEdges Method ")

[RenderBackFaces Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderBackFaces.htm "RenderBackFaces Method ")

[RenderDropShadow Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderDropShadow.htm "RenderDropShadow Method ")

[RenderEdgeShadows Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderEdgeShadows.htm "RenderEdgeShadows Method ")

[RenderForeEdges Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderForeEdges.htm "RenderForeEdges Method ")

[RenderGrip Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderGrip.htm "RenderGrip Method ")

[RenderPivot Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderPivot.htm "RenderPivot Method ")

[RenderSilhouetteEdges Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderSilhouetteEdges.htm "RenderSilhouetteEdges Method ")

[RenderSlice Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderSlice.htm "RenderSlice Method ")

[RenderSliceDropShadow Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderSliceDropShadow.htm "RenderSliceDropShadow Method ")

[RenderSliceEdgeShadows Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderSliceEdgeShadows.htm "RenderSliceEdgeShadows Method ")

[RenderSliceSilhouetteEdges Method](../html/M_Grasshopper_GUI_Base_GH_ColourCube_RenderSliceSilhouetteEdges.htm "RenderSliceSilhouetteEdges Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ColourCubeAddLanguageSpecificTextSet("LSTF0E26382\_0?cpp=::|nu=.");Blend Method |

Inteprolate between two colours.

**Namespace:**
 [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Color Blend(
	Color A,
	Color B,
	double t
)
```

```
Public Function Blend ( 
	A As Color,
	B As Color,
	t As Double
) As Color
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

A
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF0E26382\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    First colour.

B
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF0E26382\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Second colour.

t
:   Type: [SystemAddLanguageSpecificTextSet("LSTF0E26382\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Interpolation parameter.

#### Return Value

Type: [Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
Interpolated colour.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ColourCube Class](T_Grasshopper_GUI_Base_GH_ColourCube.htm)

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)