# M_Grasshopper_Kernel_Data_GH_PathOffset_OffsetPath

﻿ GH\_PathOffset.OffsetPath Method (GH\_Path, Int32, GH\_Path, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_PathOffset Class](../html/T_Grasshopper_Kernel_Data_GH_PathOffset.htm "GH_PathOffset Class")

[GH\_PathOffset Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_PathOffset.htm "GH_PathOffset Methods")

[OffsetPath Method](../html/Overload_Grasshopper_Kernel_Data_GH_PathOffset_OffsetPath.htm "OffsetPath Method ")

[OffsetPath Method (GH\_Path, Int32, GH\_Path, Int32)](../html/M_Grasshopper_Kernel_Data_GH_PathOffset_OffsetPath.htm "OffsetPath Method (GH_Path, Int32, GH_Path, Int32)")

[OffsetPath Method (GH\_Path, Int32, IGH\_Structure, GH\_Path, Int32)](../html/M_Grasshopper_Kernel_Data_GH_PathOffset_OffsetPath_1.htm "OffsetPath Method (GH_Path, Int32, IGH_Structure, GH_Path, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PathOffsetAddLanguageSpecificTextSet("LST540FF52\_0?cpp=::|nu=.");OffsetPath Method (GH\_Path, Int32, GH\_PathAddLanguageSpecificTextSet("LST540FF52\_1?cpp=%");, Int32AddLanguageSpecificTextSet("LST540FF52\_2?cpp=%");) |

Offset a path + index value without wrapping.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool OffsetPath(
	GH_Path path,
	int index,
	ref GH_Path rel_path,
	ref int rel_index
)
```

```
Public Function OffsetPath ( 
	path As GH_Path,
	index As Integer,
	ByRef rel_path As GH_Path,
	ByRef rel_index As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST540FF52\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    Path to offset.

index
:   Type: [SystemAddLanguageSpecificTextSet("LST540FF52\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Item to offset.

rel\_path
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST540FF52\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)AddLanguageSpecificTextSet("LST540FF52\_6?cpp=%");  
    Offsetted path.

rel\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST540FF52\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LST540FF52\_8?cpp=%");  
    Offsetted index.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_PathOffset Class](T_Grasshopper_Kernel_Data_GH_PathOffset.htm)

[OffsetPath Overload](Overload_Grasshopper_Kernel_Data_GH_PathOffset_OffsetPath.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)