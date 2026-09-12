# T_Grasshopper_Kernel_GH_DocEnabledEventArgs

﻿ GH\_DocEnabledEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocEnabledEventArgs Class](../html/T_Grasshopper_Kernel_GH_DocEnabledEventArgs.htm "GH_DocEnabledEventArgs Class")

[GH\_DocEnabledEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocEnabledEventArgs.htm "GH_DocEnabledEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocEnabledEventArgs Class |

These arguments are passed along with SettingsChanged events on GH\_Document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST5FD41CC2\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST5FD41CC2\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LST5FD41CC2\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocEnabledEventArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DocEnabledEventArgs : EventArgs
```

```
Public Class GH_DocEnabledEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocEnabledEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Document](P_Grasshopper_Kernel_GH_DocEnabledEventArgs_Document.htm) | Gets the document that raised the event. |
| Public property | [Enabled](P_Grasshopper_Kernel_GH_DocEnabledEventArgs_Enabled.htm) | Gets the value of the document Enabled flag at the time the event was raised, it *may* have been changed in between by other event handlers. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)