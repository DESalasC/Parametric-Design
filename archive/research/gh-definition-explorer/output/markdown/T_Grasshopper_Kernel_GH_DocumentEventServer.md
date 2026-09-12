# T_Grasshopper_Kernel_GH_DocumentEventServer

﻿ GH\_DocumentEventServer Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentEventServer Class](../html/T_Grasshopper_Kernel_GH_DocumentEventServer.htm "GH_DocumentEventServer Class")

[GH\_DocumentEventServer Constructor](../html/M_Grasshopper_Kernel_GH_DocumentEventServer__ctor.htm "GH_DocumentEventServer Constructor ")

[GH\_DocumentEventServer Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocumentEventServer.htm "GH_DocumentEventServer Properties")

[GH\_DocumentEventServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentEventServer.htm "GH_DocumentEventServer Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentEventServer Class |

RhinoCommon only event server.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST7656274D\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST7656274D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocumentEventServer

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DocumentEventServer : IGH_DebugDescription
```

```
Public Class GH_DocumentEventServer
	Implements IGH_DebugDescription
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocumentEventServer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DocumentEventServer](M_Grasshopper_Kernel_GH_DocumentEventServer__ctor.htm) | Create and register a new event server. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Enabled](P_Grasshopper_Kernel_GH_DocumentEventServer_Enabled.htm) | Gets or sets the enabled state flag for this event watcher. |
| Public property | [GuidTableRefCount](P_Grasshopper_Kernel_GH_DocumentEventServer_GuidTableRefCount.htm) | Gets the number of stored ids in the Guid Table. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendToDebugLog](M_Grasshopper_Kernel_GH_DocumentEventServer_AppendToDebugLog.htm) |  |
| Public method | [ClearGuidTable](M_Grasshopper_Kernel_GH_DocumentEventServer_ClearGuidTable.htm) | Clear the entire ID table. |
| Public method | [CreateGuidTable](M_Grasshopper_Kernel_GH_DocumentEventServer_CreateGuidTable.htm) | Create the entire ID table from scratch. |
| Public method | [EnsureGuidTable](M_Grasshopper_Kernel_GH_DocumentEventServer_EnsureGuidTable.htm) | Create the entire ID table if it doesn't exist yet. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)