# M_Grasshopper_Kernel_Types_GH_PointRefData_EvCurve

﻿ GH\_PointRefData.EvCurve Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_PointRefData Class](../html/T_Grasshopper_Kernel_Types_GH_PointRefData.htm "GH_PointRefData Class")

[GH\_PointRefData Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_PointRefData.htm "GH_PointRefData Methods")

[EvCurve Method](../html/M_Grasshopper_Kernel_Types_GH_PointRefData_EvCurve.htm "EvCurve Method ")

[EvCurveParam Method](../html/M_Grasshopper_Kernel_Types_GH_PointRefData_EvCurveParam.htm "EvCurveParam Method ")

[EvSurface Method](../html/M_Grasshopper_Kernel_Types_GH_PointRefData_EvSurface.htm "EvSurface Method ")

[SetCurveDistFromEndParam Method](../html/M_Grasshopper_Kernel_Types_GH_PointRefData_SetCurveDistFromEndParam.htm "SetCurveDistFromEndParam Method ")

[SetCurveDistFromStartParam Method](../html/M_Grasshopper_Kernel_Types_GH_PointRefData_SetCurveDistFromStartParam.htm "SetCurveDistFromStartParam Method ")

[SetCurveParam Method](../html/M_Grasshopper_Kernel_Types_GH_PointRefData_SetCurveParam.htm "SetCurveParam Method ")

[SetCurveRatioParam Method](../html/M_Grasshopper_Kernel_Types_GH_PointRefData_SetCurveRatioParam.htm "SetCurveRatioParam Method ")

[SetSurfaceParam Method](../html/M_Grasshopper_Kernel_Types_GH_PointRefData_SetSurfaceParam.htm "SetSurfaceParam Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PointRefDataAddLanguageSpecificTextSet("LST9EF72E29\_0?cpp=::|nu=.");EvCurve Method |

Evaluate this reference structure when applied to a curve

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Point3d EvCurve(
	Curve c
)
```

```
Public Function EvCurve ( 
	c As Curve
) As Point3d
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

c
:   Type: Curve  
    The curve to act on

#### Return Value

Type: Point3d  
The point on the curve if successful, or Nothing

![](../icons/SectionExpanded.png)Remarks

Evaluation depends on the value of m\_RefType

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_PointRefData Class](T_Grasshopper_Kernel_Types_GH_PointRefData.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)