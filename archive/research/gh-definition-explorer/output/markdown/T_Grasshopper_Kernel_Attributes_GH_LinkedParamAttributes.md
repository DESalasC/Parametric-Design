# T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes

﻿ GH\_LinkedParamAttributes Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Attributes](../html/N_Grasshopper_Kernel_Attributes.htm "Grasshopper.Kernel.Attributes")

[GH\_LinkedParamAttributes Class](../html/T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm "GH_LinkedParamAttributes Class")

[GH\_LinkedParamAttributes Constructor](../html/M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes__ctor.htm "GH_LinkedParamAttributes Constructor ")

[GH\_LinkedParamAttributes Properties](../html/Properties_T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm "GH_LinkedParamAttributes Properties")

[GH\_LinkedParamAttributes Methods](../html/Methods_T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm "GH_LinkedParamAttributes Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_LinkedParamAttributes Class |

These Attributes are assigned to parameters that are part of a GH\_Component.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTE3246031\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.KernelAddLanguageSpecificTextSet("LSTE3246031\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Attributes](T_Grasshopper_Kernel_GH_Attributes_1.htm)AddLanguageSpecificTextSet("LSTE3246031\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_Param](T_Grasshopper_Kernel_IGH_Param.htm)AddLanguageSpecificTextSet("LSTE3246031\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Kernel.AttributesAddLanguageSpecificTextSet("LSTE3246031\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_LinkedParamAttributes

**Namespace:**
 [Grasshopper.Kernel.Attributes](N_Grasshopper_Kernel_Attributes.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_LinkedParamAttributes : GH_Attributes<IGH_Param>
```

```
Public Class GH_LinkedParamAttributes
	Inherits GH_Attributes(Of IGH_Param)
```

AddLanguageTabSet("ID1EBCA");

The GH\_LinkedParamAttributes type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_LinkedParamAttributes](M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes__ctor.htm) | Initializes a new instance of the GH\_LinkedParamAttributes class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AllowMessageBalloon](P_Grasshopper_Kernel_GH_Attributes_1_AllowMessageBalloon.htm) | Gets a value indicating whether these attributes allow warning and error balloons to be drawn on top of them. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Bounds](P_Grasshopper_Kernel_GH_Attributes_1_Bounds.htm) | Gets the rectangle that contains the active content of the attributes. Typically the Contents determine the active area for menus, tooltips etc. Attributes are not supposed to draw objects beyond the Bounds. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_7?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_8?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [DocObject](P_Grasshopper_Kernel_GH_Attributes_1_DocObject.htm) | Gets the owner object of these attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [GetTopLevel](P_Grasshopper_Kernel_GH_Attributes_1_GetTopLevel.htm) | Gets the top-level attributes of the attribute stack these attributes belong to. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_11?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_12?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [HasInputGrip](P_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_HasInputGrip.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_13?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_14?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTE3246031\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");HasInputGrip](P_Grasshopper_Kernel_GH_Attributes_1_HasInputGrip.htm).) |
| Public property | [HasOutputGrip](P_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_HasOutputGrip.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_16?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_17?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTE3246031\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");HasOutputGrip](P_Grasshopper_Kernel_GH_Attributes_1_HasOutputGrip.htm).) |
| Public property | [InputGrip](P_Grasshopper_Kernel_GH_Attributes_1_InputGrip.htm) | Gets the input grip location for these attributes. If HasInputGrip equals False, this point is meaningless. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [InstanceGuid](P_Grasshopper_Kernel_GH_Attributes_1_InstanceGuid.htm) | Gets the instance ID of the document object that owns these attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_21?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_22?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [IsTopLevel](P_Grasshopper_Kernel_GH_Attributes_1_IsTopLevel.htm) | Gets whether these attributes are top\_level (i.e. no Parent attributes) (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_23?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_24?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [OutputGrip](P_Grasshopper_Kernel_GH_Attributes_1_OutputGrip.htm) | Gets the output grip location for these attributes. If HasOutputGrip equals False, this point is meaningless. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_25?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_26?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Owner](P_Grasshopper_Kernel_GH_Attributes_1_Owner.htm) | Gets the type-safe owner object of these attributes. This property is identical to the DocObject property. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_27?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_28?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Parent](P_Grasshopper_Kernel_GH_Attributes_1_Parent.htm) | Gets or sets the parent attributes. Top level attributes do not have parents. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_29?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_30?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [PathName](P_Grasshopper_Kernel_GH_Attributes_1_PathName.htm) | Get a description of the location of these attributes within the local attribute stack. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_31?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_32?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Pivot](P_Grasshopper_Kernel_GH_Attributes_1_Pivot.htm) | Gets or sets the pivot for these attributes. The pivot controls the general placement of the attributes. If you want to move the attributes, change the pivot location. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_33?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_34?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Selected](P_Grasshopper_Kernel_GH_Attributes_1_Selected.htm) | Gets or sets the selected state of the top-level attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_35?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_36?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [TooltipEnabled](P_Grasshopper_Kernel_GH_Attributes_1_TooltipEnabled.htm) | Gets the tooltip enabled value. If False, no further tooltip functions will be called. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_37?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_38?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendToAttributeTree](M_Grasshopper_Kernel_GH_Attributes_1_AppendToAttributeTree.htm) | Recursively append these attributes and all child attributes to the attribute list. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_39?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_40?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [ExpireLayout](M_Grasshopper_Kernel_GH_Attributes_1_ExpireLayout.htm) | Expires the entire layout of the attributes. When overridden, implementer *must* place a call to the base class ExpireLayout(). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_41?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_42?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [InvalidateCanvas](M_Grasshopper_Kernel_GH_Attributes_1_InvalidateCanvas.htm) | If the mouse location should cause a canvas invalidation then return true. You only need to override this function if you draw objects that are dependant on cursor positions outside the bounds of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_43?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_44?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsMenuRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsMenuRegion.htm) | Determines whether a point is available for context menu popups. By default, IsMenuRegion calls IsPickRegion(PointF). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_45?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_46?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsPickRegion(PointF)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm) | Determines whether a point is within the pickable region for this object. By default, any point inside the Bounds is treated as pickable. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_47?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_48?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsPickRegion(RectangleF, GH\_PickBox)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion_1.htm) | Determines whether a rectangle is a valid pick region for this object. By default, the picking rectangle is intersected with the Bounds rectangle. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_49?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_50?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsTooltipRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsTooltipRegion.htm) | Determines whether a point is available for tooltip popups. By default, IsMenuRegion calls IsTooltipRegion(PointF). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_51?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_52?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [Layout](M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_Layout.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_53?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_54?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTE3246031\_55?cs=.|vb=.|cpp=::|nu=.|fs=.");LayoutAddLanguageSpecificTextSet("LSTE3246031\_56?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Attributes_1_Layout.htm).) |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LSTE3246031\_57?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid.htm) | Generate a new instance GUID for the owner object. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_58?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_59?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [NewInstanceGuid(Guid)](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid_1.htm) | Generate a new instance GUID for the owner object. Do not use this overload unless you're > 1.95m and called David. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_60?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_61?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [PerformLayout](M_Grasshopper_Kernel_GH_Attributes_1_PerformLayout.htm) | Recompute the layout for these attributes. This function is automatically called during Drawing operations, so you typically don't have to. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_62?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_63?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [PrepareForRender](M_Grasshopper_Kernel_GH_Attributes_1_PrepareForRender.htm) | This method will always be called exactly once prior to Render(). This would be a good place to make sure all the necessary GUI data is up and running. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_64?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_65?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_GH_Attributes_1_Read.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_66?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_67?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [Render](M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_Render.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_68?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_69?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTE3246031\_70?cs=.|vb=.|cpp=::|nu=.|fs=.");Render(GH\_Canvas, Graphics, GH\_CanvasChannel)](M_Grasshopper_Kernel_GH_Attributes_1_Render.htm).) |
| Protected method | [RenderIncomingWires(GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LSTE3246031\_71?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LSTE3246031\_72?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_ParamWireDisplay)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires.htm) | Utility function for derived classes. This method draws all the wires going into the left side of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_73?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_74?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [RenderIncomingWires(GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LSTE3246031\_75?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LSTE3246031\_76?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, IEnumerableAddLanguageSpecificTextSet("LSTE3246031\_77?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");PenAddLanguageSpecificTextSet("LSTE3246031\_78?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires_1.htm) | Utility function for derived classes. This method draws all the wires going into the left side of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_79?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_80?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RenderToCanvas](M_Grasshopper_Kernel_GH_Attributes_1_RenderToCanvas.htm) | Render these attributes into a Canvas control. This function places calls to PrepareForRender() and Render(), you should override those. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_81?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_82?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToKeyDown](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyDown.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_83?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_84?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToKeyUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyUp.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_85?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_86?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseDoubleClick](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDoubleClick.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_87?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_88?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseDown](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDown.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_89?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_90?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseMove](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseMove.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_91?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_92?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseUp.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_93?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_94?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [SetupTooltip](M_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes_SetupTooltip.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_95?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_96?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTE3246031\_97?cs=.|vb=.|cpp=::|nu=.|fs=.");SetupTooltip(PointF, GH\_TooltipDisplayEventArgs)](M_Grasshopper_Kernel_GH_Attributes_1_SetupTooltip.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_GH_Attributes_1_Write.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LSTE3246031\_98?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE3246031\_99?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Attributes Namespace](N_Grasshopper_Kernel_Attributes.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)