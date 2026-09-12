# T_Grasshopper_Kernel_IGH_DataAccess

﻿ IGH\_DataAccess Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DataAccess Interface](../html/T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Interface")

[IGH\_DataAccess Properties](../html/Properties_T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Properties")

[IGH\_DataAccess Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DataAccess Interface |

Provides access to component parameters, in order to retrieve and assign data
during solutions.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_DataAccess
```

```
Public Interface IGH_DataAccess
```

AddLanguageTabSet("ID0EBCA");

The IGH\_DataAccess type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Iteration](P_Grasshopper_Kernel_IGH_DataAccess_Iteration.htm) | Gets the current iteration count. The first time the SolveInstance() function is called on a component during a solution the Iteration counter will be zero. It will be incremented by one for every subsequent call. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AbortComponentSolution](M_Grasshopper_Kernel_IGH_DataAccess_AbortComponentSolution.htm) | Call this method if you wish to stop solving this component. |
| Public method | [BlitDataAddLanguageSpecificTextSet("LST334ACA80\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST334ACA80\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_IGH_DataAccess_BlitData__1.htm) | Creates a direct copy of an existing data structure. The existing generic instance must of the exact same type as the target parameter. |
| Public method | [DisableGapLogicAddLanguageSpecificTextSet("LST334ACA80\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_IGH_DataAccess_DisableGapLogic.htm) | Call this function if you want to disable the gap null logic for the current iteration. |
| Public method | [DisableGapLogic(Int32)](M_Grasshopper_Kernel_IGH_DataAccess_DisableGapLogic_1.htm) | Call this function if you want to disable the gap null logic for a specific output parameter. |
| Public method | [GetDataAddLanguageSpecificTextSet("LST334ACA80\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(Int32, TAddLanguageSpecificTextSet("LST334ACA80\_5?cpp=%");)](M_Grasshopper_Kernel_IGH_DataAccess_GetData__1.htm) | Retrieve data from an input parameter during GH\_Component.SolveInstance(). |
| Public method | [GetDataAddLanguageSpecificTextSet("LST334ACA80\_6?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(String, TAddLanguageSpecificTextSet("LST334ACA80\_8?cpp=%");)](M_Grasshopper_Kernel_IGH_DataAccess_GetData__1_1.htm) | Retrieve data from an input parameter during GH\_Component.SolveInstance(). |
| Public method | [GetDataListAddLanguageSpecificTextSet("LST334ACA80\_9?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(Int32, ListAddLanguageSpecificTextSet("LST334ACA80\_11?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_12?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_IGH_DataAccess_GetDataList__1.htm) | Retrieve an entire list of data from an input parameter during GH\_Component.SolveInstance(). |
| Public method | [GetDataListAddLanguageSpecificTextSet("LST334ACA80\_13?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_14?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(String, ListAddLanguageSpecificTextSet("LST334ACA80\_15?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_16?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_IGH_DataAccess_GetDataList__1_1.htm) | Retrieve an entire list of data from an input parameter during GH\_Component.SolveInstance(). |
| Public method | [GetDataTreeAddLanguageSpecificTextSet("LST334ACA80\_17?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_18?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(Int32, GH\_StructureAddLanguageSpecificTextSet("LST334ACA80\_19?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_20?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST334ACA80\_21?cpp=%");)](M_Grasshopper_Kernel_IGH_DataAccess_GetDataTree__1.htm) | Retrieve an entire data tree from an input parameter during GH\_Component.SolveInstance(). |
| Public method | [GetDataTreeAddLanguageSpecificTextSet("LST334ACA80\_22?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_23?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(String, GH\_StructureAddLanguageSpecificTextSet("LST334ACA80\_24?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_25?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST334ACA80\_26?cpp=%");)](M_Grasshopper_Kernel_IGH_DataAccess_GetDataTree__1_1.htm) | Retrieve an entire data tree from an input parameter during GH\_Component.SolveInstance(). |
| Public method | [IncrementIteration](M_Grasshopper_Kernel_IGH_DataAccess_IncrementIteration.htm) | Increments the iteration count by 1. |
| Public method | [ParameterTargetIndex](M_Grasshopper_Kernel_IGH_DataAccess_ParameterTargetIndex.htm) | Get the target index for the specified output parameter. |
| Public method | [ParameterTargetPath](M_Grasshopper_Kernel_IGH_DataAccess_ParameterTargetPath.htm) | Get the target path for the specified output parameter. |
| Public method | [SetData(Int32, Object)](M_Grasshopper_Kernel_IGH_DataAccess_SetData.htm) | Stores data in an output parameter during GH\_Component.SolveInstance(). Use this function only for setting individual data items. If you want to set lists of data, you \*must\* call SetDataList() instead. |
| Public method | [SetData(String, Object)](M_Grasshopper_Kernel_IGH_DataAccess_SetData_2.htm) | Stores data in an output parameter during GH\_Component.SolveInstance(). |
| Public method | [SetData(Int32, Object, Int32)](M_Grasshopper_Kernel_IGH_DataAccess_SetData_1.htm) | Expert user function. Stores data in an output parameter during GH\_Component.SolveInstance(). Use this function only for setting individual data items. If you want to set lists of data, you \*must\* call SetDataList() instead. |
| Public method | [SetDataList(Int32, IEnumerable)](M_Grasshopper_Kernel_IGH_DataAccess_SetDataList.htm) | Stores a list of data in an output parameter during GH\_Component.SolveInstance(). |
| Public method | [SetDataList(String, IEnumerable)](M_Grasshopper_Kernel_IGH_DataAccess_SetDataList_2.htm) | Stores data in an output parameter during GH\_Component.SolveInstance(). |
| Public method | [SetDataList(Int32, IEnumerable, Int32)](M_Grasshopper_Kernel_IGH_DataAccess_SetDataList_1.htm) | Expert user function. Stores a list of data in an output parameter during GH\_Component.SolveInstance(). |
| Public method | [SetDataTree(Int32, IGH\_DataTree)](M_Grasshopper_Kernel_IGH_DataAccess_SetDataTree.htm) | Folds a utility tree representation into this tree. |
| Public method | [SetDataTree(Int32, IGH\_Structure)](M_Grasshopper_Kernel_IGH_DataAccess_SetDataTree_1.htm) | Folds a utility tree representation into this tree. |
| Public method | [Util\_CountNonNullRefsAddLanguageSpecificTextSet("LST334ACA80\_27?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_28?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_IGH_DataAccess_Util_CountNonNullRefs__1.htm) | Count all object references in L |
| Public method | [Util\_CountNullRefsAddLanguageSpecificTextSet("LST334ACA80\_29?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_30?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_IGH_DataAccess_Util_CountNullRefs__1.htm) | Count all null references in L |
| Public method | [Util\_EnsureNonNullCountAddLanguageSpecificTextSet("LST334ACA80\_31?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_32?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_IGH_DataAccess_Util_EnsureNonNullCount__1.htm) | Tests a list to see if it contains sufficient non-null references. |
| Public method | [Util\_FirstNonNullItemAddLanguageSpecificTextSet("LST334ACA80\_33?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_34?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_IGH_DataAccess_Util_FirstNonNullItem__1.htm) | Returns the index of the first non-null item in a list. |
| Public method | [Util\_RemoveNullRefsAddLanguageSpecificTextSet("LST334ACA80\_35?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST334ACA80\_36?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_IGH_DataAccess_Util_RemoveNullRefs__1.htm) | Remove all null references from a list of items. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)