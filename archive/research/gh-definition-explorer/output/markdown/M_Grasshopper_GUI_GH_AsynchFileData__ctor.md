# M_Grasshopper_GUI_GH_AsynchFileData__ctor

﻿ GH\_AsynchFileData Constructor 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_AsynchFileData Class](../html/T_Grasshopper_GUI_GH_AsynchFileData.htm "GH_AsynchFileData Class")

[GH\_AsynchFileData Constructor](../html/M_Grasshopper_GUI_GH_AsynchFileData__ctor.htm "GH_AsynchFileData Constructor ")

[GH\_AsynchFileData Properties](../html/Properties_T_Grasshopper_GUI_GH_AsynchFileData.htm "GH_AsynchFileData Properties")

[GH\_AsynchFileData Methods](../html/Methods_T_Grasshopper_GUI_GH_AsynchFileData.htm "GH_AsynchFileData Methods")

[GH\_AsynchFileData Fields](../html/Fields_T_Grasshopper_GUI_GH_AsynchFileData.htm "GH_AsynchFileData Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AsynchFileData Constructor |

Asynchronous constructor. File properties will be loaded asychronously.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_AsynchFileData(
	string filePath,
	bool harvestThumbnail,
	GH_AsynchFileDataAddLanguageSpecificTextSet("LST312A8C79_0?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChangedDelegate callback
)
```

```
Public Sub New ( 
	filePath As String,
	harvestThumbnail As Boolean,
	callback As GH_AsynchFileDataAddLanguageSpecificTextSet("LST312A8C79_1?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChangedDelegate
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

filePath
:   Type: [SystemAddLanguageSpecificTextSet("LST312A8C79\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Location of file

harvestThumbnail
:   Type: [SystemAddLanguageSpecificTextSet("LST312A8C79\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, thumbnail data will be loaded.

callback
:   Type: [Grasshopper.GUIAddLanguageSpecificTextSet("LST312A8C79\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AsynchFileDataAddLanguageSpecificTextSet("LST312A8C79\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChangedDelegate](T_Grasshopper_GUI_GH_AsynchFileData_FileChangedDelegate.htm)  
    Callback delegate for file changes.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_AsynchFileData Class](T_Grasshopper_GUI_GH_AsynchFileData.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)