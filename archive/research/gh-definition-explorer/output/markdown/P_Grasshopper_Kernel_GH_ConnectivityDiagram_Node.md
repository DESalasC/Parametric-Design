# P_Grasshopper_Kernel_GH_ConnectivityDiagram_Node

﻿ GH\_ConnectivityDiagram.Node Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ConnectivityDiagram Class](../html/T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm "GH_ConnectivityDiagram Class")

[GH\_ConnectivityDiagram Properties](../html/Properties_T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm "GH_ConnectivityDiagram Properties")

[Node Property](../html/P_Grasshopper_Kernel_GH_ConnectivityDiagram_Node.htm "Node Property ")

[NodeCount Property](../html/P_Grasshopper_Kernel_GH_ConnectivityDiagram_NodeCount.htm "NodeCount Property ")

[Nodes Property](../html/P_Grasshopper_Kernel_GH_ConnectivityDiagram_Nodes.htm "Nodes Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ConnectivityDiagramAddLanguageSpecificTextSet("LSTAE684B83\_0?cpp=::|nu=.");Node Property |

Get the connectivity node with the specified ID.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_ConnectivityNode this[
	Guid id
] { get; }
```

```
Public ReadOnly Default Property Node ( 
	id As Guid
) As GH_ConnectivityNode
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

id
:   Type: [SystemAddLanguageSpecificTextSet("LSTAE684B83\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    ID of node to search for.

#### Property Value

Type: [GH\_ConnectivityNode](T_Grasshopper_Kernel_GH_ConnectivityNode.htm)  

[Missing <value> documentation for "P:Grasshopper.Kernel.GH\_ConnectivityDiagram.Node(System.Guid)"]

#### Return Value

Type: [GH\_ConnectivityNode](T_Grasshopper_Kernel_GH_ConnectivityNode.htm)  
The node on success or null on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ConnectivityDiagram Class](T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)