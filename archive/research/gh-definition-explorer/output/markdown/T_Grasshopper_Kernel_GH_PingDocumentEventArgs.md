# T_Grasshopper_Kernel_GH_PingDocumentEventArgs

﻿ GH\_PingDocumentEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_PingDocumentEventArgs Class](../html/T_Grasshopper_Kernel_GH_PingDocumentEventArgs.htm "GH_PingDocumentEventArgs Class")

[GH\_PingDocumentEventArgs Constructor](../html/M_Grasshopper_Kernel_GH_PingDocumentEventArgs__ctor.htm "GH_PingDocumentEventArgs Constructor ")

[GH\_PingDocumentEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_PingDocumentEventArgs.htm "GH_PingDocumentEventArgs Properties")

[GH\_PingDocumentEventArgs Fields](../html/Fields_T_Grasshopper_Kernel_GH_PingDocumentEventArgs.htm "GH_PingDocumentEventArgs Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PingDocumentEventArgs Class |

Event arguments passed during PingDocument events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTAC4BDF33\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTAC4BDF33\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LSTAC4BDF33\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PingDocumentEventArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_PingDocumentEventArgs : EventArgs
```

```
Public Class GH_PingDocumentEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_PingDocumentEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_PingDocumentEventArgs](M_Grasshopper_Kernel_GH_PingDocumentEventArgs__ctor.htm) | Initializes a new instance of the GH\_PingDocumentEventArgs class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Document](P_Grasshopper_Kernel_GH_PingDocumentEventArgs_Document.htm) | If you're a GH\_Document that owns this object, you must fill out this field. This is the **only** way for objects to know which document they belong to. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_document](F_Grasshopper_Kernel_GH_PingDocumentEventArgs_m_document.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)