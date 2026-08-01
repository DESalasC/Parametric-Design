# M_Grasshopper_Kernel_Types_GH_Point_ReferenceType_1

﻿ GH\_Point.ReferenceType Method (GH\_PointRefType)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Point Class](../html/T_Grasshopper_Kernel_Types_GH_Point.htm "GH_Point Class")

[GH\_Point Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Point.htm "GH_Point Methods")

[ReferenceType Method](../html/Overload_Grasshopper_Kernel_Types_GH_Point_ReferenceType.htm "ReferenceType Method ")

[ReferenceType Method](../html/M_Grasshopper_Kernel_Types_GH_Point_ReferenceType.htm "ReferenceType Method ")

[ReferenceType Method (GH\_PointRefType)](../html/M_Grasshopper_Kernel_Types_GH_Point_ReferenceType_1.htm "ReferenceType Method (GH_PointRefType)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PointAddLanguageSpecificTextSet("LST5807F89B\_0?cpp=::|nu=.");ReferenceType Method (GH\_PointRefType) |

Sets the type of the point reference data.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void ReferenceType(
	GH_PointRefType new_type
)
```

```
Public Sub ReferenceType ( 
	new_type As GH_PointRefType
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

new\_type
:   Type: [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST5807F89B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PointRefType](T_Grasshopper_Kernel_Types_GH_PointRefType.htm)  
    The new type, if type = Coordinate or Unset, then the Reference data will be erased.

![](../icons/SectionExpanded.png)Remarks

If there is no reference data, this function will create a new instance.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Point Class](T_Grasshopper_Kernel_Types_GH_Point.htm)

[ReferenceType Overload](Overload_Grasshopper_Kernel_Types_GH_Point_ReferenceType.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)