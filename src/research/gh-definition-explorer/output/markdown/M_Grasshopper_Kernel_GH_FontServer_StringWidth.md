# M_Grasshopper_Kernel_GH_FontServer_StringWidth

﻿ GH\_FontServer.StringWidth Method (IEnumerable(String), Font)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_FontServer Class](../html/T_Grasshopper_Kernel_GH_FontServer.htm "GH_FontServer Class")

[GH\_FontServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_FontServer.htm "GH_FontServer Methods")

[StringWidth Method](../html/Overload_Grasshopper_Kernel_GH_FontServer_StringWidth.htm "StringWidth Method ")

[StringWidth Method (IEnumerable(String), Font)](../html/M_Grasshopper_Kernel_GH_FontServer_StringWidth.htm "StringWidth Method (IEnumerable(String), Font)")

[StringWidth Method (String, Font)](../html/M_Grasshopper_Kernel_GH_FontServer_StringWidth_1.htm "StringWidth Method (String, Font)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FontServerAddLanguageSpecificTextSet("LST5665A303\_0?cpp=::|nu=.");StringWidth Method (IEnumerableAddLanguageSpecificTextSet("LST5665A303\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LST5665A303\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Font) |

Measure the maximum width of a collection of strings

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static int StringWidth(
	IEnumerable<string> text,
	Font font
)
```

```
Public Shared Function StringWidth ( 
	text As IEnumerable(Of String),
	font As Font
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

text
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST5665A303\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LST5665A303\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LST5665A303\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    The strings to measure

font
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST5665A303\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Font](https://docs.microsoft.com/dotnet/api/system.drawing.font)  
    The font to measure with

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_FontServer Class](T_Grasshopper_Kernel_GH_FontServer.htm)

[StringWidth Overload](Overload_Grasshopper_Kernel_GH_FontServer_StringWidth.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)