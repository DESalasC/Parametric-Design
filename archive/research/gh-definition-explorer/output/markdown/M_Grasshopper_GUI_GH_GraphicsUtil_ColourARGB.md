# M_Grasshopper_GUI_GH_GraphicsUtil_ColourARGB

﻿ GH\_GraphicsUtil.ColourARGB Method (Double, Double, Double)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[ColourARGB Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_ColourARGB.htm "ColourARGB Method ")

[ColourARGB Method (Double, Double, Double)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_ColourARGB.htm "ColourARGB Method (Double, Double, Double)")

[ColourARGB Method (Int32, Int32, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_ColourARGB_1.htm "ColourARGB Method (Int32, Int32, Int32)")

[ColourARGB Method (Int32, Int32, Int32, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_ColourARGB_2.htm "ColourARGB Method (Int32, Int32, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LST86B2B5BD\_0?cpp=::|nu=.");ColourARGB Method (Double, Double, Double) |

Create a colour from floating ARGB channels (0.0~1.0).
Channels are clipped to valid ranges.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static Color ColourARGB(
	double r,
	double g,
	double b
)
```

```
Public Shared Function ColourARGB ( 
	r As Double,
	g As Double,
	b As Double
) As Color
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

r
:   Type: [SystemAddLanguageSpecificTextSet("LST86B2B5BD\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)

g
:   Type: [SystemAddLanguageSpecificTextSet("LST86B2B5BD\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)

b
:   Type: [SystemAddLanguageSpecificTextSet("LST86B2B5BD\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)

#### Return Value

Type: [Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
The colour implied by the RGB channel values.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[ColourARGB Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_ColourARGB.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)