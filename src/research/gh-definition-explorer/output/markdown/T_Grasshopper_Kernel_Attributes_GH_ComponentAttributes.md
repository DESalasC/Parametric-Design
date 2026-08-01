# T_Grasshopper_Kernel_Attributes_GH_ComponentAttributes

﻿ GH\_ComponentAttributes Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Attributes](../html/N_Grasshopper_Kernel_Attributes.htm "Grasshopper.Kernel.Attributes")

[GH\_ComponentAttributes Class](../html/T_Grasshopper_Kernel_Attributes_GH_ComponentAttributes.htm "GH_ComponentAttributes Class")

[GH\_ComponentAttributes Constructor](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes__ctor.htm "GH_ComponentAttributes Constructor ")

[GH\_ComponentAttributes Properties](../html/Properties_T_Grasshopper_Kernel_Attributes_GH_ComponentAttributes.htm "GH_ComponentAttributes Properties")

[GH\_ComponentAttributes Methods](../html/Methods_T_Grasshopper_Kernel_Attributes_GH_ComponentAttributes.htm "GH_ComponentAttributes Methods")

[GH\_ComponentAttributes Fields](../html/Fields_T_Grasshopper_Kernel_Attributes_GH_ComponentAttributes.htm "GH_ComponentAttributes Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAttributes Class |

These Attributes are the default for GH\_Components.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST1C0FFBC0\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.KernelAddLanguageSpecificTextSet("LST1C0FFBC0\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Attributes](T_Grasshopper_Kernel_GH_Attributes_1.htm)AddLanguageSpecificTextSet("LST1C0FFBC0\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm)AddLanguageSpecificTextSet("LST1C0FFBC0\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Kernel.AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ComponentAttributes

**Namespace:**
 [Grasshopper.Kernel.Attributes](N_Grasshopper_Kernel_Attributes.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ComponentAttributes : GH_Attributes<IGH_Component>
```

```
Public Class GH_ComponentAttributes
	Inherits GH_Attributes(Of IGH_Component)
```

AddLanguageTabSet("ID1EBCA");

The GH\_ComponentAttributes type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ComponentAttributes](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes__ctor.htm) | Initializes a new instance of the GH\_ComponentAttributes class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AllowMessageBalloon](P_Grasshopper_Kernel_GH_Attributes_1_AllowMessageBalloon.htm) | Gets a value indicating whether these attributes allow warning and error balloons to be drawn on top of them. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Bounds](P_Grasshopper_Kernel_GH_Attributes_1_Bounds.htm) | Gets the rectangle that contains the active content of the attributes. Typically the Contents determine the active area for menus, tooltips etc. Attributes are not supposed to draw objects beyond the Bounds. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_7?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_8?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [ContentBox](P_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_ContentBox.htm) | Gets the bounds of the component area of the attributes. |
| Public property | [DocObject](P_Grasshopper_Kernel_GH_Attributes_1_DocObject.htm) | Gets the owner object of these attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [GetTopLevel](P_Grasshopper_Kernel_GH_Attributes_1_GetTopLevel.htm) | Gets the top-level attributes of the attribute stack these attributes belong to. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_11?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_12?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [HasInputGrip](P_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_HasInputGrip.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_13?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_14?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST1C0FFBC0\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");HasInputGrip](P_Grasshopper_Kernel_GH_Attributes_1_HasInputGrip.htm).) |
| Public property | [HasOutputGrip](P_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_HasOutputGrip.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_16?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_17?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST1C0FFBC0\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");HasOutputGrip](P_Grasshopper_Kernel_GH_Attributes_1_HasOutputGrip.htm).) |
| Public property | [InputGrip](P_Grasshopper_Kernel_GH_Attributes_1_InputGrip.htm) | Gets the input grip location for these attributes. If HasInputGrip equals False, this point is meaningless. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [InstanceGuid](P_Grasshopper_Kernel_GH_Attributes_1_InstanceGuid.htm) | Gets the instance ID of the document object that owns these attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_21?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_22?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [IsTopLevel](P_Grasshopper_Kernel_GH_Attributes_1_IsTopLevel.htm) | Gets whether these attributes are top\_level (i.e. no Parent attributes) (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_23?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_24?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [OutputGrip](P_Grasshopper_Kernel_GH_Attributes_1_OutputGrip.htm) | Gets the output grip location for these attributes. If HasOutputGrip equals False, this point is meaningless. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_25?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_26?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Owner](P_Grasshopper_Kernel_GH_Attributes_1_Owner.htm) | Gets the type-safe owner object of these attributes. This property is identical to the DocObject property. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_27?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_28?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Parent](P_Grasshopper_Kernel_GH_Attributes_1_Parent.htm) | Gets or sets the parent attributes. Top level attributes do not have parents. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_29?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_30?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [PathName](P_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_PathName.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_31?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_32?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST1C0FFBC0\_33?cs=.|vb=.|cpp=::|nu=.|fs=.");PathName](P_Grasshopper_Kernel_GH_Attributes_1_PathName.htm).) |
| Public property | [Pivot](P_Grasshopper_Kernel_GH_Attributes_1_Pivot.htm) | Gets or sets the pivot for these attributes. The pivot controls the general placement of the attributes. If you want to move the attributes, change the pivot location. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_34?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_35?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Selected](P_Grasshopper_Kernel_GH_Attributes_1_Selected.htm) | Gets or sets the selected state of the top-level attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_36?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_37?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [TooltipEnabled](P_Grasshopper_Kernel_GH_Attributes_1_TooltipEnabled.htm) | Gets the tooltip enabled value. If False, no further tooltip functions will be called. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_38?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_39?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendToAttributeTree](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_AppendToAttributeTree.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_40?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_41?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST1C0FFBC0\_42?cs=.|vb=.|cpp=::|nu=.|fs=.");AppendToAttributeTree(ListAddLanguageSpecificTextSet("LST1C0FFBC0\_43?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_44?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Attributes_1_AppendToAttributeTree.htm).) |
| Public method | [ExpireLayout](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_ExpireLayout.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_45?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_46?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST1C0FFBC0\_47?cs=.|vb=.|cpp=::|nu=.|fs=.");ExpireLayoutAddLanguageSpecificTextSet("LST1C0FFBC0\_48?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Attributes_1_ExpireLayout.htm).) |
| Public method | [InvalidateCanvas](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_InvalidateCanvas.htm) | The canvas must be invalidated when the mouse is near enough and this component has variable parameters. (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_49?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_50?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST1C0FFBC0\_51?cs=.|vb=.|cpp=::|nu=.|fs=.");InvalidateCanvas(GH\_Canvas, GH\_CanvasMouseEvent)](M_Grasshopper_Kernel_GH_Attributes_1_InvalidateCanvas.htm).) |
| Public method | [IsMenuRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsMenuRegion.htm) | Determines whether a point is available for context menu popups. By default, IsMenuRegion calls IsPickRegion(PointF). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_52?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_53?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsPickRegion(PointF)](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_IsPickRegion.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_54?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_55?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST1C0FFBC0\_56?cs=.|vb=.|cpp=::|nu=.|fs=.");IsPickRegion(PointF)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm).) |
| Public method | [IsPickRegion(RectangleF, GH\_PickBox)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion_1.htm) | Determines whether a rectangle is a valid pick region for this object. By default, the picking rectangle is intersected with the Bounds rectangle. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_57?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_58?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsTooltipRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsTooltipRegion.htm) | Determines whether a point is available for tooltip popups. By default, IsMenuRegion calls IsTooltipRegion(PointF). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_59?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_60?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [Layout](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_Layout.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_61?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_62?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST1C0FFBC0\_63?cs=.|vb=.|cpp=::|nu=.|fs=.");LayoutAddLanguageSpecificTextSet("LST1C0FFBC0\_64?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Attributes_1_Layout.htm).) |
| Public methodStatic member | [LayoutBounds](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_LayoutBounds.htm) |  |
| Public methodStatic member | [LayoutComponentBox](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_LayoutComponentBox.htm) | Utility layout method for GH\_Component style UI. |
| Public methodStatic member | [LayoutInputParams](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_LayoutInputParams.htm) |  |
| Public methodStatic member | [LayoutOutputParams](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_LayoutOutputParams.htm) |  |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LST1C0FFBC0\_65?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid.htm) | Generate a new instance GUID for the owner object. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_66?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_67?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [NewInstanceGuid(Guid)](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid_1.htm) | Generate a new instance GUID for the owner object. Do not use this overload unless you're > 1.95m and called David. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_68?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_69?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [PerformLayout](M_Grasshopper_Kernel_GH_Attributes_1_PerformLayout.htm) | Recompute the layout for these attributes. This function is automatically called during Drawing operations, so you typically don't have to. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_70?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_71?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [PrepareForRender](M_Grasshopper_Kernel_GH_Attributes_1_PrepareForRender.htm) | This method will always be called exactly once prior to Render(). This would be a good place to make sure all the necessary GUI data is up and running. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_72?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_73?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_GH_Attributes_1_Read.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_74?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_75?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [Render](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_Render.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_76?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_77?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST1C0FFBC0\_78?cs=.|vb=.|cpp=::|nu=.|fs=.");Render(GH\_Canvas, Graphics, GH\_CanvasChannel)](M_Grasshopper_Kernel_GH_Attributes_1_Render.htm).) |
| Protected method | [RenderComponentCapsule(GH\_Canvas, Graphics)](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RenderComponentCapsule.htm) | Utility function, draws the complete component capsule including all parameter data. |
| Protected method | [RenderComponentCapsule(GH\_Canvas, Graphics, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean)](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RenderComponentCapsule_1.htm) | Utility function, draws the component capsule including all specified elements. |
| Public methodStatic member | [RenderComponentParameters](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RenderComponentParameters.htm) | Utility method for rendering all component parameters. |
| Protected method | [RenderIncomingWires(GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LST1C0FFBC0\_79?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LST1C0FFBC0\_80?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_ParamWireDisplay)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires.htm) | Utility function for derived classes. This method draws all the wires going into the left side of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_81?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_82?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [RenderIncomingWires(GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LST1C0FFBC0\_83?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LST1C0FFBC0\_84?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, IEnumerableAddLanguageSpecificTextSet("LST1C0FFBC0\_85?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");PenAddLanguageSpecificTextSet("LST1C0FFBC0\_86?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires_1.htm) | Utility function for derived classes. This method draws all the wires going into the left side of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_87?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_88?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RenderToCanvas](M_Grasshopper_Kernel_GH_Attributes_1_RenderToCanvas.htm) | Render these attributes into a Canvas control. This function places calls to PrepareForRender() and Render(), you should override those. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_89?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_90?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [RenderVariableParameterUI](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RenderVariableParameterUI.htm) |  |
| Public method | [RespondToKeyDown](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyDown.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_91?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_92?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToKeyUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyUp.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_93?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_94?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseDoubleClick](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDoubleClick.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_95?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_96?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseDown](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RespondToMouseDown.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_97?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_98?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST1C0FFBC0\_99?cs=.|vb=.|cpp=::|nu=.|fs=.");RespondToMouseDown(GH\_Canvas, GH\_CanvasMouseEvent)](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDown.htm).) |
| Public method | [RespondToMouseMove](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseMove.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_100?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_101?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseUp.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_102?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_103?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [SetupTooltip](M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_SetupTooltip.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_104?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_105?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST1C0FFBC0\_106?cs=.|vb=.|cpp=::|nu=.|fs=.");SetupTooltip(PointF, GH\_TooltipDisplayEventArgs)](M_Grasshopper_Kernel_GH_Attributes_1_SetupTooltip.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_GH_Attributes_1_Write.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST1C0FFBC0\_107?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1C0FFBC0\_108?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_innerBounds](F_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_m_innerBounds.htm) | Represents the Rectangle that contains the component black box. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Attributes Namespace](N_Grasshopper_Kernel_Attributes.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)