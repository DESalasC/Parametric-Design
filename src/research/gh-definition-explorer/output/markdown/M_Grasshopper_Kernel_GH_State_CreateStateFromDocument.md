# M_Grasshopper_Kernel_GH_State_CreateStateFromDocument

﻿ GH\_State.CreateStateFromDocument Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_State Class](../html/T_Grasshopper_Kernel_GH_State.htm "GH_State Class")

[GH\_State Methods](../html/Methods_T_Grasshopper_Kernel_GH_State.htm "GH_State Methods")

[AddStateObject Method](../html/M_Grasshopper_Kernel_GH_State_AddStateObject.htm "AddStateObject Method ")

[ClearStates Method](../html/M_Grasshopper_Kernel_GH_State_ClearStates.htm "ClearStates Method ")

[CreateStateFromDocument Method](../html/M_Grasshopper_Kernel_GH_State_CreateStateFromDocument.htm "CreateStateFromDocument Method ")

[Read Method](../html/M_Grasshopper_Kernel_GH_State_Read.htm "Read Method ")

[RemoveStateObject Method](../html/M_Grasshopper_Kernel_GH_State_RemoveStateObject.htm "RemoveStateObject Method ")

[Write Method](../html/M_Grasshopper_Kernel_GH_State_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StateAddLanguageSpecificTextSet("LSTA527A0F1\_0?cpp=::|nu=.");CreateStateFromDocument Method |

Creates a state database from a document.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int CreateStateFromDocument(
	GH_Document doc
)
```

```
Public Function CreateStateFromDocument ( 
	doc As GH_Document
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

doc
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTA527A0F1\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Document](T_Grasshopper_Kernel_GH_Document.htm)  
    Document to parse.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
Number of states saved or -1 if the user aborted.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_State Class](T_Grasshopper_Kernel_GH_State.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)