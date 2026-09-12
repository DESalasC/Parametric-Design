# Properties_T_Grasshopper_Kernel_IGH_Attributes

﻿ IGH\_Attributes Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_Attributes Interface](../html/T_Grasshopper_Kernel_IGH_Attributes.htm "IGH_Attributes Interface")

[IGH\_Attributes Properties](../html/Properties_T_Grasshopper_Kernel_IGH_Attributes.htm "IGH_Attributes Properties")

[AllowMessageBalloon Property](../html/P_Grasshopper_Kernel_IGH_Attributes_AllowMessageBalloon.htm "AllowMessageBalloon Property ")

[Bounds Property](../html/P_Grasshopper_Kernel_IGH_Attributes_Bounds.htm "Bounds Property ")

[DocObject Property](../html/P_Grasshopper_Kernel_IGH_Attributes_DocObject.htm "DocObject Property ")

[GetTopLevel Property](../html/P_Grasshopper_Kernel_IGH_Attributes_GetTopLevel.htm "GetTopLevel Property ")

[HasInputGrip Property](../html/P_Grasshopper_Kernel_IGH_Attributes_HasInputGrip.htm "HasInputGrip Property ")

[HasOutputGrip Property](../html/P_Grasshopper_Kernel_IGH_Attributes_HasOutputGrip.htm "HasOutputGrip Property ")

[InputGrip Property](../html/P_Grasshopper_Kernel_IGH_Attributes_InputGrip.htm "InputGrip Property ")

[InstanceGuid Property](../html/P_Grasshopper_Kernel_IGH_Attributes_InstanceGuid.htm "InstanceGuid Property ")

[IsTopLevel Property](../html/P_Grasshopper_Kernel_IGH_Attributes_IsTopLevel.htm "IsTopLevel Property ")

[OutputGrip Property](../html/P_Grasshopper_Kernel_IGH_Attributes_OutputGrip.htm "OutputGrip Property ")

[Parent Property](../html/P_Grasshopper_Kernel_IGH_Attributes_Parent.htm "Parent Property ")

[PathName Property](../html/P_Grasshopper_Kernel_IGH_Attributes_PathName.htm "PathName Property ")

[Pivot Property](../html/P_Grasshopper_Kernel_IGH_Attributes_Pivot.htm "Pivot Property ")

[Selected Property](../html/P_Grasshopper_Kernel_IGH_Attributes_Selected.htm "Selected Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_Attributes Properties |

The [IGH\_Attributes](T_Grasshopper_Kernel_IGH_Attributes.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AllowMessageBalloon](P_Grasshopper_Kernel_IGH_Attributes_AllowMessageBalloon.htm) | Gets a value indicating whether these attributes allow warning and error boxes to be drawn on top of them. |
| Public property | [Bounds](P_Grasshopper_Kernel_IGH_Attributes_Bounds.htm) | Gets the rectangle that contains the active content of the attributes. Typically the Contents determine the active area for menus, tooltips etc. Attributes are not supposed to draw objects beyond the Bounds. |
| Public property | [DocObject](P_Grasshopper_Kernel_IGH_Attributes_DocObject.htm) | Gets the owner object of these attributes. |
| Public property | [GetTopLevel](P_Grasshopper_Kernel_IGH_Attributes_GetTopLevel.htm) | Gets the top level attributes of these attributes. |
| Public property | [HasInputGrip](P_Grasshopper_Kernel_IGH_Attributes_HasInputGrip.htm) | Gets a value indicating whether or not these attributes have an input grip. |
| Public property | [HasOutputGrip](P_Grasshopper_Kernel_IGH_Attributes_HasOutputGrip.htm) | Gets a value indicating whether or not these attributes have an output grip. |
| Public property | [InputGrip](P_Grasshopper_Kernel_IGH_Attributes_InputGrip.htm) | Gets the input grip location for these attributes. If HasInputGrip equals False, this point is meaningless. |
| Public property | [InstanceGuid](P_Grasshopper_Kernel_IGH_Attributes_InstanceGuid.htm) | Gets the instance ID for these attributes. |
| Public property | [IsTopLevel](P_Grasshopper_Kernel_IGH_Attributes_IsTopLevel.htm) | Gets whether these attributes are top\_level (i.e. no Parent attributes) |
| Public property | [OutputGrip](P_Grasshopper_Kernel_IGH_Attributes_OutputGrip.htm) | Gets the output grip location for these attributes. If HasOutputGrip equals False, this point is meaningless. |
| Public property | [Parent](P_Grasshopper_Kernel_IGH_Attributes_Parent.htm) | Gets or sets the parent attributes. Top level attributes do not have parents. |
| Public property | [PathName](P_Grasshopper_Kernel_IGH_Attributes_PathName.htm) | Get a description of the location of these attributes within the local attribute tree. |
| Public property | [Pivot](P_Grasshopper_Kernel_IGH_Attributes_Pivot.htm) | Gets the pivot for these attributes. The pivot controls the general placement of the attributes. If you want to move the attributes, change the pivot location. |
| Public property | [Selected](P_Grasshopper_Kernel_IGH_Attributes_Selected.htm) | Gets or sets the selected state of the top-level attributes. |
| Public property | [TooltipEnabled](P_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_TooltipEnabled.htm) | Gets the tooltip enabled value. If False, no further tooltip functions will be called. (Inherited from [IGH\_TooltipAwareObject](T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Attributes Interface](T_Grasshopper_Kernel_IGH_Attributes.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)