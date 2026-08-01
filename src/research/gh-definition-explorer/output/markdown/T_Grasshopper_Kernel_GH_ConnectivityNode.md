# T_Grasshopper_Kernel_GH_ConnectivityNode

﻿ GH\_ConnectivityNode Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ConnectivityNode Class](../html/T_Grasshopper_Kernel_GH_ConnectivityNode.htm "GH_ConnectivityNode Class")

[GH\_ConnectivityNode Constructor](../html/M_Grasshopper_Kernel_GH_ConnectivityNode__ctor.htm "GH_ConnectivityNode Constructor ")

[GH\_ConnectivityNode Properties](../html/Properties_T_Grasshopper_Kernel_GH_ConnectivityNode.htm "GH_ConnectivityNode Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ConnectivityNode Class |

Represents a single node in a Grasshopper connectivity diagram.
A single node represents a single IGH\_Param instance.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST816E8275\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST816E8275\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ConnectivityNode

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ConnectivityNode
```

```
Public Class GH_ConnectivityNode
```

AddLanguageTabSet("ID1EBCA");

The GH\_ConnectivityNode type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ConnectivityNode](M_Grasshopper_Kernel_GH_ConnectivityNode__ctor.htm) | Initializes a new instance of the GH\_ConnectivityNode class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [NodeID](P_Grasshopper_Kernel_GH_ConnectivityNode_NodeID.htm) | Gets the InstanceID of the Parameter that this node represents. |
| Public property | [NodeIn](P_Grasshopper_Kernel_GH_ConnectivityNode_NodeIn.htm) | Gets the list of IDs that are connected to the input of this node. |
| Public property | [NodeOut](P_Grasshopper_Kernel_GH_ConnectivityNode_NodeOut.htm) | Gets the list of IDs that are connected to the input of this node. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)