# M_Grasshopper_Kernel_Data_GH_TreeFilter_FindNextLevelChar

﻿ GH\_TreeFilter.FindNextLevelChar Method 

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
| GH\_TreeFilterAddLanguageSpecificTextSet("LSTA7A1AE0C\_0?cpp=::|nu=.");FindNextLevelChar Method |

Find the next occurance of a char in a string that is level with the search start index.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static int FindNextLevelChar(
	string text,
	int index,
	char char
)
```

```
Public Shared Function FindNextLevelChar ( 
	text As String,
	index As Integer,
	char As Char
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

text
:   Type: [SystemAddLanguageSpecificTextSet("LSTA7A1AE0C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    String to search.

index
:   Type: [SystemAddLanguageSpecificTextSet("LSTA7A1AE0C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index to search from.

char
:   Type: [SystemAddLanguageSpecificTextSet("LSTA7A1AE0C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Char](https://docs.microsoft.com/dotnet/api/system.char)  
    Char to match.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
The index of the first level character match or -1 if no such character could be found.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TreeFilter Class](T_Grasshopper_Kernel_Data_GH_TreeFilter.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)