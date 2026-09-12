# M_Grasshopper_Kernel_GH_GHXHarvester_HarvestPivots_1

﻿ GH\_GHXHarvester.HarvestPivots Method (GH\_IReader)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_GHXHarvester Class](../html/T_Grasshopper_Kernel_GH_GHXHarvester.htm "GH_GHXHarvester Class")

[GH\_GHXHarvester Methods](../html/Methods_T_Grasshopper_Kernel_GH_GHXHarvester.htm "GH_GHXHarvester Methods")

[HarvestPivots Method](../html/Overload_Grasshopper_Kernel_GH_GHXHarvester_HarvestPivots.htm "HarvestPivots Method ")

[HarvestPivots Method (GH\_Archive)](../html/M_Grasshopper_Kernel_GH_GHXHarvester_HarvestPivots.htm "HarvestPivots Method (GH_Archive)")

[HarvestPivots Method (GH\_IReader)](../html/M_Grasshopper_Kernel_GH_GHXHarvester_HarvestPivots_1.htm "HarvestPivots Method (GH_IReader)")

[HarvestPivots Method (String)](../html/M_Grasshopper_Kernel_GH_GHXHarvester_HarvestPivots_2.htm "HarvestPivots Method (String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GHXHarvesterAddLanguageSpecificTextSet("LST3EA56B01\_0?cpp=::|nu=.");HarvestPivots Method (GH\_IReader) |

Harvest all attribute pivots from a GHX/GH node.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static List<PointF> HarvestPivots(
	GH_IReader node
)
```

```
Public Shared Function HarvestPivots ( 
	node As GH_IReader
) As List(Of PointF)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

node
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LST3EA56B01\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IReader](T_GH_IO_Serialization_GH_IReader.htm)  
    Node to parse.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST3EA56B01\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)AddLanguageSpecificTextSet("LST3EA56B01\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list of all attribute pivots or null on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GHXHarvester Class](T_Grasshopper_Kernel_GH_GHXHarvester.htm)

[HarvestPivots Overload](Overload_Grasshopper_Kernel_GH_GHXHarvester_HarvestPivots.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)