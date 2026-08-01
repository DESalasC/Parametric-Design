# M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform

﻿ GH\_GeometricGoo(T).Transform Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_GeometricGoo(T) Class](../html/T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm "GH_GeometricGoo(T) Class")

[GH\_GeometricGoo(T) Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm "GH_GeometricGoo(T) Methods")

[CastFrom Method](../html/M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm "CastFrom Method ")

[CastTo Method](../html/Overload_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo.htm "CastTo Method ")

[ClearCaches Method](../html/M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ClearCaches.htm "ClearCaches Method ")

[Duplicate Method](../html/M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Duplicate.htm "Duplicate Method ")

[DuplicateGeometry Method](../html/M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_DuplicateGeometry.htm "DuplicateGeometry Method ")

[EmitProxy Method](../html/M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_EmitProxy.htm "EmitProxy Method ")

[GetBoundingBox Method](../html/M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_GetBoundingBox.htm "GetBoundingBox Method ")

[LoadGeometry Method](../html/Overload_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm "LoadGeometry Method ")

[Morph Method](../html/M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Morph.htm "Morph Method ")

[Transform Method](../html/M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform.htm "Transform Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GeometricGooAddLanguageSpecificTextSet("LSTDC80AC0D\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTDC80AC0D\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTDC80AC0D\_2?cpp=::|nu=.");Transform Method |

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
public abstract IGH_GeometricGoo Transform(
	Transform xform
)
```

```
Public MustOverride Function Transform ( 
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

#### Implements

[IGH\_GeometricGooAddLanguageSpecificTextSet("LSTDC80AC0D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Transform(Transform)](M_Grasshopper_Kernel_Types_IGH_GeometricGoo_Transform.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GeometricGooAddLanguageSpecificTextSet("LSTDC80AC0D\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDC80AC0D\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)