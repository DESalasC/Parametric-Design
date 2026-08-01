# T_Grasshopper_Kernel_Expressions_GH_Variant

﻿ GH\_Variant Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Expressions](../html/N_Grasshopper_Kernel_Expressions.htm "Grasshopper.Kernel.Expressions")

[GH\_Variant Class](../html/T_Grasshopper_Kernel_Expressions_GH_Variant.htm "GH_Variant Class")

[GH\_Variant Constructor](../html/Overload_Grasshopper_Kernel_Expressions_GH_Variant__ctor.htm "GH_Variant Constructor ")

[GH\_Variant Properties](../html/Properties_T_Grasshopper_Kernel_Expressions_GH_Variant.htm "GH_Variant Properties")

[GH\_Variant Methods](../html/Methods_T_Grasshopper_Kernel_Expressions_GH_Variant.htm "GH_Variant Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Variant Class |

Variant data used in Grasshopper Expressions.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST6C364642\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.ExpressionsAddLanguageSpecificTextSet("LST6C364642\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Variant

**Namespace:**
 [Grasshopper.Kernel.Expressions](N_Grasshopper_Kernel_Expressions.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Variant
```

```
Public Class GH_Variant
```

AddLanguageTabSet("ID1EBCA");

The GH\_Variant type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_VariantAddLanguageSpecificTextSet("LST6C364642\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor.htm) | Create a new Null variant. |
| Public method | [GH\_Variant(Boolean)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_6.htm) | Create a new Bool variant. |
| Public method | [GH\_Variant(Complex)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_2.htm) | Create a new Complex variant. |
| Public method | [GH\_Variant(Double)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_7.htm) | Create a new Double variant. |
| Public method | [GH\_Variant(GH\_Variant)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_1.htm) | Duplicate a Variant. |
| Public method | [GH\_Variant(Int32)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_8.htm) | Create a new Integer variant. |
| Public method | [GH\_Variant(Plane)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_3.htm) | Create a new Plane variant. |
| Public method | [GH\_Variant(Point3d)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_4.htm) | Create a new Point variant. |
| Public method | [GH\_Variant(String)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_9.htm) | Create a new String variant. |
| Public method | [GH\_Variant(Vector3d)](M_Grasshopper_Kernel_Expressions_GH_Variant__ctor_5.htm) | Create a new Point variant. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [\_Bool](P_Grasshopper_Kernel_Expressions_GH_Variant__Bool.htm) | Gets the contents of this Variant as a bool. |
| Public property | [\_Complex](P_Grasshopper_Kernel_Expressions_GH_Variant__Complex.htm) | Gets the contents of this Variant as a complex number. |
| Public property | [\_Double](P_Grasshopper_Kernel_Expressions_GH_Variant__Double.htm) | Gets the contents of this Variant as a double. If the Variant is of type Integer this cast will also work. |
| Public property | [\_Int](P_Grasshopper_Kernel_Expressions_GH_Variant__Int.htm) | Gets the contents of this Variant as an integer. |
| Public property | [\_Plane](P_Grasshopper_Kernel_Expressions_GH_Variant__Plane.htm) | Gets the contents of this Variant as a Plane. |
| Public property | [\_Point](P_Grasshopper_Kernel_Expressions_GH_Variant__Point.htm) | Gets the contents of this Variant as a Point. |
| Public property | [\_String](P_Grasshopper_Kernel_Expressions_GH_Variant__String.htm) | Gets the contents of this Variant as a String. This function will work for all Variant types. |
| Public property | [\_Vector](P_Grasshopper_Kernel_Expressions_GH_Variant__Vector.htm) | Gets the contents of this Variant as a Vector. |
| Public property | [IsNumeric](P_Grasshopper_Kernel_Expressions_GH_Variant_IsNumeric.htm) | Gets a value indicating whether or not the Variant is a numeric type. Only Doubles and Integers are considered to be Numeric. |
| Public property | [Type](P_Grasshopper_Kernel_Expressions_GH_Variant_Type.htm) | Gets the Type of this Variant. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [DataAddLanguageSpecificTextSet("LST6C364642\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST6C364642\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_Expressions_GH_Variant_Data__1.htm) | Perform a straight cast of the data inside this Variant. |
| Public method | [Duplicate](M_Grasshopper_Kernel_Expressions_GH_Variant_Duplicate.htm) | Duplicate this Variant. If the type of this Variant is [unknown] the contents are not guaranteed to be duplicated. |
| Public method | [Evaluate](M_Grasshopper_Kernel_Expressions_GH_Variant_Evaluate.htm) | If this variant represents a string, this function will attempt to evaluate that string and replace the data inside this variant. |
| Public method | [ToGoo](M_Grasshopper_Kernel_Expressions_GH_Variant_ToGoo.htm) | Attempt to convert a Variant to a Grasshopper IGH\_Goo type. |
| Public method | [ToString](M_Grasshopper_Kernel_Expressions_GH_Variant_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST6C364642\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST6C364642\_6?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Expressions Namespace](N_Grasshopper_Kernel_Expressions.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)