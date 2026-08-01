# T_Grasshopper_Versioning

﻿ Versioning Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Versioning Class](../html/T_Grasshopper_Versioning.htm "Versioning Class")

[Versioning Properties](../html/Properties_T_Grasshopper_Versioning.htm "Versioning Properties")

[Versioning Methods](../html/Methods_T_Grasshopper_Versioning.htm "Versioning Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Versioning Class |

Static class that provides information regarding the Grasshopper versioning.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTD75FD301\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  GrasshopperAddLanguageSpecificTextSet("LSTD75FD301\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Versioning

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class Versioning
```

```
Public NotInheritable Class Versioning
```

AddLanguageTabSet("ID1EBCA");

The Versioning type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public propertyStatic member | [BuildDate](P_Grasshopper_Versioning_BuildDate.htm) | Gets the build date string. This is the visible release iteration tag. Typically the BuildDate is just the date (MMMM-dd, yyyy), but it may carry a prefix or suffix for special builds. |
| Public propertyStatic member | [Version](P_Grasshopper_Versioning_Version.htm) | Gets the version of the current build of Grasshopper. |
| Public propertyStatic member | [VersionString](P_Grasshopper_Versioning_VersionString.htm) | Gets the version of the current build of Grasshopper. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [SyncVersionHistoryData](M_Grasshopper_Versioning_SyncVersionHistoryData.htm) | Attempts to download the version history information. The downloaded data (if the download works) will eventually be stored at: Grasshopper.Folders.VersionHistoryFile |
| Public methodStatic member | [VersionHistoryData](M_Grasshopper_Versioning_VersionHistoryData.htm) | Gets the currently most up-to-date version history data. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)