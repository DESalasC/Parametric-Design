# M_Grasshopper_Kernel_Data_GH_IndexRange_Intersection

﻿ GH\_IndexRange.Intersection Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_IndexRange Structure](../html/T_Grasshopper_Kernel_Data_GH_IndexRange.htm "GH_IndexRange Structure")

[GH\_IndexRange Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_IndexRange.htm "GH_IndexRange Methods")

[AdjacentTo Method](../html/M_Grasshopper_Kernel_Data_GH_IndexRange_AdjacentTo.htm "AdjacentTo Method ")

[Contains Method](../html/Overload_Grasshopper_Kernel_Data_GH_IndexRange_Contains.htm "Contains Method ")

[Intersection Method](../html/M_Grasshopper_Kernel_Data_GH_IndexRange_Intersection.htm "Intersection Method ")

[IntersectsWith Method](../html/M_Grasshopper_Kernel_Data_GH_IndexRange_IntersectsWith.htm "IntersectsWith Method ")

[Split Method](../html/M_Grasshopper_Kernel_Data_GH_IndexRange_Split.htm "Split Method ")

[ToString Method](../html/M_Grasshopper_Kernel_Data_GH_IndexRange_ToString.htm "ToString Method ")

[Union Method](../html/M_Grasshopper_Kernel_Data_GH_IndexRange_Union.htm "Union Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IndexRangeAddLanguageSpecificTextSet("LST2356D1D0\_0?cpp=::|nu=.");Intersection Method |

Create the intersection between two ranges.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_IndexRange Intersection(
	GH_IndexRange range0,
	GH_IndexRange range1
)
```

```
Public Shared Function Intersection ( 
	range0 As GH_IndexRange,
	range1 As GH_IndexRange
) As GH_IndexRange
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

range0
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST2356D1D0\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IndexRange](T_Grasshopper_Kernel_Data_GH_IndexRange.htm)  
    First range to intersect.

range1
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST2356D1D0\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IndexRange](T_Grasshopper_Kernel_Data_GH_IndexRange.htm)  
    Second range to intersect.

#### Return Value

Type: [GH\_IndexRange](T_Grasshopper_Kernel_Data_GH_IndexRange.htm)  
The intersection or an invalid range if the input doesn't intersect.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IndexRange Structure](T_Grasshopper_Kernel_Data_GH_IndexRange.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)