# Methods_T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes

﻿ GH\_LinkedParamAttributes Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Attributes](../html/N_Grasshopper_Kernel_Attributes.htm "Grasshopper.Kernel.Attributes")

[GH\_LinkedParamAttributes Class](../html/T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm "GH_LinkedParamAttributes Class")

[GH\_LinkedParamAttributes Methods](../html/Methods_T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm "GH_LinkedParamAttributes Methods")

[Layout Method](../html/M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_Layout.htm "Layout Method ")

[Render Method](../html/M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_Render.htm "Render Method ")

[SetupTooltip Method](../html/M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_SetupTooltip.htm "SetupTooltip Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_LinkedParamAttributes Methods |

The [GH\_LinkedParamAttributes](T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendToAttributeTree](M_Grasshopper_Kernel_GH_Attributes_1_AppendToAttributeTree.htm) | Recursively append these attributes and all child attributes to the attribute list. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_0?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_1?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [ExpireLayout](M_Grasshopper_Kernel_GH_Attributes_1_ExpireLayout.htm) | Expires the entire layout of the attributes. When overridden, implementer *must* place a call to the base class ExpireLayout(). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_2?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_3?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [InvalidateCanvas](M_Grasshopper_Kernel_GH_Attributes_1_InvalidateCanvas.htm) | If the mouse location should cause a canvas invalidation then return true. You only need to override this function if you draw objects that are dependant on cursor positions outside the bounds of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsMenuRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsMenuRegion.htm) | Determines whether a point is available for context menu popups. By default, IsMenuRegion calls IsPickRegion(PointF). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsPickRegion(PointF)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm) | Determines whether a point is within the pickable region for this object. By default, any point inside the Bounds is treated as pickable. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsPickRegion(RectangleF, GH\_PickBox)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion_1.htm) | Determines whether a rectangle is a valid pick region for this object. By default, the picking rectangle is intersected with the Bounds rectangle. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_10?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_11?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsTooltipRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsTooltipRegion.htm) | Determines whether a point is available for tooltip popups. By default, IsMenuRegion calls IsTooltipRegion(PointF). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [Layout](M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_Layout.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_14?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_15?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTA0BE5ADB\_16?cs=.|vb=.|cpp=::|nu=.|fs=.");LayoutAddLanguageSpecificTextSet("LSTA0BE5ADB\_17?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Attributes_1_Layout.htm).) |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LSTA0BE5ADB\_18?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid.htm) | Generate a new instance GUID for the owner object. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [NewInstanceGuid(Guid)](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid_1.htm) | Generate a new instance GUID for the owner object. Do not use this overload unless you're > 1.95m and called David. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_21?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_22?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [PerformLayout](M_Grasshopper_Kernel_GH_Attributes_1_PerformLayout.htm) | Recompute the layout for these attributes. This function is automatically called during Drawing operations, so you typically don't have to. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_23?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_24?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [PrepareForRender](M_Grasshopper_Kernel_GH_Attributes_1_PrepareForRender.htm) | This method will always be called exactly once prior to Render(). This would be a good place to make sure all the necessary GUI data is up and running. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_25?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_26?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_GH_Attributes_1_Read.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_27?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_28?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [Render](M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_Render.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_29?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_30?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTA0BE5ADB\_31?cs=.|vb=.|cpp=::|nu=.|fs=.");Render(GH\_Canvas, Graphics, GH\_CanvasChannel)](M_Grasshopper_Kernel_GH_Attributes_1_Render.htm).) |
| Protected method | [RenderIncomingWires(GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LSTA0BE5ADB\_32?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LSTA0BE5ADB\_33?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_ParamWireDisplay)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires.htm) | Utility function for derived classes. This method draws all the wires going into the left side of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_34?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_35?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [RenderIncomingWires(GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LSTA0BE5ADB\_36?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LSTA0BE5ADB\_37?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, IEnumerableAddLanguageSpecificTextSet("LSTA0BE5ADB\_38?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");PenAddLanguageSpecificTextSet("LSTA0BE5ADB\_39?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires_1.htm) | Utility function for derived classes. This method draws all the wires going into the left side of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_40?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_41?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RenderToCanvas](M_Grasshopper_Kernel_GH_Attributes_1_RenderToCanvas.htm) | Render these attributes into a Canvas control. This function places calls to PrepareForRender() and Render(), you should override those. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_42?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_43?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToKeyDown](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyDown.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_44?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_45?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToKeyUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyUp.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_46?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_47?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseDoubleClick](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDoubleClick.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_48?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_49?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseDown](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDown.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_50?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_51?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseMove](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseMove.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_52?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_53?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseUp.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_54?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_55?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [SetupTooltip](M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_SetupTooltip.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_56?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_57?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTA0BE5ADB\_58?cs=.|vb=.|cpp=::|nu=.|fs=.");SetupTooltip(PointF, GH\_TooltipDisplayEventArgs)](M_Grasshopper_Kernel_GH_Attributes_1_SetupTooltip.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_GH_Attributes_1_Write.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTA0BE5ADB\_59?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTA0BE5ADB\_60?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_LinkedParamAttributes Class](T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm)

[Grasshopper.Kernel.Attributes Namespace](N_Grasshopper_Kernel_Attributes.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)