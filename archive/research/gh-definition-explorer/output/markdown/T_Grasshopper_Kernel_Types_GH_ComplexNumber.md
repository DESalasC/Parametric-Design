# T_Grasshopper_Kernel_Types_GH_ComplexNumber

﻿ GH\_ComplexNumber Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_ComplexNumber Class](../html/T_Grasshopper_Kernel_Types_GH_ComplexNumber.htm "GH_ComplexNumber Class")

[GH\_ComplexNumber Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_ComplexNumber__ctor.htm "GH_ComplexNumber Constructor ")

[GH\_ComplexNumber Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_ComplexNumber.htm "GH_ComplexNumber Properties")

[GH\_ComplexNumber Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_ComplexNumber.htm "GH_ComplexNumber Methods")

[GH\_ComplexNumber Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_ComplexNumber.htm "GH_ComplexNumber Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComplexNumber Class |

Wraps up the Complex data type for IGH\_Goo adherence.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST9C407DCF\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST9C407DCF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST9C407DCF\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Complex](T_Grasshopper_Kernel_Types_Complex.htm)AddLanguageSpecificTextSet("LST9C407DCF\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST9C407DCF\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ComplexNumber

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ComplexNumber : GH_Goo<Complex>
```

```
Public Class GH_ComplexNumber
	Inherits GH_Goo(Of Complex)
```

AddLanguageTabSet("ID1EBCA");

The GH\_ComplexNumber type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ComplexNumberAddLanguageSpecificTextSet("LST9C407DCF\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_ComplexNumber__ctor.htm) | Blank constructor |
| Public method | [GH\_ComplexNumber(Complex)](M_Grasshopper_Kernel_Types_GH_ComplexNumber__ctor_1.htm) | Initializes a new instance of the GH\_ComplexNumber class |
| Public method | [GH\_ComplexNumber(GH\_ComplexNumber)](M_Grasshopper_Kernel_Types_GH_ComplexNumber__ctor_2.htm) | Initializes a new instance of the GH\_ComplexNumber class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_ComplexNumber_IsValid.htm) | Gets the validity of this instance. If either the real or the imaginary component are NaN, then it is considered invalid (Overrides [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST9C407DCF\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_ComplexNumber_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST9C407DCF\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_ComplexNumber_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST9C407DCF\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_ComplexNumber_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST9C407DCF\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm) | Gets or sets the internal data. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_18?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_19?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_ComplexNumber_CastFrom.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_20?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_21?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST9C407DCF\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST9C407DCF\_23?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST9C407DCF\_24?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST9C407DCF\_25?cpp=%");)](M_Grasshopper_Kernel_Types_GH_ComplexNumber_CastTo__1.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_26?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_27?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST9C407DCF\_28?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST9C407DCF\_29?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST9C407DCF\_30?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST9C407DCF\_31?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST9C407DCF\_32?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST9C407DCF\_33?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST9C407DCF\_34?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_35?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_36?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_ComplexNumber_Duplicate.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_37?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_38?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST9C407DCF\_39?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST9C407DCF\_40?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).) |
| Public method | [DuplicateComplex](M_Grasshopper_Kernel_Types_GH_ComplexNumber_DuplicateComplex.htm) |  |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_ComplexNumber_EmitProxy.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_41?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_42?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST9C407DCF\_43?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LST9C407DCF\_44?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_ComplexNumber_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_45?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_46?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST9C407DCF\_47?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disappears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_48?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_49?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_ComplexNumber_ToString.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_50?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_51?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST9C407DCF\_52?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST9C407DCF\_53?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_ComplexNumber_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_54?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_55?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST9C407DCF\_56?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST9C407DCF\_57?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9C407DCF\_58?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)