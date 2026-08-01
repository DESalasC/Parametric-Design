# M_Grasshopper_Kernel_GH_FontServer_StringToFont

﻿ GH\_FontServer.StringToFont Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_FontServer Class](../html/T_Grasshopper_Kernel_GH_FontServer.htm "GH_FontServer Class")

[GH\_FontServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_FontServer.htm "GH_FontServer Methods")

[FontToString Method](../html/M_Grasshopper_Kernel_GH_FontServer_FontToString.htm "FontToString Method ")

[MeasureString Method](../html/Overload_Grasshopper_Kernel_GH_FontServer_MeasureString.htm "MeasureString Method ")

[NewFont Method](../html/Overload_Grasshopper_Kernel_GH_FontServer_NewFont.htm "NewFont Method ")

[StringToFont Method](../html/M_Grasshopper_Kernel_GH_FontServer_StringToFont.htm "StringToFont Method ")

[StringWidth Method](../html/Overload_Grasshopper_Kernel_GH_FontServer_StringWidth.htm "StringWidth Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FontServerAddLanguageSpecificTextSet("LSTDCD6AE38\_0?cpp=::|nu=.");StringToFont Method |

Convert a font description string back into a font.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static Font StringToFont(
	string text
)
```

```
Public Shared Function StringToFont ( 
	text As String
) As Font
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

text
:   Type: [SystemAddLanguageSpecificTextSet("LSTDCD6AE38\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Text to parse.

#### Return Value

Type: [Font](https://docs.microsoft.com/dotnet/api/system.drawing.font)  
Font represented by the text, or null if no font could be created.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_FontServer Class](T_Grasshopper_Kernel_GH_FontServer.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)