# T_Grasshopper_Kernel_GH_DocModifiedEventArgs

﻿ GH\_DocModifiedEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocModifiedEventArgs Class](../html/T_Grasshopper_Kernel_GH_DocModifiedEventArgs.htm "GH_DocModifiedEventArgs Class")

[GH\_DocModifiedEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocModifiedEventArgs.htm "GH_DocModifiedEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocModifiedEventArgs Class |

These arguments are passed along with ModifiedChanged events on GH\_Document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST417EA358\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST417EA358\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LST417EA358\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocModifiedEventArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DocModifiedEventArgs : EventArgs
```

```
Public Class GH_DocModifiedEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocModifiedEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Document](P_Grasshopper_Kernel_GH_DocModifiedEventArgs_Document.htm) | Gets the document that raised the event. |
| Public property | [Modified](P_Grasshopper_Kernel_GH_DocModifiedEventArgs_Modified.htm) | Gets the value of the document Modified flag at the time the event was raised, it *may* have been changed in between by other event handlers. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)