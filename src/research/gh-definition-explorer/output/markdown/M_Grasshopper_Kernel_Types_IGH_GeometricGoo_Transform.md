# M_Grasshopper_Kernel_Types_IGH_GeometricGoo_Transform

﻿ IGH\_GeometricGoo.Transform Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[IGH\_GeometricGoo Interface](../html/T_Grasshopper_Kernel_Types_IGH_GeometricGoo.htm "IGH_GeometricGoo Interface")

[IGH\_GeometricGoo Methods](../html/Methods_T_Grasshopper_Kernel_Types_IGH_GeometricGoo.htm "IGH_GeometricGoo Methods")

[ClearCaches Method](../html/M_Grasshopper_Kernel_Types_IGH_GeometricGoo_ClearCaches.htm "ClearCaches Method ")

[DuplicateGeometry Method](../html/M_Grasshopper_Kernel_Types_IGH_GeometricGoo_DuplicateGeometry.htm "DuplicateGeometry Method ")

[GetBoundingBox Method](../html/M_Grasshopper_Kernel_Types_IGH_GeometricGoo_GetBoundingBox.htm "GetBoundingBox Method ")

[LoadGeometry Method](../html/Overload_Grasshopper_Kernel_Types_IGH_GeometricGoo_LoadGeometry.htm "LoadGeometry Method ")

[Morph Method](../html/M_Grasshopper_Kernel_Types_IGH_GeometricGoo_Morph.htm "Morph Method ")

[Transform Method](../html/M_Grasshopper_Kernel_Types_IGH_GeometricGoo_Transform.htm "Transform Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_GeometricGooAddLanguageSpecificTextSet("LSTF0D81B3A\_0?cpp=::|nu=.");Transform Method |

Transforms the object or a deformable representation of the object.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
IGH_GeometricGoo Transform(
	Transform xform
)
```

```
Function Transform ( 
	xform As Transform
) As IGH_GeometricGoo
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

xform
:   Type: Transform  
    Transformation matrix.

#### Return Value

Type: [IGH\_GeometricGoo](T_Grasshopper_Kernel_Types_IGH_GeometricGoo.htm)  
Transformed geometry. If the local geometry can be transformed accurately,
then the returned instance equals this instance. Not all geometry types can be accurately
transformed under all circumstances though, if this is the case, this function will
return an instance of another IGH\_GeometricGoo derived type which *can* be transformed.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_GeometricGoo Interface](T_Grasshopper_Kernel_Types_IGH_GeometricGoo.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)