# M_Grasshopper_Kernel_GH_Attributes_1_IsIconMode

﻿ GH\_Attributes(T).IsIconMode Method 

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
| GH\_AttributesAddLanguageSpecificTextSet("LST6E5764D6\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST6E5764D6\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST6E5764D6\_2?cpp=::|nu=.");IsIconMode Method |

Utility function for determining Icon display modes.
If the supplied mode is ::application, then it will be adjusted to match the current app settings.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected static bool IsIconMode(
	GH_IconDisplayMode mode
)
```

```
Protected Shared Function IsIconMode ( 
	mode As GH_IconDisplayMode
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

mode
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST6E5764D6\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IconDisplayMode](T_Grasshopper_Kernel_GH_IconDisplayMode.htm)

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_AttributesAddLanguageSpecificTextSet("LST6E5764D6\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST6E5764D6\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_Attributes_1.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)