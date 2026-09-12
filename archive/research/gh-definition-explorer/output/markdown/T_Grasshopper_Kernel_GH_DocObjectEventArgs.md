# T_Grasshopper_Kernel_GH_DocObjectEventArgs

﻿ GH\_DocObjectEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocObjectEventArgs Class](../html/T_Grasshopper_Kernel_GH_DocObjectEventArgs.htm "GH_DocObjectEventArgs Class")

[GH\_DocObjectEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocObjectEventArgs.htm "GH_DocObjectEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocObjectEventArgs Class |

These arguments are passed along with ObjectsAdded and ObjectsRemoved events on GH\_Document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTBECF1DD1\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTBECF1DD1\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LSTBECF1DD1\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocObjectEventArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DocObjectEventArgs : EventArgs
```

```
Public Class GH_DocObjectEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocObjectEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Attributes](P_Grasshopper_Kernel_GH_DocObjectEventArgs_Attributes.htm) | Gets all the attributes that are associated with all objects in the event. |
| Public property | [Document](P_Grasshopper_Kernel_GH_DocObjectEventArgs_Document.htm) | Gets the document that raised the event. |
| Public property | [Object](P_Grasshopper_Kernel_GH_DocObjectEventArgs_Object.htm) | Gets the object to which this event pertains. |
| Public property | [ObjectCount](P_Grasshopper_Kernel_GH_DocObjectEventArgs_ObjectCount.htm) | Gets the number of objects in this event. |
| Public property | [Objects](P_Grasshopper_Kernel_GH_DocObjectEventArgs_Objects.htm) | Gets a readonly list of the objects to which this event pertains. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)