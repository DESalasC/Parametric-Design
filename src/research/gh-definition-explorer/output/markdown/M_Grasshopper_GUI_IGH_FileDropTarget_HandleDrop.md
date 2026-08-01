# M_Grasshopper_GUI_IGH_FileDropTarget_HandleDrop

﻿ IGH\_FileDropTarget.HandleDrop Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[IGH\_FileDropTarget Interface](../html/T_Grasshopper_GUI_IGH_FileDropTarget.htm "IGH_FileDropTarget Interface")

[IGH\_FileDropTarget Methods](../html/Methods_T_Grasshopper_GUI_IGH_FileDropTarget.htm "IGH_FileDropTarget Methods")

[AcceptableFile Method](../html/M_Grasshopper_GUI_IGH_FileDropTarget_AcceptableFile.htm "AcceptableFile Method ")

[HandleDrop Method](../html/M_Grasshopper_GUI_IGH_FileDropTarget_HandleDrop.htm "HandleDrop Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_FileDropTargetAddLanguageSpecificTextSet("LST82806348\_0?cpp=::|nu=.");HandleDrop Method |

Handle a file drop.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool HandleDrop(
	string path,
	PointF mouse_pt
)
```

```
Function HandleDrop ( 
	path As String,
	mouse_pt As PointF
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [SystemAddLanguageSpecificTextSet("LST82806348\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Path of file to handle.

mouse\_pt
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST82806348\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Point at which the drop occured.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_FileDropTarget Interface](T_Grasshopper_GUI_IGH_FileDropTarget.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)