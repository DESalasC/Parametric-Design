# M_Grasshopper_Kernel_Data_GH_Path_SplitPathLikeString

﻿ GH\_Path.SplitPathLikeString Method 

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
| GH\_PathAddLanguageSpecificTextSet("LST71C37C9C\_0?cpp=::|nu=.");SplitPathLikeString Method |

Try to split up a path-like formatted string "{A;B;C}(i)" into component parts.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool SplitPathLikeString(
	string s,
	out string[] path_segments,
	out string index_segment
)
```

```
Public Shared Function SplitPathLikeString ( 
	s As String,
	<OutAttribute> ByRef path_segments As String(),
	<OutAttribute> ByRef index_segment As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

s
:   Type: [SystemAddLanguageSpecificTextSet("LST71C37C9C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    String to parse.

path\_segments
:   Type: AddLanguageSpecificTextSet("LST71C37C9C\_2?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LST71C37C9C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LST71C37C9C\_4?cpp=&gt;|vb=()|nu=[]");AddLanguageSpecificTextSet("LST71C37C9C\_5?cpp=%");  
    Output - Strings inside the path portion of s.

index\_segment
:   Type: [SystemAddLanguageSpecificTextSet("LST71C37C9C\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LST71C37C9C\_7?cpp=%");  
    Output - String inside the index portion of s.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Path Class](T_Grasshopper_Kernel_Data_GH_Path.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)