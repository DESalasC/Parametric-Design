# T_Grasshopper_Kernel_GH_DocContextEventArgs

﻿ GH\_DocContextEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocContextEventArgs Class](../html/T_Grasshopper_Kernel_GH_DocContextEventArgs.htm "GH_DocContextEventArgs Class")

[GH\_DocContextEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocContextEventArgs.htm "GH_DocContextEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocContextEventArgs Class |

These arguments are passed along with SettingsChanged events on GH\_Document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST5CCF99EF\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST5CCF99EF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LST5CCF99EF\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocContextEventArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DocContextEventArgs : EventArgs
```

```
Public Class GH_DocContextEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocContextEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Context](P_Grasshopper_Kernel_GH_DocContextEventArgs_Context.htm) | Gets the value of the document context flag at the time the event was raised, it *may* have been changed in between by other event handlers. |
| Public property | [Document](P_Grasshopper_Kernel_GH_DocContextEventArgs_Document.htm) | Gets the document that raised the event. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)