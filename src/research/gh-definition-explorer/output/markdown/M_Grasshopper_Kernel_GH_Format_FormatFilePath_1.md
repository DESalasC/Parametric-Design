# M_Grasshopper_Kernel_GH_Format_FormatFilePath_1

﻿ GH\_Format.FormatFilePath Method (String, Int32, Font)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Format Class](../html/T_Grasshopper_Kernel_GH_Format.htm "GH_Format Class")

[GH\_Format Methods](../html/Methods_T_Grasshopper_Kernel_GH_Format.htm "GH_Format Methods")

[FormatFilePath Method](../html/Overload_Grasshopper_Kernel_GH_Format_FormatFilePath.htm "FormatFilePath Method ")

[FormatFilePath Method (String, Int32)](../html/M_Grasshopper_Kernel_GH_Format_FormatFilePath.htm "FormatFilePath Method (String, Int32)")

[FormatFilePath Method (String, Int32, Font)](../html/M_Grasshopper_Kernel_GH_Format_FormatFilePath_1.htm "FormatFilePath Method (String, Int32, Font)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FormatAddLanguageSpecificTextSet("LST72FB7FC2\_0?cpp=::|nu=.");FormatFilePath Method (String, Int32, Font) |

Format a filepath so that it doesn't exceed width.
If the filepath filename is already longer than maxLength it will be returned intact.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static string FormatFilePath(
	string path,
	int maxWidth,
	Font font
)
```

```
Public Shared Function FormatFilePath ( 
	path As String,
	maxWidth As Integer,
	font As Font
) As String
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [SystemAddLanguageSpecificTextSet("LST72FB7FC2\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Path to format.

maxWidth
:   Type: [SystemAddLanguageSpecificTextSet("LST72FB7FC2\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Maximum allowed width (in pixels)

font
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST72FB7FC2\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Font](https://docs.microsoft.com/dotnet/api/system.drawing.font)  
    Font to use for measuring.

#### Return Value

Type: [String](https://docs.microsoft.com/dotnet/api/system.string)  
The formatted path.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Format Class](T_Grasshopper_Kernel_GH_Format.htm)

[FormatFilePath Overload](Overload_Grasshopper_Kernel_GH_Format_FormatFilePath.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)