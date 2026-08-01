# M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_2

﻿ IGH\_DocumentObject.TriggerAutoSave Method (GH\_AutoSaveTrigger, Guid)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DocumentObject Interface](../html/T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Interface")

[IGH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Methods")

[TriggerAutoSave Method](../html/Overload_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave.htm "TriggerAutoSave Method ")

[TriggerAutoSave Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave.htm "TriggerAutoSave Method ")

[TriggerAutoSave Method (GH\_AutoSaveTrigger)](../html/M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_1.htm "TriggerAutoSave Method (GH_AutoSaveTrigger)")

[TriggerAutoSave Method (Guid)](../html/M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_3.htm "TriggerAutoSave Method (Guid)")

[TriggerAutoSave Method (GH\_AutoSaveTrigger, Guid)](../html/M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_2.htm "TriggerAutoSave Method (GH_AutoSaveTrigger, Guid)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DocumentObjectAddLanguageSpecificTextSet("LST5E7E718\_0?cpp=::|nu=.");TriggerAutoSave Method (GH\_AutoSaveTrigger, Guid) |

Triggers the AutoSave function on the owner document with a custom flag.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void TriggerAutoSave(
	GH_AutoSaveTrigger trigger,
	Guid id
)
```

```
Sub TriggerAutoSave ( 
	trigger As GH_AutoSaveTrigger,
	id As Guid
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

trigger
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST5E7E718\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AutoSaveTrigger](T_Grasshopper_Kernel_GH_AutoSaveTrigger.htm)  
    Reason for the autosave operation. It is possible that a user has decided
    to avoid autosave events for specific types, so if you can, try and provide a correct trigger flag.

id
:   Type: [SystemAddLanguageSpecificTextSet("LST5E7E718\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    ID of autosave event. Consecutive autosave requests with the same ID will be ignored.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DocumentObject Interface](T_Grasshopper_Kernel_IGH_DocumentObject.htm)

[TriggerAutoSave Overload](Overload_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)