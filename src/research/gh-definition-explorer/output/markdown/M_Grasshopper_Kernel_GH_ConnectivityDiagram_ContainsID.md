# M_Grasshopper_Kernel_GH_ConnectivityDiagram_ContainsID

﻿ GH\_ConnectivityDiagram.ContainsID Method 

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
| GH\_ConnectivityDiagramAddLanguageSpecificTextSet("LSTECC49D36\_0?cpp=::|nu=.");ContainsID Method |

Test the diagram for a given Node ID.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool ContainsID(
	Guid id
)
```

```
Public Function ContainsID ( 
	id As Guid
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

id
:   Type: [SystemAddLanguageSpecificTextSet("LSTECC49D36\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    ID to search for.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the ID is part of this diagram, false if otherwise.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ConnectivityDiagram Class](T_Grasshopper_Kernel_GH_ConnectivityDiagram.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)