# M_Grasshopper_Kernel_GH_FontServer_NewFont_5

﻿ GH\_FontServer.NewFont Method (String, Single, FontStyle)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_FontServer Class](../html/T_Grasshopper_Kernel_GH_FontServer.htm "GH_FontServer Class")

[GH\_FontServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_FontServer.htm "GH_FontServer Methods")

[NewFont Method](../html/Overload_Grasshopper_Kernel_GH_FontServer_NewFont.htm "NewFont Method ")

[NewFont Method (Font, FontStyle)](../html/M_Grasshopper_Kernel_GH_FontServer_NewFont.htm "NewFont Method (Font, FontStyle)")

[NewFont Method (Font, Single)](../html/M_Grasshopper_Kernel_GH_FontServer_NewFont_1.htm "NewFont Method (Font, Single)")

[NewFont Method (FontFamily, Single)](../html/M_Grasshopper_Kernel_GH_FontServer_NewFont_3.htm "NewFont Method (FontFamily, Single)")

[NewFont Method (Font, Single, FontStyle)](../html/M_Grasshopper_Kernel_GH_FontServer_NewFont_2.htm "NewFont Method (Font, Single, FontStyle)")

[NewFont Method (FontFamily, Single, FontStyle)](../html/M_Grasshopper_Kernel_GH_FontServer_NewFont_4.htm "NewFont Method (FontFamily, Single, FontStyle)")

[NewFont Method (String, Single, FontStyle)](../html/M_Grasshopper_Kernel_GH_FontServer_NewFont_5.htm "NewFont Method (String, Single, FontStyle)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FontServerAddLanguageSpecificTextSet("LST8E928AFE\_0?cpp=::|nu=.");NewFont Method (String, Single, FontStyle) |

High level function for Font creation. We've ran into loads of trouble in the past with missing Fonts.
*Never* create a font directly via GDI+, *always* use this method.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static Font NewFont(
	string family,
	float size,
	FontStyle style
)
```

```
Public Shared Function NewFont ( 
	family As String,
	size As Single,
	style As FontStyle
) As Font
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

family
:   Type: [SystemAddLanguageSpecificTextSet("LST8E928AFE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Font Family Name. If a font is found with the exact name, it will be loaded.

size
:   Type: [SystemAddLanguageSpecificTextSet("LST8E928AFE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Size of font.

style
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST8E928AFE\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");FontStyle](https://docs.microsoft.com/dotnet/api/system.drawing.fontstyle)  
    Font style, if the requested family does not support the requested style, the style flags will be ignored.

#### Return Value

Type: [Font](https://docs.microsoft.com/dotnet/api/system.drawing.font)  
A font that might or might not be what you asked for.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_FontServer Class](T_Grasshopper_Kernel_GH_FontServer.htm)

[NewFont Overload](Overload_Grasshopper_Kernel_GH_FontServer_NewFont.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)