# M_Grasshopper_Kernel_IGH_Attributes_InvalidateCanvas

﻿ IGH\_Attributes.InvalidateCanvas Method 

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
| IGH\_AttributesAddLanguageSpecificTextSet("LSTA9C138FB\_0?cpp=::|nu=.");InvalidateCanvas Method |

If the mouse location should cause a canvas invalidation then return true.
You only need to override this function if you draw objects that are dependant
on cursor positions outside the bounds of the attributes.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool InvalidateCanvas(
	GH_Canvas canvas,
	GH_CanvasMouseEvent e
)
```

```
Function InvalidateCanvas ( 
	canvas As GH_Canvas,
	e As GH_CanvasMouseEvent
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

canvas
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LSTA9C138FB\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Canvas](T_Grasshopper_GUI_Canvas_GH_Canvas.htm)  
    Canvas to potentially invalidate.

e
:   Type: [Grasshopper.GUIAddLanguageSpecificTextSet("LSTA9C138FB\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CanvasMouseEvent](T_Grasshopper_GUI_GH_CanvasMouseEvent.htm)  
    Event arguments for canvas mousemove.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the canvas ought to be invalidated.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Attributes Interface](T_Grasshopper_Kernel_IGH_Attributes.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)