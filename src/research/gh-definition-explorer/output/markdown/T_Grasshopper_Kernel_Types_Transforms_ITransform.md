# T_Grasshopper_Kernel_Types_Transforms_ITransform

﻿ ITransform Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types.Transforms](../html/N_Grasshopper_Kernel_Types_Transforms.htm "Grasshopper.Kernel.Types.Transforms")

[ITransform Interface](../html/T_Grasshopper_Kernel_Types_Transforms_ITransform.htm "ITransform Interface")

[ITransform Properties](../html/Properties_T_Grasshopper_Kernel_Types_Transforms_ITransform.htm "ITransform Properties")

[ITransform Methods](../html/Methods_T_Grasshopper_Kernel_Types_Transforms_ITransform.htm "ITransform Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ITransform Interface |

Basic interface for a single Grasshopper transformation.

**Namespace:**
 [Grasshopper.Kernel.Types.Transforms](N_Grasshopper_Kernel_Types_Transforms.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface ITransform : GH_ISerializable
```

```
Public Interface ITransform
	Inherits GH_ISerializable
```

AddLanguageTabSet("ID0EBCA");

The ITransform type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Name](P_Grasshopper_Kernel_Types_Transforms_ITransform_Name.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_Transforms_ITransform_Duplicate.htm) |  |
| Public method | [Read](M_GH_IO_GH_ISerializable_Read.htm) | This method is called whenever the instance is required to deserialize itself. (Inherited from [GH\_ISerializable](T_GH_IO_GH_ISerializable.htm).) |
| Public method | [Reverse](M_Grasshopper_Kernel_Types_Transforms_ITransform_Reverse.htm) |  |
| Public method | [ToMatrix](M_Grasshopper_Kernel_Types_Transforms_ITransform_ToMatrix.htm) |  |
| Public method | [ToString](M_Grasshopper_Kernel_Types_Transforms_ITransform_ToString.htm) |  |
| Public method | [Write](M_GH_IO_GH_ISerializable_Write.htm) | This method is called whenever the instance is required to serialize itself. (Inherited from [GH\_ISerializable](T_GH_IO_GH_ISerializable.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types.Transforms Namespace](N_Grasshopper_Kernel_Types_Transforms.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)