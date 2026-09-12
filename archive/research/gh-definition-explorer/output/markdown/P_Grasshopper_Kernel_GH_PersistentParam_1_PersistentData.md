# P_Grasshopper_Kernel_GH_PersistentParam_1_PersistentData

﻿ GH\_PersistentParam(T).PersistentData Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_PersistentParam(T) Class](../html/T_Grasshopper_Kernel_GH_PersistentParam_1.htm "GH_PersistentParam(T) Class")

[GH\_PersistentParam(T) Properties](../html/Properties_T_Grasshopper_Kernel_GH_PersistentParam_1.htm "GH_PersistentParam(T) Properties")

[DataType Property](../html/P_Grasshopper_Kernel_GH_PersistentParam_1_DataType.htm "DataType Property ")

[PersistentData Property](../html/P_Grasshopper_Kernel_GH_PersistentParam_1_PersistentData.htm "PersistentData Property ")

[PersistentDataCount Property](../html/P_Grasshopper_Kernel_GH_PersistentParam_1_PersistentDataCount.htm "PersistentDataCount Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PersistentParamAddLanguageSpecificTextSet("LST4B4D8A7A\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST4B4D8A7A\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST4B4D8A7A\_2?cpp=::|nu=.");PersistentData Property |

Gets the persistent data stored in this parameter.
If you modify the persistent data, be sure to call the:
OnObjectChanged(GH\_ObjectEventType.PersistentData)
event.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_Structure<T> PersistentData { get; }
```

```
Public ReadOnly Property PersistentData As GH_Structure(Of T)
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [GH\_Structure](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)AddLanguageSpecificTextSet("LST4B4D8A7A\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[T](T_Grasshopper_Kernel_GH_PersistentParam_1.htm)AddLanguageSpecificTextSet("LST4B4D8A7A\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  

[Missing <value> documentation for "P:Grasshopper.Kernel.GH\_PersistentParam`1.PersistentData"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_PersistentParamAddLanguageSpecificTextSet("LST4B4D8A7A\_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4B4D8A7A\_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_PersistentParam_1.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)