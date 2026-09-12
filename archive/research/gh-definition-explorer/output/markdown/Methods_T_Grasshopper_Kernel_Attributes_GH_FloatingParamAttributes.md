# Methods_T_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes

﻿ GH\_FloatingParamAttributes Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Attributes](../html/N_Grasshopper_Kernel_Attributes.htm "Grasshopper.Kernel.Attributes")

[GH\_FloatingParamAttributes Class](../html/T_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes.htm "GH_FloatingParamAttributes Class")

[GH\_FloatingParamAttributes Methods](../html/Methods_T_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes.htm "GH_FloatingParamAttributes Methods")

[Layout Method](../html/M_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes_Layout.htm "Layout Method ")

[Render Method](../html/M_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes_Render.htm "Render Method ")

[RespondToMouseDoubleClick Method](../html/M_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes_RespondToMouseDoubleClick.htm "RespondToMouseDoubleClick Method ")

[SetupTooltip Method](../html/M_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes_SetupTooltip.htm "SetupTooltip Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FloatingParamAttributes Methods |

The [GH\_FloatingParamAttributes](T_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendToAttributeTree](M_Grasshopper_Kernel_GH_Attributes_1_AppendToAttributeTree.htm) | Recursively append these attributes and all child attributes to the attribute list. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_0?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_1?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [ExpireLayout](M_Grasshopper_Kernel_GH_Attributes_1_ExpireLayout.htm) | Expires the entire layout of the attributes. When overridden, implementer *must* place a call to the base class ExpireLayout(). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_2?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_3?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [InvalidateCanvas](M_Grasshopper_Kernel_GH_Attributes_1_InvalidateCanvas.htm) | If the mouse location should cause a canvas invalidation then return true. You only need to override this function if you draw objects that are dependant on cursor positions outside the bounds of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsMenuRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsMenuRegion.htm) | Determines whether a point is available for context menu popups. By default, IsMenuRegion calls IsPickRegion(PointF). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsPickRegion(PointF)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm) | Determines whether a point is within the pickable region for this object. By default, any point inside the Bounds is treated as pickable. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsPickRegion(RectangleF, GH\_PickBox)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion_1.htm) | Determines whether a rectangle is a valid pick region for this object. By default, the picking rectangle is intersected with the Bounds rectangle. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_10?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_11?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsTooltipRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsTooltipRegion.htm) | Determines whether a point is available for tooltip popups. By default, IsMenuRegion calls IsTooltipRegion(PointF). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [Layout](M_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes_Layout.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_14?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_15?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTDB4BB850\_16?cs=.|vb=.|cpp=::|nu=.|fs=.");LayoutAddLanguageSpecificTextSet("LSTDB4BB850\_17?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Attributes_1_Layout.htm).) |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LSTDB4BB850\_18?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid.htm) | Generate a new instance GUID for the owner object. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [NewInstanceGuid(Guid)](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid_1.htm) | Generate a new instance GUID for the owner object. Do not use this overload unless you're > 1.95m and called David. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_21?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_22?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [PerformLayout](M_Grasshopper_Kernel_GH_Attributes_1_PerformLayout.htm) | Recompute the layout for these attributes. This function is automatically called during Drawing operations, so you typically don't have to. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_23?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_24?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [PrepareForRender](M_Grasshopper_Kernel_GH_Attributes_1_PrepareForRender.htm) | This method will always be called exactly once prior to Render(). This would be a good place to make sure all the necessary GUI data is up and running. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_25?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_26?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_GH_Attributes_1_Read.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_27?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_28?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [Render](M_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes_Render.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_29?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_30?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTDB4BB850\_31?cs=.|vb=.|cpp=::|nu=.|fs=.");Render(GH\_Canvas, Graphics, GH\_CanvasChannel)](M_Grasshopper_Kernel_GH_Attributes_1_Render.htm).) |
| Protected method | [RenderIncomingWires(GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LSTDB4BB850\_32?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LSTDB4BB850\_33?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_ParamWireDisplay)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires.htm) | Utility function for derived classes. This method draws all the wires going into the left side of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_34?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_35?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [RenderIncomingWires(GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LSTDB4BB850\_36?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LSTDB4BB850\_37?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, IEnumerableAddLanguageSpecificTextSet("LSTDB4BB850\_38?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");PenAddLanguageSpecificTextSet("LSTDB4BB850\_39?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires_1.htm) | Utility function for derived classes. This method draws all the wires going into the left side of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_40?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_41?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RenderToCanvas](M_Grasshopper_Kernel_GH_Attributes_1_RenderToCanvas.htm) | Render these attributes into a Canvas control. This function places calls to PrepareForRender() and Render(), you should override those. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_42?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_43?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToKeyDown](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyDown.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_44?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_45?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToKeyUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyUp.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_46?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_47?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseDoubleClick](M_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes_RespondToMouseDoubleClick.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_48?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_49?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTDB4BB850\_50?cs=.|vb=.|cpp=::|nu=.|fs=.");RespondToMouseDoubleClick(GH\_Canvas, GH\_CanvasMouseEvent)](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDoubleClick.htm).) |
| Public method | [RespondToMouseDown](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDown.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_51?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_52?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseMove](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseMove.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_53?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_54?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseUp.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_55?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_56?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [SetupTooltip](M_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes_SetupTooltip.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_57?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_58?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTDB4BB850\_59?cs=.|vb=.|cpp=::|nu=.|fs=.");SetupTooltip(PointF, GH\_TooltipDisplayEventArgs)](M_Grasshopper_Kernel_GH_Attributes_1_SetupTooltip.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_GH_Attributes_1_Write.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTDB4BB850\_60?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDB4BB850\_61?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_FloatingParamAttributes Class](T_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes.htm)

[Grasshopper.Kernel.Attributes Namespace](N_Grasshopper_Kernel_Attributes.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)