# T_Grasshopper_Kernel_Types_GH_PointCharge

﻿ GH\_PointCharge Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_PointCharge Class](../html/T_Grasshopper_Kernel_Types_GH_PointCharge.htm "GH_PointCharge Class")

[GH\_PointCharge Constructor](../html/M_Grasshopper_Kernel_Types_GH_PointCharge__ctor.htm "GH_PointCharge Constructor ")

[GH\_PointCharge Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_PointCharge.htm "GH_PointCharge Properties")

[GH\_PointCharge Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_PointCharge.htm "GH_PointCharge Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PointCharge Class |

Point charge implementation for IGH\_Fields.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST6043F93F\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST6043F93F\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm)  
    Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST6043F93F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PointCharge

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_PointCharge : GH_FieldElement
```

```
Public Class GH_PointCharge
	Inherits GH_FieldElement
```

AddLanguageTabSet("ID1EBCA");

The GH\_PointCharge type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_PointCharge](M_Grasshopper_Kernel_Types_GH_PointCharge__ctor.htm) | Initializes a new instance of the GH\_PointCharge class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BoundingBox](P_Grasshopper_Kernel_Types_GH_PointCharge_BoundingBox.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LST6043F93F\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");BoundingBox](P_Grasshopper_Kernel_Types_GH_FieldElement_BoundingBox.htm).) |
| Public property | [Charge](P_Grasshopper_Kernel_Types_GH_PointCharge_Charge.htm) |  |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_FieldElement_ClippingBox.htm) | (Inherited from [GH\_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).) |
| Public property | [Decay](P_Grasshopper_Kernel_Types_GH_PointCharge_Decay.htm) |  |
| Public property | [ElementGuid](P_Grasshopper_Kernel_Types_GH_PointCharge_ElementGuid.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LST6043F93F\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ElementGuid](P_Grasshopper_Kernel_Types_GH_FieldElement_ElementGuid.htm).) |
| Public property | [IsLimited](P_Grasshopper_Kernel_Types_GH_FieldElement_IsLimited.htm) | (Inherited from [GH\_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).) |
| Public property | [Limits](P_Grasshopper_Kernel_Types_GH_FieldElement_Limits.htm) | (Inherited from [GH\_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).) |
| Public property | [Location](P_Grasshopper_Kernel_Types_GH_PointCharge_Location.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_FieldElement_DrawViewportMeshes.htm) | (Inherited from [GH\_FieldElement](T_Grasshopper_Kernel_Types_GH_FieldElement.htm).) |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_PointCharge_DrawViewportWires.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LST6043F93F\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");DrawViewportWires(GH\_PreviewWireArgs)](M_Grasshopper_Kernel_Types_GH_FieldElement_DrawViewportWires.htm).) |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_PointCharge_Duplicate.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LST6043F93F\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST6043F93F\_7?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_FieldElement_Duplicate.htm).) |
| Public method | [Force](M_Grasshopper_Kernel_Types_GH_PointCharge_Force.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LST6043F93F\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");Force(Point3d)](M_Grasshopper_Kernel_Types_GH_FieldElement_Force.htm).) |
| Public method | [IsCoincident](M_Grasshopper_Kernel_Types_GH_PointCharge_IsCoincident.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LST6043F93F\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");IsCoincident(Point3d, Double)](M_Grasshopper_Kernel_Types_GH_FieldElement_IsCoincident.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_PointCharge_Read.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LST6043F93F\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_FieldElement_Read.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_PointCharge_Write.htm) | (Overrides [GH\_FieldElementAddLanguageSpecificTextSet("LST6043F93F\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_FieldElement_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)