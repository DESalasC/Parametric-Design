# T_Grasshopper_Kernel_Types_GH_Point

﻿ GH\_Point Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Point Class](../html/T_Grasshopper_Kernel_Types_GH_Point.htm "GH_Point Class")

[GH\_Point Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Point__ctor.htm "GH_Point Constructor ")

[GH\_Point Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Point.htm "GH_Point Properties")

[GH\_Point Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Point.htm "GH_Point Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Point Class |

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST60E05932\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST60E05932\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Point

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Point : IGH_GeometricGoo, IGH_BakeAwareData, 
	IGH_PreviewData
```

```
Public Class GH_Point
	Implements IGH_GeometricGoo, IGH_BakeAwareData, IGH_PreviewData
```

AddLanguageTabSet("ID1EBCA");

The GH\_Point type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_PointAddLanguageSpecificTextSet("LST60E05932\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Point__ctor.htm) | Initializes a new instance of the GH\_Point class |
| Public method | [GH\_Point(GH\_Point)](M_Grasshopper_Kernel_Types_GH_Point__ctor_1.htm) | Initializes a new instance of the GH\_Point class |
| Public method | [GH\_Point(Guid)](M_Grasshopper_Kernel_Types_GH_Point__ctor_3.htm) | Initializes a new instance of the GH\_Point class |
| Public method | [GH\_Point(Point3d)](M_Grasshopper_Kernel_Types_GH_Point__ctor_2.htm) | Initializes a new instance of the GH\_Point class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundingbox](P_Grasshopper_Kernel_Types_GH_Point_Boundingbox.htm) |  |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_Point_ClippingBox.htm) |  |
| Public property | [IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_Point_IsGeometryLoaded.htm) |  |
| Public property | [IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_Point_IsReferencedGeometry.htm) |  |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Point_IsValid.htm) |  |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Point_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. |
| Public property | [ReferenceData](P_Grasshopper_Kernel_Types_GH_Point_ReferenceData.htm) | Gets or sets the reference data of this point geometry. |
| Public property | [ReferenceID](P_Grasshopper_Kernel_Types_GH_Point_ReferenceID.htm) |  |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Point_TypeDescription.htm) |  |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Point_TypeName.htm) |  |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Point_Value.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry](M_Grasshopper_Kernel_Types_GH_Point_BakeGeometry.htm) |  |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Point_CastFrom.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LST60E05932\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST60E05932\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_Types_GH_Point_CastTo__1.htm) |  |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_Point_ClearCaches.htm) |  |
| Public method | [CreateFromCoordinate](M_Grasshopper_Kernel_Types_GH_Point_CreateFromCoordinate.htm) | Create a new point geometry instance based on a fixed coordinate |
| Public method | [CreateFromCurveDistance](M_Grasshopper_Kernel_Types_GH_Point_CreateFromCurveDistance.htm) | Create new point geometry instance based on a curve distance parameter |
| Public method | [CreateFromCurveRatio](M_Grasshopper_Kernel_Types_GH_Point_CreateFromCurveRatio.htm) | Create new point geometry instance based on a curve parameter ratio |
| Public method | [CreateFromEdgeDistance](M_Grasshopper_Kernel_Types_GH_Point_CreateFromEdgeDistance.htm) | Create new point geometry instance based on a curve distance parameter |
| Public method | [CreateFromEdgeRatio](M_Grasshopper_Kernel_Types_GH_Point_CreateFromEdgeRatio.htm) | Create new point geometry instance based on an edge parameter ratio |
| Public method | [CreateFromPointObject](M_Grasshopper_Kernel_Types_GH_Point_CreateFromPointObject.htm) | Create a new point geometry instance based on point object ID. Technically this now also accepts Dot object IDs. |
| Public method | [CreateFromSurfaceParam](M_Grasshopper_Kernel_Types_GH_Point_CreateFromSurfaceParam.htm) | Create new point geometry instance based on a curve distance parameter |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_Point_DrawViewportMeshes.htm) |  |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_Point_DrawViewportWires.htm) |  |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_Point_Duplicate.htm) |  |
| Public method | [DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_Point_DuplicateGeometry.htm) |  |
| Public method | [DuplicatePoint](M_Grasshopper_Kernel_Types_GH_Point_DuplicatePoint.htm) |  |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Point_EmitProxy.htm) |  |
| Public method | [EnsureReferenceData](M_Grasshopper_Kernel_Types_GH_Point_EnsureReferenceData.htm) | Creates new Reference data if it doesn't already exists |
| Public method | [GetBoundingBox](M_Grasshopper_Kernel_Types_GH_Point_GetBoundingBox.htm) |  |
| Public method | [LoadGeometryAddLanguageSpecificTextSet("LST60E05932\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Point_LoadGeometry.htm) |  |
| Public method | [LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_Point_LoadGeometry_1.htm) |  |
| Public method | [Morph](M_Grasshopper_Kernel_Types_GH_Point_Morph.htm) |  |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Point_Read.htm) |  |
| Public method | [ReferenceCurveAddLanguageSpecificTextSet("LST60E05932\_6?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Point_ReferenceCurve.htm) |  |
| Public method | [ReferenceCurve(RhinoObject)](M_Grasshopper_Kernel_Types_GH_Point_ReferenceCurve_1.htm) |  |
| Public method | [ReferenceIndexAddLanguageSpecificTextSet("LST60E05932\_7?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Point_ReferenceIndex.htm) | Retrieve the index of the point reference data. |
| Public method | [ReferenceIndex(Int32)](M_Grasshopper_Kernel_Types_GH_Point_ReferenceIndex_1.htm) | Sets the index of the point reference data. |
| Public method | [ReferenceParam(Int32)](M_Grasshopper_Kernel_Types_GH_Point_ReferenceParam.htm) | Retrieve the indexed param of the point reference data. |
| Public method | [ReferenceParam(Int32, Double)](M_Grasshopper_Kernel_Types_GH_Point_ReferenceParam_1.htm) | Sets the index of the point reference data. |
| Public method | [ReferencesCurve](M_Grasshopper_Kernel_Types_GH_Point_ReferencesCurve.htm) | Returns true if this point is based on a curve reference |
| Public method | [ReferencesEdge](M_Grasshopper_Kernel_Types_GH_Point_ReferencesEdge.htm) | Returns True if this point is based on an edge reference |
| Public method | [ReferenceSurface](M_Grasshopper_Kernel_Types_GH_Point_ReferenceSurface.htm) |  |
| Public method | [ReferenceTypeAddLanguageSpecificTextSet("LST60E05932\_8?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Point_ReferenceType.htm) | Retrieve the reference type of this point object. |
| Public method | [ReferenceType(GH\_PointRefType)](M_Grasshopper_Kernel_Types_GH_Point_ReferenceType_1.htm) | Sets the type of the point reference data. |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Point_ScriptVariable.htm) |  |
| Public method | [SetReferenceParams](M_Grasshopper_Kernel_Types_GH_Point_SetReferenceParams.htm) | Sets both param values of the point reference |
| Public method | [ShowReferenceDialogAddLanguageSpecificTextSet("LST60E05932\_9?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Point_ShowReferenceDialog.htm) |  |
| Public method | [ShowReferenceDialog(IWin32Window)](M_Grasshopper_Kernel_Types_GH_Point_ShowReferenceDialog_1.htm) |  |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Point_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST60E05932\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST60E05932\_11?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |
| Public method | [Transform](M_Grasshopper_Kernel_Types_GH_Point_Transform.htm) |  |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Point_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)