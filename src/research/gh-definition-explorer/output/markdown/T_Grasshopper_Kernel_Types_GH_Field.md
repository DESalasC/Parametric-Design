# T_Grasshopper_Kernel_Types_GH_Field

﻿ GH\_Field Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Field Class](../html/T_Grasshopper_Kernel_Types_GH_Field.htm "GH_Field Class")

[GH\_Field Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Field__ctor.htm "GH_Field Constructor ")

[GH\_Field Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Field.htm "GH_Field Properties")

[GH\_Field Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Field.htm "GH_Field Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Field Class |

Represents a field of forces.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST36F9D458\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST36F9D458\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Field

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Field : IGH_Goo, IGH_PreviewData
```

```
Public Class GH_Field
	Implements IGH_Goo, IGH_PreviewData
```

AddLanguageTabSet("ID1EBCA");

The GH\_Field type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_FieldAddLanguageSpecificTextSet("LST36F9D458\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Field__ctor.htm) | Blank constructor. |
| Public method | [GH\_Field(GH\_Field)](M_Grasshopper_Kernel_Types_GH_Field__ctor_1.htm) | Copy constructor. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_Field_ClippingBox.htm) |  |
| Public property | [Elements](P_Grasshopper_Kernel_Types_GH_Field_Elements.htm) | Gets the list of elements of this field. |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Field_IsValid.htm) |  |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Field_IsValidWhyNot.htm) |  |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Field_TypeDescription.htm) |  |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Field_TypeName.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Field_CastFrom.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LST36F9D458\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST36F9D458\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_Types_GH_Field_CastTo__1.htm) |  |
| Public method | [CurvatureAt](M_Grasshopper_Kernel_Types_GH_Field_CurvatureAt.htm) |  |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_Field_DrawViewportMeshes.htm) |  |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_Field_DrawViewportWires.htm) |  |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_Field_Duplicate.htm) |  |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Field_EmitProxy.htm) |  |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Field_Read.htm) |  |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Field_ScriptVariable.htm) |  |
| Public method | [SolveStep](M_Grasshopper_Kernel_Types_GH_Field_SolveStep.htm) | Move a point through the field. |
| Public method | [SolveSteps](M_Grasshopper_Kernel_Types_GH_Field_SolveSteps.htm) | Move a point through a succession of steps. |
| Public method | [TensorAt](M_Grasshopper_Kernel_Types_GH_Field_TensorAt.htm) | Compute the field tensor at the given location as contributed by all the field elements. |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Field_ToString.htm) |  |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Field_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)