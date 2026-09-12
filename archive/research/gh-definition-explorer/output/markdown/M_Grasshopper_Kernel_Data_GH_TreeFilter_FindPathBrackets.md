# M_Grasshopper_Kernel_Data_GH_TreeFilter_FindPathBrackets

﻿ GH\_TreeFilter.FindPathBrackets Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_TreeFilter Class](../html/T_Grasshopper_Kernel_Data_GH_TreeFilter.htm "GH_TreeFilter Class")

[GH\_TreeFilter Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_TreeFilter.htm "GH_TreeFilter Methods")

[FindItemBrackets Method](../html/M_Grasshopper_Kernel_Data_GH_TreeFilter_FindItemBrackets.htm "FindItemBrackets Method ")

[FindNextLevelChar Method](../html/M_Grasshopper_Kernel_Data_GH_TreeFilter_FindNextLevelChar.htm "FindNextLevelChar Method ")

[FindPathBrackets Method](../html/M_Grasshopper_Kernel_Data_GH_TreeFilter_FindPathBrackets.htm "FindPathBrackets Method ")

[FindPrevLevelChar Method](../html/M_Grasshopper_Kernel_Data_GH_TreeFilter_FindPrevLevelChar.htm "FindPrevLevelChar Method ")

[ParsePattern Method](../html/M_Grasshopper_Kernel_Data_GH_TreeFilter_ParsePattern.htm "ParsePattern Method ")

[SplitStringWithExpressions Method](../html/M_Grasshopper_Kernel_Data_GH_TreeFilter_SplitStringWithExpressions.htm "SplitStringWithExpressions Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TreeFilterAddLanguageSpecificTextSet("LST96C3F900\_0?cpp=::|nu=.");FindPathBrackets Method |

Locate the two curly brackets that delineate the path segment of an Index Rule set.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool FindPathBrackets(
	string text,
	out int index0,
	out int index1
)
```

```
Public Shared Function FindPathBrackets ( 
	text As String,
	<OutAttribute> ByRef index0 As Integer,
	<OutAttribute> ByRef index1 As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

text
:   Type: [SystemAddLanguageSpecificTextSet("LST96C3F900\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    String to search.

index0
:   Type: [SystemAddLanguageSpecificTextSet("LST96C3F900\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LST96C3F900\_3?cpp=%");  
    Index of opening curly bracket.

index1
:   Type: [SystemAddLanguageSpecificTextSet("LST96C3F900\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LST96C3F900\_5?cpp=%");  
    Index of closing curly bracket.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if valid brackets were found, false if not.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TreeFilter Class](T_Grasshopper_Kernel_Data_GH_TreeFilter.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)