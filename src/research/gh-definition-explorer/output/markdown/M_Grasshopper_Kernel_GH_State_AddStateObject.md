# M_Grasshopper_Kernel_GH_State_AddStateObject

﻿ GH\_State.AddStateObject Method 

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
| GH\_StateAddLanguageSpecificTextSet("LST9789E0D2\_0?cpp=::|nu=.");AddStateObject Method |

Append a new object to the database.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void AddStateObject(
	IGH_StateAwareObject obj,
	Guid obj_id
)
```

```
Public Sub AddStateObject ( 
	obj As IGH_StateAwareObject,
	obj_id As Guid
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

obj
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST9789E0D2\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_StateAwareObject](T_Grasshopper_Kernel_IGH_StateAwareObject.htm)  
    Object to append.

obj\_id
:   Type: [SystemAddLanguageSpecificTextSet("LST9789E0D2\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    Instance GUID of object in document.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_State Class](T_Grasshopper_Kernel_GH_State.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)