# T_Grasshopper_Kernel_Data_GH_TreeFilter

﻿ GH\_TreeFilter Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_TreeFilter Class](../html/T_Grasshopper_Kernel_Data_GH_TreeFilter.htm "GH_TreeFilter Class")

[GH\_TreeFilter Constructor](../html/M_Grasshopper_Kernel_Data_GH_TreeFilter__ctor.htm "GH_TreeFilter Constructor ")

[GH\_TreeFilter Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_TreeFilter.htm "GH_TreeFilter Methods")

[GH\_TreeFilter Fields](../html/Fields_T_Grasshopper_Kernel_Data_GH_TreeFilter.htm "GH_TreeFilter Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TreeFilter Class |

Represents a collection of rules for validating DataTree paths and indices.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST2F06E001\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST2F06E001\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_TreeFilter

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_TreeFilter
```

```
Public Class GH_TreeFilter
```

AddLanguageTabSet("ID1EBCA");

The GH\_TreeFilter type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_TreeFilter](M_Grasshopper_Kernel_Data_GH_TreeFilter__ctor.htm) | Initializes a new instance of the GH\_TreeFilter class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [FindItemBrackets](M_Grasshopper_Kernel_Data_GH_TreeFilter_FindItemBrackets.htm) | Locate the two parenthesis that delineate the index segment of an Index Rule set. |
| Public methodStatic member | [FindNextLevelChar](M_Grasshopper_Kernel_Data_GH_TreeFilter_FindNextLevelChar.htm) | Find the next occurance of a char in a string that is level with the search start index. |
| Public methodStatic member | [FindPathBrackets](M_Grasshopper_Kernel_Data_GH_TreeFilter_FindPathBrackets.htm) | Locate the two curly brackets that delineate the path segment of an Index Rule set. |
| Public methodStatic member | [FindPrevLevelChar](M_Grasshopper_Kernel_Data_GH_TreeFilter_FindPrevLevelChar.htm) | Find the previous occurance of a char in a string that is level with the search start index. |
| Public methodStatic member | [ParsePattern](M_Grasshopper_Kernel_Data_GH_TreeFilter_ParsePattern.htm) | Parses a textual filter and returns an instance of the GH\_TreeFilter. If the filter cannot be parsed an exception will be thrown. |
| Public methodStatic member | [SplitStringWithExpressions](M_Grasshopper_Kernel_Data_GH_TreeFilter_SplitStringWithExpressions.htm) | Split a string into segments using level-aware split. This method throws exceptions if the input string is not correctly formatted. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public fieldStatic member | [ItemClose](F_Grasshopper_Kernel_Data_GH_TreeFilter_ItemClose.htm) |  |
| Public fieldStatic member | [ItemOpen](F_Grasshopper_Kernel_Data_GH_TreeFilter_ItemOpen.htm) |  |
| Public fieldStatic member | [PathClose](F_Grasshopper_Kernel_Data_GH_TreeFilter_PathClose.htm) |  |
| Public fieldStatic member | [PathOpen](F_Grasshopper_Kernel_Data_GH_TreeFilter_PathOpen.htm) |  |
| Public fieldStatic member | [PathSeparator](F_Grasshopper_Kernel_Data_GH_TreeFilter_PathSeparator.htm) |  |
| Public fieldStatic member | [SegmentSeparator](F_Grasshopper_Kernel_Data_GH_TreeFilter_SegmentSeparator.htm) |  |
| Public fieldStatic member | [StringDelimeter](F_Grasshopper_Kernel_Data_GH_TreeFilter_StringDelimeter.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)