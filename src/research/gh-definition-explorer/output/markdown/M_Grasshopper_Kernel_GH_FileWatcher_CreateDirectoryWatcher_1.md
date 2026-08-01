# M_Grasshopper_Kernel_GH_FileWatcher_CreateDirectoryWatcher_1

﻿ GH\_FileWatcher.CreateDirectoryWatcher Method (String, String, GH\_FileWatcherEvents, GH\_FileWatcher.FileChangedSimple)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_FileWatcher Class](../html/T_Grasshopper_Kernel_GH_FileWatcher.htm "GH_FileWatcher Class")

[GH\_FileWatcher Methods](../html/Methods_T_Grasshopper_Kernel_GH_FileWatcher.htm "GH_FileWatcher Methods")

[CreateDirectoryWatcher Method](../html/Overload_Grasshopper_Kernel_GH_FileWatcher_CreateDirectoryWatcher.htm "CreateDirectoryWatcher Method ")

[CreateDirectoryWatcher Method (String, String, GH\_FileWatcherEvents, GH\_FileWatcher.FileChanged)](../html/M_Grasshopper_Kernel_GH_FileWatcher_CreateDirectoryWatcher.htm "CreateDirectoryWatcher Method (String, String, GH_FileWatcherEvents, GH_FileWatcher.FileChanged)")

[CreateDirectoryWatcher Method (String, String, GH\_FileWatcherEvents, GH\_FileWatcher.FileChangedSimple)](../html/M_Grasshopper_Kernel_GH_FileWatcher_CreateDirectoryWatcher_1.htm "CreateDirectoryWatcher Method (String, String, GH_FileWatcherEvents, GH_FileWatcher.FileChangedSimple)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FileWatcherAddLanguageSpecificTextSet("LST923964AE\_0?cpp=::|nu=.");CreateDirectoryWatcher Method (String, String, GH\_FileWatcherEvents, GH\_FileWatcherAddLanguageSpecificTextSet("LST923964AE\_1?cpp=::|nu=.");FileChangedSimple) |

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
public static GH_FileWatcher CreateDirectoryWatcher(
	string folderPath,
	string filter,
	GH_FileWatcherEvents events,
	GH_FileWatcherAddLanguageSpecificTextSet("LST923964AE_2?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChangedSimple delegate
)
```

```
Public Shared Function CreateDirectoryWatcher ( 
	folderPath As String,
	filter As String,
	events As GH_FileWatcherEvents,
	delegate As GH_FileWatcherAddLanguageSpecificTextSet("LST923964AE_3?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChangedSimple
) As GH_FileWatcher
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

folderPath
:   Type: [SystemAddLanguageSpecificTextSet("LST923964AE\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Folder to watch.

filter
:   Type: [SystemAddLanguageSpecificTextSet("LST923964AE\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Filter string for filenames.

events
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST923964AE\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FileWatcherEvents](T_Grasshopper_Kernel_GH_FileWatcherEvents.htm)  
    Events to watch for.

delegate
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST923964AE\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FileWatcherAddLanguageSpecificTextSet("LST923964AE\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChangedSimple](T_Grasshopper_Kernel_GH_FileWatcher_FileChangedSimple.htm)  
    Callback delegate.

#### Return Value

Type: [GH\_FileWatcher](T_Grasshopper_Kernel_GH_FileWatcher.htm)  
A new filewatcher aimed at the specified folder.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_FileWatcher Class](T_Grasshopper_Kernel_GH_FileWatcher.htm)

[CreateDirectoryWatcher Overload](Overload_Grasshopper_Kernel_GH_FileWatcher_CreateDirectoryWatcher.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)