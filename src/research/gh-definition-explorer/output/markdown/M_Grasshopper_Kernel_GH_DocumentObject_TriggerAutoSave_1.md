# M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_1

﻿ GH\_DocumentObject.TriggerAutoSave Method (GH\_AutoSaveTrigger)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentObject Class](../html/T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Class")

[GH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Methods")

[TriggerAutoSave Method](../html/Overload_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave.htm "TriggerAutoSave Method ")

[TriggerAutoSave Method](../html/M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave.htm "TriggerAutoSave Method ")

[TriggerAutoSave Method (GH\_AutoSaveTrigger)](../html/M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_1.htm "TriggerAutoSave Method (GH_AutoSaveTrigger)")

[TriggerAutoSave Method (Guid)](../html/M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_3.htm "TriggerAutoSave Method (Guid)")

[TriggerAutoSave Method (GH\_AutoSaveTrigger, Guid)](../html/M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_2.htm "TriggerAutoSave Method (GH_AutoSaveTrigger, Guid)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentObjectAddLanguageSpecificTextSet("LSTB5744E3A\_0?cpp=::|nu=.");TriggerAutoSave Method (GH\_AutoSaveTrigger) |

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
public void TriggerAutoSave(
	GH_AutoSaveTrigger trigger
)
```

```
Public Sub TriggerAutoSave ( 
	trigger As GH_AutoSaveTrigger
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

trigger
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTB5744E3A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AutoSaveTrigger](T_Grasshopper_Kernel_GH_AutoSaveTrigger.htm)  
    Reason for the autosave operation. It is possible that a user has decided
    to avoid autosave events for specific types, so if you can, try and provide a correct trigger flag.

#### Implements

[IGH\_DocumentObjectAddLanguageSpecificTextSet("LSTB5744E3A\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");TriggerAutoSave(GH\_AutoSaveTrigger)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentObject Class](T_Grasshopper_Kernel_GH_DocumentObject.htm)

[TriggerAutoSave Overload](Overload_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)