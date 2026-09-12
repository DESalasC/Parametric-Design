# T_Grasshopper_Kernel_GH_Attributes_1

﻿ GH\_Attributes(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Attributes(T) Class](../html/T_Grasshopper_Kernel_GH_Attributes_1.htm "GH_Attributes(T) Class")

[GH\_Attributes(T) Constructor](../html/M_Grasshopper_Kernel_GH_Attributes_1__ctor.htm "GH_Attributes(T) Constructor ")

[GH\_Attributes(T) Properties](../html/Properties_T_Grasshopper_Kernel_GH_Attributes_1.htm "GH_Attributes(T) Properties")

[GH\_Attributes(T) Methods](../html/Methods_T_Grasshopper_Kernel_GH_Attributes_1.htm "GH_Attributes(T) Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AttributesAddLanguageSpecificTextSet("LST996641DF\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST996641DF\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

Derive from this class rather than implementing IGH\_Attributes from scratch.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST996641DF\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST996641DF\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AttributesAddLanguageSpecificTextSet("LST996641DF\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST996641DF\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");  
    [Grasshopper.Kernel.AttributesAddLanguageSpecificTextSet("LST996641DF\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ComponentAttributes](T_Grasshopper_Kernel_Attributes_GH_ComponentAttributes.htm)  
    [Grasshopper.Kernel.AttributesAddLanguageSpecificTextSet("LST996641DF\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FloatingParamAttributes](T_Grasshopper_Kernel_Attributes_GH_FloatingParamAttributes.htm)  
    [Grasshopper.Kernel.AttributesAddLanguageSpecificTextSet("LST996641DF\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_LinkedParamAttributes](T_Grasshopper_Kernel_Attributes_GH_LinkedParamAttributes.htm)  
    [Grasshopper.Kernel.AttributesAddLanguageSpecificTextSet("LST996641DF\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ResizableAttributesAddLanguageSpecificTextSet("LST996641DF\_10?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST996641DF\_11?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Attributes_GH_ResizableAttributes_1.htm)  
    [Grasshopper.KernelAddLanguageSpecificTextSet("LST996641DF\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ComponentParamServerAddLanguageSpecificTextSet("LST996641DF\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");NullParamAttributes](T_Grasshopper_Kernel_GH_ComponentParamServer_NullParamAttributes.htm)

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_Attributes<T> : IGH_Attributes
where T : IGH_DocumentObject
```

```
Public MustInherit Class GH_Attributes(Of T As IGH_DocumentObject)
	Implements IGH_Attributes
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T
:   Type of the objects that owns these attributes.

The GH\_AttributesAddLanguageSpecificTextSet("LST996641DF\_14?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST996641DF\_15?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_AttributesAddLanguageSpecificTextSet("LST996641DF\_16?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST996641DF\_17?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](M_Grasshopper_Kernel_GH_Attributes_1__ctor.htm) | Construct a new instance of this class. |

[Top](#PageHeader)

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

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendToAttributeTree](M_Grasshopper_Kernel_GH_Attributes_1_AppendToAttributeTree.htm) | Recursively append these attributes and all child attributes to the attribute list. |
| Public method | [ExpireLayout](M_Grasshopper_Kernel_GH_Attributes_1_ExpireLayout.htm) | Expires the entire layout of the attributes. When overridden, implementer *must* place a call to the base class ExpireLayout(). |
| Public method | [InvalidateCanvas](M_Grasshopper_Kernel_GH_Attributes_1_InvalidateCanvas.htm) | If the mouse location should cause a canvas invalidation then return true. You only need to override this function if you draw objects that are dependant on cursor positions outside the bounds of the attributes. |
| Protected methodStatic member | [IsIconMode](M_Grasshopper_Kernel_GH_Attributes_1_IsIconMode.htm) | Utility function for determining Icon display modes. If the supplied mode is ::application, then it will be adjusted to match the current app settings. |
| Public method | [IsMenuRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsMenuRegion.htm) | Determines whether a point is available for context menu popups. By default, IsMenuRegion calls IsPickRegion(PointF). |
| Public method | [IsPickRegion(PointF)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm) | Determines whether a point is within the pickable region for this object. By default, any point inside the Bounds is treated as pickable. |
| Public method | [IsPickRegion(RectangleF, GH\_PickBox)](M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion_1.htm) | Determines whether a rectangle is a valid pick region for this object. By default, the picking rectangle is intersected with the Bounds rectangle. |
| Public method | [IsTooltipRegion](M_Grasshopper_Kernel_GH_Attributes_1_IsTooltipRegion.htm) | Determines whether a point is available for tooltip popups. By default, IsMenuRegion calls IsTooltipRegion(PointF). |
| Protected method | [Layout](M_Grasshopper_Kernel_GH_Attributes_1_Layout.htm) | Perform dedicated layout logic specific to this particular DocumentObject. This method is called from PerformLayout if the existing layout is stale. |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LST996641DF\_18?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid.htm) | Generate a new instance GUID for the owner object. |
| Public method | [NewInstanceGuid(Guid)](M_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid_1.htm) | Generate a new instance GUID for the owner object. Do not use this overload unless you're > 1.95m and called David. |
| Public method | [PerformLayout](M_Grasshopper_Kernel_GH_Attributes_1_PerformLayout.htm) | Recompute the layout for these attributes. This function is automatically called during Drawing operations, so you typically don't have to. |
| Protected method | [PrepareForRender](M_Grasshopper_Kernel_GH_Attributes_1_PrepareForRender.htm) | This method will always be called exactly once prior to Render(). This would be a good place to make sure all the necessary GUI data is up and running. |
| Public method | [Read](M_Grasshopper_Kernel_GH_Attributes_1_Read.htm) |  |
| Protected method | [Render](M_Grasshopper_Kernel_GH_Attributes_1_Render.htm) | Override this function to supply custom Render logic. |
| Protected method | [RenderIncomingWires(GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LST996641DF\_19?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LST996641DF\_20?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_ParamWireDisplay)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires.htm) | Utility function for derived classes. This method draws all the wires going into the left side of the attributes. |
| Protected method | [RenderIncomingWires(GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LST996641DF\_21?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LST996641DF\_22?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, IEnumerableAddLanguageSpecificTextSet("LST996641DF\_23?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");PenAddLanguageSpecificTextSet("LST996641DF\_24?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires_1.htm) | Utility function for derived classes. This method draws all the wires going into the left side of the attributes. |
| Public method | [RenderToCanvas](M_Grasshopper_Kernel_GH_Attributes_1_RenderToCanvas.htm) | Render these attributes into a Canvas control. This function places calls to PrepareForRender() and Render(), you should override those. |
| Public method | [RespondToKeyDown](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyDown.htm) |  |
| Public method | [RespondToKeyUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyUp.htm) |  |
| Public method | [RespondToMouseDoubleClick](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDoubleClick.htm) |  |
| Public method | [RespondToMouseDown](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDown.htm) |  |
| Public method | [RespondToMouseMove](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseMove.htm) |  |
| Public method | [RespondToMouseUp](M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseUp.htm) |  |
| Public method | [SetupTooltip](M_Grasshopper_Kernel_GH_Attributes_1_SetupTooltip.htm) | Populates the Grasshopper tooltip with all relevant data. If this function returns True, it is assumed that all possible fields have been filled out and the tooltip is ready for display. |
| Public methodStatic member | [SolvePathBoxPick](M_Grasshopper_Kernel_GH_Attributes_1_SolvePathBoxPick.htm) | Utility function for testing window selections with freeform Graphics paths. |
| Public method | [Write](M_Grasshopper_Kernel_GH_Attributes_1_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)