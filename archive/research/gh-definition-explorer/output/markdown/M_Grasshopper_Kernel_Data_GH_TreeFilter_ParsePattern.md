# M_Grasshopper_Kernel_Data_GH_TreeFilter_ParsePattern

﻿ GH\_TreeFilter.ParsePattern Method 

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
| GH\_TreeFilterAddLanguageSpecificTextSet("LSTF79AA833\_0?cpp=::|nu=.");ParsePattern Method |

Parses a textual filter and returns an instance of the GH\_TreeFilter.
If the filter cannot be parsed an exception will be thrown.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_TreeFilter ParsePattern(
	string filter
)
```

```
Public Shared Function ParsePattern ( 
	filter As String
) As GH_TreeFilter
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

filter
:   Type: [SystemAddLanguageSpecificTextSet("LSTF79AA833\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Filter to parse.

#### Return Value

Type: [GH\_TreeFilter](T_Grasshopper_Kernel_Data_GH_TreeFilter.htm)  
An instance of GH\_TreeFilter describing the textual filter.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TreeFilter Class](T_Grasshopper_Kernel_Data_GH_TreeFilter.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)