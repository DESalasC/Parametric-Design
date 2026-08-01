# M_Grasshopper_Kernel_GH_Param_1_AddVolatileData

﻿ GH\_Param(T).AddVolatileData Method (GH\_Path, Int32, Object)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Param(T) Class](../html/T_Grasshopper_Kernel_GH_Param_1.htm "GH_Param(T) Class")

[GH\_Param(T) Methods](../html/Methods_T_Grasshopper_Kernel_GH_Param_1.htm "GH_Param(T) Methods")

[AddVolatileData Method](../html/Overload_Grasshopper_Kernel_GH_Param_1_AddVolatileData.htm "AddVolatileData Method ")

[AddVolatileData Method (GH\_Path, Int32, T)](../html/M_Grasshopper_Kernel_GH_Param_1_AddVolatileData_1.htm "AddVolatileData Method (GH_Path, Int32, T)")

[AddVolatileData Method (GH\_Path, Int32, Object)](../html/M_Grasshopper_Kernel_GH_Param_1_AddVolatileData.htm "AddVolatileData Method (GH_Path, Int32, Object)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ParamAddLanguageSpecificTextSet("LSTB3EAFCD6\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTB3EAFCD6\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTB3EAFCD6\_2?cpp=::|nu=.");AddVolatileData Method (GH\_Path, Int32, Object) |

Inserts an item of volatile data into the data structure.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool AddVolatileData(
	GH_Path path,
	int index,
	Object data
)
```

```
Public Function AddVolatileData ( 
	path As GH_Path,
	index As Integer,
	data As Object
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LSTB3EAFCD6\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    The branch path of the data. If the path doesn't exist yet, it will be created.

index
:   Type: [SystemAddLanguageSpecificTextSet("LSTB3EAFCD6\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    The item index of the data. If the path doesn't contain the index yet,
    it will be enlarged to encompass the index.

data
:   Type: [SystemAddLanguageSpecificTextSet("LSTB3EAFCD6\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
    The data to store.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, False on failure. If the data cannot be converted, the topology will remain unmolested.

#### Implements

[IGH\_ParamAddLanguageSpecificTextSet("LSTB3EAFCD6\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");AddVolatileData(GH\_Path, Int32, Object)](M_Grasshopper_Kernel_IGH_Param_AddVolatileData.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ParamAddLanguageSpecificTextSet("LSTB3EAFCD6\_7?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB3EAFCD6\_8?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_Param_1.htm)

[AddVolatileData Overload](Overload_Grasshopper_Kernel_GH_Param_1_AddVolatileData.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)