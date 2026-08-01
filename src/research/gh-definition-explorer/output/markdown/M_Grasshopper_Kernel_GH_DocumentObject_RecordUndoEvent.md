# M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent

﻿ GH\_DocumentObject.RecordUndoEvent Method (GH\_UndoRecord)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentObject Class](../html/T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Class")

[GH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Methods")

[RecordUndoEvent Method](../html/Overload_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent.htm "RecordUndoEvent Method ")

[RecordUndoEvent Method (GH\_UndoRecord)](../html/M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent.htm "RecordUndoEvent Method (GH_UndoRecord)")

[RecordUndoEvent Method (String)](../html/M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_1.htm "RecordUndoEvent Method (String)")

[RecordUndoEvent Method (String, IGH\_UndoAction)](../html/M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_2.htm "RecordUndoEvent Method (String, IGH_UndoAction)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentObjectAddLanguageSpecificTextSet("LSTD15180D\_0?cpp=::|nu=.");RecordUndoEvent Method (GH\_UndoRecord) |

Record an entire undo record.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void RecordUndoEvent(
	GH_UndoRecord record
)
```

```
Public Sub RecordUndoEvent ( 
	record As GH_UndoRecord
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

record
:   Type: [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LSTD15180D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UndoRecord](T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm)  
    Record to push.

#### Implements

[IGH\_DocumentObjectAddLanguageSpecificTextSet("LSTD15180D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");RecordUndoEvent(GH\_UndoRecord)](M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentObject Class](T_Grasshopper_Kernel_GH_DocumentObject.htm)

[RecordUndoEvent Overload](Overload_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)