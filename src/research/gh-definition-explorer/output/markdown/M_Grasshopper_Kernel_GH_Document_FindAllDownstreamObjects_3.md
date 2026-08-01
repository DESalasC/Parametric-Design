# M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects_3

﻿ GH\_Document.FindAllDownstreamObjects Method (List(IGH\_ActiveObject), GH\_Document.GH\_ActiveObjectFilter)

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
| GH\_DocumentAddLanguageSpecificTextSet("LST3B707D69\_0?cpp=::|nu=.");FindAllDownstreamObjects Method (ListAddLanguageSpecificTextSet("LST3B707D69\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ActiveObjectAddLanguageSpecificTextSet("LST3B707D69\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_DocumentAddLanguageSpecificTextSet("LST3B707D69\_3?cpp=::|nu=.");GH\_ActiveObjectFilter) |

Find all objects that depend in some way on the Source collection

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
	List<IGH_ActiveObject> from,
	GH_DocumentAddLanguageSpecificTextSet("LST3B707D69_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH_ActiveObjectFilter filter
)
```

```
Public Function FindAllDownstreamObjects ( 
	from As List(Of IGH_ActiveObject),
	filter As GH_DocumentAddLanguageSpecificTextSet("LST3B707D69_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH_ActiveObjectFilter
) As List(Of IGH_ActiveObject)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

from
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST3B707D69\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST3B707D69\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm)AddLanguageSpecificTextSet("LST3B707D69\_8?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Objects to start searching from.

filter
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST3B707D69\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocumentAddLanguageSpecificTextSet("LST3B707D69\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ActiveObjectFilter](T_Grasshopper_Kernel_GH_Document_GH_ActiveObjectFilter.htm)  
    The inclusion delegate

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST3B707D69\_11?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm)AddLanguageSpecificTextSet("LST3B707D69\_12?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[FindAllDownstreamObjects Overload](Overload_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)