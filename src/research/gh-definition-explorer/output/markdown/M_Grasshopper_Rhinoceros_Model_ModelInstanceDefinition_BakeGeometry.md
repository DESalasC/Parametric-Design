# M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_BakeGeometry

﻿ ModelInstanceDefinition.BakeGeometry Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Model](../html/N_Grasshopper_Rhinoceros_Model.htm "Grasshopper.Rhinoceros.Model")

[ModelInstanceDefinition Class](../html/T_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition.htm "ModelInstanceDefinition Class")

[ModelInstanceDefinition Methods](../html/Methods_T_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition.htm "ModelInstanceDefinition Methods")

[BakeGeometry Method](../html/M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_BakeGeometry.htm "BakeGeometry Method ")

[Cast Method](../html/M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_Cast.htm "Cast Method ")

[CastTo Method](../html/Overload_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_CastTo.htm "CastTo Method ")

[GetBoundingBox Method](../html/M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_GetBoundingBox.htm "GetBoundingBox Method ")

[ToAttributes Method](../html/M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_ToAttributes.htm "ToAttributes Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelInstanceDefinitionAddLanguageSpecificTextSet("LST3679A697\_0?cpp=::|nu=.");BakeGeometry Method |

**Namespace:**
 [Grasshopper.Rhinoceros.Model](N_Grasshopper_Rhinoceros_Model.htm)  
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
:   Type: [SystemAddLanguageSpecificTextSet("LST3679A697\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)AddLanguageSpecificTextSet("LST3679A697\_2?cpp=%");

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

#### Implements

[IGH\_BakeAwareDataAddLanguageSpecificTextSet("LST3679A697\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");BakeGeometry(RhinoDoc, ObjectAttributes, GuidAddLanguageSpecificTextSet("LST3679A697\_4?cpp=%");)](M_Grasshopper_Kernel_IGH_BakeAwareData_BakeGeometry.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[ModelInstanceDefinition Class](T_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition.htm)

[Grasshopper.Rhinoceros.Model Namespace](N_Grasshopper_Rhinoceros_Model.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)