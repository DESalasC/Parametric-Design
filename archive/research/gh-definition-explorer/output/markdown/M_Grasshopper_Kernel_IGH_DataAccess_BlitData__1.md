# M_Grasshopper_Kernel_IGH_DataAccess_BlitData__1

﻿ IGH\_DataAccess.BlitData(Q) Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DataAccess Interface](../html/T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Interface")

[IGH\_DataAccess Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Methods")

[AbortComponentSolution Method](../html/M_Grasshopper_Kernel_IGH_DataAccess_AbortComponentSolution.htm "AbortComponentSolution Method ")

[BlitData(Q) Method](../html/M_Grasshopper_Kernel_IGH_DataAccess_BlitData__1.htm "BlitData(Q) Method ")

[DisableGapLogic Method](../html/Overload_Grasshopper_Kernel_IGH_DataAccess_DisableGapLogic.htm "DisableGapLogic Method ")

[GetData Method](../html/Overload_Grasshopper_Kernel_IGH_DataAccess_GetData.htm "GetData Method ")

[GetDataList Method](../html/Overload_Grasshopper_Kernel_IGH_DataAccess_GetDataList.htm "GetDataList Method ")

[GetDataTree Method](../html/Overload_Grasshopper_Kernel_IGH_DataAccess_GetDataTree.htm "GetDataTree Method ")

[IncrementIteration Method](../html/M_Grasshopper_Kernel_IGH_DataAccess_IncrementIteration.htm "IncrementIteration Method ")

[ParameterTargetIndex Method](../html/M_Grasshopper_Kernel_IGH_DataAccess_ParameterTargetIndex.htm "ParameterTargetIndex Method ")

[ParameterTargetPath Method](../html/M_Grasshopper_Kernel_IGH_DataAccess_ParameterTargetPath.htm "ParameterTargetPath Method ")

[SetData Method](../html/Overload_Grasshopper_Kernel_IGH_DataAccess_SetData.htm "SetData Method ")

[SetDataList Method](../html/Overload_Grasshopper_Kernel_IGH_DataAccess_SetDataList.htm "SetDataList Method ")

[SetDataTree Method](../html/Overload_Grasshopper_Kernel_IGH_DataAccess_SetDataTree.htm "SetDataTree Method ")

[Util\_CountNonNullRefs(T) Method](../html/M_Grasshopper_Kernel_IGH_DataAccess_Util_CountNonNullRefs__1.htm "Util_CountNonNullRefs(T) Method ")

[Util\_CountNullRefs(T) Method](../html/M_Grasshopper_Kernel_IGH_DataAccess_Util_CountNullRefs__1.htm "Util_CountNullRefs(T) Method ")

[Util\_EnsureNonNullCount(T) Method](../html/M_Grasshopper_Kernel_IGH_DataAccess_Util_EnsureNonNullCount__1.htm "Util_EnsureNonNullCount(T) Method ")

[Util\_FirstNonNullItem(T) Method](../html/M_Grasshopper_Kernel_IGH_DataAccess_Util_FirstNonNullItem__1.htm "Util_FirstNonNullItem(T) Method ")

[Util\_RemoveNullRefs(T) Method](../html/M_Grasshopper_Kernel_IGH_DataAccess_Util_RemoveNullRefs__1.htm "Util_RemoveNullRefs(T) Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DataAccessAddLanguageSpecificTextSet("LST4F41D26\_0?cpp=::|nu=.");BlitDataAddLanguageSpecificTextSet("LST4F41D26\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST4F41D26\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Method |

Creates a direct copy of an existing data structure.
The existing generic instance must of the exact same type as the target parameter.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool BlitData<Q>(
	int paramIndex,
	GH_Structure<Q> tree,
	bool overwrite
)
where Q : IGH_Goo
```

```
Function BlitData(Of Q As IGH_Goo) ( 
	paramIndex As Integer,
	tree As GH_Structure(Of Q),
	overwrite As Boolean
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

paramIndex
:   Type: [SystemAddLanguageSpecificTextSet("LST4F41D26\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of output parameter.

tree
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST4F41D26\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Structure](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)AddLanguageSpecificTextSet("LST4F41D26\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST4F41D26\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Parameter whose data to blit

overwrite
:   Type: [SystemAddLanguageSpecificTextSet("LST4F41D26\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, any existing data will be removed.

#### Type Parameters

Q
:   Type specified for GH\_Structure(Of Q) comparison.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DataAccess Interface](T_Grasshopper_Kernel_IGH_DataAccess.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)