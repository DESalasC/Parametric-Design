# M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendTextItem

﻿ GH\_DocumentObject.Menu\_AppendTextItem Method (ToolStripDropDown, String, GH\_MenuTextBox.KeyDownEventHandler, GH\_MenuTextBox.TextChangedEventHandler, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentObject Class](../html/T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Class")

[GH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Methods")

[Menu\_AppendTextItem Method](../html/Overload_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendTextItem.htm "Menu_AppendTextItem Method ")

[Menu\_AppendTextItem Method (ToolStripDropDown, String, GH\_MenuTextBox.KeyDownEventHandler, GH\_MenuTextBox.TextChangedEventHandler, Boolean)](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendTextItem.htm "Menu_AppendTextItem Method (ToolStripDropDown, String, GH_MenuTextBox.KeyDownEventHandler, GH_MenuTextBox.TextChangedEventHandler, Boolean)")

[Menu\_AppendTextItem Method (ToolStripDropDown, String, GH\_MenuTextBox.KeyDownEventHandler, GH\_MenuTextBox.TextChangedEventHandler, Boolean, Int32, Boolean)](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendTextItem_1.htm "Menu_AppendTextItem Method (ToolStripDropDown, String, GH_MenuTextBox.KeyDownEventHandler, GH_MenuTextBox.TextChangedEventHandler, Boolean, Int32, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentObjectAddLanguageSpecificTextSet("LSTEA547A5F\_0?cpp=::|nu=.");Menu\_AppendTextItem Method (ToolStripDropDown, String, GH\_MenuTextBoxAddLanguageSpecificTextSet("LSTEA547A5F\_1?cpp=::|nu=.");KeyDownEventHandler, GH\_MenuTextBoxAddLanguageSpecificTextSet("LSTEA547A5F\_2?cpp=::|nu=.");TextChangedEventHandler, Boolean) |

Utility function for inserting text boxes into menus.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static ToolStripTextBox Menu_AppendTextItem(
	ToolStripDropDown menu,
	string text,
	GH_MenuTextBoxAddLanguageSpecificTextSet("LSTEA547A5F_3?cs=.|vb=.|cpp=::|nu=.|fs=.");KeyDownEventHandler keydown,
	GH_MenuTextBoxAddLanguageSpecificTextSet("LSTEA547A5F_4?cs=.|vb=.|cpp=::|nu=.|fs=.");TextChangedEventHandler textchanged,
	bool lockOnFocus
)
```

```
Public Shared Function Menu_AppendTextItem ( 
	menu As ToolStripDropDown,
	text As String,
	keydown As GH_MenuTextBoxAddLanguageSpecificTextSet("LSTEA547A5F_5?cs=.|vb=.|cpp=::|nu=.|fs=.");KeyDownEventHandler,
	textchanged As GH_MenuTextBoxAddLanguageSpecificTextSet("LSTEA547A5F_6?cs=.|vb=.|cpp=::|nu=.|fs=.");TextChangedEventHandler,
	lockOnFocus As Boolean
) As ToolStripTextBox
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

menu
:   Type: [System.Windows.FormsAddLanguageSpecificTextSet("LSTEA547A5F\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");ToolStripDropDown](https://docs.microsoft.com/dotnet/api/system.windows.forms.toolstripdropdown)  
    Menu to add a textbox to.

text
:   Type: [SystemAddLanguageSpecificTextSet("LSTEA547A5F\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Content of textbox.

keydown
:   Type: [Grasshopper.GUIAddLanguageSpecificTextSet("LSTEA547A5F\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MenuTextBoxAddLanguageSpecificTextSet("LSTEA547A5F\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");KeyDownEventHandler](T_Grasshopper_GUI_GH_MenuTextBox_KeyDownEventHandler.htm)  
    Delegate for the KeyDown event.

textchanged
:   Type: [Grasshopper.GUIAddLanguageSpecificTextSet("LSTEA547A5F\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MenuTextBoxAddLanguageSpecificTextSet("LSTEA547A5F\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");TextChangedEventHandler](T_Grasshopper_GUI_GH_MenuTextBox_TextChangedEventHandler.htm)  
    Delegate for the TextChanged event.

lockOnFocus
:   Type: [SystemAddLanguageSpecificTextSet("LSTEA547A5F\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, then a GotFocus event will lock the other menu items.

#### Return Value

Type: [ToolStripTextBox](https://docs.microsoft.com/dotnet/api/system.windows.forms.toolstriptextbox)  
The appended text box item.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentObject Class](T_Grasshopper_Kernel_GH_DocumentObject.htm)

[Menu\_AppendTextItem Overload](Overload_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendTextItem.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)