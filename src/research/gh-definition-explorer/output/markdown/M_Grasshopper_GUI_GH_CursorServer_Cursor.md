# M_Grasshopper_GUI_GH_CursorServer_Cursor

﻿ GH\_CursorServer.Cursor Method 

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
| GH\_CursorServerAddLanguageSpecificTextSet("LST822D0B8A\_0?cpp=::|nu=.");Cursor Method |

Gets a cursor from the cache.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Cursor Cursor(
	string name
)
```

```
Public Function Cursor ( 
	name As String
) As Cursor
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST822D0B8A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of cursor to retrieve.

#### Return Value

Type: [Cursor](https://docs.microsoft.com/dotnet/api/system.windows.forms.cursor)  
The cursor that is associated with the given name or null if not cursor could be matched.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_CursorServer Class](T_Grasshopper_GUI_GH_CursorServer.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)