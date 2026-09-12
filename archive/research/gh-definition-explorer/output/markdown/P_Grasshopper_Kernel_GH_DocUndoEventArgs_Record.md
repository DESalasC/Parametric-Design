# P_Grasshopper_Kernel_GH_DocUndoEventArgs_Record

﻿ GH\_DocUndoEventArgs.Record Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocUndoEventArgs Class](../html/T_Grasshopper_Kernel_GH_DocUndoEventArgs.htm "GH_DocUndoEventArgs Class")

[GH\_DocUndoEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocUndoEventArgs.htm "GH_DocUndoEventArgs Properties")

[Document Property](../html/P_Grasshopper_Kernel_GH_DocUndoEventArgs_Document.htm "Document Property ")

[Operation Property](../html/P_Grasshopper_Kernel_GH_DocUndoEventArgs_Operation.htm "Operation Property ")

[Record Property](../html/P_Grasshopper_Kernel_GH_DocUndoEventArgs_Record.htm "Record Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocUndoEventArgsAddLanguageSpecificTextSet("LST52D95ADA\_0?cpp=::|nu=.");Record Property |

Gets the UndoRecord pertaining to this event.
Not every Event type has a single record associated with it
so be sure to test for null.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_UndoRecord Record { get; }
```

```
Public ReadOnly Property Record As GH_UndoRecord
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [GH\_UndoRecord](T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm)  

[Missing <value> documentation for "P:Grasshopper.Kernel.GH\_DocUndoEventArgs.Record"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocUndoEventArgs Class](T_Grasshopper_Kernel_GH_DocUndoEventArgs.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)