# T_Grasshopper_Kernel_GH_FontServer

﻿ GH\_FontServer Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_FontServer Class](../html/T_Grasshopper_Kernel_GH_FontServer.htm "GH_FontServer Class")

[GH\_FontServer Properties](../html/Properties_T_Grasshopper_Kernel_GH_FontServer.htm "GH_FontServer Properties")

[GH\_FontServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_FontServer.htm "GH_FontServer Methods")

[GH\_FontServer Events](../html/Events_T_Grasshopper_Kernel_GH_FontServer.htm "GH_FontServer Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FontServer Class |

Maintains a collection of standard fonts and mays to measure them.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST19AC51EA\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST19AC51EA\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FontServer

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_FontServer
```

```
Public NotInheritable Class GH_FontServer
```

AddLanguageTabSet("ID1EBCA");

The GH\_FontServer type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public propertyStatic member | [Console](P_Grasshopper_Kernel_GH_FontServer_Console.htm) | FontFamily.GenericMonospace, 10pt, regular |
| Public propertyStatic member | [ConsoleAdjusted](P_Grasshopper_Kernel_GH_FontServer_ConsoleAdjusted.htm) | FontFamily.GenericMonospace, 10pt, regular, adjusted to counter UI scaling. |
| Public propertyStatic member | [ConsoleSmall](P_Grasshopper_Kernel_GH_FontServer_ConsoleSmall.htm) | FontFamily.GenericMonospace, 8pt, regular |
| Public propertyStatic member | [ConsoleSmallAdjusted](P_Grasshopper_Kernel_GH_FontServer_ConsoleSmallAdjusted.htm) | FontFamily.GenericMonospace, 8pt, regular, adjusted to counter UI scaling. |
| Public propertyStatic member | [FamilyConsole](P_Grasshopper_Kernel_GH_FontServer_FamilyConsole.htm) | Gets or sets the FontFamily used for monospaced fonts in Grasshopper. |
| Public propertyStatic member | [FamilyScript](P_Grasshopper_Kernel_GH_FontServer_FamilyScript.htm) | Gets or sets the FontFamily used for scripted fonts in Grasshopper. |
| Public propertyStatic member | [FamilyStandard](P_Grasshopper_Kernel_GH_FontServer_FamilyStandard.htm) | Gets or sets the FontFamily used for standard fonts in Grasshopper. |
| Public propertyStatic member | [Large](P_Grasshopper_Kernel_GH_FontServer_Large.htm) | SystemFonts.CaptionFont, 10pt, bold |
| Public propertyStatic member | [LargeAdjusted](P_Grasshopper_Kernel_GH_FontServer_LargeAdjusted.htm) | SystemFonts.CaptionFont, 10pt, bold, adjusted for logical pixel size. |
| Public propertyStatic member | [Script](P_Grasshopper_Kernel_GH_FontServer_Script.htm) | FontFamily.GenericSansSerif, 10pt, italic |
| Public propertyStatic member | [ScriptSmall](P_Grasshopper_Kernel_GH_FontServer_ScriptSmall.htm) | FontFamily.GenericSansSerif, 8pt, italic |
| Public propertyStatic member | [Small](P_Grasshopper_Kernel_GH_FontServer_Small.htm) | SystemFonts.CaptionFont, 6pt, regular |
| Public propertyStatic member | [Standard](P_Grasshopper_Kernel_GH_FontServer_Standard.htm) | SystemFonts.CaptionFont, 8pt, regular |
| Public propertyStatic member | [StandardAdjusted](P_Grasshopper_Kernel_GH_FontServer_StandardAdjusted.htm) | SystemFonts.CaptionFont, 8pt, regular, adjusted for logical pixel size. |
| Public propertyStatic member | [StandardBold](P_Grasshopper_Kernel_GH_FontServer_StandardBold.htm) | SystemFonts.CaptionFont, 8pt, bold |
| Public propertyStatic member | [StandardItalic](P_Grasshopper_Kernel_GH_FontServer_StandardItalic.htm) | SystemFonts.CaptionFont, 8pt, italic |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [FontToString](M_Grasshopper_Kernel_GH_FontServer_FontToString.htm) | Convert a font to a string. |
| Public methodStatic member | [MeasureString(String, Font)](M_Grasshopper_Kernel_GH_FontServer_MeasureString.htm) | Measure the size of a string |
| Public methodStatic member | [MeasureString(String, Font, SizeF)](M_Grasshopper_Kernel_GH_FontServer_MeasureString_1.htm) | Measure the size of a string |
| Public methodStatic member | [MeasureString(String, Font, Single)](M_Grasshopper_Kernel_GH_FontServer_MeasureString_2.htm) | Measure the size of a string |
| Public methodStatic member | [NewFont(Font, FontStyle)](M_Grasshopper_Kernel_GH_FontServer_NewFont.htm) | Safe font constructor. |
| Public methodStatic member | [NewFont(Font, Single)](M_Grasshopper_Kernel_GH_FontServer_NewFont_1.htm) | Safe font constructor. |
| Public methodStatic member | [NewFont(FontFamily, Single)](M_Grasshopper_Kernel_GH_FontServer_NewFont_3.htm) | Safe font constructor. |
| Public methodStatic member | [NewFont(Font, Single, FontStyle)](M_Grasshopper_Kernel_GH_FontServer_NewFont_2.htm) | Safe font constructor. |
| Public methodStatic member | [NewFont(FontFamily, Single, FontStyle)](M_Grasshopper_Kernel_GH_FontServer_NewFont_4.htm) | Safe font constructor. |
| Public methodStatic member | [NewFont(String, Single, FontStyle)](M_Grasshopper_Kernel_GH_FontServer_NewFont_5.htm) | High level function for Font creation. We've ran into loads of trouble in the past with missing Fonts. *Never* create a font directly via GDI+, *always* use this method. |
| Public methodStatic member | [StringToFont](M_Grasshopper_Kernel_GH_FontServer_StringToFont.htm) | Convert a font description string back into a font. |
| Public methodStatic member | [StringWidth(IEnumerableAddLanguageSpecificTextSet("LST19AC51EA\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LST19AC51EA\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Font)](M_Grasshopper_Kernel_GH_FontServer_StringWidth.htm) | Measure the maximum width of a collection of strings |
| Public methodStatic member | [StringWidth(String, Font)](M_Grasshopper_Kernel_GH_FontServer_StringWidth_1.htm) | Measure the width of a string in pixels |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public eventStatic member | [ConsoleFamilyChanged](E_Grasshopper_Kernel_GH_FontServer_ConsoleFamilyChanged.htm) | Raised whenever the MonospacedFamily is changed. |
| Public eventStatic member | [ScriptFamilyChanged](E_Grasshopper_Kernel_GH_FontServer_ScriptFamilyChanged.htm) | Raised whenever the ScriptFamily is changed. |
| Public eventStatic member | [StandardFamilyChanged](E_Grasshopper_Kernel_GH_FontServer_StandardFamilyChanged.htm) | Raised whenever the StandardFamily is changed. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)