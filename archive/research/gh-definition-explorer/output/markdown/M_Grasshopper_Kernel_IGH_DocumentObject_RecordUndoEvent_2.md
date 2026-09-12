# M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent_2

﻿ IGH\_DocumentObject.RecordUndoEvent Method (String, IGH\_UndoAction)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DocumentObject Interface](../html/T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Interface")

[IGH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Methods")

[RecordUndoEvent Method](../html/Overload_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent.htm "RecordUndoEvent Method ")

[RecordUndoEvent Method (GH\_UndoRecord)](../html/M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent.htm "RecordUndoEvent Method (GH_UndoRecord)")

[RecordUndoEvent Method (String)](../html/M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent_1.htm "RecordUndoEvent Method (String)")

[RecordUndoEvent Method (String, IGH\_UndoAction)](../html/M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent_2.htm "RecordUndoEvent Method (String, IGH_UndoAction)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DocumentObjectAddLanguageSpecificTextSet("LSTB46284B\_0?cpp=::|nu=.");RecordUndoEvent Method (String, IGH\_UndoAction) |

Record a specific object change undo event.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
Guid RecordUndoEvent(
	string undoName,
	IGH_UndoAction action
)
```

```
Function RecordUndoEvent ( 
	undoName As String,
	action As IGH_UndoAction
) As Guid
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

undoName
:   Type: [SystemAddLanguageSpecificTextSet("LSTB46284B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of undo record.

action
:   Type: [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LSTB46284B\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_UndoAction](T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm)  
    Undo action to record.

#### Return Value

Type: [Guid](https://docs.microsoft.com/dotnet/api/system.guid)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DocumentObject Interface](T_Grasshopper_Kernel_IGH_DocumentObject.htm)

[RecordUndoEvent Overload](Overload_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)