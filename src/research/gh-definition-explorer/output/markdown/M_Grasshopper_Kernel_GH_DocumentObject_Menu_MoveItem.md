# M_Grasshopper_Kernel_GH_DocumentObject_Menu_MoveItem

﻿ GH\_DocumentObject.Menu\_MoveItem Method (ToolStripItem, Boolean, String[])

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentObject Class](../html/T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Class")

[GH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Methods")

[Menu\_MoveItem Method](../html/Overload_Grasshopper_Kernel_GH_DocumentObject_Menu_MoveItem.htm "Menu_MoveItem Method ")

[Menu\_MoveItem Method (ToolStripItem, String[])](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_MoveItem_1.htm "Menu_MoveItem Method (ToolStripItem, String[])")

[Menu\_MoveItem Method (ToolStripItem, Boolean, String[])](../html/M_Grasshopper_Kernel_GH_DocumentObject_Menu_MoveItem.htm "Menu_MoveItem Method (ToolStripItem, Boolean, String[])")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentObjectAddLanguageSpecificTextSet("LSTCC832CCC\_0?cpp=::|nu=.");Menu\_MoveItem Method (ToolStripItem, Boolean, AddLanguageSpecificTextSet("LSTCC832CCC\_1?cpp=array&lt;");StringAddLanguageSpecificTextSet("LSTCC832CCC\_2?cpp=&gt;|vb=()|nu=[]");) |

Utility function for moving menu items.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool Menu_MoveItem(
	ToolStripItem item,
	bool insertBelow,
	params string[] targets
)
```

```
Public Shared Function Menu_MoveItem ( 
	item As ToolStripItem,
	insertBelow As Boolean,
	ParamArray targets As String()
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item
:   Type: [System.Windows.FormsAddLanguageSpecificTextSet("LSTCC832CCC\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ToolStripItem](https://docs.microsoft.com/dotnet/api/system.windows.forms.toolstripitem)  
    Item to move, it must already be part of the dropdown menu.

insertBelow
:   Type: [SystemAddLanguageSpecificTextSet("LSTCC832CCC\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, the item will be inserted below the match, if false, above the match.

targets
:   Type: AddLanguageSpecificTextSet("LSTCC832CCC\_5?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LSTCC832CCC\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LSTCC832CCC\_7?cpp=&gt;|vb=()|nu=[]");  
    Names of move to targets, the item will be inserted next to the first name, if that fails the second, etc. etc.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentObject Class](T_Grasshopper_Kernel_GH_DocumentObject.htm)

[Menu\_MoveItem Overload](Overload_Grasshopper_Kernel_GH_DocumentObject_Menu_MoveItem.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)