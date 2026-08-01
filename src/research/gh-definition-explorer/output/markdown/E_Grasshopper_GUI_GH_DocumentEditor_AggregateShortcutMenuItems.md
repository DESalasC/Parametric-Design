# E_Grasshopper_GUI_GH_DocumentEditor_AggregateShortcutMenuItems

﻿ GH\_DocumentEditor.AggregateShortcutMenuItems Event

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_DocumentEditor Class](../html/T_Grasshopper_GUI_GH_DocumentEditor.htm "GH_DocumentEditor Class")

[GH\_DocumentEditor Events](../html/Events_T_Grasshopper_GUI_GH_DocumentEditor.htm "GH_DocumentEditor Events")

[AggregateShortcutMenuItems Event](../html/E_Grasshopper_GUI_GH_DocumentEditor_AggregateShortcutMenuItems.htm "AggregateShortcutMenuItems Event")

[EditorFoldStateChanged Event](../html/E_Grasshopper_GUI_GH_DocumentEditor_EditorFoldStateChanged.htm "EditorFoldStateChanged Event")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentEditorAddLanguageSpecificTextSet("LST96EFD770\_0?cpp=::|nu=.");AggregateShortcutMenuItems Event |

This event is raised whenever a GH\_DocumentEditor collects all shortcuttable menu items.
If you added items to the menu and you want to be able to have custom shortcuts on these items,
you must handle this event and insert your own items.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static event GH_DocumentEditorAddLanguageSpecificTextSet("LST96EFD770_1?cs=.|vb=.|cpp=::|nu=.|fs=.");AggregateShortcutMenuItemsEventHandler AggregateShortcutMenuItems
```

```
Public Shared Event AggregateShortcutMenuItems As GH_DocumentEditorAddLanguageSpecificTextSet("LST96EFD770_2?cs=.|vb=.|cpp=::|nu=.|fs=.");AggregateShortcutMenuItemsEventHandler
```

AddLanguageTabSet("ID0EBCA");

#### Value

Type: [Grasshopper.GUIAddLanguageSpecificTextSet("LST96EFD770\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocumentEditorAddLanguageSpecificTextSet("LST96EFD770\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");AggregateShortcutMenuItemsEventHandler](T_Grasshopper_GUI_GH_DocumentEditor_AggregateShortcutMenuItemsEventHandler.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentEditor Class](T_Grasshopper_GUI_GH_DocumentEditor.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)