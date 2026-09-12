# M_Grasshopper_Kernel_Types_GH_Line_BakeGeometry

﻿ GH\_Line.BakeGeometry Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Line Class](../html/T_Grasshopper_Kernel_Types_GH_Line.htm "GH_Line Class")

[GH\_Line Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Line.htm "GH_Line Methods")

[BakeGeometry Method](../html/M_Grasshopper_Kernel_Types_GH_Line_BakeGeometry.htm "BakeGeometry Method ")

[CastFrom Method](../html/M_Grasshopper_Kernel_Types_GH_Line_CastFrom.htm "CastFrom Method ")

[CastTo Method](../html/Overload_Grasshopper_Kernel_Types_GH_Line_CastTo.htm "CastTo Method ")

[DrawViewportMeshes Method](../html/M_Grasshopper_Kernel_Types_GH_Line_DrawViewportMeshes.htm "DrawViewportMeshes Method ")

[DrawViewportWires Method](../html/M_Grasshopper_Kernel_Types_GH_Line_DrawViewportWires.htm "DrawViewportWires Method ")

[Duplicate Method](../html/M_Grasshopper_Kernel_Types_GH_Line_Duplicate.htm "Duplicate Method ")

[DuplicateGeometry Method](../html/M_Grasshopper_Kernel_Types_GH_Line_DuplicateGeometry.htm "DuplicateGeometry Method ")

[DuplicateLine Method](../html/M_Grasshopper_Kernel_Types_GH_Line_DuplicateLine.htm "DuplicateLine Method ")

[EmitProxy Method](../html/M_Grasshopper_Kernel_Types_GH_Line_EmitProxy.htm "EmitProxy Method ")

[GetBoundingBox Method](../html/M_Grasshopper_Kernel_Types_GH_Line_GetBoundingBox.htm "GetBoundingBox Method ")

[Morph Method](../html/M_Grasshopper_Kernel_Types_GH_Line_Morph.htm "Morph Method ")

[Read Method](../html/M_Grasshopper_Kernel_Types_GH_Line_Read.htm "Read Method ")

[ToString Method](../html/M_Grasshopper_Kernel_Types_GH_Line_ToString.htm "ToString Method ")

[Transform Method](../html/M_Grasshopper_Kernel_Types_GH_Line_Transform.htm "Transform Method ")

[Write Method](../html/M_Grasshopper_Kernel_Types_GH_Line_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_LineAddLanguageSpecificTextSet("LSTBD0B5AC5\_0?cpp=::|nu=.");BakeGeometry Method |

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
:   Type: [SystemAddLanguageSpecificTextSet("LSTBD0B5AC5\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)AddLanguageSpecificTextSet("LSTBD0B5AC5\_2?cpp=%");

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

#### Implements

[IGH\_BakeAwareDataAddLanguageSpecificTextSet("LSTBD0B5AC5\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");BakeGeometry(RhinoDoc, ObjectAttributes, GuidAddLanguageSpecificTextSet("LSTBD0B5AC5\_4?cpp=%");)](M_Grasshopper_Kernel_IGH_BakeAwareData_BakeGeometry.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Line Class](T_Grasshopper_Kernel_Types_GH_Line.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)