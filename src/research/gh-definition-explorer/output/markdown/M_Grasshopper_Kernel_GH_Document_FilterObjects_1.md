# M_Grasshopper_Kernel_GH_Document_FilterObjects_1

﻿ GH\_Document.FilterObjects Method (List(IGH\_DocumentObject), GH\_Filter, GH\_Filter, GH\_Filter)

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
| GH\_DocumentAddLanguageSpecificTextSet("LST1D06D885\_0?cpp=::|nu=.");FilterObjects Method (ListAddLanguageSpecificTextSet("LST1D06D885\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_DocumentObjectAddLanguageSpecificTextSet("LST1D06D885\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_Filter, GH\_Filter, GH\_Filter) |

Filter a list of objects using several filters at once

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static List<IGH_DocumentObject> FilterObjects(
	List<IGH_DocumentObject> in,
	GH_Filter bSelectedObjects = GH_Filter.DontCare,
	GH_Filter bEnabledObjects = GH_Filter.DontCare,
	GH_Filter bActiveObjects = GH_Filter.DontCare
)
```

```
Public Shared Function FilterObjects ( 
	in As List(Of IGH_DocumentObject),
	Optional bSelectedObjects As GH_Filter = GH_Filter.DontCare,
	Optional bEnabledObjects As GH_Filter = GH_Filter.DontCare,
	Optional bActiveObjects As GH_Filter = GH_Filter.DontCare
) As List(Of IGH_DocumentObject)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

in
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST1D06D885\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST1D06D885\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm)AddLanguageSpecificTextSet("LST1D06D885\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    The set to filter

bSelectedObjects (Optional)
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST1D06D885\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Filter](T_Grasshopper_Kernel_GH_Filter.htm)  
    Filter (non)selected objects only

bEnabledObjects (Optional)
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST1D06D885\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Filter](T_Grasshopper_Kernel_GH_Filter.htm)  
    Filter (non)enabled objects only

bActiveObjects (Optional)
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST1D06D885\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Filter](T_Grasshopper_Kernel_GH_Filter.htm)  
    Filter (non)active objects only

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST1D06D885\_9?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm)AddLanguageSpecificTextSet("LST1D06D885\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list with all objects that pass all filters

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[FilterObjects Overload](Overload_Grasshopper_Kernel_GH_Document_FilterObjects.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)