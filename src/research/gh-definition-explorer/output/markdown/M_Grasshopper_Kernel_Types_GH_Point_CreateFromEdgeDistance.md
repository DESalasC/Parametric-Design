# M_Grasshopper_Kernel_Types_GH_Point_CreateFromEdgeDistance

﻿ GH\_Point.CreateFromEdgeDistance Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Point Class](../html/T_Grasshopper_Kernel_Types_GH_Point.htm "GH_Point Class")

[GH\_Point Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Point.htm "GH_Point Methods")

[BakeGeometry Method](../html/M_Grasshopper_Kernel_Types_GH_Point_BakeGeometry.htm "BakeGeometry Method ")

[CastFrom Method](../html/M_Grasshopper_Kernel_Types_GH_Point_CastFrom.htm "CastFrom Method ")

[CastTo(T) Method](../html/M_Grasshopper_Kernel_Types_GH_Point_CastTo__1.htm "CastTo(T) Method ")

[ClearCaches Method](../html/M_Grasshopper_Kernel_Types_GH_Point_ClearCaches.htm "ClearCaches Method ")

[CreateFromCoordinate Method](../html/M_Grasshopper_Kernel_Types_GH_Point_CreateFromCoordinate.htm "CreateFromCoordinate Method ")

[CreateFromCurveDistance Method](../html/M_Grasshopper_Kernel_Types_GH_Point_CreateFromCurveDistance.htm "CreateFromCurveDistance Method ")

[CreateFromCurveRatio Method](../html/M_Grasshopper_Kernel_Types_GH_Point_CreateFromCurveRatio.htm "CreateFromCurveRatio Method ")

[CreateFromEdgeDistance Method](../html/M_Grasshopper_Kernel_Types_GH_Point_CreateFromEdgeDistance.htm "CreateFromEdgeDistance Method ")

[CreateFromEdgeRatio Method](../html/M_Grasshopper_Kernel_Types_GH_Point_CreateFromEdgeRatio.htm "CreateFromEdgeRatio Method ")

[CreateFromPointObject Method](../html/M_Grasshopper_Kernel_Types_GH_Point_CreateFromPointObject.htm "CreateFromPointObject Method ")

[CreateFromSurfaceParam Method](../html/M_Grasshopper_Kernel_Types_GH_Point_CreateFromSurfaceParam.htm "CreateFromSurfaceParam Method ")

[DrawViewportMeshes Method](../html/M_Grasshopper_Kernel_Types_GH_Point_DrawViewportMeshes.htm "DrawViewportMeshes Method ")

[DrawViewportWires Method](../html/M_Grasshopper_Kernel_Types_GH_Point_DrawViewportWires.htm "DrawViewportWires Method ")

[Duplicate Method](../html/M_Grasshopper_Kernel_Types_GH_Point_Duplicate.htm "Duplicate Method ")

[DuplicateGeometry Method](../html/M_Grasshopper_Kernel_Types_GH_Point_DuplicateGeometry.htm "DuplicateGeometry Method ")

[DuplicatePoint Method](../html/M_Grasshopper_Kernel_Types_GH_Point_DuplicatePoint.htm "DuplicatePoint Method ")

[EmitProxy Method](../html/M_Grasshopper_Kernel_Types_GH_Point_EmitProxy.htm "EmitProxy Method ")

[EnsureReferenceData Method](../html/M_Grasshopper_Kernel_Types_GH_Point_EnsureReferenceData.htm "EnsureReferenceData Method ")

[GetBoundingBox Method](../html/M_Grasshopper_Kernel_Types_GH_Point_GetBoundingBox.htm "GetBoundingBox Method ")

[LoadGeometry Method](../html/Overload_Grasshopper_Kernel_Types_GH_Point_LoadGeometry.htm "LoadGeometry Method ")

[Morph Method](../html/M_Grasshopper_Kernel_Types_GH_Point_Morph.htm "Morph Method ")

[Read Method](../html/M_Grasshopper_Kernel_Types_GH_Point_Read.htm "Read Method ")

[ReferenceCurve Method](../html/Overload_Grasshopper_Kernel_Types_GH_Point_ReferenceCurve.htm "ReferenceCurve Method ")

[ReferenceIndex Method](../html/Overload_Grasshopper_Kernel_Types_GH_Point_ReferenceIndex.htm "ReferenceIndex Method ")

[ReferenceParam Method](../html/Overload_Grasshopper_Kernel_Types_GH_Point_ReferenceParam.htm "ReferenceParam Method ")

[ReferencesCurve Method](../html/M_Grasshopper_Kernel_Types_GH_Point_ReferencesCurve.htm "ReferencesCurve Method ")

[ReferencesEdge Method](../html/M_Grasshopper_Kernel_Types_GH_Point_ReferencesEdge.htm "ReferencesEdge Method ")

[ReferenceSurface Method](../html/M_Grasshopper_Kernel_Types_GH_Point_ReferenceSurface.htm "ReferenceSurface Method ")

[ReferenceType Method](../html/Overload_Grasshopper_Kernel_Types_GH_Point_ReferenceType.htm "ReferenceType Method ")

[ScriptVariable Method](../html/M_Grasshopper_Kernel_Types_GH_Point_ScriptVariable.htm "ScriptVariable Method ")

[SetReferenceParams Method](../html/M_Grasshopper_Kernel_Types_GH_Point_SetReferenceParams.htm "SetReferenceParams Method ")

[ShowReferenceDialog Method](../html/Overload_Grasshopper_Kernel_Types_GH_Point_ShowReferenceDialog.htm "ShowReferenceDialog Method ")

[ToString Method](../html/M_Grasshopper_Kernel_Types_GH_Point_ToString.htm "ToString Method ")

[Transform Method](../html/M_Grasshopper_Kernel_Types_GH_Point_Transform.htm "Transform Method ")

[Write Method](../html/M_Grasshopper_Kernel_Types_GH_Point_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PointAddLanguageSpecificTextSet("LST2E6810A4\_0?cpp=::|nu=.");CreateFromEdgeDistance Method |

Create new point geometry instance based on a curve distance parameter

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void CreateFromEdgeDistance(
	Guid brp_id,
	Curve edge,
	int e_index,
	double t,
	bool bFromStart
)
```

```
Public Sub CreateFromEdgeDistance ( 
	brp_id As Guid,
	edge As Curve,
	e_index As Integer,
	t As Double,
	bFromStart As Boolean
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

brp\_id
:   Type: [SystemAddLanguageSpecificTextSet("LST2E6810A4\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    ID of the curve this object references

edge
:   Type: Curve  
    The edge curve

e\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST2E6810A4\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of edge to reference

t
:   Type: [SystemAddLanguageSpecificTextSet("LST2E6810A4\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Parameter along the curve in curve domain space

bFromStart
:   Type: [SystemAddLanguageSpecificTextSet("LST2E6810A4\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    True if the distance is to be measured from the start of the curve

![](../icons/SectionExpanded.png)Remarks

This 'constructor' merely sets fields, it doesn't load the geometry and it doesn't perform validity checking.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Point Class](T_Grasshopper_Kernel_Types_GH_Point.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)