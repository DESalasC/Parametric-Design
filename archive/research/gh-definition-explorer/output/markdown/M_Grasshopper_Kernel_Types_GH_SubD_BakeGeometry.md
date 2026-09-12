# M_Grasshopper_Kernel_Types_GH_SubD_BakeGeometry

﻿ GH\_SubD.BakeGeometry Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_SubD Class](../html/T_Grasshopper_Kernel_Types_GH_SubD.htm "GH_SubD Class")

[GH\_SubD Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_SubD.htm "GH_SubD Methods")

[AppendRenderGeometry Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_AppendRenderGeometry.htm "AppendRenderGeometry Method ")

[BakeGeometry Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_BakeGeometry.htm "BakeGeometry Method ")

[CastFrom Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_CastFrom.htm "CastFrom Method ")

[CastTo Method](../html/Overload_Grasshopper_Kernel_Types_GH_SubD_CastTo.htm "CastTo Method ")

[ClearCaches Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_ClearCaches.htm "ClearCaches Method ")

[DestroyPreviewMeshes Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_DestroyPreviewMeshes.htm "DestroyPreviewMeshes Method ")

[DrawViewportMeshes Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_DrawViewportMeshes.htm "DrawViewportMeshes Method ")

[DrawViewportWires Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_DrawViewportWires.htm "DrawViewportWires Method ")

[Duplicate Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_Duplicate.htm "Duplicate Method ")

[DuplicateGeometry Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_DuplicateGeometry.htm "DuplicateGeometry Method ")

[DuplicateSubD Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_DuplicateSubD.htm "DuplicateSubD Method ")

[EmitProxy Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_EmitProxy.htm "EmitProxy Method ")

[GetBoundingBox Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_GetBoundingBox.htm "GetBoundingBox Method ")

[GetPreviewMeshes Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_GetPreviewMeshes.htm "GetPreviewMeshes Method ")

[LoadGeometry Method](../html/Overload_Grasshopper_Kernel_Types_GH_SubD_LoadGeometry.htm "LoadGeometry Method ")

[Morph Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_Morph.htm "Morph Method ")

[Read Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_Read.htm "Read Method ")

[ScriptVariable Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_ScriptVariable.htm "ScriptVariable Method ")

[ToString Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_ToString.htm "ToString Method ")

[Transform Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_Transform.htm "Transform Method ")

[Write Method](../html/M_Grasshopper_Kernel_Types_GH_SubD_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SubDAddLanguageSpecificTextSet("LST77E56013\_0?cpp=::|nu=.");BakeGeometry Method |

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
:   Type: [SystemAddLanguageSpecificTextSet("LST77E56013\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)AddLanguageSpecificTextSet("LST77E56013\_2?cpp=%");

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

#### Implements

[IGH\_BakeAwareDataAddLanguageSpecificTextSet("LST77E56013\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");BakeGeometry(RhinoDoc, ObjectAttributes, GuidAddLanguageSpecificTextSet("LST77E56013\_4?cpp=%");)](M_Grasshopper_Kernel_IGH_BakeAwareData_BakeGeometry.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_SubD Class](T_Grasshopper_Kernel_Types_GH_SubD.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)