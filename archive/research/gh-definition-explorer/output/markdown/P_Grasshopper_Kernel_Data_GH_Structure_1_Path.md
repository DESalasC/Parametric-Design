# P_Grasshopper_Kernel_Data_GH_Structure_1_Path

﻿ GH\_Structure(T).Path Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Structure(T) Class](../html/T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Class")

[GH\_Structure(T) Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Properties")

[Branch Property](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_Branch.htm "Branch Property ")

[Branches Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_Branches.htm "Branches Property ")

[DataCount Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_DataCount.htm "DataCount Property ")

[DataItem Property](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_DataItem.htm "DataItem Property ")

[DataList Property](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_DataList.htm "DataList Property ")

[FirstItem Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_FirstItem.htm "FirstItem Property ")

[IsEmpty Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_IsEmpty.htm "IsEmpty Property ")

[LastItem Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_LastItem.htm "LastItem Property ")

[NonNulls Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_NonNulls.htm "NonNulls Property ")

[Path Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_Path.htm "Path Property ")

[PathCount Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_PathCount.htm "PathCount Property ")

[Paths Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_Paths.htm "Paths Property ")

[StructureProxy Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_StructureProxy.htm "StructureProxy Property ")

[TopologyDescription Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_TopologyDescription.htm "TopologyDescription Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StructureAddLanguageSpecificTextSet("LSTECB4EF1E\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTECB4EF1E\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTECB4EF1E\_2?cpp=::|nu=.");Path Property |

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
public GH_Path this[
	int index
] { get; }
```

```
Public ReadOnly Property Path ( 
	index As Integer
) As GH_Path
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

index
:   Type: [SystemAddLanguageSpecificTextSet("LSTECB4EF1E\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of path to retrieve.

#### Property Value

Type: [GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  

[Missing <value> documentation for "P:Grasshopper.Kernel.Data.GH\_Structure`1.Path(System.Int32)"]

#### Implements

[IGH\_StructureAddLanguageSpecificTextSet("LSTECB4EF1E\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");PathAddLanguageSpecificTextSet("LSTECB4EF1E\_5?cs=[|vb=(|cpp=[|nu=(|fs= ");Int32AddLanguageSpecificTextSet("LSTECB4EF1E\_6?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_IGH_Structure_Path.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [IndexOutOfRangeException](https://docs.microsoft.com/dotnet/api/system.indexoutofrangeexception) | Thrown if the index does not represent a valid path. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_StructureAddLanguageSpecificTextSet("LSTECB4EF1E\_7?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTECB4EF1E\_8?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)