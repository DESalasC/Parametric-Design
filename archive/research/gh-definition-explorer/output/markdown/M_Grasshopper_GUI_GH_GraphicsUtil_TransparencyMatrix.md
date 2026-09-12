# M_Grasshopper_GUI_GH_GraphicsUtil_TransparencyMatrix

﻿ GH\_GraphicsUtil.TransparencyMatrix Method (Double)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[TransparencyMatrix Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_TransparencyMatrix.htm "TransparencyMatrix Method ")

[TransparencyMatrix Method (Double)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_TransparencyMatrix.htm "TransparencyMatrix Method (Double)")

[TransparencyMatrix Method (Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_TransparencyMatrix_1.htm "TransparencyMatrix Method (Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LSTDE612B49\_0?cpp=::|nu=.");TransparencyMatrix Method (Double) |

Create an image transparency matrix for a specific blending factor.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static ColorMatrix TransparencyMatrix(
	double fade
)
```

```
Public Shared Function TransparencyMatrix ( 
	fade As Double
) As ColorMatrix
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

fade
:   Type: [SystemAddLanguageSpecificTextSet("LSTDE612B49\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Alpha fade amount. 0.0=complete transparency, 1.0=original transparency.

#### Return Value

Type: [ColorMatrix](https://docs.microsoft.com/dotnet/api/system.drawing.imaging.colormatrix)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[TransparencyMatrix Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_TransparencyMatrix.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)