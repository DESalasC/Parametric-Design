# M_Grasshopper_Kernel_GH_StateServer_RestoreState_1

﻿ GH\_StateServer.RestoreState Method (Int32, Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_StateServer Class](../html/T_Grasshopper_Kernel_GH_StateServer.htm "GH_StateServer Class")

[GH\_StateServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_StateServer.htm "GH_StateServer Methods")

[RestoreState Method](../html/Overload_Grasshopper_Kernel_GH_StateServer_RestoreState.htm "RestoreState Method ")

[RestoreState Method (Int32, Int32, Int32)](../html/M_Grasshopper_Kernel_GH_StateServer_RestoreState_1.htm "RestoreState Method (Int32, Int32, Int32)")

[RestoreState Method (String, Int32, Int32)](../html/M_Grasshopper_Kernel_GH_StateServer_RestoreState_2.htm "RestoreState Method (String, Int32, Int32)")

[RestoreState Method (Int32, Boolean, Int32, Int32)](../html/M_Grasshopper_Kernel_GH_StateServer_RestoreState.htm "RestoreState Method (Int32, Boolean, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StateServerAddLanguageSpecificTextSet("LST39F9994D\_0?cpp=::|nu=.");RestoreState Method (Int32, Int32AddLanguageSpecificTextSet("LST39F9994D\_1?cpp=%");, Int32AddLanguageSpecificTextSet("LST39F9994D\_2?cpp=%");) |

Restore a certain state.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool RestoreState(
	int index,
	out int restored_objects,
	out int missing_objects
)
```

```
Public Function RestoreState ( 
	index As Integer,
	<OutAttribute> ByRef restored_objects As Integer,
	<OutAttribute> ByRef missing_objects As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

index
:   Type: [SystemAddLanguageSpecificTextSet("LST39F9994D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of state to restore.

restored\_objects
:   Type: [SystemAddLanguageSpecificTextSet("LST39F9994D\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LST39F9994D\_5?cpp=%");  
    Number of objects successfully restored.

missing\_objects
:   Type: [SystemAddLanguageSpecificTextSet("LST39F9994D\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LST39F9994D\_7?cpp=%");  
    Number of objects that could not be found.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_StateServer Class](T_Grasshopper_Kernel_GH_StateServer.htm)

[RestoreState Overload](Overload_Grasshopper_Kernel_GH_StateServer_RestoreState.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)