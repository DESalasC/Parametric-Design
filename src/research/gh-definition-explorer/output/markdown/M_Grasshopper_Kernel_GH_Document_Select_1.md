# M_Grasshopper_Kernel_GH_Document_Select_1

﻿ GH\_Document.Select Method (GH\_RelevantObjectData, Boolean, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[Select Method](../html/Overload_Grasshopper_Kernel_GH_Document_Select.htm "Select Method ")

[Select Method (GH\_RelevantObjectData)](../html/M_Grasshopper_Kernel_GH_Document_Select.htm "Select Method (GH_RelevantObjectData)")

[Select Method (GH\_RelevantObjectData, Boolean, Boolean)](../html/M_Grasshopper_Kernel_GH_Document_Select_1.htm "Select Method (GH_RelevantObjectData, Boolean, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LST858915B6\_0?cpp=::|nu=.");Select Method (GH\_RelevantObjectData, Boolean, Boolean) |

Default pick selection behaviour

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_SelectionState Select(
	GH_RelevantObjectData obj_dat,
	bool bAdd,
	bool bRemove
)
```

```
Public Function Select ( 
	obj_dat As GH_RelevantObjectData,
	bAdd As Boolean,
	bRemove As Boolean
) As GH_SelectionState
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

obj\_dat
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST858915B6\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RelevantObjectData](T_Grasshopper_Kernel_GH_RelevantObjectData.htm)  
    Information regarding the object to be selected.

bAdd
:   Type: [SystemAddLanguageSpecificTextSet("LST858915B6\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, it will add the topmost unselected object that contains pt to the selection set.
    If False, the selection set will be cleared when an unselected object is picked

bRemove
:   Type: [SystemAddLanguageSpecificTextSet("LST858915B6\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, it will remove the topmost selected object that contains pt from the selection set.

#### Return Value

Type: [GH\_SelectionState](T_Grasshopper_Kernel_GH_SelectionState.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[Select Overload](Overload_Grasshopper_Kernel_GH_Document_Select.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)