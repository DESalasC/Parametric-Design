# T_Grasshopper_Kernel_Data_IGH_StructureEnumerator

﻿ IGH\_StructureEnumerator Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_BracketMismatchException Class](../html/T_Grasshopper_Kernel_Data_GH_BracketMismatchException.htm "GH_BracketMismatchException Class")

[GH\_ExpandMode Enumeration](../html/T_Grasshopper_Kernel_Data_GH_ExpandMode.htm "GH_ExpandMode Enumeration")

[GH\_GraftMode Enumeration](../html/T_Grasshopper_Kernel_Data_GH_GraftMode.htm "GH_GraftMode Enumeration")

[GH\_IndexRange Structure](../html/T_Grasshopper_Kernel_Data_GH_IndexRange.htm "GH_IndexRange Structure")

[GH\_IndexRanges Class](../html/T_Grasshopper_Kernel_Data_GH_IndexRanges.htm "GH_IndexRanges Class")

[GH\_IndexRuleSet Class](../html/T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm "GH_IndexRuleSet Class")

[GH\_Lexer Class](../html/T_Grasshopper_Kernel_Data_GH_Lexer.htm "GH_Lexer Class")

[GH\_LexerCombo Class](../html/T_Grasshopper_Kernel_Data_GH_LexerCombo.htm "GH_LexerCombo Class")

[GH\_Path Class](../html/T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Class")

[GH\_Path.PathLengthComparer Class](../html/T_Grasshopper_Kernel_Data_GH_Path_PathLengthComparer.htm "GH_Path.PathLengthComparer Class")

[GH\_PathOffset Class](../html/T_Grasshopper_Kernel_Data_GH_PathOffset.htm "GH_PathOffset Class")

[GH\_RuleAnyNumber Class](../html/T_Grasshopper_Kernel_Data_GH_RuleAnyNumber.htm "GH_RuleAnyNumber Class")

[GH\_RuleAnyNumbers Class](../html/T_Grasshopper_Kernel_Data_GH_RuleAnyNumbers.htm "GH_RuleAnyNumbers Class")

[GH\_RuleComplex Class](../html/T_Grasshopper_Kernel_Data_GH_RuleComplex.htm "GH_RuleComplex Class")

[GH\_RuleGroup Class](../html/T_Grasshopper_Kernel_Data_GH_RuleGroup.htm "GH_RuleGroup Class")

[GH\_RuleKind Enumeration](../html/T_Grasshopper_Kernel_Data_GH_RuleKind.htm "GH_RuleKind Enumeration")

[GH\_RuleNumber Class](../html/T_Grasshopper_Kernel_Data_GH_RuleNumber.htm "GH_RuleNumber Class")

[GH\_RuleOperator Enumeration](../html/T_Grasshopper_Kernel_Data_GH_RuleOperator.htm "GH_RuleOperator Enumeration")

[GH\_RuleRange Class](../html/T_Grasshopper_Kernel_Data_GH_RuleRange.htm "GH_RuleRange Class")

[GH\_RuleResult Enumeration](../html/T_Grasshopper_Kernel_Data_GH_RuleResult.htm "GH_RuleResult Enumeration")

[GH\_RuleSequence Class](../html/T_Grasshopper_Kernel_Data_GH_RuleSequence.htm "GH_RuleSequence Class")

[GH\_SimplificationMode Enumeration](../html/T_Grasshopper_Kernel_Data_GH_SimplificationMode.htm "GH_SimplificationMode Enumeration")

[GH\_StringMismatchException Class](../html/T_Grasshopper_Kernel_Data_GH_StringMismatchException.htm "GH_StringMismatchException Class")

[GH\_Structure(T) Class](../html/T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Class")

[GH\_Structure(T).ConversionDelegate(Tfrom, Tto) Delegate](../html/T_Grasshopper_Kernel_Data_GH_Structure_1_ConversionDelegate_2.htm "GH_Structure(T).ConversionDelegate(Tfrom, Tto) Delegate")

[GH\_TreeFilter Class](../html/T_Grasshopper_Kernel_Data_GH_TreeFilter.htm "GH_TreeFilter Class")

[GH\_TreeIndex Structure](../html/T_Grasshopper_Kernel_Data_GH_TreeIndex.htm "GH_TreeIndex Structure")

[GH\_TreeRules Class](../html/T_Grasshopper_Kernel_Data_GH_TreeRules.htm "GH_TreeRules Class")

[IGH\_DataTree Interface](../html/T_Grasshopper_Kernel_Data_IGH_DataTree.htm "IGH_DataTree Interface")

[IGH\_IndexRule Interface](../html/T_Grasshopper_Kernel_Data_IGH_IndexRule.htm "IGH_IndexRule Interface")

[IGH\_Rule Interface](../html/T_Grasshopper_Kernel_Data_IGH_Rule.htm "IGH_Rule Interface")

[IGH\_Structure Interface](../html/T_Grasshopper_Kernel_Data_IGH_Structure.htm "IGH_Structure Interface")

[IGH\_StructureEnumerator Interface](../html/T_Grasshopper_Kernel_Data_IGH_StructureEnumerator.htm "IGH_StructureEnumerator Interface")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_StructureEnumerator Interface |

Defines a minimum interface for iterating over all data in an IGH\_Structure.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_StructureEnumerator : IEnumerable<IGH_Goo>
```

```
Public Interface IGH_StructureEnumerator
	Inherits IEnumerable(Of IGH_Goo)
```

AddLanguageTabSet("ID0EBCA");

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)