# M_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry_1

﻿ IGH\_BakeAwareObject.BakeGeometry Method (RhinoDoc, List(Guid))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_BakeAwareObject Interface](../html/T_Grasshopper_Kernel_IGH_BakeAwareObject.htm "IGH_BakeAwareObject Interface")

[IGH\_BakeAwareObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_BakeAwareObject.htm "IGH_BakeAwareObject Methods")

[BakeGeometry Method](../html/Overload_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry.htm "BakeGeometry Method ")

[BakeGeometry Method (RhinoDoc, List(Guid))](../html/M_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry_1.htm "BakeGeometry Method (RhinoDoc, List(Guid))")

[BakeGeometry Method (RhinoDoc, ObjectAttributes, List(Guid))](../html/M_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry.htm "BakeGeometry Method (RhinoDoc, ObjectAttributes, List(Guid))")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_BakeAwareObjectAddLanguageSpecificTextSet("LST693B1F2\_0?cpp=::|nu=.");BakeGeometry Method (RhinoDoc, ListAddLanguageSpecificTextSet("LST693B1F2\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GuidAddLanguageSpecificTextSet("LST693B1F2\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Bake all the goemetry in this object in the given Rhino document.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void BakeGeometry(
	RhinoDoc doc,
	List<Guid> obj_ids
)
```

```
Sub BakeGeometry ( 
	doc As RhinoDoc,
	obj_ids As List(Of Guid)
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

doc
:   Type: RhinoDoc  
    Document to bake into.

obj\_ids
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST693B1F2\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST693B1F2\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Guid](https://docs.microsoft.com/dotnet/api/system.guid)AddLanguageSpecificTextSet("LST693B1F2\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    All bake objects IDs will be appended to this list.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_BakeAwareObject Interface](T_Grasshopper_Kernel_IGH_BakeAwareObject.htm)

[BakeGeometry Overload](Overload_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)