# T_Grasshopper_Kernel_GH_FileSystemEventServer

﻿ GH\_FileSystemEventServer Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_FileSystemEventServer Class](../html/T_Grasshopper_Kernel_GH_FileSystemEventServer.htm "GH_FileSystemEventServer Class")

[GH\_FileSystemEventServer Properties](../html/Properties_T_Grasshopper_Kernel_GH_FileSystemEventServer.htm "GH_FileSystemEventServer Properties")

[GH\_FileSystemEventServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_FileSystemEventServer.htm "GH_FileSystemEventServer Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FileSystemEventServer Class |

Provides a easy-to-use way to keep tabs on files.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTC1E3323D\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTC1E3323D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FileSystemEventServer

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_FileSystemEventServer
```

```
Public NotInheritable Class GH_FileSystemEventServer
```

AddLanguageTabSet("ID1EBCA");

The GH\_FileSystemEventServer type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public propertyStatic member | [AllPaths](P_Grasshopper_Kernel_GH_FileSystemEventServer_AllPaths.htm) | Gets a list of all the paths currently under surveillance. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [AddWatcher](M_Grasshopper_Kernel_GH_FileSystemEventServer_AddWatcher.htm) | Add a new file watcher instance. |
| Public methodStatic member | [RemoveWatcher(Object)](M_Grasshopper_Kernel_GH_FileSystemEventServer_RemoveWatcher.htm) | Remove all watchers that are linked to a specific object. |
| Public methodStatic member | [RemoveWatcher(Object, String)](M_Grasshopper_Kernel_GH_FileSystemEventServer_RemoveWatcher_1.htm) | Remove all watchers that are linked to a specific object and a specific file path. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)