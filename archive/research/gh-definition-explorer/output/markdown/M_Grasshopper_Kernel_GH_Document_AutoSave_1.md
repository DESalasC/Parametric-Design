# M_Grasshopper_Kernel_GH_Document_AutoSave_1

﻿ GH\_Document.AutoSave Method (GH\_AutoSaveTrigger, Guid)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[AutoSave Method](../html/Overload_Grasshopper_Kernel_GH_Document_AutoSave.htm "AutoSave Method ")

[AutoSave Method (GH\_AutoSaveTrigger)](../html/M_Grasshopper_Kernel_GH_Document_AutoSave.htm "AutoSave Method (GH_AutoSaveTrigger)")

[AutoSave Method (GH\_AutoSaveTrigger, Guid)](../html/M_Grasshopper_Kernel_GH_Document_AutoSave_1.htm "AutoSave Method (GH_AutoSaveTrigger, Guid)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LST2001BB6\_0?cpp=::|nu=.");AutoSave Method (GH\_AutoSaveTrigger, Guid) |

Creates a new autosave file on the disk. The previous autosave file (assuming it exists)
will be temporarily renamed and eventually deleted entirely.
Note: AutoSave is only possible on Documents that have TopLevel Rank and a valid FilePath.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool AutoSave(
	GH_AutoSaveTrigger trigger,
	Guid id
)
```

```
Public Function AutoSave ( 
	trigger As GH_AutoSaveTrigger,
	id As Guid
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

trigger
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST2001BB6\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AutoSaveTrigger](T_Grasshopper_Kernel_GH_AutoSaveTrigger.htm)  
    Reason for autosave. User can choose to ignore certain autosave reasons.

id
:   Type: [SystemAddLanguageSpecificTextSet("LST2001BB6\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    Guid of autosave operation, consecutive calls to autosave with the same Guid will be ignored.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[AutoSave Overload](Overload_Grasshopper_Kernel_GH_Document_AutoSave.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)