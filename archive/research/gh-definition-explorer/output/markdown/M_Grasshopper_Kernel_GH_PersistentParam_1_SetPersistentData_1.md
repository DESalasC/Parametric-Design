# M_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData_1

﻿ GH\_PersistentParam(T).SetPersistentData Method (IEnumerable(T))

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
| GH\_PersistentParamAddLanguageSpecificTextSet("LSTAEAD9787\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTAEAD9787\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTAEAD9787\_2?cpp=::|nu=.");SetPersistentData Method (IEnumerableAddLanguageSpecificTextSet("LSTAEAD9787\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTAEAD9787\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Assign a list of items to the persistent data.
This method will erase any existing data,
record an undo event,
raise the OnObjectChanged event for PersistentData flags and
place a call to ExpireSolution(False).
If you want to add a tree of data, you should use the appropriate overload for this method.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void SetPersistentData(
	IEnumerable<T> items
)
```

```
Public Sub SetPersistentData ( 
	items As IEnumerable(Of T)
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

items
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LSTAEAD9787\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LSTAEAD9787\_6?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[T](T_Grasshopper_Kernel_GH_PersistentParam_1.htm)AddLanguageSpecificTextSet("LSTAEAD9787\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Items to add.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_PersistentParamAddLanguageSpecificTextSet("LSTAEAD9787\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTAEAD9787\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_PersistentParam_1.htm)

[SetPersistentData Overload](Overload_Grasshopper_Kernel_GH_PersistentParam_1_SetPersistentData.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)