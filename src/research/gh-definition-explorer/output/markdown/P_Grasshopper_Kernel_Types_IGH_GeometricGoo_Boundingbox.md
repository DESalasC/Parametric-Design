# P_Grasshopper_Kernel_Types_IGH_GeometricGoo_Boundingbox

﻿ IGH\_GeometricGoo.Boundingbox Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[IGH\_GeometricGoo Interface](../html/T_Grasshopper_Kernel_Types_IGH_GeometricGoo.htm "IGH_GeometricGoo Interface")

[IGH\_GeometricGoo Properties](../html/Properties_T_Grasshopper_Kernel_Types_IGH_GeometricGoo.htm "IGH_GeometricGoo Properties")

[Boundingbox Property](../html/P_Grasshopper_Kernel_Types_IGH_GeometricGoo_Boundingbox.htm "Boundingbox Property ")

[IsGeometryLoaded Property](../html/P_Grasshopper_Kernel_Types_IGH_GeometricGoo_IsGeometryLoaded.htm "IsGeometryLoaded Property ")

[IsReferencedGeometry Property](../html/P_Grasshopper_Kernel_Types_IGH_GeometricGoo_IsReferencedGeometry.htm "IsReferencedGeometry Property ")

[ReferenceID Property](../html/P_Grasshopper_Kernel_Types_IGH_GeometricGoo_ReferenceID.htm "ReferenceID Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_GeometricGooAddLanguageSpecificTextSet("LSTA04F2350\_0?cpp=::|nu=.");Boundingbox Property |

Gets the (cached) boundingbox for this geometry.
Not all geometry types cache boundingbox results.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
BoundingBox Boundingbox { get; }
```

```
ReadOnly Property Boundingbox As BoundingBox
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: BoundingBox  

[Missing <value> documentation for "P:Grasshopper.Kernel.Types.IGH\_GeometricGoo.Boundingbox"]

#### Return Value

Type: BoundingBox  
The boundingbox for this piece of geometry or
Boundingbox.Empty if the geometry is null or invalid.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_GeometricGoo Interface](T_Grasshopper_Kernel_Types_IGH_GeometricGoo.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)