# M_Grasshopper_Kernel_Data_GH_Path_IsAncestor

﻿ GH\_Path.IsAncestor Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Path Class](../html/T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Class")

[GH\_Path Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Methods")

[AppendElement Method](../html/M_Grasshopper_Kernel_Data_GH_Path_AppendElement.htm "AppendElement Method ")

[Compare Method](../html/M_Grasshopper_Kernel_Data_GH_Path_Compare.htm "Compare Method ")

[CompareTo Method](../html/M_Grasshopper_Kernel_Data_GH_Path_CompareTo.htm "CompareTo Method ")

[CullElement Method](../html/M_Grasshopper_Kernel_Data_GH_Path_CullElement.htm "CullElement Method ")

[CullFirstElement Method](../html/M_Grasshopper_Kernel_Data_GH_Path_CullFirstElement.htm "CullFirstElement Method ")

[Format Method](../html/M_Grasshopper_Kernel_Data_GH_Path_Format.htm "Format Method ")

[FromString Method](../html/M_Grasshopper_Kernel_Data_GH_Path_FromString.htm "FromString Method ")

[GetHashCode Method](../html/M_Grasshopper_Kernel_Data_GH_Path_GetHashCode.htm "GetHashCode Method ")

[Increment Method](../html/Overload_Grasshopper_Kernel_Data_GH_Path_Increment.htm "Increment Method ")

[IsAncestor Method](../html/M_Grasshopper_Kernel_Data_GH_Path_IsAncestor.htm "IsAncestor Method ")

[IsCoincident Method](../html/Overload_Grasshopper_Kernel_Data_GH_Path_IsCoincident.htm "IsCoincident Method ")

[PrependElement Method](../html/M_Grasshopper_Kernel_Data_GH_Path_PrependElement.htm "PrependElement Method ")

[Read Method](../html/M_Grasshopper_Kernel_Data_GH_Path_Read.htm "Read Method ")

[SplitPathLikeString Method](../html/M_Grasshopper_Kernel_Data_GH_Path_SplitPathLikeString.htm "SplitPathLikeString Method ")

[ToString Method](../html/Overload_Grasshopper_Kernel_Data_GH_Path_ToString.htm "ToString Method ")

[Write Method](../html/M_Grasshopper_Kernel_Data_GH_Path_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PathAddLanguageSpecificTextSet("LSTD76710DB\_0?cpp=::|nu=.");IsAncestor Method |

Test another path to see if it is an ancestor of this path.
For a path to be considered an ancestor, it must share the initial dimensions.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool IsAncestor(
	GH_Path potential_ancestor,
	ref int additional_generations
)
```

```
Public Function IsAncestor ( 
	potential_ancestor As GH_Path,
	ByRef additional_generations As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

potential\_ancestor
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LSTD76710DB\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    Parental path to test.

additional\_generations
:   Type: [SystemAddLanguageSpecificTextSet("LSTD76710DB\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LSTD76710DB\_3?cpp=%");  
    This value will hold
    the number of generations between parent and child path.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if other overlaps completely with this path while
being at least one element shorter.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Path Class](T_Grasshopper_Kernel_Data_GH_Path.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)