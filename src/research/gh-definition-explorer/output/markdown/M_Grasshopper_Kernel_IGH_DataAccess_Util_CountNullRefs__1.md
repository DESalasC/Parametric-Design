# M_Grasshopper_Kernel_IGH_DataAccess_Util_CountNullRefs__1

﻿ IGH\_DataAccess.Util\_CountNullRefs(T) Method 

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
| IGH\_DataAccessAddLanguageSpecificTextSet("LST39F987BC\_0?cpp=::|nu=.");Util\_CountNullRefsAddLanguageSpecificTextSet("LST39F987BC\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST39F987BC\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Method |

Count all null references in L

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
int Util_CountNullRefs<T>(
	List<T> L
)
```

```
Function Util_CountNullRefs(Of T) ( 
	L As List(Of T)
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

L
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST39F987BC\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST39F987BC\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST39F987BC\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    List to parse

#### Type Parameters

T
:   Type of list

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
Number of nulls in L

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DataAccess Interface](T_Grasshopper_Kernel_IGH_DataAccess.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)