# P_Grasshopper_Kernel_Data_IGH_Structure_Path

﻿ IGH\_Structure.Path Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[IGH\_Structure Interface](../html/T_Grasshopper_Kernel_Data_IGH_Structure.htm "IGH_Structure Interface")

[IGH\_Structure Properties](../html/Properties_T_Grasshopper_Kernel_Data_IGH_Structure.htm "IGH_Structure Properties")

[Branch Property](../html/Overload_Grasshopper_Kernel_Data_IGH_Structure_Branch.htm "Branch Property ")

[DataCount Property](../html/P_Grasshopper_Kernel_Data_IGH_Structure_DataCount.htm "DataCount Property ")

[IsEmpty Property](../html/P_Grasshopper_Kernel_Data_IGH_Structure_IsEmpty.htm "IsEmpty Property ")

[Path Property](../html/P_Grasshopper_Kernel_Data_IGH_Structure_Path.htm "Path Property ")

[PathCount Property](../html/P_Grasshopper_Kernel_Data_IGH_Structure_PathCount.htm "PathCount Property ")

[Paths Property](../html/P_Grasshopper_Kernel_Data_IGH_Structure_Paths.htm "Paths Property ")

[StructureProxy Property](../html/P_Grasshopper_Kernel_Data_IGH_Structure_StructureProxy.htm "StructureProxy Property ")

[TopologyDescription Property](../html/P_Grasshopper_Kernel_Data_IGH_Structure_TopologyDescription.htm "TopologyDescription Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_StructureAddLanguageSpecificTextSet("LSTC2253B45\_0?cpp=::|nu=.");Path Property |

Gets the data path at the specified index.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
GH_Path this[
	int index
] { get; }
```

```
ReadOnly Property Path ( 
	index As Integer
) As GH_Path
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

index
:   Type: [SystemAddLanguageSpecificTextSet("LSTC2253B45\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of path to retrieve.

#### Property Value

Type: [GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  

[Missing <value> documentation for "P:Grasshopper.Kernel.Data.IGH\_Structure.Path(System.Int32)"]

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [IndexOutOfRangeException](https://docs.microsoft.com/dotnet/api/system.indexoutofrangeexception) | Thrown if the index does not represent a valid path. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Structure Interface](T_Grasshopper_Kernel_Data_IGH_Structure.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)