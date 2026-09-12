# T_Grasshopper_Kernel_Types_IGH_FieldElement

﻿ IGH\_FieldElement Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[IGH\_FieldElement Interface](../html/T_Grasshopper_Kernel_Types_IGH_FieldElement.htm "IGH_FieldElement Interface")

[IGH\_FieldElement Properties](../html/Properties_T_Grasshopper_Kernel_Types_IGH_FieldElement.htm "IGH_FieldElement Properties")

[IGH\_FieldElement Methods](../html/Methods_T_Grasshopper_Kernel_Types_IGH_FieldElement.htm "IGH_FieldElement Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_FieldElement Interface |

Represents the basic interface for field elements.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_FieldElement : GH_ISerializable, 
	IGH_PreviewData
```

```
Public Interface IGH_FieldElement
	Inherits GH_ISerializable, IGH_PreviewData
```

AddLanguageTabSet("ID0EBCA");

The IGH\_FieldElement type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BoundingBox](P_Grasshopper_Kernel_Types_IGH_FieldElement_BoundingBox.htm) | Gets the visual boundingbox of all the geometry used to represent this element in 3D. |
| Public property | [ClippingBox](P_Grasshopper_Kernel_IGH_PreviewData_ClippingBox.htm) | Gets the clipping box for this data. The clipping box is typically the same as the boundingbox. (Inherited from [IGH\_PreviewData](T_Grasshopper_Kernel_IGH_PreviewData.htm).) |
| Public property | [ElementGuid](P_Grasshopper_Kernel_Types_IGH_FieldElement_ElementGuid.htm) | Gets the element Guid for this element. |
| Public property | [IsLimited](P_Grasshopper_Kernel_Types_IGH_FieldElement_IsLimited.htm) | Gets or sets whether this element affects a limited region. |
| Public property | [Limits](P_Grasshopper_Kernel_Types_IGH_FieldElement_Limits.htm) | Gets or sets the limits of this region. Unless IsLimited equals true, the Limits property is ignored. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_IGH_PreviewData_DrawViewportMeshes.htm) | Implement this function to draw all shaded meshes. If the viewport does not support shading, this function will not be called. (Inherited from [IGH\_PreviewData](T_Grasshopper_Kernel_IGH_PreviewData.htm).) |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_IGH_PreviewData_DrawViewportWires.htm) | Implement this function to draw all wire and point previews. (Inherited from [IGH\_PreviewData](T_Grasshopper_Kernel_IGH_PreviewData.htm).) |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_IGH_FieldElement_Duplicate.htm) | Create an exact copy of this element. |
| Public method | [Force](M_Grasshopper_Kernel_Types_IGH_FieldElement_Force.htm) | Compute the force at a given location. |
| Public method | [IsCoincident](M_Grasshopper_Kernel_Types_IGH_FieldElement_IsCoincident.htm) | Computes whether the point can be considered coincident with the element. |
| Public method | [Read](M_GH_IO_GH_ISerializable_Read.htm) | This method is called whenever the instance is required to deserialize itself. (Inherited from [GH\_ISerializable](T_GH_IO_GH_ISerializable.htm).) |
| Public method | [Write](M_GH_IO_GH_ISerializable_Write.htm) | This method is called whenever the instance is required to serialize itself. (Inherited from [GH\_ISerializable](T_GH_IO_GH_ISerializable.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)