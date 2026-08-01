# T_Grasshopper_GUI_GH_CursorServer

﻿ GH\_CursorServer Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_CursorServer Class](../html/T_Grasshopper_GUI_GH_CursorServer.htm "GH_CursorServer Class")

[GH\_CursorServer Properties](../html/Properties_T_Grasshopper_GUI_GH_CursorServer.htm "GH_CursorServer Properties")

[GH\_CursorServer Methods](../html/Methods_T_Grasshopper_GUI_GH_CursorServer.htm "GH_CursorServer Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CursorServer Class |

Class used to cache and set cursors.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST53392EA7\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LST53392EA7\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CursorServer

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_CursorServer
```

```
Public NotInheritable Class GH_CursorServer
```

AddLanguageTabSet("ID1EBCA");

The GH\_CursorServer type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Count](P_Grasshopper_GUI_GH_CursorServer_Count.htm) | Gets the number of cached cursors. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AttachCursor](M_Grasshopper_GUI_GH_CursorServer_AttachCursor.htm) | Attach a cursor to a control. |
| Public method | [Cursor](M_Grasshopper_GUI_GH_CursorServer_Cursor.htm) | Gets a cursor from the cache. |
| Public method | [IsCursor](M_Grasshopper_GUI_GH_CursorServer_IsCursor.htm) | Test for the existence of a cursor. |
| Public method | [ReferenceCursors](M_Grasshopper_GUI_GH_CursorServer_ReferenceCursors.htm) | Reference all the cursor files in a given directory. |
| Public method | [ResetCursor](M_Grasshopper_GUI_GH_CursorServer_ResetCursor.htm) | Reset the cursor of the given control to default. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)