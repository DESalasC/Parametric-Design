# T_Grasshopper_Rhinoceros_ModelColor

﻿ ModelColor Structure

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm "Grasshopper.Rhinoceros")

[ModelColor Structure](../html/T_Grasshopper_Rhinoceros_ModelColor.htm "ModelColor Structure")

[ModelColor Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelColor.htm "ModelColor Methods")

[ModelColor Operators and Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_ModelColor.htm "ModelColor Operators and Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelColor Structure |

Represents a color stored on a model.

**Namespace:**
 [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public struct ModelColor : IGH_Goo, 
	IFormattable, IEquatable<ModelColor>, IComparable, IComparable<ModelColor>
```

```
Public Structure ModelColor
	Implements IGH_Goo, IFormattable, IEquatable(Of ModelColor), 
	IComparable, IComparable(Of ModelColor)
```

AddLanguageTabSet("ID0EBCA");

The ModelColor type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CompareTo](M_Grasshopper_Rhinoceros_ModelColor_CompareTo.htm) |  |
| Public method | [Equals(ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_Equals.htm) |  |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelColor_Equals_1.htm) | (Overrides [ValueTypeAddLanguageSpecificTextSet("LST1C637AB2\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Equals(Object)](https://docs.microsoft.com/dotnet/api/system.valuetype.equals#system-valuetype-equals(system-object)).) |
| Public methodStatic member | [FromArgb(Int32)](M_Grasshopper_Rhinoceros_ModelColor_FromArgb_2.htm) |  |
| Public methodStatic member | [FromArgb(Byte, Byte, Byte)](M_Grasshopper_Rhinoceros_ModelColor_FromArgb.htm) |  |
| Public methodStatic member | [FromArgb(Byte, Byte, Byte, Byte)](M_Grasshopper_Rhinoceros_ModelColor_FromArgb_1.htm) |  |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelColor_GetHashCode.htm) | (Overrides [ValueTypeAddLanguageSpecificTextSet("LST1C637AB2\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GetHashCodeAddLanguageSpecificTextSet("LST1C637AB2\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-valuetype-gethashcode).) |
| Public method | [ToArgb](M_Grasshopper_Rhinoceros_ModelColor_ToArgb.htm) |  |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelColor_ToString.htm) | (Overrides [ValueTypeAddLanguageSpecificTextSet("LST1C637AB2\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST1C637AB2\_4?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.valuetype.tostring#system-valuetype-tostring).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [Equality(Color, ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_op_Equality_2.htm) |  |
| Public operatorStatic member | [Equality(ModelColor, ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_op_Equality.htm) |  |
| Public operatorStatic member | [Equality(ModelColor, Color)](M_Grasshopper_Rhinoceros_ModelColor_op_Equality_1.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST1C637AB2\_5?cs=Explicit|vb=Narrowing|cpp=Explicit|nu=Explicit|fs=Explicit");(ModelColor to ColorRGBA)](M_Grasshopper_Rhinoceros_ModelColor_op_Explicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST1C637AB2\_6?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(Color to ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_op_Implicit_2.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST1C637AB2\_7?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ColorRGBA to ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_op_Implicit_1.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST1C637AB2\_8?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ModelColor to Color)](M_Grasshopper_Rhinoceros_ModelColor_op_Implicit.htm) |  |
| Public operatorStatic member | [Inequality(Color, ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_op_Inequality_2.htm) |  |
| Public operatorStatic member | [Inequality(ModelColor, ModelColor)](M_Grasshopper_Rhinoceros_ModelColor_op_Inequality.htm) |  |
| Public operatorStatic member | [Inequality(ModelColor, Color)](M_Grasshopper_Rhinoceros_ModelColor_op_Inequality_1.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Remarks

This is an opaque representation of a color with conversion methods to and from other color types.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)