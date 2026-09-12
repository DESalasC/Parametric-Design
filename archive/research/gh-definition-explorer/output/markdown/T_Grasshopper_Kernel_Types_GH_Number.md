# T_Grasshopper_Kernel_Types_GH_Number

﻿ GH\_Number Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Number Class](../html/T_Grasshopper_Kernel_Types_GH_Number.htm "GH_Number Class")

[GH\_Number Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Number__ctor.htm "GH_Number Constructor ")

[GH\_Number Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Number.htm "GH_Number Properties")

[GH\_Number Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Number.htm "GH_Number Methods")

[GH\_Number Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Number.htm "GH_Number Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Number Class |

Represents a double-precision floating point number. GH\_Number re-implements the framework System.Double type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTD96194E3\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTD96194E3\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LSTD96194E3\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Double](https://docs.microsoft.com/dotnet/api/system.double)AddLanguageSpecificTextSet("LSTD96194E3\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTD96194E3\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Number  
      [Grasshopper.Rhinoceros.DraftingAddLanguageSpecificTextSet("LSTD96194E3\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelLineWidth](T_Grasshopper_Rhinoceros_Drafting_ModelLineWidth.htm)

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Number : GH_Goo<double>
```

```
Public Class GH_Number
	Inherits GH_Goo(Of Double)
```

AddLanguageTabSet("ID1EBCA");

The GH\_Number type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_NumberAddLanguageSpecificTextSet("LSTD96194E3\_6?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Number__ctor.htm) | Blank constructor |
| Public method | [GH\_Number(Double)](M_Grasshopper_Kernel_Types_GH_Number__ctor_2.htm) | Initializes a new instance of the GH\_Number class |
| Public method | [GH\_Number(GH\_Number)](M_Grasshopper_Kernel_Types_GH_Number__ctor_1.htm) | Initializes a new instance of the GH\_Number class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Number_IsValid.htm) | Gets the validity of this instance. If the number is NaN, then it is considered invalid (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_7?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_8?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTD96194E3\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Number_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_10?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_11?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTD96194E3\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Number_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_13?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_14?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTD96194E3\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Number_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_16?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_17?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTD96194E3\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm) | Gets or sets the internal data. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Number_CastFrom.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_21?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_22?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTD96194E3\_23?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTD96194E3\_24?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTD96194E3\_25?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTD96194E3\_26?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_27?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_28?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTD96194E3\_29?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD96194E3\_30?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTD96194E3\_31?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Number_CastTo__1.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_32?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_33?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTD96194E3\_34?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LSTD96194E3\_35?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTD96194E3\_36?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTD96194E3\_37?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).) |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_Number_Duplicate.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_38?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_39?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTD96194E3\_40?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LSTD96194E3\_41?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).) |
| Public method | [DuplicateNumber](M_Grasshopper_Kernel_Types_GH_Number_DuplicateNumber.htm) |  |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Number_EmitProxy.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_42?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_43?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTD96194E3\_44?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LSTD96194E3\_45?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Number_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_46?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_47?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTD96194E3\_48?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disappears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_49?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_50?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Number_ToString.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_51?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_52?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTD96194E3\_53?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTD96194E3\_54?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Number_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_55?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_56?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTD96194E3\_57?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTD96194E3\_58?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD96194E3\_59?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)