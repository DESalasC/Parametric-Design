# M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects

﻿ GH\_Document.FindAllDownstreamObjects Method (IGH\_ActiveObject)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[FindAllDownstreamObjects Method](../html/Overload_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects.htm "FindAllDownstreamObjects Method ")

[FindAllDownstreamObjects Method (IGH\_ActiveObject)](../html/M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects.htm "FindAllDownstreamObjects Method (IGH_ActiveObject)")

[FindAllDownstreamObjects Method (List(IGH\_ActiveObject))](../html/M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects_2.htm "FindAllDownstreamObjects Method (List(IGH_ActiveObject))")

[FindAllDownstreamObjects Method (IGH\_ActiveObject, GH\_Document.GH\_ActiveObjectFilter)](../html/M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects_1.htm "FindAllDownstreamObjects Method (IGH_ActiveObject, GH_Document.GH_ActiveObjectFilter)")

[FindAllDownstreamObjects Method (List(IGH\_ActiveObject), GH\_Document.GH\_ActiveObjectFilter)](../html/M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects_3.htm "FindAllDownstreamObjects Method (List(IGH_ActiveObject), GH_Document.GH_ActiveObjectFilter)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LST41D4C5A4\_0?cpp=::|nu=.");FindAllDownstreamObjects Method (IGH\_ActiveObject) |

Find all objects that depend in some way on the Source.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public List<IGH_ActiveObject> FindAllDownstreamObjects(
	IGH_ActiveObject from
)
```

```
Public Function FindAllDownstreamObjects ( 
	from As IGH_ActiveObject
) As List(Of IGH_ActiveObject)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

from
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST41D4C5A4\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm)  
    Object to start searching from.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST41D4C5A4\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm)AddLanguageSpecificTextSet("LST41D4C5A4\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[FindAllDownstreamObjects Overload](Overload_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)