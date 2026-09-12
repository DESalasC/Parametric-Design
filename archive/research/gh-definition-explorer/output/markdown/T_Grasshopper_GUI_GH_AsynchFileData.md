# T_Grasshopper_GUI_GH_AsynchFileData

﻿ GH\_AsynchFileData Class

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
| GH\_AsynchFileData Class |

This class provides asynchronous methods to keep tabs on a file.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTEE143E17\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LSTEE143E17\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AsynchFileData

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_AsynchFileData : IDisposable
```

```
Public Class GH_AsynchFileData
	Implements IDisposable
```

AddLanguageTabSet("ID1EBCA");

The GH\_AsynchFileData type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_AsynchFileData](M_Grasshopper_GUI_GH_AsynchFileData__ctor.htm) | Asynchronous constructor. File properties will be loaded asychronously. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Callback](P_Grasshopper_GUI_GH_AsynchFileData_Callback.htm) | Gets or sets the callback delegate to be used when properties are updated. |
| Public property | [FileCreated](P_Grasshopper_GUI_GH_AsynchFileData_FileCreated.htm) | Gets the date at which the file was created. |
| Public property | [FileExists](P_Grasshopper_GUI_GH_AsynchFileData_FileExists.htm) | Gets whether the file exists. Note that this property returns false if DataExists=False, regardless of whether the file exists. |
| Public property | [FileLastChanged](P_Grasshopper_GUI_GH_AsynchFileData_FileLastChanged.htm) | Gets the date at which the file was last changed. |
| Public property | [FileSize](P_Grasshopper_GUI_GH_AsynchFileData_FileSize.htm) | Gets the size of the file. |
| Public property | [FileThumbnail](P_Grasshopper_GUI_GH_AsynchFileData_FileThumbnail.htm) | Gets the thumbnail bitmap associated with the file. |
| Public property | [HarvestThumbnail](P_Grasshopper_GUI_GH_AsynchFileData_HarvestThumbnail.htm) | Gets or sets whether the thumbnail ought to be parsed. At the moment this only makes sense for GH/GHX files. |
| Public property | [IsFileData](P_Grasshopper_GUI_GH_AsynchFileData_IsFileData.htm) | Gets whether the data has been retrieved at least once. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](M_Grasshopper_GUI_GH_AsynchFileData_Dispose.htm) | Releases all resources used by the GH\_AsynchFileData |
| Public method | [UpdateProperties](M_Grasshopper_GUI_GH_AsynchFileData_UpdateProperties.htm) | Updates all file properties on the thread on which this method is called. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public field | [FilePath](F_Grasshopper_GUI_GH_AsynchFileData_FilePath.htm) | Gets the location this instance is watching. |
| Public field | [IsLocal](F_Grasshopper_GUI_GH_AsynchFileData_IsLocal.htm) | Gets whether Grasshopper thinks the file it is watching is on a local machine. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)