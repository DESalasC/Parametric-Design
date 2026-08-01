# T_Grasshopper_Rhinoceros_ModelUserText

﻿ ModelUserText Structure

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm "Grasshopper.Rhinoceros")

[ModelUserText Structure](../html/T_Grasshopper_Rhinoceros_ModelUserText.htm "ModelUserText Structure")

[ModelUserText Constructor](../html/M_Grasshopper_Rhinoceros_ModelUserText__ctor.htm "ModelUserText Constructor ")

[ModelUserText Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelUserText.htm "ModelUserText Properties")

[ModelUserText Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelUserText.htm "ModelUserText Methods")

[ModelUserText Operators](../html/Operators_T_Grasshopper_Rhinoceros_ModelUserText.htm "ModelUserText Operators")

[ModelUserText Fields](../html/Fields_T_Grasshopper_Rhinoceros_ModelUserText.htm "ModelUserText Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelUserText Structure |

Represents an immutable collection of string/string pairs.

**Namespace:**
 [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public struct ModelUserText : GH_ISerializable, 
	IReadOnlyList<KeyValuePair<string, string>>, IReadOnlyDictionary<string, string>, 
	IEquatable<ModelUserText>, IStructuralEquatable
```

```
Public Structure ModelUserText
	Implements GH_ISerializable, IReadOnlyList(Of KeyValuePair(Of String, String)), 
	IReadOnlyDictionary(Of String, String), IEquatable(Of ModelUserText), 
	IStructuralEquatable
```

AddLanguageTabSet("ID0EBCA");

The ModelUserText type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelUserText](M_Grasshopper_Rhinoceros_ModelUserText__ctor.htm) | Initializes a new instance of the ModelUserText class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Count](P_Grasshopper_Rhinoceros_ModelUserText_Count.htm) |  |
| Public property | [IsDefault](P_Grasshopper_Rhinoceros_ModelUserText_IsDefault.htm) |  |
| Public property | [IsDefaultOrEmpty](P_Grasshopper_Rhinoceros_ModelUserText_IsDefaultOrEmpty.htm) |  |
| Public property | [IsEmpty](P_Grasshopper_Rhinoceros_ModelUserText_IsEmpty.htm) |  |
| Public property | [ItemAddLanguageSpecificTextSet("LSTF7FDFD07\_0?cs=[|vb=(|cpp=[|nu=(|fs= ");Int32AddLanguageSpecificTextSet("LSTF7FDFD07\_1?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Rhinoceros_ModelUserText_Item.htm) |  |
| Public property | [ItemAddLanguageSpecificTextSet("LSTF7FDFD07\_2?cs=[|vb=(|cpp=[|nu=(|fs= ");StringAddLanguageSpecificTextSet("LSTF7FDFD07\_3?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Rhinoceros_ModelUserText_Item_1.htm) |  |
| Public property | [Keys](P_Grasshopper_Rhinoceros_ModelUserText_Keys.htm) |  |
| Public property | [Values](P_Grasshopper_Rhinoceros_ModelUserText_Values.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [ContainsKey](M_Grasshopper_Rhinoceros_ModelUserText_ContainsKey.htm) |  |
| Public method | [EnsureRange(IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");KeyValuePairAddLanguageSpecificTextSet("LSTF7FDFD07\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");String, StringAddLanguageSpecificTextSet("LSTF7FDFD07\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTF7FDFD07\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_EnsureRange.htm) |  |
| Public method | [EnsureRange(IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_8?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LSTF7FDFD07\_9?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_EnsureRange_1.htm) |  |
| Public method | [Equals(ModelUserText)](M_Grasshopper_Rhinoceros_ModelUserText_Equals.htm) |  |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelUserText_Equals_1.htm) | (Overrides [ValueTypeAddLanguageSpecificTextSet("LSTF7FDFD07\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");Equals(Object)](https://docs.microsoft.com/dotnet/api/system.valuetype.equals#system-valuetype-equals(system-object)).) |
| Public method | [GetEnumerator](M_Grasshopper_Rhinoceros_ModelUserText_GetEnumerator.htm) |  |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelUserText_GetHashCode.htm) | (Overrides [ValueTypeAddLanguageSpecificTextSet("LSTF7FDFD07\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");GetHashCodeAddLanguageSpecificTextSet("LSTF7FDFD07\_12?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-valuetype-gethashcode).) |
| Public method | [MergeRange(IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_13?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");KeyValuePairAddLanguageSpecificTextSet("LSTF7FDFD07\_14?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");String, StringAddLanguageSpecificTextSet("LSTF7FDFD07\_15?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTF7FDFD07\_16?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_MergeRange.htm) |  |
| Public method | [MergeRange(IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_17?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LSTF7FDFD07\_18?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_MergeRange_1.htm) |  |
| Public method | [RemoveRange(IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_19?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");KeyValuePairAddLanguageSpecificTextSet("LSTF7FDFD07\_20?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");String, StringAddLanguageSpecificTextSet("LSTF7FDFD07\_21?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTF7FDFD07\_22?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_RemoveRange.htm) |  |
| Public method | [RemoveRange(IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_23?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LSTF7FDFD07\_24?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_RemoveRange_1.htm) |  |
| Public method | [TryGetValue](M_Grasshopper_Rhinoceros_ModelUserText_TryGetValue.htm) |  |
| Public method | [UpdateRange(IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_25?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");KeyValuePairAddLanguageSpecificTextSet("LSTF7FDFD07\_26?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");String, StringAddLanguageSpecificTextSet("LSTF7FDFD07\_27?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTF7FDFD07\_28?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_UpdateRange.htm) |  |
| Public method | [UpdateRange(IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_29?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LSTF7FDFD07\_30?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_UpdateRange_1.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [Addition(ModelUserText, IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_31?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");KeyValuePairAddLanguageSpecificTextSet("LSTF7FDFD07\_32?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");String, StringAddLanguageSpecificTextSet("LSTF7FDFD07\_33?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTF7FDFD07\_34?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_op_Addition.htm) |  |
| Public operatorStatic member | [Addition(ModelUserText, IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_35?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LSTF7FDFD07\_36?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_op_Addition_1.htm) |  |
| Public operatorStatic member | [BitwiseAnd(ModelUserText, IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_37?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");KeyValuePairAddLanguageSpecificTextSet("LSTF7FDFD07\_38?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");String, StringAddLanguageSpecificTextSet("LSTF7FDFD07\_39?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTF7FDFD07\_40?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_op_BitwiseAnd.htm) |  |
| Public operatorStatic member | [BitwiseAnd(ModelUserText, IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_41?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LSTF7FDFD07\_42?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_op_BitwiseAnd_1.htm) |  |
| Public operatorStatic member | [BitwiseOr(ModelUserText, IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_43?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");KeyValuePairAddLanguageSpecificTextSet("LSTF7FDFD07\_44?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");String, StringAddLanguageSpecificTextSet("LSTF7FDFD07\_45?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTF7FDFD07\_46?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_op_BitwiseOr.htm) |  |
| Public operatorStatic member | [BitwiseOr(ModelUserText, IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_47?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LSTF7FDFD07\_48?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_op_BitwiseOr_1.htm) |  |
| Public operatorStatic member | [Equality](M_Grasshopper_Rhinoceros_ModelUserText_op_Equality.htm) |  |
| Public operatorStatic member | [Inequality](M_Grasshopper_Rhinoceros_ModelUserText_op_Inequality.htm) |  |
| Public operatorStatic member | [Subtraction(ModelUserText, IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_49?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");KeyValuePairAddLanguageSpecificTextSet("LSTF7FDFD07\_50?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");String, StringAddLanguageSpecificTextSet("LSTF7FDFD07\_51?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTF7FDFD07\_52?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_op_Subtraction.htm) |  |
| Public operatorStatic member | [Subtraction(ModelUserText, IEnumerableAddLanguageSpecificTextSet("LSTF7FDFD07\_53?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LSTF7FDFD07\_54?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Rhinoceros_ModelUserText_op_Subtraction_1.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public fieldStatic member | [Empty](F_Grasshopper_Rhinoceros_ModelUserText_Empty.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Remarks

Key comparison is not case sensitive.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)