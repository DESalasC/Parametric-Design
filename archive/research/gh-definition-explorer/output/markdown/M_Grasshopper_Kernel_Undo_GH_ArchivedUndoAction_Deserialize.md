# M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Deserialize

﻿ GH\_ArchivedUndoAction.Deserialize Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[GH\_ArchivedUndoAction Class](../html/T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm "GH_ArchivedUndoAction Class")

[GH\_ArchivedUndoAction Methods](../html/Methods_T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm "GH_ArchivedUndoAction Methods")

[Deserialize Method](../html/M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Deserialize.htm "Deserialize Method ")

[Read Method](../html/M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Read.htm "Read Method ")

[Serialize Method](../html/M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Serialize.htm "Serialize Method ")

[SerializeToByteArray Method](../html/M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_SerializeToByteArray.htm "SerializeToByteArray Method ")

[Write Method](../html/M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ArchivedUndoActionAddLanguageSpecificTextSet("LST6DBAA2F4\_0?cpp=::|nu=.");Deserialize Method |

Deserializes the obj from the local archive.

**Namespace:**
 [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected void Deserialize(
	GH_ISerializable obj
)
```

```
Protected Sub Deserialize ( 
	obj As GH_ISerializable
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

obj
:   Type: [GH\_IOAddLanguageSpecificTextSet("LST6DBAA2F4\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ISerializable](T_GH_IO_GH_ISerializable.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](https://docs.microsoft.com/dotnet/api/system.argumentnullexception) | Thrown when obj is a null reference. |
| [NullReferenceException](https://docs.microsoft.com/dotnet/api/system.nullreferenceexception) | Thrown when the internal archive data is null. |
| [IOException](https://docs.microsoft.com/dotnet/api/system.io.ioexception) | Thrown when the deserialization fails. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ArchivedUndoAction Class](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm)

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)