# M_Grasshopper_Kernel_IGH_DataAccess_GetDataTree__1_1

﻿ IGH\_DataAccess.GetDataTree(T) Method (String, GH\_Structure(T))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DataAccess Interface](../html/T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Interface")

[IGH\_DataAccess Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Methods")

[GetDataTree Method](../html/Overload_Grasshopper_Kernel_IGH_DataAccess_GetDataTree.htm "GetDataTree Method ")

[GetDataTree(T) Method (Int32, GH\_Structure(T))](../html/M_Grasshopper_Kernel_IGH_DataAccess_GetDataTree__1.htm "GetDataTree(T) Method (Int32, GH_Structure(T))")

[GetDataTree(T) Method (String, GH\_Structure(T))](../html/M_Grasshopper_Kernel_IGH_DataAccess_GetDataTree__1_1.htm "GetDataTree(T) Method (String, GH_Structure(T))")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DataAccessAddLanguageSpecificTextSet("LSTBCF82DF2\_0?cpp=::|nu=.");GetDataTreeAddLanguageSpecificTextSet("LSTBCF82DF2\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTBCF82DF2\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Method (String, GH\_StructureAddLanguageSpecificTextSet("LSTBCF82DF2\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTBCF82DF2\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTBCF82DF2\_5?cpp=%");) |

Retrieve an entire data tree from an input parameter during GH\_Component.SolveInstance().

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool GetDataTree<T>(
	string name,
	out GH_Structure<T> tree
)
where T : IGH_Goo
```

```
Function GetDataTree(Of T As IGH_Goo) ( 
	name As String,
	<OutAttribute> ByRef tree As GH_Structure(Of T)
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LSTBCF82DF2\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)

tree
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LSTBCF82DF2\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Structure](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)AddLanguageSpecificTextSet("LSTBCF82DF2\_8?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTBCF82DF2\_9?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTBCF82DF2\_10?cpp=%");

#### Type Parameters

T
:   Type of the data to retrieve. Must be identical to the type stored in the parameter.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)Remarks

Parameter access by index is faster, consider using the other overload if possible.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DataAccess Interface](T_Grasshopper_Kernel_IGH_DataAccess.htm)

[GetDataTree Overload](Overload_Grasshopper_Kernel_IGH_DataAccess_GetDataTree.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)