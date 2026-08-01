# Properties_T_Grasshopper_Kernel_GH_Attributes_1

﻿ GH\_Attributes(T) Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Attributes(T) Class](../html/T_Grasshopper_Kernel_GH_Attributes_1.htm "GH_Attributes(T) Class")

[GH\_Attributes(T) Properties](../html/Properties_T_Grasshopper_Kernel_GH_Attributes_1.htm "GH_Attributes(T) Properties")

[AllowMessageBalloon Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_AllowMessageBalloon.htm "AllowMessageBalloon Property ")

[Bounds Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_Bounds.htm "Bounds Property ")

[DocObject Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_DocObject.htm "DocObject Property ")

[GetTopLevel Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_GetTopLevel.htm "GetTopLevel Property ")

[HasInputGrip Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_HasInputGrip.htm "HasInputGrip Property ")

[HasOutputGrip Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_HasOutputGrip.htm "HasOutputGrip Property ")

[InputGrip Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_InputGrip.htm "InputGrip Property ")

[InstanceGuid Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_InstanceGuid.htm "InstanceGuid Property ")

[IsTopLevel Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_IsTopLevel.htm "IsTopLevel Property ")

[OutputGrip Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_OutputGrip.htm "OutputGrip Property ")

[Owner Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_Owner.htm "Owner Property ")

[Parent Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_Parent.htm "Parent Property ")

[PathName Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_PathName.htm "PathName Property ")

[Pivot Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_Pivot.htm "Pivot Property ")

[Selected Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_Selected.htm "Selected Property ")

[TooltipEnabled Property](../html/P_Grasshopper_Kernel_GH_Attributes_1_TooltipEnabled.htm "TooltipEnabled Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AttributesAddLanguageSpecificTextSet("LSTA5FE1B00\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTA5FE1B00\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Properties |

The [GH\_AttributesAddLanguageSpecificTextSet("LSTA5FE1B00\_2?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA5FE1B00\_3?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm) generic type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AllowMessageBalloon](P_Grasshopper_Kernel_GH_Attributes_1_AllowMessageBalloon.htm) | Gets a value indicating whether these attributes allow warning and error balloons to be drawn on top of them. |
| Public property | [Bounds](P_Grasshopper_Kernel_GH_Attributes_1_Bounds.htm) | Gets the rectangle that contains the active content of the attributes. Typically the Contents determine the active area for menus, tooltips etc. Attributes are not supposed to draw objects beyond the Bounds. |
| Public property | [DocObject](P_Grasshopper_Kernel_GH_Attributes_1_DocObject.htm) | Gets the owner object of these attributes. |
| Public property | [GetTopLevel](P_Grasshopper_Kernel_GH_Attributes_1_GetTopLevel.htm) | Gets the top-level attributes of the attribute stack these attributes belong to. |
| Public property | [HasInputGrip](P_Grasshopper_Kernel_GH_Attributes_1_HasInputGrip.htm) | Gets a value indicating whether or not these attributes have an input grip. |
| Public property | [HasOutputGrip](P_Grasshopper_Kernel_GH_Attributes_1_HasOutputGrip.htm) | Gets a value indicating whether or not these attributes have an output grip. |
| Public property | [InputGrip](P_Grasshopper_Kernel_GH_Attributes_1_InputGrip.htm) | Gets the input grip location for these attributes. If HasInputGrip equals False, this point is meaningless. |
| Public property | [InstanceGuid](P_Grasshopper_Kernel_GH_Attributes_1_InstanceGuid.htm) | Gets the instance ID of the document object that owns these attributes. |
| Public property | [IsTopLevel](P_Grasshopper_Kernel_GH_Attributes_1_IsTopLevel.htm) | Gets whether these attributes are top\_level (i.e. no Parent attributes) |
| Public property | [OutputGrip](P_Grasshopper_Kernel_GH_Attributes_1_OutputGrip.htm) | Gets the output grip location for these attributes. If HasOutputGrip equals False, this point is meaningless. |
| Public property | [Owner](P_Grasshopper_Kernel_GH_Attributes_1_Owner.htm) | Gets the type-safe owner object of these attributes. This property is identical to the DocObject property. |
| Public property | [Parent](P_Grasshopper_Kernel_GH_Attributes_1_Parent.htm) | Gets or sets the parent attributes. Top level attributes do not have parents. |
| Public property | [PathName](P_Grasshopper_Kernel_GH_Attributes_1_PathName.htm) | Get a description of the location of these attributes within the local attribute stack. |
| Public property | [Pivot](P_Grasshopper_Kernel_GH_Attributes_1_Pivot.htm) | Gets or sets the pivot for these attributes. The pivot controls the general placement of the attributes. If you want to move the attributes, change the pivot location. |
| Public property | [Selected](P_Grasshopper_Kernel_GH_Attributes_1_Selected.htm) | Gets or sets the selected state of the top-level attributes. |
| Public property | [TooltipEnabled](P_Grasshopper_Kernel_GH_Attributes_1_TooltipEnabled.htm) | Gets the tooltip enabled value. If False, no further tooltip functions will be called. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_AttributesAddLanguageSpecificTextSet("LSTA5FE1B00\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA5FE1B00\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_Attributes_1.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)