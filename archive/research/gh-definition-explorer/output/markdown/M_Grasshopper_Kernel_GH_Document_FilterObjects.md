# M_Grasshopper_Kernel_GH_Document_FilterObjects

﻿ GH\_Document.FilterObjects Method (GH\_Filter, GH\_Filter, GH\_Filter)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[FilterObjects Method](../html/Overload_Grasshopper_Kernel_GH_Document_FilterObjects.htm "FilterObjects Method ")

[FilterObjects Method (GH\_Filter, GH\_Filter, GH\_Filter)](../html/M_Grasshopper_Kernel_GH_Document_FilterObjects.htm "FilterObjects Method (GH_Filter, GH_Filter, GH_Filter)")

[FilterObjects Method (List(IGH\_DocumentObject), GH\_Filter, GH\_Filter, GH\_Filter)](../html/M_Grasshopper_Kernel_GH_Document_FilterObjects_1.htm "FilterObjects Method (List(IGH_DocumentObject), GH_Filter, GH_Filter, GH_Filter)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LSTB91C5389\_0?cpp=::|nu=.");FilterObjects Method (GH\_Filter, GH\_Filter, GH\_Filter) |

Returns all objects in the document that pass the filter specification

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public List<IGH_DocumentObject> FilterObjects(
	GH_Filter selectedObjects = GH_Filter.DontCare,
	GH_Filter enabledObjects = GH_Filter.DontCare,
	GH_Filter activeObjects = GH_Filter.DontCare
)
```

```
Public Function FilterObjects ( 
	Optional selectedObjects As GH_Filter = GH_Filter.DontCare,
	Optional enabledObjects As GH_Filter = GH_Filter.DontCare,
	Optional activeObjects As GH_Filter = GH_Filter.DontCare
) As List(Of IGH_DocumentObject)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

selectedObjects (Optional)
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTB91C5389\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Filter](T_Grasshopper_Kernel_GH_Filter.htm)

enabledObjects (Optional)
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTB91C5389\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Filter](T_Grasshopper_Kernel_GH_Filter.htm)

activeObjects (Optional)
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTB91C5389\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Filter](T_Grasshopper_Kernel_GH_Filter.htm)

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LSTB91C5389\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm)AddLanguageSpecificTextSet("LSTB91C5389\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[FilterObjects Overload](Overload_Grasshopper_Kernel_GH_Document_FilterObjects.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)