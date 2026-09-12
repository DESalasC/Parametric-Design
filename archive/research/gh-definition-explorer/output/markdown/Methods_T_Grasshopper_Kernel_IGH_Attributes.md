# Methods_T_Grasshopper_Kernel_IGH_Attributes

﻿ IGH\_Attributes Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_Attributes Interface](../html/T_Grasshopper_Kernel_IGH_Attributes.htm "IGH_Attributes Interface")

[IGH\_Attributes Methods](../html/Methods_T_Grasshopper_Kernel_IGH_Attributes.htm "IGH_Attributes Methods")

[AppendToAttributeTree Method](../html/M_Grasshopper_Kernel_IGH_Attributes_AppendToAttributeTree.htm "AppendToAttributeTree Method ")

[ExpireLayout Method](../html/M_Grasshopper_Kernel_IGH_Attributes_ExpireLayout.htm "ExpireLayout Method ")

[InvalidateCanvas Method](../html/M_Grasshopper_Kernel_IGH_Attributes_InvalidateCanvas.htm "InvalidateCanvas Method ")

[IsMenuRegion Method](../html/M_Grasshopper_Kernel_IGH_Attributes_IsMenuRegion.htm "IsMenuRegion Method ")

[IsPickRegion Method](../html/Overload_Grasshopper_Kernel_IGH_Attributes_IsPickRegion.htm "IsPickRegion Method ")

[NewInstanceGuid Method](../html/Overload_Grasshopper_Kernel_IGH_Attributes_NewInstanceGuid.htm "NewInstanceGuid Method ")

[PerformLayout Method](../html/M_Grasshopper_Kernel_IGH_Attributes_PerformLayout.htm "PerformLayout Method ")

[RenderToCanvas Method](../html/M_Grasshopper_Kernel_IGH_Attributes_RenderToCanvas.htm "RenderToCanvas Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_Attributes Methods |

The [IGH\_Attributes](T_Grasshopper_Kernel_IGH_Attributes.htm) type exposes the following members.

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
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LST2518D5F\_0?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_IGH_Attributes_NewInstanceGuid.htm) | Generate a new instance GUID for the owner object. |
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

[IGH\_Attributes Interface](T_Grasshopper_Kernel_IGH_Attributes.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)