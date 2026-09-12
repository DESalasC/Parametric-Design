# M_Grasshopper_Kernel_Types_IGH_FieldElement_IsCoincident

﻿ IGH\_FieldElement.IsCoincident Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[IGH\_FieldElement Interface](../html/T_Grasshopper_Kernel_Types_IGH_FieldElement.htm "IGH_FieldElement Interface")

[IGH\_FieldElement Methods](../html/Methods_T_Grasshopper_Kernel_Types_IGH_FieldElement.htm "IGH_FieldElement Methods")

[Duplicate Method](../html/M_Grasshopper_Kernel_Types_IGH_FieldElement_Duplicate.htm "Duplicate Method ")

[Force Method](../html/M_Grasshopper_Kernel_Types_IGH_FieldElement_Force.htm "Force Method ")

[IsCoincident Method](../html/M_Grasshopper_Kernel_Types_IGH_FieldElement_IsCoincident.htm "IsCoincident Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_FieldElementAddLanguageSpecificTextSet("LSTC435386C\_0?cpp=::|nu=.");IsCoincident Method |

Computes whether the point can be considered coincident with the element.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool IsCoincident(
	Point3d point,
	double tolerance
)
```

```
Function IsCoincident ( 
	point As Point3d,
	tolerance As Double
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

point
:   Type: Point3d  
    Point to test.

tolerance
:   Type: [SystemAddLanguageSpecificTextSet("LSTC435386C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Tolerance to use.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the point is coincident within tolerance.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_FieldElement Interface](T_Grasshopper_Kernel_Types_IGH_FieldElement.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)