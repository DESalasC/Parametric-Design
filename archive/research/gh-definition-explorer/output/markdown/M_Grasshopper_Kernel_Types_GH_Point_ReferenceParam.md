# M_Grasshopper_Kernel_Types_GH_Point_ReferenceParam

﻿ GH\_Point.ReferenceParam Method (Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Point Class](../html/T_Grasshopper_Kernel_Types_GH_Point.htm "GH_Point Class")

[GH\_Point Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Point.htm "GH_Point Methods")

[ReferenceParam Method](../html/Overload_Grasshopper_Kernel_Types_GH_Point_ReferenceParam.htm "ReferenceParam Method ")

[ReferenceParam Method (Int32)](../html/M_Grasshopper_Kernel_Types_GH_Point_ReferenceParam.htm "ReferenceParam Method (Int32)")

[ReferenceParam Method (Int32, Double)](../html/M_Grasshopper_Kernel_Types_GH_Point_ReferenceParam_1.htm "ReferenceParam Method (Int32, Double)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PointAddLanguageSpecificTextSet("LSTCFB56E1D\_0?cpp=::|nu=.");ReferenceParam Method (Int32) |

Retrieve the indexed param of the point reference data.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public double ReferenceParam(
	int index
)
```

```
Public Function ReferenceParam ( 
	index As Integer
) As Double
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

index
:   Type: [SystemAddLanguageSpecificTextSet("LSTCFB56E1D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of parameter. Only 0 and 1 are valid values.

#### Return Value

Type: [Double](https://docs.microsoft.com/dotnet/api/system.double)  
The indexed param of the reference data.

![](../icons/SectionExpanded.png)Remarks

If there exists no reference data, NaN is returned.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Point Class](T_Grasshopper_Kernel_Types_GH_Point.htm)

[ReferenceParam Overload](Overload_Grasshopper_Kernel_Types_GH_Point_ReferenceParam.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)