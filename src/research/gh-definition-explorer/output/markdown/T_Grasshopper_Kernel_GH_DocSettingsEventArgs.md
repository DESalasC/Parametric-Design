# T_Grasshopper_Kernel_GH_DocSettingsEventArgs

﻿ GH\_DocSettingsEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocSettingsEventArgs Class](../html/T_Grasshopper_Kernel_GH_DocSettingsEventArgs.htm "GH_DocSettingsEventArgs Class")

[GH\_DocSettingsEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocSettingsEventArgs.htm "GH_DocSettingsEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocSettingsEventArgs Class |

These arguments are passed along with SettingsChanged events on GH\_Document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTDBD410F1\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTDBD410F1\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LSTDBD410F1\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocSettingsEventArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DocSettingsEventArgs : EventArgs
```

```
Public Class GH_DocSettingsEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocSettingsEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Document](P_Grasshopper_Kernel_GH_DocSettingsEventArgs_Document.htm) | Gets the document that raised the event. |
| Public property | [Kind](P_Grasshopper_Kernel_GH_DocSettingsEventArgs_Kind.htm) | Gets the type of setting that was changed. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)