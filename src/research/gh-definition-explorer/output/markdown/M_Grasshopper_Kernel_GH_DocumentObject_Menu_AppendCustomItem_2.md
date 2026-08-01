# M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendCustomItem_2

﻿ GH\_DocumentObject.Menu\_AppendCustomItem Method (ToolStripDropDown, Control, GH\_MenuCustomControl.KeyDownEventHandler, Boolean, Int32, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentObject Class](../html/T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Class")

[GH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Methods")

[Menu\_AppendCustomItem Method](../html/Overload_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendCustomItem.htm "Menu_AppendCustomItem Method ")

[Menu\_AppendCustomItem Method (ToolStripDropDown, Control)](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendCustomItem.htm "Menu_AppendCustomItem Method (ToolStripDropDown, Control)")

[Menu\_AppendCustomItem Method (ToolStripDropDown, Control, GH\_MenuCustomControl.KeyDownEventHandler)](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendCustomItem_1.htm "Menu_AppendCustomItem Method (ToolStripDropDown, Control, GH_MenuCustomControl.KeyDownEventHandler)")

[Menu\_AppendCustomItem Method (ToolStripDropDown, Control, GH\_MenuCustomControl.KeyDownEventHandler, Boolean, Int32, Boolean)](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendCustomItem_2.htm "Menu_AppendCustomItem Method (ToolStripDropDown, Control, GH_MenuCustomControl.KeyDownEventHandler, Boolean, Int32, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentObjectAddLanguageSpecificTextSet("LST6AE7A3D2\_0?cpp=::|nu=.");Menu\_AppendCustomItem Method (ToolStripDropDown, Control, GH\_MenuCustomControlAddLanguageSpecificTextSet("LST6AE7A3D2\_1?cpp=::|nu=.");KeyDownEventHandler, Boolean, Int32, Boolean) |

Utility function for inserting exotic controls into dropdown menus.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool Menu_AppendCustomItem(
	ToolStripDropDown menu,
	Control control,
	KeyDownEventHandler keydown,
	bool enabled,
	int width,
	bool lockOnFocus
)
```

```
Public Shared Function Menu_AppendCustomItem ( 
	menu As ToolStripDropDown,
	control As Control,
	keydown As KeyDownEventHandler,
	enabled As Boolean,
	width As Integer,
	lockOnFocus As Boolean
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

menu
:   Type: [System.Windows.FormsAddLanguageSpecificTextSet("LST6AE7A3D2\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ToolStripDropDown](https://docs.microsoft.com/dotnet/api/system.windows.forms.toolstripdropdown)  
    Dropdown to add a control to.

control
:   Type: [System.Windows.FormsAddLanguageSpecificTextSet("LST6AE7A3D2\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Control](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
    Control to insert.

keydown
:   Type: KeyDownEventHandler  
    Delegate for key-presses.

enabled
:   Type: [SystemAddLanguageSpecificTextSet("LST6AE7A3D2\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, the control will be enabled.

width
:   Type: [SystemAddLanguageSpecificTextSet("LST6AE7A3D2\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Width hint for the control.

lockOnFocus
:   Type: [SystemAddLanguageSpecificTextSet("LST6AE7A3D2\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true and the control gets focus, the rest of the menu will be locked.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentObject Class](T_Grasshopper_Kernel_GH_DocumentObject.htm)

[Menu\_AppendCustomItem Overload](Overload_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendCustomItem.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)