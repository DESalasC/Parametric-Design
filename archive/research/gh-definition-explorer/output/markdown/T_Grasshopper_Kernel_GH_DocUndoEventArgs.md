# T_Grasshopper_Kernel_GH_DocUndoEventArgs

﻿ GH\_DocUndoEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocUndoEventArgs Class](../html/T_Grasshopper_Kernel_GH_DocUndoEventArgs.htm "GH_DocUndoEventArgs Class")

[GH\_DocUndoEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocUndoEventArgs.htm "GH_DocUndoEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocUndoEventArgs Class |

These arguments are passed along with UndoStateChanged events on GH\_Document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTB0AD746\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTB0AD746\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LSTB0AD746\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocUndoEventArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DocUndoEventArgs : EventArgs
```

```
Public Class GH_DocUndoEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocUndoEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Document](P_Grasshopper_Kernel_GH_DocUndoEventArgs_Document.htm) | Gets the document that raised the event. |
| Public property | [Operation](P_Grasshopper_Kernel_GH_DocUndoEventArgs_Operation.htm) | Gets the type of undo operation that caused this event. |
| Public property | [Record](P_Grasshopper_Kernel_GH_DocUndoEventArgs_Record.htm) | Gets the UndoRecord pertaining to this event. Not every Event type has a single record associated with it so be sure to test for null. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)