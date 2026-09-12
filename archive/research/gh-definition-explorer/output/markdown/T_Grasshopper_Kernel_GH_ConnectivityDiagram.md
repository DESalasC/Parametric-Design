# T_Grasshopper_Kernel_GH_ConnectivityDiagram

﻿ GH\_ConnectivityDiagram Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ConnectivityDiagram Class](../html/T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm "GH_ConnectivityDiagram Class")

[GH\_ConnectivityDiagram Constructor](../html/Overload_Grasshopper_Kernel_GH_ConnectivityDiagram__ctor.htm "GH_ConnectivityDiagram Constructor ")

[GH\_ConnectivityDiagram Properties](../html/Properties_T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm "GH_ConnectivityDiagram Properties")

[GH\_ConnectivityDiagram Methods](../html/Methods_T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm "GH_ConnectivityDiagram Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ConnectivityDiagram Class |

Represents a complete connectivity diagram (topology) of a GH\_Document.
A connectivity diagram is basically an undirected network of all the wires in a document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTE45F64E8\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTE45F64E8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ConnectivityDiagram

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ConnectivityDiagram
```

```
Public Class GH_ConnectivityDiagram
```

AddLanguageTabSet("ID1EBCA");

The GH\_ConnectivityDiagram type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ConnectivityDiagram(GH\_ConnectivityDiagram)](M_Grasshopper_Kernel_GH_ConnectivityDiagram__ctor.htm) | Create a duplicate of another Connectivity Diagram. |
| Public method | [GH\_ConnectivityDiagram(GH\_Document)](M_Grasshopper_Kernel_GH_ConnectivityDiagram__ctor_1.htm) | Create a new Connectivity Diagram from a GH\_Document. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Node](P_Grasshopper_Kernel_GH_ConnectivityDiagram_Node.htm) | Get the connectivity node with the specified ID. |
| Public property | [NodeCount](P_Grasshopper_Kernel_GH_ConnectivityDiagram_NodeCount.htm) | Gets the number of connectivity nodes in this diagram. |
| Public property | [Nodes](P_Grasshopper_Kernel_GH_ConnectivityDiagram_Nodes.htm) | Gets a proxy for all the Nodes in this diagram. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [ContainsID](M_Grasshopper_Kernel_GH_ConnectivityDiagram_ContainsID.htm) | Test the diagram for a given Node ID. |
| Public method | [GetAllInputs](M_Grasshopper_Kernel_GH_ConnectivityDiagram_GetAllInputs.htm) | Get all the Nodes that are part of the specified node input. |
| Public method | [GetAllOutputs](M_Grasshopper_Kernel_GH_ConnectivityDiagram_GetAllOutputs.htm) | Get all the Nodes that are part of the specified node output. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)