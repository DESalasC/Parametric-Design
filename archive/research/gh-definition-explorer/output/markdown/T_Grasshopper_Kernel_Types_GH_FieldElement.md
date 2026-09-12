# T_Grasshopper_Kernel_Types_GH_FieldElement

﻿ GH\_FieldElement Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_FieldElement Class](../html/T_Grasshopper_Kernel_Types_GH_FieldElement.htm "GH_FieldElement Class")

[GH\_FieldElement Constructor](../html/M_Grasshopper_Kernel_Types_GH_FieldElement__ctor.htm "GH_FieldElement Constructor ")

[GH\_FieldElement Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_FieldElement.htm "GH_FieldElement Properties")

[GH\_FieldElement Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_FieldElement.htm "GH_FieldElement Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FieldElement Class |

Abstract implementation of IGH\_FieldElement, derive from this class
rather than implementing IGH\_FieldElement to save yourself time and effort.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST368ED671\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST368ED671\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FieldElement  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST368ED671\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_LineCharge](T_Grasshopper_Kernel_Types_GH_LineCharge.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST368ED671\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PointCharge](T_Grasshopper_Kernel_Types_GH_PointCharge.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST368ED671\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SpinForce](T_Grasshopper_Kernel_Types_GH_SpinForce.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST368ED671\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_VectorForce](T_Grasshopper_Kernel_Types_GH_VectorForce.htm)

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_FieldElement : IGH_FieldElement
```

```
Public MustInherit Class GH_FieldElement
	Implements IGH_FieldElement
```

AddLanguageTabSet("ID1EBCA");

The GH\_FieldElement type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_FieldElement](M_Grasshopper_Kernel_Types_GH_FieldElement__ctor.htm) | Initializes a new instance of the GH\_FieldElement class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BoundingBox](P_Grasshopper_Kernel_Types_GH_FieldElement_BoundingBox.htm) |  |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_FieldElement_ClippingBox.htm) |  |
| Public property | [ElementGuid](P_Grasshopper_Kernel_Types_GH_FieldElement_ElementGuid.htm) |  |
| Public property | [IsLimited](P_Grasshopper_Kernel_Types_GH_FieldElement_IsLimited.htm) |  |
| Public property | [Limits](P_Grasshopper_Kernel_Types_GH_FieldElement_Limits.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_FieldElement_DrawViewportMeshes.htm) |  |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_FieldElement_DrawViewportWires.htm) |  |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_FieldElement_Duplicate.htm) |  |
| Public method | [Force](M_Grasshopper_Kernel_Types_GH_FieldElement_Force.htm) |  |
| Public method | [IsCoincident](M_Grasshopper_Kernel_Types_GH_FieldElement_IsCoincident.htm) |  |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_FieldElement_Read.htm) |  |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_FieldElement_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)