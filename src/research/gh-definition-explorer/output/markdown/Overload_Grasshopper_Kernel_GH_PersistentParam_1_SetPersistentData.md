# Overload_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData

﻿ GH\_PersistentParam(T).SetPersistentData Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_PersistentParam(T) Class](../html/T_Grasshopper_Kernel_GH_PersistentParam_1.htm "GH_PersistentParam(T) Class")

[GH\_PersistentParam(T) Methods](../html/Methods_T_Grasshopper_Kernel_GH_PersistentParam_1.htm "GH_PersistentParam(T) Methods")

[SetPersistentData Method](../html/Overload_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData.htm "SetPersistentData Method ")

[SetPersistentData Method (T)](../html/M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData_3.htm "SetPersistentData Method (T)")

[SetPersistentData Method (GH\_Structure(T))](../html/M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData.htm "SetPersistentData Method (GH_Structure(T))")

[SetPersistentData Method (IEnumerable(T))](../html/M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData_1.htm "SetPersistentData Method (IEnumerable(T))")

[SetPersistentData Method (Object[])](../html/M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData_2.htm "SetPersistentData Method (Object[])")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PersistentParamAddLanguageSpecificTextSet("LSTC9F811E9\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTC9F811E9\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTC9F811E9\_2?cpp=::|nu=.");SetPersistentData Method |

![](../icons/SectionExpanded.png)Overload List

|  | Name | Description |
| --- | --- | --- |
| Public method | [SetPersistentData(T)](M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData_3.htm) | Add a single item to the persistent data. This method will record an undo event, raise the OnObjectChanged event for PersistentData flags and place a call to ExpireSolution(False). If you want to add more than one piece of data, you should use the appropriate overload for this method. |
| Public method | [SetPersistentData(GH\_StructureAddLanguageSpecificTextSet("LSTC9F811E9\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTC9F811E9\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData.htm) | Assign a tree of items to the persistent data. This method will erase any existing data, record an undo event, raise the OnObjectChanged event for PersistentData flags and place a call to ExpireSolution(False). If you want to add a tree of data, you should use the appropriate overload for this method. |
| Public method | [SetPersistentData(IEnumerableAddLanguageSpecificTextSet("LSTC9F811E9\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTC9F811E9\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData_1.htm) | Assign a list of items to the persistent data. This method will erase any existing data, record an undo event, raise the OnObjectChanged event for PersistentData flags and place a call to ExpireSolution(False). If you want to add a tree of data, you should use the appropriate overload for this method. |
| Public method | [SetPersistentData(AddLanguageSpecificTextSet("LSTC9F811E9\_7?cpp=array&lt;");ObjectAddLanguageSpecificTextSet("LSTC9F811E9\_8?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData_2.htm) | Add a collection of values to the persistent data. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_PersistentParamAddLanguageSpecificTextSet("LSTC9F811E9\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC9F811E9\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_PersistentParam_1.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)