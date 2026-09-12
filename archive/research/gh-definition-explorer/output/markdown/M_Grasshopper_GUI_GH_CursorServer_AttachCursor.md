# M_Grasshopper_GUI_GH_CursorServer_AttachCursor

﻿ GH\_CursorServer.AttachCursor Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_CursorServer Class](../html/T_Grasshopper_GUI_GH_CursorServer.htm "GH_CursorServer Class")

[GH\_CursorServer Methods](../html/Methods_T_Grasshopper_GUI_GH_CursorServer.htm "GH_CursorServer Methods")

[AttachCursor Method](../html/M_Grasshopper_GUI_GH_CursorServer_AttachCursor.htm "AttachCursor Method ")

[Cursor Method](../html/M_Grasshopper_GUI_GH_CursorServer_Cursor.htm "Cursor Method ")

[IsCursor Method](../html/M_Grasshopper_GUI_GH_CursorServer_IsCursor.htm "IsCursor Method ")

[ReferenceCursors Method](../html/M_Grasshopper_GUI_GH_CursorServer_ReferenceCursors.htm "ReferenceCursors Method ")

[ResetCursor Method](../html/M_Grasshopper_GUI_GH_CursorServer_ResetCursor.htm "ResetCursor Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CursorServerAddLanguageSpecificTextSet("LST9CB4057A\_0?cpp=::|nu=.");AttachCursor Method |

Attach a cursor to a control.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool AttachCursor(
	Control control,
	string name
)
```

```
Public Function AttachCursor ( 
	control As Control,
	name As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

control
:   Type: [System.Windows.FormsAddLanguageSpecificTextSet("LST9CB4057A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Control](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
    Control to assign cursor to.

name
:   Type: [SystemAddLanguageSpecificTextSet("LST9CB4057A\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of cursor to assign. This is the filename of the
    original cursor file minus the extension.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if cursor was assigned, or false if no matching cursor could be found.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_CursorServer Class](T_Grasshopper_GUI_GH_CursorServer.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)