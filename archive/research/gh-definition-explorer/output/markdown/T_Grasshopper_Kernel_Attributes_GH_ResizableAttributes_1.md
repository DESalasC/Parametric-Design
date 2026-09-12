# T_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1

﻿ GH\_ResizableAttributes(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Attributes](../html/N_Grasshopper_Kernel_Attributes.htm "Grasshopper.Kernel.Attributes")

[GH\_ResizableAttributes(T) Class](../html/T_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1.htm "GH_ResizableAttributes(T) Class")

[GH\_ResizableAttributes(T) Constructor](../html/M_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1__ctor.htm "GH_ResizableAttributes(T) Constructor ")

[GH\_ResizableAttributes(T) Properties](../html/Properties_T_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1.htm "GH_ResizableAttributes(T) Properties")

[GH\_ResizableAttributes(T) Methods](../html/Methods_T_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1.htm "GH_ResizableAttributes(T) Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ResizableAttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST7C0D6C6F\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

These Attributes provide basic resizing logic.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST7C0D6C6F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.KernelAddLanguageSpecificTextSet("LST7C0D6C6F\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Attributes](T_Grasshopper_Kernel_GH_Attributes_1.htm)AddLanguageSpecificTextSet("LST7C0D6C6F\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST7C0D6C6F\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Kernel.AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ResizableAttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_7?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_8?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");

**Namespace:**
 [Grasshopper.Kernel.Attributes](N_Grasshopper_Kernel_Attributes.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_ResizableAttributes<T> : GH_Attributes<T>
where T : IGH_DocumentObject
```

```
Public MustInherit Class GH_ResizableAttributes(Of T As IGH_DocumentObject)
	Inherits GH_Attributes(Of T)
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T

The GH\_ResizableAttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_ResizableAttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_11?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_12?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](M_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1__ctor.htm) | Initializes a new instance of the GH\_ResizableAttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_13?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_14?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AllowMessageBalloon](P_Grasshopper_Kernel_GH_Attributes_1_AllowMessageBalloon.htm) | Gets a value indicating whether these attributes allow warning and error balloons to be drawn on top of them. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Bounds](P_Grasshopper_Kernel_GH_Attributes_1_Bounds.htm) | Gets the rectangle that contains the active content of the attributes. Typically the Contents determine the active area for menus, tooltips etc. Attributes are not supposed to draw objects beyond the Bounds. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_17?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_18?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [DocObject](P_Grasshopper_Kernel_GH_Attributes_1_DocObject.htm) | Gets the owner object of these attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [GetTopLevel](P_Grasshopper_Kernel_GH_Attributes_1_GetTopLevel.htm) | Gets the top-level attributes of the attribute stack these attributes belong to. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_21?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_22?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [HasInputGrip](P_Grasshopper_Kernel_GH_Attributes_1_HasInputGrip.htm) | Gets a value indicating whether or not these attributes have an input grip. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_23?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_24?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [HasOutputGrip](P_Grasshopper_Kernel_GH_Attributes_1_HasOutputGrip.htm) | Gets a value indicating whether or not these attributes have an output grip. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_25?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_26?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [InputGrip](P_Grasshopper_Kernel_GH_Attributes_1_InputGrip.htm) | Gets the input grip location for these attributes. If HasInputGrip equals False, this point is meaningless. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_27?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_28?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [InstanceGuid](P_Grasshopper_Kernel_GH_Attributes_1_InstanceGuid.htm) | Gets the instance ID of the document object that owns these attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_29?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_30?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [IsTopLevel](P_Grasshopper_Kernel_GH_Attributes_1_IsTopLevel.htm) | Gets whether these attributes are top\_level (i.e. no Parent attributes) (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_31?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_32?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected property | [MaximumSize](P_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1_MaximumSize.htm) |  |
| Protected property | [MinimumSize](P_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1_MinimumSize.htm) |  |
| Public property | [OutputGrip](P_Grasshopper_Kernel_GH_Attributes_1_OutputGrip.htm) | Gets the output grip location for these attributes. If HasOutputGrip equals False, this point is meaningless. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_33?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_34?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Owner](P_Grasshopper_Kernel_GH_Attributes_1_Owner.htm) | Gets the type-safe owner object of these attributes. This property is identical to the DocObject property. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_35?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_36?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Parent](P_Grasshopper_Kernel_GH_Attributes_1_Parent.htm) | Gets or sets the parent attributes. Top level attributes do not have parents. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_37?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_38?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [PathName](P_Grasshopper_Kernel_GH_Attributes_1_PathName.htm) | Get a description of the location of these attributes within the local attribute stack. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_39?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_40?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Pivot](P_Grasshopper_Kernel_GH_Attributes_1_Pivot.htm) | Gets or sets the pivot for these attributes. The pivot controls the general placement of the attributes. If you want to move the attributes, change the pivot location. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_41?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_42?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public property | [Selected](P_Grasshopper_Kernel_GH_Attributes_1_Selected.htm) | Gets or sets the selected state of the top-level attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_43?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_44?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected property | [SizingBorders](P_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1_SizingBorders.htm) |  |
| Public property | [TooltipEnabled](P_Grasshopper_Kernel_GH_Attributes_1_TooltipEnabled.htm) | Gets the tooltip enabled value. If False, no further tooltip functions will be called. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_45?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_46?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendToAttributeTree](M_Grasshopper_Kernel_GH_Attributes_1_AppendToAttributeTree.htm) | Recursively append these attributes and all child attributes to the attribute list. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_47?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_48?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [ExpireLayout](M_Grasshopper_Kernel_GH_Attributes_1_ExpireLayout.htm) | Expires the entire layout of the attributes. When overridden, implementer *must* place a call to the base class ExpireLayout(). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_49?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_50?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [InvalidateCanvas](M_Grasshopper_Kernel_GH_Attributes_1_InvalidateCanvas.htm) | If the mouse location should cause a canvas invalidation then return true. You only need to override this function if you draw objects that are dependant on cursor positions outside the bounds of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_51?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_52?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsMenuRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsMenuRegion.htm) | Determines whether a point is available for context menu popups. By default, IsMenuRegion calls IsPickRegion(PointF). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_53?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_54?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsPickRegion(PointF)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm) | Determines whether a point is within the pickable region for this object. By default, any point inside the Bounds is treated as pickable. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_55?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_56?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsPickRegion(RectangleF, GH\_PickBox)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion_1.htm) | Determines whether a rectangle is a valid pick region for this object. By default, the picking rectangle is intersected with the Bounds rectangle. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_57?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_58?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [IsTooltipRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsTooltipRegion.htm) | Determines whether a point is available for tooltip popups. By default, IsMenuRegion calls IsTooltipRegion(PointF). (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_59?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_60?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [Layout](M_Grasshopper_Kernel_GH_Attributes_1_Layout.htm) | Perform dedicated layout logic specific to this particular DocumentObject. This method is called from PerformLayout if the existing layout is stale. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_61?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_62?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LST7C0D6C6F\_63?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid.htm) | Generate a new instance GUID for the owner object. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_64?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_65?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [NewInstanceGuid(Guid)](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid_1.htm) | Generate a new instance GUID for the owner object. Do not use this overload unless you're > 1.95m and called David. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_66?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_67?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [PerformLayout](M_Grasshopper_Kernel_GH_Attributes_1_PerformLayout.htm) | Recompute the layout for these attributes. This function is automatically called during Drawing operations, so you typically don't have to. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_68?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_69?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [PrepareForRender](M_Grasshopper_Kernel_GH_Attributes_1_PrepareForRender.htm) | This method will always be called exactly once prior to Render(). This would be a good place to make sure all the necessary GUI data is up and running. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_70?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_71?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_GH_Attributes_1_Read.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_72?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_73?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [Render](M_Grasshopper_Kernel_GH_Attributes_1_Render.htm) | Override this function to supply custom Render logic. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_74?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_75?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [RenderIncomingWires(GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LST7C0D6C6F\_76?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LST7C0D6C6F\_77?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_ParamWireDisplay)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires.htm) | Utility function for derived classes. This method draws all the wires going into the left side of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_78?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_79?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Protected method | [RenderIncomingWires(GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LST7C0D6C6F\_80?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LST7C0D6C6F\_81?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, IEnumerableAddLanguageSpecificTextSet("LST7C0D6C6F\_82?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");PenAddLanguageSpecificTextSet("LST7C0D6C6F\_83?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires_1.htm) | Utility function for derived classes. This method draws all the wires going into the left side of the attributes. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_84?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_85?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RenderToCanvas](M_Grasshopper_Kernel_GH_Attributes_1_RenderToCanvas.htm) | Render these attributes into a Canvas control. This function places calls to PrepareForRender() and Render(), you should override those. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_86?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_87?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToKeyDown](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyDown.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_88?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_89?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToKeyUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyUp.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_90?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_91?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseDoubleClick](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDoubleClick.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_92?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_93?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [RespondToMouseDown](M_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1_RespondToMouseDown.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_94?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_95?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST7C0D6C6F\_96?cs=.|vb=.|cpp=::|nu=.|fs=.");RespondToMouseDown(GH\_Canvas, GH\_CanvasMouseEvent)](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDown.htm).) |
| Public method | [RespondToMouseMove](M_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1_RespondToMouseMove.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_97?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_98?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST7C0D6C6F\_99?cs=.|vb=.|cpp=::|nu=.|fs=.");RespondToMouseMove(GH\_Canvas, GH\_CanvasMouseEvent)](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseMove.htm).) |
| Public method | [RespondToMouseUp](M_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1_RespondToMouseUp.htm) | (Overrides [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_100?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_101?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST7C0D6C6F\_102?cs=.|vb=.|cpp=::|nu=.|fs=.");RespondToMouseUp(GH\_Canvas, GH\_CanvasMouseEvent)](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseUp.htm).) |
| Public method | [SetupTooltip](M_Grasshopper_Kernel_GH_Attributes_1_SetupTooltip.htm) | Populates the Grasshopper tooltip with all relevant data. If this function returns True, it is assumed that all possible fields have been filled out and the tooltip is ready for display. (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_103?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_104?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_GH_Attributes_1_Write.htm) | (Inherited from [GH\_AttributesAddLanguageSpecificTextSet("LST7C0D6C6F\_105?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7C0D6C6F\_106?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_GH_Attributes_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Attributes Namespace](N_Grasshopper_Kernel_Attributes.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)