# M_Grasshopper_Kernel_Data_GH_Lexer_PerformLexicalReplace__1

﻿ GH\_Lexer.PerformLexicalReplace(T) Method (GH\_Lexer, GH\_Lexer, DataTree(T), DataTree(T))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Lexer Class](../html/T_Grasshopper_Kernel_Data_GH_Lexer.htm "GH_Lexer Class")

[GH\_Lexer Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Lexer.htm "GH_Lexer Methods")

[PerformLexicalReplace Method](../html/Overload_Grasshopper_Kernel_Data_GH_Lexer_PerformLexicalReplace.htm "PerformLexicalReplace Method ")

[PerformLexicalReplace(T) Method (GH\_Lexer, GH\_Lexer, DataTree(T), DataTree(T))](../html/M_Grasshopper_Kernel_Data_GH_Lexer_PerformLexicalReplace__1.htm "PerformLexicalReplace(T) Method (GH_Lexer, GH_Lexer, DataTree(T), DataTree(T))")

[PerformLexicalReplace(T) Method (GH\_Lexer, GH\_Lexer, IGH\_Structure, GH\_Structure(T))](../html/M_Grasshopper_Kernel_Data_GH_Lexer_PerformLexicalReplace__1_1.htm "PerformLexicalReplace(T) Method (GH_Lexer, GH_Lexer, IGH_Structure, GH_Structure(T))")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_LexerAddLanguageSpecificTextSet("LST3193F6D9\_0?cpp=::|nu=.");PerformLexicalReplaceAddLanguageSpecificTextSet("LST3193F6D9\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST3193F6D9\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Method (GH\_Lexer, GH\_Lexer, DataTreeAddLanguageSpecificTextSet("LST3193F6D9\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST3193F6D9\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, DataTreeAddLanguageSpecificTextSet("LST3193F6D9\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST3193F6D9\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Lexical Find..Replace operations.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void PerformLexicalReplace<T>(
	GH_Lexer source,
	GH_Lexer target,
	DataTree<T> tree_in,
	DataTree<T> tree_out
)
```

```
Public Shared Sub PerformLexicalReplace(Of T) ( 
	source As GH_Lexer,
	target As GH_Lexer,
	tree_in As DataTree(Of T),
	tree_out As DataTree(Of T)
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

source
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST3193F6D9\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Lexer](T_Grasshopper_Kernel_Data_GH_Lexer.htm)  
    Search mask.

target
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST3193F6D9\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Lexer](T_Grasshopper_Kernel_Data_GH_Lexer.htm)  
    Replace pattern.

tree\_in
:   Type: [GrasshopperAddLanguageSpecificTextSet("LST3193F6D9\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");DataTree](T_Grasshopper_DataTree_1.htm)AddLanguageSpecificTextSet("LST3193F6D9\_10?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST3193F6D9\_11?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Source data tree.

tree\_out
:   Type: [GrasshopperAddLanguageSpecificTextSet("LST3193F6D9\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");DataTree](T_Grasshopper_DataTree_1.htm)AddLanguageSpecificTextSet("LST3193F6D9\_13?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST3193F6D9\_14?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Target data tree.

#### Type Parameters

T
:   Type of data in target tree.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Lexer Class](T_Grasshopper_Kernel_Data_GH_Lexer.htm)

[PerformLexicalReplace Overload](Overload_Grasshopper_Kernel_Data_GH_Lexer_PerformLexicalReplace.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)