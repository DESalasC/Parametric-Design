# T_Grasshopper_Kernel_Types_GH_Interval

﻿ GH\_Interval Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Interval Class](../html/T_Grasshopper_Kernel_Types_GH_Interval.htm "GH_Interval Class")

[GH\_Interval Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Interval__ctor.htm "GH_Interval Constructor ")

[GH\_Interval Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Interval.htm "GH_Interval Properties")

[GH\_Interval Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Interval.htm "GH_Interval Methods")

[GH\_Interval Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Interval.htm "GH_Interval Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Interval Class |

Represents a one-dimensional numeric domain.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST4CB4CFED\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST4CB4CFED\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST4CB4CFED\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IntervalAddLanguageSpecificTextSet("LST4CB4CFED\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST4CB4CFED\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Interval

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Interval : GH_Goo<Interval>
```

```
Public Class GH_Interval
	Inherits GH_Goo(Of Interval)
```

AddLanguageTabSet("ID1EBCA");

The GH\_Interval type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_IntervalAddLanguageSpecificTextSet("LST4CB4CFED\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Interval__ctor.htm) | Default constructor |
| Public method | [GH\_Interval(GH\_Interval)](M_Grasshopper_Kernel_Types_GH_Interval__ctor_1.htm) | Create a duplicate from another interval. |
| Public method | [GH\_Interval(Interval)](M_Grasshopper_Kernel_Types_GH_Interval__ctor_2.htm) | Create a duplicate of another interval |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Interval_IsValid.htm) | Gets the validity of this instance. Intervals are invalid if either of the extremes is a #NaN. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST4CB4CFED\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Interval_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST4CB4CFED\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Interval_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST4CB4CFED\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Interval_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST4CB4CFED\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm) | Gets or sets the internal data. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_18?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_19?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Interval_CastFrom.htm) | Remote to Local caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_20?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_21?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST4CB4CFED\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST4CB4CFED\_23?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST4CB4CFED\_24?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST4CB4CFED\_25?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_26?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_27?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST4CB4CFED\_28?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST4CB4CFED\_29?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST4CB4CFED\_30?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Interval_CastTo__1.htm) | Local to Remote caster function. this stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_31?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_32?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST4CB4CFED\_33?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST4CB4CFED\_34?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST4CB4CFED\_35?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST4CB4CFED\_36?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).) |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_Interval_Duplicate.htm) | Create a duplicate of this interval. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_37?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_38?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST4CB4CFED\_39?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST4CB4CFED\_40?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).) |
| Public method | [DuplicateInterval](M_Grasshopper_Kernel_Types_GH_Interval_DuplicateInterval.htm) | Create a duplicate of this interval. |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Interval_EmitProxy.htm) | Returns a proxy that represents this interval. Do not call this function unless you're (Overrides [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_41?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_42?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST4CB4CFED\_43?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LST4CB4CFED\_44?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Interval_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_45?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_46?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST4CB4CFED\_47?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disappears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_48?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_49?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Interval_ToString.htm) | Format the interval using default grasshopper formatting logic. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_50?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_51?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST4CB4CFED\_52?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST4CB4CFED\_53?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Interval_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_54?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_55?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST4CB4CFED\_56?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST4CB4CFED\_57?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4CB4CFED\_58?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)