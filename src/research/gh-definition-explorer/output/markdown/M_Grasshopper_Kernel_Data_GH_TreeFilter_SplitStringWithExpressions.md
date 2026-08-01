# M_Grasshopper_Kernel_Data_GH_TreeFilter_SplitStringWithExpressions

﻿ GH\_TreeFilter.SplitStringWithExpressions Method 

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
| GH\_TreeFilterAddLanguageSpecificTextSet("LST728B793C\_0?cpp=::|nu=.");SplitStringWithExpressions Method |

Split a string into segments using level-aware split.
This method throws exceptions if the input string is not correctly formatted.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static List<string> SplitStringWithExpressions(
	string text,
	char separator
)
```

```
Public Shared Function SplitStringWithExpressions ( 
	text As String,
	separator As Char
) As List(Of String)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

text
:   Type: [SystemAddLanguageSpecificTextSet("LST728B793C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    String to split.

separator
:   Type: [SystemAddLanguageSpecificTextSet("LST728B793C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Char](https://docs.microsoft.com/dotnet/api/system.char)  
    Splitting character.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST728B793C\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LST728B793C\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list of string segments.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [GH\_BracketMismatchException](T_Grasshopper_Kernel_Data_GH_BracketMismatchException.htm) | Thrown when the opening and closing brackets don't add up. |
| [GH\_StringMismatchException](T_Grasshopper_Kernel_Data_GH_StringMismatchException.htm) | Thrown when the string delimeter symbols don't add up. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TreeFilter Class](T_Grasshopper_Kernel_Data_GH_TreeFilter.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)