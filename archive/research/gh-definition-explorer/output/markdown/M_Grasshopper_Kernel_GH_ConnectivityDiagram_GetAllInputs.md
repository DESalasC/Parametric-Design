# M_Grasshopper_Kernel_GH_ConnectivityDiagram_GetAllInputs

﻿ GH\_ConnectivityDiagram.GetAllInputs Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ConnectivityDiagram Class](../html/T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm "GH_ConnectivityDiagram Class")

[GH\_ConnectivityDiagram Methods](../html/Methods_T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm "GH_ConnectivityDiagram Methods")

[ContainsID Method](../html/M_Grasshopper_Kernel_GH_ConnectivityDiagram_ContainsID.htm "ContainsID Method ")

[GetAllInputs Method](../html/M_Grasshopper_Kernel_GH_ConnectivityDiagram_GetAllInputs.htm "GetAllInputs Method ")

[GetAllOutputs Method](../html/M_Grasshopper_Kernel_GH_ConnectivityDiagram_GetAllOutputs.htm "GetAllOutputs Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ConnectivityDiagramAddLanguageSpecificTextSet("LST93337E5\_0?cpp=::|nu=.");GetAllInputs Method |

Get all the Nodes that are part of the specified node input.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public List<Guid> GetAllInputs(
	Guid id
)
```

```
Public Function GetAllInputs ( 
	id As Guid
) As List(Of Guid)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

id
:   Type: [SystemAddLanguageSpecificTextSet("LST93337E5\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    ID of node to query.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST93337E5\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Guid](https://docs.microsoft.com/dotnet/api/system.guid)AddLanguageSpecificTextSet("LST93337E5\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list of input nodes.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ConnectivityDiagram Class](T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)