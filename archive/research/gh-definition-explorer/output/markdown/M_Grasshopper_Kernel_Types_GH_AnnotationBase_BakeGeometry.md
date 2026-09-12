# M_Grasshopper_Kernel_Types_GH_AnnotationBase_BakeGeometry

﻿ GH\_AnnotationBase.BakeGeometry Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_AnnotationBase Class](../html/T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm "GH_AnnotationBase Class")

[GH\_AnnotationBase Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm "GH_AnnotationBase Methods")

[BakeGeometry Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_BakeGeometry.htm "BakeGeometry Method ")

[CastTo Method](../html/Overload_Grasshopper_Kernel_Types_GH_AnnotationBase_CastTo.htm "CastTo Method ")

[ClearCaches Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_ClearCaches.htm "ClearCaches Method ")

[DrawViewportMeshes Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_DrawViewportMeshes.htm "DrawViewportMeshes Method ")

[DrawViewportWires Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_DrawViewportWires.htm "DrawViewportWires Method ")

[Duplicate Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_Duplicate.htm "Duplicate Method ")

[DuplicateAnnotation Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_DuplicateAnnotation.htm "DuplicateAnnotation Method ")

[DuplicateGeometry Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_DuplicateGeometry.htm "DuplicateGeometry Method ")

[EmitProxy Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_EmitProxy.htm "EmitProxy Method ")

[GetBoundingBox Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_GetBoundingBox.htm "GetBoundingBox Method ")

[LoadGeometry Method](../html/Overload_Grasshopper_Kernel_Types_GH_AnnotationBase_LoadGeometry.htm "LoadGeometry Method ")

[Morph Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_Morph.htm "Morph Method ")

[Read Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_Read.htm "Read Method ")

[ScriptVariable Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_ScriptVariable.htm "ScriptVariable Method ")

[ToString Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_ToString.htm "ToString Method ")

[Transform Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_Transform.htm "Transform Method ")

[Write Method](../html/M_Grasshopper_Kernel_Types_GH_AnnotationBase_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AnnotationBaseAddLanguageSpecificTextSet("LST3265AF61\_0?cpp=::|nu=.");BakeGeometry Method |

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool BakeGeometry(
	RhinoDoc doc,
	ObjectAttributes att,
	ref Guid obj_guid
)
```

```
Public Function BakeGeometry ( 
	doc As RhinoDoc,
	att As ObjectAttributes,
	ByRef obj_guid As Guid
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

doc
:   Type: RhinoDoc

att
:   Type: ObjectAttributes

obj\_guid
:   Type: [SystemAddLanguageSpecificTextSet("LST3265AF61\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)AddLanguageSpecificTextSet("LST3265AF61\_2?cpp=%");

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

#### Implements

[IGH\_BakeAwareDataAddLanguageSpecificTextSet("LST3265AF61\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");BakeGeometry(RhinoDoc, ObjectAttributes, GuidAddLanguageSpecificTextSet("LST3265AF61\_4?cpp=%");)](M_Grasshopper_Kernel_IGH_BakeAwareData_BakeGeometry.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_AnnotationBase Class](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)