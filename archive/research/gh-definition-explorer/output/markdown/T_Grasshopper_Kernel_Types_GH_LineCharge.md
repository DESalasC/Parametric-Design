# T_Grasshopper_Kernel_Types_GH_LineCharge

﻿ GH\_LineCharge Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_LineCharge Class](../html/T_Grasshopper_Kernel_Types_GH_LineCharge.htm "GH_LineCharge Class")

[GH\_LineCharge Constructor](../html/M_Grasshopper_Kernel_Types_GH_LineCharge__ctor.htm "GH_LineCharge Constructor ")

[GH\_LineCharge Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_LineCharge.htm "GH_LineCharge Properties")

[GH\_LineCharge Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_LineCharge.htm "GH_LineCharge Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_LineCharge Class |

Line charge implementation for IGH\_Fields.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTF21D391C\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTF21D391C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm)  
    Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTF21D391C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_LineCharge

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_LineCharge : GH_FieldElement
```

```
Public Class GH_LineCharge
	Inherits GH_FieldElement
```

AddLanguageTabSet("ID1EBCA");

The GH\_LineCharge type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_LineCharge](M_Grasshopper_Kernel_Types_GH_LineCharge__ctor.htm) | Initializes a new instance of the GH\_LineCharge class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BoundingBox](P_Grasshopper_Kernel_Types_GH_LineCharge_BoundingBox.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LSTF21D391C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");BoundingBox](P_Grasshopper_Kernel_Types_GH_FieldElement_BoundingBox.htm).) |
| Public property | [Charge](P_Grasshopper_Kernel_Types_GH_LineCharge_Charge.htm) |  |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_FieldElement_ClippingBox.htm) | (Inherited from [GH\_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).) |
| Public property | [ElementGuid](P_Grasshopper_Kernel_Types_GH_LineCharge_ElementGuid.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LSTF21D391C\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ElementGuid](P_Grasshopper_Kernel_Types_GH_FieldElement_ElementGuid.htm).) |
| Public property | [IsLimited](P_Grasshopper_Kernel_Types_GH_FieldElement_IsLimited.htm) | (Inherited from [GH\_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).) |
| Public property | [Limits](P_Grasshopper_Kernel_Types_GH_FieldElement_Limits.htm) | (Inherited from [GH\_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).) |
| Public property | [Segment](P_Grasshopper_Kernel_Types_GH_LineCharge_Segment.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_FieldElement_DrawViewportMeshes.htm) | (Inherited from [GH\_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).) |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_LineCharge_DrawViewportWires.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LSTF21D391C\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");DrawViewportWires(GH\_PreviewWireArgs)](M_Grasshopper_Kernel_Types_GH_FieldElement_DrawViewportWires.htm).) |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_LineCharge_Duplicate.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LSTF21D391C\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LSTF21D391C\_7?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_FieldElement_Duplicate.htm).) |
| Public method | [Force](M_Grasshopper_Kernel_Types_GH_LineCharge_Force.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LSTF21D391C\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");Force(Point3d)](M_Grasshopper_Kernel_Types_GH_FieldElement_Force.htm).) |
| Public method | [IsCoincident](M_Grasshopper_Kernel_Types_GH_LineCharge_IsCoincident.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LSTF21D391C\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");IsCoincident(Point3d, Double)](M_Grasshopper_Kernel_Types_GH_FieldElement_IsCoincident.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_LineCharge_Read.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LSTF21D391C\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_FieldElement_Read.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_LineCharge_Write.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LSTF21D391C\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_FieldElement_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)