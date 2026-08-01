# M_Grasshopper_Kernel_GH_StateServer_RemoveState

﻿ GH\_StateServer.RemoveState Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_StateServer Class](../html/T_Grasshopper_Kernel_GH_StateServer.htm "GH_StateServer Class")

[GH\_StateServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_StateServer.htm "GH_StateServer Methods")

[NewStateFromDocument Method](../html/M_Grasshopper_Kernel_GH_StateServer_NewStateFromDocument.htm "NewStateFromDocument Method ")

[Read Method](../html/M_Grasshopper_Kernel_GH_StateServer_Read.htm "Read Method ")

[RemoveState Method](../html/M_Grasshopper_Kernel_GH_StateServer_RemoveState.htm "RemoveState Method ")

[RestoreState Method](../html/Overload_Grasshopper_Kernel_GH_StateServer_RestoreState.htm "RestoreState Method ")

[Write Method](../html/M_Grasshopper_Kernel_GH_StateServer_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StateServerAddLanguageSpecificTextSet("LST11D5DCD4\_0?cpp=::|nu=.");RemoveState Method |

Remove a certain state. This method adds an undo record to the document.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool RemoveState(
	int index
)
```

```
Public Function RemoveState ( 
	index As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

index
:   Type: [SystemAddLanguageSpecificTextSet("LST11D5DCD4\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of state to remove.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_StateServer Class](T_Grasshopper_Kernel_GH_StateServer.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)