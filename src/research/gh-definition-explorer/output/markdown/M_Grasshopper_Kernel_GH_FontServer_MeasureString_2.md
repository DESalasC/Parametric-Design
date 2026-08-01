# M_Grasshopper_Kernel_GH_FontServer_MeasureString_2

﻿ GH\_FontServer.MeasureString Method (String, Font, Single)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_FontServer Class](../html/T_Grasshopper_Kernel_GH_FontServer.htm "GH_FontServer Class")

[GH\_FontServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_FontServer.htm "GH_FontServer Methods")

[MeasureString Method](../html/Overload_Grasshopper_Kernel_GH_FontServer_MeasureString.htm "MeasureString Method ")

[MeasureString Method (String, Font)](../html/M_Grasshopper_Kernel_GH_FontServer_MeasureString.htm "MeasureString Method (String, Font)")

[MeasureString Method (String, Font, SizeF)](../html/M_Grasshopper_Kernel_GH_FontServer_MeasureString_1.htm "MeasureString Method (String, Font, SizeF)")

[MeasureString Method (String, Font, Single)](../html/M_Grasshopper_Kernel_GH_FontServer_MeasureString_2.htm "MeasureString Method (String, Font, Single)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FontServerAddLanguageSpecificTextSet("LST2379FCFF\_0?cpp=::|nu=.");MeasureString Method (String, Font, Single) |

Measure the size of a string

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static Size MeasureString(
	string text,
	Font font,
	float maxwidth
)
```

```
Public Shared Function MeasureString ( 
	text As String,
	font As Font,
	maxwidth As Single
) As Size
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

text
:   Type: [SystemAddLanguageSpecificTextSet("LST2379FCFF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The string to measure

font
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST2379FCFF\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Font](https://docs.microsoft.com/dotnet/api/system.drawing.font)  
    The font to measure with

maxwidth
:   Type: [SystemAddLanguageSpecificTextSet("LST2379FCFF\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    The maximum width (in pixels) for the layout

#### Return Value

Type: [Size](https://docs.microsoft.com/dotnet/api/system.drawing.size)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_FontServer Class](T_Grasshopper_Kernel_GH_FontServer.htm)

[MeasureString Overload](Overload_Grasshopper_Kernel_GH_FontServer_MeasureString.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)