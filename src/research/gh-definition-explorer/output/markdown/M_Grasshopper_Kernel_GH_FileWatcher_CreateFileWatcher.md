# M_Grasshopper_Kernel_GH_FileWatcher_CreateFileWatcher

﻿ GH\_FileWatcher.CreateFileWatcher Method (String, GH\_FileWatcherEvents, GH\_FileWatcher.FileChanged)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_FileWatcher Class](../html/T_Grasshopper_Kernel_GH_FileWatcher.htm "GH_FileWatcher Class")

[GH\_FileWatcher Methods](../html/Methods_T_Grasshopper_Kernel_GH_FileWatcher.htm "GH_FileWatcher Methods")

[CreateFileWatcher Method](../html/Overload_Grasshopper_Kernel_GH_FileWatcher_CreateFileWatcher.htm "CreateFileWatcher Method ")

[CreateFileWatcher Method (String, GH\_FileWatcherEvents, GH\_FileWatcher.FileChanged)](../html/M_Grasshopper_Kernel_GH_FileWatcher_CreateFileWatcher.htm "CreateFileWatcher Method (String, GH_FileWatcherEvents, GH_FileWatcher.FileChanged)")

[CreateFileWatcher Method (String, GH\_FileWatcherEvents, GH\_FileWatcher.FileChangedSimple)](../html/M_Grasshopper_Kernel_GH_FileWatcher_CreateFileWatcher_1.htm "CreateFileWatcher Method (String, GH_FileWatcherEvents, GH_FileWatcher.FileChangedSimple)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FileWatcherAddLanguageSpecificTextSet("LST7CE5E210\_0?cpp=::|nu=.");CreateFileWatcher Method (String, GH\_FileWatcherEvents, GH\_FileWatcherAddLanguageSpecificTextSet("LST7CE5E210\_1?cpp=::|nu=.");FileChanged) |

Create a new FileSystem Watcher object aimed at a specific file.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_FileWatcher CreateFileWatcher(
	string filePath,
	GH_FileWatcherEvents events,
	GH_FileWatcherAddLanguageSpecificTextSet("LST7CE5E210_2?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChanged delegate
)
```

```
Public Shared Function CreateFileWatcher ( 
	filePath As String,
	events As GH_FileWatcherEvents,
	delegate As GH_FileWatcherAddLanguageSpecificTextSet("LST7CE5E210_3?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChanged
) As GH_FileWatcher
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

filePath
:   Type: [SystemAddLanguageSpecificTextSet("LST7CE5E210\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    File to watch.

events
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST7CE5E210\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FileWatcherEvents](T_Grasshopper_Kernel_GH_FileWatcherEvents.htm)  
    Events to watch for.

delegate
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST7CE5E210\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FileWatcherAddLanguageSpecificTextSet("LST7CE5E210\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChanged](T_Grasshopper_Kernel_GH_FileWatcher_FileChanged.htm)  
    Callback delegate.

#### Return Value

Type: [GH\_FileWatcher](T_Grasshopper_Kernel_GH_FileWatcher.htm)  
A new filewatcher aimed at the specified file.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_FileWatcher Class](T_Grasshopper_Kernel_GH_FileWatcher.htm)

[CreateFileWatcher Overload](Overload_Grasshopper_Kernel_GH_FileWatcher_CreateFileWatcher.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)