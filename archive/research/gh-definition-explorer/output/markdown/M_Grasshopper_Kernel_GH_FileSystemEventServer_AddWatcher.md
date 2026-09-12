# M_Grasshopper_Kernel_GH_FileSystemEventServer_AddWatcher

﻿ GH\_FileSystemEventServer.AddWatcher Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_FileSystemEventServer Class](../html/T_Grasshopper_Kernel_GH_FileSystemEventServer.htm "GH_FileSystemEventServer Class")

[GH\_FileSystemEventServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_FileSystemEventServer.htm "GH_FileSystemEventServer Methods")

[AddWatcher Method](../html/M_Grasshopper_Kernel_GH_FileSystemEventServer_AddWatcher.htm "AddWatcher Method ")

[RemoveWatcher Method](../html/Overload_Grasshopper_Kernel_GH_FileSystemEventServer_RemoveWatcher.htm "RemoveWatcher Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FileSystemEventServerAddLanguageSpecificTextSet("LST13913830\_0?cpp=::|nu=.");AddWatcher Method |

Add a new file watcher instance.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void AddWatcher(
	Object owner,
	string path,
	GH_FileSystemEventServerAddLanguageSpecificTextSet("LST13913830_1?cs=.|vb=.|cpp=::|nu=.|fs=.");FileEvent callback
)
```

```
Public Shared Sub AddWatcher ( 
	owner As Object,
	path As String,
	callback As GH_FileSystemEventServerAddLanguageSpecificTextSet("LST13913830_2?cs=.|vb=.|cpp=::|nu=.|fs=.");FileEvent
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

owner
:   Type: [SystemAddLanguageSpecificTextSet("LST13913830\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
    The object that owns this watcher.

path
:   Type: [SystemAddLanguageSpecificTextSet("LST13913830\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The path of the file to watch.

callback
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST13913830\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FileSystemEventServerAddLanguageSpecificTextSet("LST13913830\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");FileEvent](T_Grasshopper_Kernel_GH_FileSystemEventServer_FileEvent.htm)  
    Callback delegate used during file changes.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_FileSystemEventServer Class](T_Grasshopper_Kernel_GH_FileSystemEventServer.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)