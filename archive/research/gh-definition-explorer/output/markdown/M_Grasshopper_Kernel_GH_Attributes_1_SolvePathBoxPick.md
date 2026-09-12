# M_Grasshopper_Kernel_GH_Attributes_1_SolvePathBoxPick

﻿ GH\_Attributes(T).SolvePathBoxPick Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Attributes(T) Class](../html/T_Grasshopper_Kernel_GH_Attributes_1.htm "GH_Attributes(T) Class")

[GH\_Attributes(T) Methods](../html/Methods_T_Grasshopper_Kernel_GH_Attributes_1.htm "GH_Attributes(T) Methods")

[AppendToAttributeTree Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_AppendToAttributeTree.htm "AppendToAttributeTree Method ")

[ExpireLayout Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_ExpireLayout.htm "ExpireLayout Method ")

[InvalidateCanvas Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_InvalidateCanvas.htm "InvalidateCanvas Method ")

[IsIconMode Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_IsIconMode.htm "IsIconMode Method ")

[IsMenuRegion Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_IsMenuRegion.htm "IsMenuRegion Method ")

[IsPickRegion Method](../html/Overload_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm "IsPickRegion Method ")

[IsTooltipRegion Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_IsTooltipRegion.htm "IsTooltipRegion Method ")

[Layout Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_Layout.htm "Layout Method ")

[NewInstanceGuid Method](../html/Overload_Grasshopper_Kernel_GH_Attributes_1_NewInstanceGuid.htm "NewInstanceGuid Method ")

[PerformLayout Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_PerformLayout.htm "PerformLayout Method ")

[PrepareForRender Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_PrepareForRender.htm "PrepareForRender Method ")

[Read Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_Read.htm "Read Method ")

[Render Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_Render.htm "Render Method ")

[RenderIncomingWires Method](../html/Overload_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires.htm "RenderIncomingWires Method ")

[RenderToCanvas Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_RenderToCanvas.htm "RenderToCanvas Method ")

[RespondToKeyDown Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyDown.htm "RespondToKeyDown Method ")

[RespondToKeyUp Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_RespondToKeyUp.htm "RespondToKeyUp Method ")

[RespondToMouseDoubleClick Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDoubleClick.htm "RespondToMouseDoubleClick Method ")

[RespondToMouseDown Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseDown.htm "RespondToMouseDown Method ")

[RespondToMouseMove Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseMove.htm "RespondToMouseMove Method ")

[RespondToMouseUp Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_RespondToMouseUp.htm "RespondToMouseUp Method ")

[SetupTooltip Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_SetupTooltip.htm "SetupTooltip Method ")

[SolvePathBoxPick Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_SolvePathBoxPick.htm "SolvePathBoxPick Method ")

[Write Method](../html/M_Grasshopper_Kernel_GH_Attributes_1_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AttributesAddLanguageSpecificTextSet("LSTB84B9A5E\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTB84B9A5E\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTB84B9A5E\_2?cpp=::|nu=.");SolvePathBoxPick Method |

Utility function for testing window selections with freeform Graphics paths.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool SolvePathBoxPick(
	GraphicsPath path,
	RectangleF box,
	float fuzz,
	GH_PickBox mode
)
```

```
Public Shared Function SolvePathBoxPick ( 
	path As GraphicsPath,
	box As RectangleF,
	fuzz As Single,
	mode As GH_PickBox
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [System.Drawing.Drawing2DAddLanguageSpecificTextSet("LSTB84B9A5E\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GraphicsPath](https://docs.microsoft.com/dotnet/api/system.drawing.drawing2d.graphicspath)  
    Path to test.

box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTB84B9A5E\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Window selection box.

fuzz
:   Type: [SystemAddLanguageSpecificTextSet("LSTB84B9A5E\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Fuzzy pixels around object.

mode
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTB84B9A5E\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PickBox](T_Grasshopper_Kernel_GH_PickBox.htm)  
    Selection mode to apply.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if box contains the path.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_AttributesAddLanguageSpecificTextSet("LSTB84B9A5E\_7?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB84B9A5E\_8?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_Attributes_1.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)