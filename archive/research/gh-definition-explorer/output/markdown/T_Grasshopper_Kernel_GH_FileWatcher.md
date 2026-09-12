# T_Grasshopper_Kernel_GH_FileWatcher

﻿ GH\_FileWatcher Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_FileWatcher Class](../html/T_Grasshopper_Kernel_GH_FileWatcher.htm "GH_FileWatcher Class")

[GH\_FileWatcher Properties](../html/Properties_T_Grasshopper_Kernel_GH_FileWatcher.htm "GH_FileWatcher Properties")

[GH\_FileWatcher Methods](../html/Methods_T_Grasshopper_Kernel_GH_FileWatcher.htm "GH_FileWatcher Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FileWatcher Class |

Provides easy mechanisms to monitor changes to the local File System.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTC27C3D54\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTC27C3D54\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FileWatcher

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_FileWatcher : IDisposable
```

```
Public Class GH_FileWatcher
	Implements IDisposable
```

AddLanguageTabSet("ID1EBCA");

The GH\_FileWatcher type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Active](P_Grasshopper_Kernel_GH_FileWatcher_Active.htm) | Gets or sets the active flag on this watcher. |
| Public property | [Buffer](P_Grasshopper_Kernel_GH_FileWatcher_Buffer.htm) | Gets or sets the time during which events are buffered. If multiple events for the same file occur within the buffered timespan, they will be merged into one event. |
| Public property | [InvokeOnDefaultThread](P_Grasshopper_Kernel_GH_FileWatcher_InvokeOnDefaultThread.htm) | Gets or sets invoke behaviour for events. If true, then the event delegate is called via the Grasshopper main UI thread. This is almost always what you need. |
| Public property | [IsDisposed](P_Grasshopper_Kernel_GH_FileWatcher_IsDisposed.htm) |  |
| Public property | [Path](P_Grasshopper_Kernel_GH_FileWatcher_Path.htm) | Gets the file or folder path currently being watched. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [CreateDirectoryWatcher(String, String, GH\_FileWatcherEvents, GH\_FileWatcherAddLanguageSpecificTextSet("LSTC27C3D54\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChanged)](M_Grasshopper_Kernel_GH_FileWatcher_CreateDirectoryWatcher.htm) | Create a new FileSystem Watcher object aimed at a specific file. |
| Public methodStatic member | [CreateDirectoryWatcher(String, String, GH\_FileWatcherEvents, GH\_FileWatcherAddLanguageSpecificTextSet("LSTC27C3D54\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChangedSimple)](M_Grasshopper_Kernel_GH_FileWatcher_CreateDirectoryWatcher_1.htm) | Create a new FileSystem Watcher object aimed at a specific file. |
| Public methodStatic member | [CreateFileWatcher(String, GH\_FileWatcherEvents, GH\_FileWatcherAddLanguageSpecificTextSet("LSTC27C3D54\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChanged)](M_Grasshopper_Kernel_GH_FileWatcher_CreateFileWatcher.htm) | Create a new FileSystem Watcher object aimed at a specific file. |
| Public methodStatic member | [CreateFileWatcher(String, GH\_FileWatcherEvents, GH\_FileWatcherAddLanguageSpecificTextSet("LSTC27C3D54\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");FileChangedSimple)](M_Grasshopper_Kernel_GH_FileWatcher_CreateFileWatcher_1.htm) | Create a new FileSystem Watcher object aimed at a specific file. |
| Public method | [DisposeAddLanguageSpecificTextSet("LSTC27C3D54\_6?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_FileWatcher_Dispose.htm) | Releases all resources used by the GH\_FileWatcher |
| Protected method | [Dispose(Boolean)](M_Grasshopper_Kernel_GH_FileWatcher_Dispose_1.htm) | Releases the unmanaged resources used by the GH\_FileWatcher and optionally releases the managed resources |
| Public method | [SetCustomUIThread(Control)](M_Grasshopper_Kernel_GH_FileWatcher_SetCustomUIThread.htm) | If you want to override the default Invoke behaviour, you must set InvokeOnDefaultThread to False and supply either a custom Control or a Form. |
| Public method | [SetCustomUIThread(Form)](M_Grasshopper_Kernel_GH_FileWatcher_SetCustomUIThread_1.htm) | If you want to override the default Invoke behaviour, you must set InvokeOnDefaultThread to False and supply either a custom Control or a Form. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)