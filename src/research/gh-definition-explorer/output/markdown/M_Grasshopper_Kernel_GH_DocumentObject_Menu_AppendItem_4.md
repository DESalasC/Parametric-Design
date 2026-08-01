# M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_4

﻿ GH\_DocumentObject.Menu\_AppendItem Method (ToolStrip, String, EventHandler, Image)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentObject Class](../html/T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Class")

[GH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Methods")

[Menu\_AppendItem Method](../html/Overload_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem.htm "Menu_AppendItem Method ")

[Menu\_AppendItem Method (ToolStrip, String)](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem.htm "Menu_AppendItem Method (ToolStrip, String)")

[Menu\_AppendItem Method (ToolStrip, String, EventHandler)](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_1.htm "Menu_AppendItem Method (ToolStrip, String, EventHandler)")

[Menu\_AppendItem Method (ToolStrip, String, EventHandler, Boolean)](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_2.htm "Menu_AppendItem Method (ToolStrip, String, EventHandler, Boolean)")

[Menu\_AppendItem Method (ToolStrip, String, EventHandler, Image)](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_4.htm "Menu_AppendItem Method (ToolStrip, String, EventHandler, Image)")

[Menu\_AppendItem Method (ToolStrip, String, EventHandler, Boolean, Boolean)](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_3.htm "Menu_AppendItem Method (ToolStrip, String, EventHandler, Boolean, Boolean)")

[Menu\_AppendItem Method (ToolStrip, String, EventHandler, Image, Object)](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_6.htm "Menu_AppendItem Method (ToolStrip, String, EventHandler, Image, Object)")

[Menu\_AppendItem Method (ToolStrip, String, EventHandler, Image, Boolean, Boolean)](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_5.htm "Menu_AppendItem Method (ToolStrip, String, EventHandler, Image, Boolean, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentObjectAddLanguageSpecificTextSet("LSTAA5B5AFF\_0?cpp=::|nu=.");Menu\_AppendItem Method (ToolStrip, String, EventHandler, Image) |

Utility function for appending generic menu items.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static ToolStripMenuItem Menu_AppendItem(
	ToolStrip menu,
	string text,
	EventHandler click,
	Image icon
)
```

```
Public Shared Function Menu_AppendItem ( 
	menu As ToolStrip,
	text As String,
	click As EventHandler,
	icon As Image
) As ToolStripMenuItem
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

menu
:   Type: [System.Windows.FormsAddLanguageSpecificTextSet("LSTAA5B5AFF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ToolStrip](https://docs.microsoft.com/dotnet/api/system.windows.forms.toolstrip)  
    Menu to append item to.

text
:   Type: [SystemAddLanguageSpecificTextSet("LSTAA5B5AFF\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Item text.

click
:   Type: [SystemAddLanguageSpecificTextSet("LSTAA5B5AFF\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");EventHandler](https://docs.microsoft.com/dotnet/api/system.eventhandler)  
    Delegate that handles click events. If nothing, the click event will not be handled.

icon
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTAA5B5AFF\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Image](https://docs.microsoft.com/dotnet/api/system.drawing.image)  
    Item icon, or null for no icon.

#### Return Value

Type: [ToolStripMenuItem](https://docs.microsoft.com/dotnet/api/system.windows.forms.toolstripmenuitem)  
The appended item

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentObject Class](T_Grasshopper_Kernel_GH_DocumentObject.htm)

[Menu\_AppendItem Overload](Overload_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)