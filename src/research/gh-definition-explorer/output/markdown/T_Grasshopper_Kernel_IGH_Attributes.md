# T_Grasshopper_Kernel_IGH_Attributes

﻿ IGH\_Attributes Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_Attributes Interface](../html/T_Grasshopper_Kernel_IGH_Attributes.htm "IGH_Attributes Interface")

[IGH\_Attributes Properties](../html/Properties_T_Grasshopper_Kernel_IGH_Attributes.htm "IGH_Attributes Properties")

[IGH\_Attributes Methods](../html/Methods_T_Grasshopper_Kernel_IGH_Attributes.htm "IGH_Attributes Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_Attributes Interface |

Base interface for all Attributes. Attributes are the visual portion of GH\_DocumentObjects.
They handle display, mouse events, layout, context menus etc. etc.
You should consider inheriting from GH\_Attributes or some other abstract class instead of
implementing this interface from scratch.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_Attributes : GH_ISerializable, 
	IGH_ResponsiveObject, IGH_TooltipAwareObject
```

```
Public Interface IGH_Attributes
	Inherits GH_ISerializable, IGH_ResponsiveObject, IGH_TooltipAwareObject
```

AddLanguageTabSet("ID0EBCA");

The IGH\_Attributes type exposes the following members.

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

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendToAttributeTree](M_Grasshopper_Kernel_IGH_Attributes_AppendToAttributeTree.htm) | Recursively append these attributes and all child attributes to the attribute list. |
| Public method | [ExpireLayout](M_Grasshopper_Kernel_IGH_Attributes_ExpireLayout.htm) | Expires the entire layout of the attributes. When overridden, implementer *must* place a call to the base class ExpireLayout(). |
| Public method | [InvalidateCanvas](M_Grasshopper_Kernel_IGH_Attributes_InvalidateCanvas.htm) | If the mouse location should cause a canvas invalidation then return true. You only need to override this function if you draw objects that are dependant on cursor positions outside the bounds of the attributes. |
| Public method | [IsMenuRegion](M_Grasshopper_Kernel_IGH_Attributes_IsMenuRegion.htm) | Determines whether a point is available for context menu popups. By default, IsMenuRegion calls IsPickRegion(PointF). |
| Public method | [IsPickRegion(PointF)](M_Grasshopper_Kernel_IGH_Attributes_IsPickRegion.htm) | Determines whether a point is within the pickable region for this object. By default, any point inside the Bounds is treated as pickable. |
| Public method | [IsPickRegion(RectangleF, GH\_PickBox)](M_Grasshopper_Kernel_IGH_Attributes_IsPickRegion_1.htm) | Determines whether a rectangle is a valid pick region for this object. By default, the picking rectangle is intersected with the Bounds rectangle. |
| Public method | [IsTooltipRegion](M_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_IsTooltipRegion.htm) | Determine whether the specified pixel should result in a tooltip when the cursor hovers over it. (Inherited from [IGH\_TooltipAwareObject](T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm).) |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LST3E0FF3F0\_0?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_IGH_Attributes_NewInstanceGuid.htm) | Generate a new instance GUID for the owner object. |
| Public method | [NewInstanceGuid(Guid)](M_Grasshopper_Kernel_IGH_Attributes_NewInstanceGuid_1.htm) | Generate a new instance GUID for the owner object. Do not use this overload unless you're > 1.95m and called David. |
| Public method | [PerformLayout](M_Grasshopper_Kernel_IGH_Attributes_PerformLayout.htm) | Recompute the layout for these attributes. This function is automatically called during Drawing operations, so you typically don't have to. |
| Public method | [Read](M_GH_IO_GH_ISerializable_Read.htm) | This method is called whenever the instance is required to deserialize itself. (Inherited from [GH\_ISerializable](T_GH_IO_GH_ISerializable.htm).) |
| Public method | [RenderToCanvas](M_Grasshopper_Kernel_IGH_Attributes_RenderToCanvas.htm) | Render these attributes into a Canvas control. |
| Public method | [RespondToKeyDown](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToKeyDown.htm) | (Inherited from [IGH\_ResponsiveObject](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm).) |
| Public method | [RespondToKeyUp](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToKeyUp.htm) | (Inherited from [IGH\_ResponsiveObject](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm).) |
| Public method | [RespondToMouseDoubleClick](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseDoubleClick.htm) | This function will be called whenever the left button is double-clicked over the canvas. If you are active, you will be the only object who gets called. (Inherited from [IGH\_ResponsiveObject](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm).) |
| Public method | [RespondToMouseDown](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseDown.htm) | This function will be called whenever a mouse button is pressed over the canvas. If you are active, you will be the only object who gets called. If you are inactive, you might get called if nobody on top of you decides to become active. (Inherited from [IGH\_ResponsiveObject](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm).) |
| Public method | [RespondToMouseMove](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseMove.htm) | This function will be called when the mouse moves across the canvas. If you are active, you will be the only object who gets called. If you are inactive, you might get called if nobody on top of you decides to become active. (Inherited from [IGH\_ResponsiveObject](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm).) |
| Public method | [RespondToMouseUp](M_Grasshopper_GUI_Canvas_IGH_ResponsiveObject_RespondToMouseUp.htm) | This function will be called whenever a mouse button is released over the canvas. If you are active, you will be the only object who gets called. If you are inactive, you will not be called at all for MouseUp events. (Inherited from [IGH\_ResponsiveObject](T_Grasshopper_GUI_Canvas_IGH_ResponsiveObject.htm).) |
| Public method | [SetupTooltip](M_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_SetupTooltip.htm) | This function is called when a tooltip it about to be displayed. (Inherited from [IGH\_TooltipAwareObject](T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm).) |
| Public method | [Write](M_GH_IO_GH_ISerializable_Write.htm) | This method is called whenever the instance is required to serialize itself. (Inherited from [GH\_ISerializable](T_GH_IO_GH_ISerializable.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)