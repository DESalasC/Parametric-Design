# T_Grasshopper_Kernel_GH_AutoSaveSettings

﻿ GH\_AutoSaveSettings Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_AutoSaveSettings Class](../html/T_Grasshopper_Kernel_GH_AutoSaveSettings.htm "GH_AutoSaveSettings Class")

[GH\_AutoSaveSettings Constructor](../html/M_Grasshopper_Kernel_GH_AutoSaveSettings__ctor.htm "GH_AutoSaveSettings Constructor ")

[GH\_AutoSaveSettings Properties](../html/Properties_T_Grasshopper_Kernel_GH_AutoSaveSettings.htm "GH_AutoSaveSettings Properties")

[GH\_AutoSaveSettings Methods](../html/Methods_T_Grasshopper_Kernel_GH_AutoSaveSettings.htm "GH_AutoSaveSettings Methods")

[GH\_AutoSaveSettings Events](../html/Events_T_Grasshopper_Kernel_GH_AutoSaveSettings.htm "GH_AutoSaveSettings Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AutoSaveSettings Class |

Provides access to all AutoSave event flags.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTB1C4382B\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTB1C4382B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AutoSaveSettings

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_AutoSaveSettings
```

```
Public NotInheritable Class GH_AutoSaveSettings
```

AddLanguageTabSet("ID1EBCA");

The GH\_AutoSaveSettings type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_AutoSaveSettings](M_Grasshopper_Kernel_GH_AutoSaveSettings__ctor.htm) | Initializes a new instance of the GH\_AutoSaveSettings class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public propertyStatic member | [EnableAutoSave](P_Grasshopper_Kernel_GH_AutoSaveSettings_EnableAutoSave.htm) |  |
| Public propertyStatic member | [SaveOnDataFlattening](P_Grasshopper_Kernel_GH_AutoSaveSettings_SaveOnDataFlattening.htm) |  |
| Public propertyStatic member | [SaveOnDocumentUnload](P_Grasshopper_Kernel_GH_AutoSaveSettings_SaveOnDocumentUnload.htm) |  |
| Public propertyStatic member | [SaveOnObjectAdded](P_Grasshopper_Kernel_GH_AutoSaveSettings_SaveOnObjectAdded.htm) |  |
| Public propertyStatic member | [SaveOnObjectChange](P_Grasshopper_Kernel_GH_AutoSaveSettings_SaveOnObjectChange.htm) |  |
| Public propertyStatic member | [SaveOnObjectRemoved](P_Grasshopper_Kernel_GH_AutoSaveSettings_SaveOnObjectRemoved.htm) |  |
| Public propertyStatic member | [SaveOnWireEvent](P_Grasshopper_Kernel_GH_AutoSaveSettings_SaveOnWireEvent.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [AutosaveFilter](M_Grasshopper_Kernel_GH_AutoSaveSettings_AutosaveFilter.htm) | Tests a given trigger to see if it allows an autosave operation. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public eventStatic member | [AutoSaveFileFormatChanged](E_Grasshopper_Kernel_GH_AutoSaveSettings_AutoSaveFileFormatChanged.htm) |  |
| Public eventStatic member | [EnableAutoSaveChanged](E_Grasshopper_Kernel_GH_AutoSaveSettings_EnableAutoSaveChanged.htm) |  |
| Public eventStatic member | [SaveOnDataFlatteningChanged](E_Grasshopper_Kernel_GH_AutoSaveSettings_SaveOnDataFlatteningChanged.htm) |  |
| Public eventStatic member | [SaveOnDocumentUnloadChanged](E_Grasshopper_Kernel_GH_AutoSaveSettings_SaveOnDocumentUnloadChanged.htm) |  |
| Public eventStatic member | [SaveOnObjectAddedChanged](E_Grasshopper_Kernel_GH_AutoSaveSettings_SaveOnObjectAddedChanged.htm) |  |
| Public eventStatic member | [SaveOnObjectChangeChanged](E_Grasshopper_Kernel_GH_AutoSaveSettings_SaveOnObjectChangeChanged.htm) |  |
| Public eventStatic member | [SaveOnObjectRemovedChanged](E_Grasshopper_Kernel_GH_AutoSaveSettings_SaveOnObjectRemovedChanged.htm) |  |
| Public eventStatic member | [SaveOnWireEventChanged](E_Grasshopper_Kernel_GH_AutoSaveSettings_SaveOnWireEventChanged.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)