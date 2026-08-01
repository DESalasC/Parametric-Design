# M_Grasshopper_Kernel_GH_ListUtil_CountNullRefs__1

﻿ GH\_ListUtil.CountNullRefs(T) Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ListUtil Class](../html/T_Grasshopper_Kernel_GH_ListUtil.htm "GH_ListUtil Class")

[GH\_ListUtil Methods](../html/Methods_T_Grasshopper_Kernel_GH_ListUtil.htm "GH_ListUtil Methods")

[CountNonNullRefs(T) Method](../html/M_Grasshopper_Kernel_GH_ListUtil_CountNonNullRefs__1.htm "CountNonNullRefs(T) Method ")

[CountNullRefs(T) Method](../html/M_Grasshopper_Kernel_GH_ListUtil_CountNullRefs__1.htm "CountNullRefs(T) Method ")

[EnsureNonNullCount(T) Method](../html/M_Grasshopper_Kernel_GH_ListUtil_EnsureNonNullCount__1.htm "EnsureNonNullCount(T) Method ")

[FirstNonNullItem(T) Method](../html/M_Grasshopper_Kernel_GH_ListUtil_FirstNonNullItem__1.htm "FirstNonNullItem(T) Method ")

[RemoveNullRefs(T) Method](../html/M_Grasshopper_Kernel_GH_ListUtil_RemoveNullRefs__1.htm "RemoveNullRefs(T) Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ListUtilAddLanguageSpecificTextSet("LST54CA8D56\_0?cpp=::|nu=.");CountNullRefsAddLanguageSpecificTextSet("LST54CA8D56\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST54CA8D56\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Method |

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
public static int CountNullRefs<T>(
	List<T> L
)
```

```
Public Shared Function CountNullRefs(Of T) ( 
	L As List(Of T)
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

L
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST54CA8D56\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST54CA8D56\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST54CA8D56\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    List to parse

#### Type Parameters

T
:   Type of list

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
Number of nulls in L

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ListUtil Class](T_Grasshopper_Kernel_GH_ListUtil.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)