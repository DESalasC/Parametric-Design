# T_Grasshopper_Kernel_Data_GH_Lexer

﻿ GH\_Lexer Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Lexer Class](../html/T_Grasshopper_Kernel_Data_GH_Lexer.htm "GH_Lexer Class")

[GH\_Lexer Constructor](../html/Overload_Grasshopper_Kernel_Data_GH_Lexer__ctor.htm "GH_Lexer Constructor ")

[GH\_Lexer Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_Lexer.htm "GH_Lexer Properties")

[GH\_Lexer Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Lexer.htm "GH_Lexer Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Lexer Class |

Represents a lexical mask for path operations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST11576682\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST11576682\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Lexer

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Lexer
```

```
Public Class GH_Lexer
```

AddLanguageTabSet("ID1EBCA");

The GH\_Lexer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_LexerAddLanguageSpecificTextSet("LST11576682\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Data_GH_Lexer__ctor.htm) | Blank constructor. |
| Public method | [GH\_Lexer(String)](M_Grasshopper_Kernel_Data_GH_Lexer__ctor_1.htm) | Create a new mask from a textual string. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsItem](P_Grasshopper_Kernel_Data_GH_Lexer_IsItem.htm) | Gets a value indicating whether or not the item portion of the lexer has been set. |
| Public property | [IsPath](P_Grasshopper_Kernel_Data_GH_Lexer_IsPath.htm) | Gets a value indicating whether or not the path portion of the lexer has been set. |
| Public property | [Item](P_Grasshopper_Kernel_Data_GH_Lexer_Item.htm) | Gets the item string that was extracted from the mask. The default is "append" |
| Public property | [Mask](P_Grasshopper_Kernel_Data_GH_Lexer_Mask.htm) | Gets the original string that represents the user input for this lexer. |
| Public property | [Path](P_Grasshopper_Kernel_Data_GH_Lexer_Path.htm) | Gets the list of path strings that was extracted from the mask. If the mask hasn't been parsed yet, it will be parsed now. If the returned list is still nothing, parsing failed. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [EvaluatePath](M_Grasshopper_Kernel_Data_GH_Lexer_EvaluatePath.htm) | Evaluate the variables in this mask with the provided expression solver. |
| Public methodStatic member | [PerformLexicalReplaceAddLanguageSpecificTextSet("LST11576682\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST11576682\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(GH\_Lexer, GH\_Lexer, DataTreeAddLanguageSpecificTextSet("LST11576682\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST11576682\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, DataTreeAddLanguageSpecificTextSet("LST11576682\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST11576682\_8?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_Data_GH_Lexer_PerformLexicalReplace__1.htm) | Lexical Find..Replace operations. |
| Public methodStatic member | [PerformLexicalReplaceAddLanguageSpecificTextSet("LST11576682\_9?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST11576682\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(GH\_Lexer, GH\_Lexer, IGH\_Structure, GH\_StructureAddLanguageSpecificTextSet("LST11576682\_11?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST11576682\_12?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_Data_GH_Lexer_PerformLexicalReplace__1_1.htm) | Lexical Find..Replace operations. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)