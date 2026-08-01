# T_Grasshopper_Kernel_Types_GH_Transform

﻿ GH\_Transform Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Transform Class](../html/T_Grasshopper_Kernel_Types_GH_Transform.htm "GH_Transform Class")

[GH\_Transform Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Transform__ctor.htm "GH_Transform Constructor ")

[GH\_Transform Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Transform.htm "GH_Transform Properties")

[GH\_Transform Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Transform.htm "GH_Transform Methods")

[GH\_Transform Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Transform.htm "GH_Transform Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Transform Class |

Represents a collection of transformations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST2C41A2C1\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST2C41A2C1\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST2C41A2C1\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TransformAddLanguageSpecificTextSet("LST2C41A2C1\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST2C41A2C1\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Transform

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Transform : GH_Goo<Transform>
```

```
Public Class GH_Transform
	Inherits GH_Goo(Of Transform)
```

AddLanguageTabSet("ID1EBCA");

The GH\_Transform type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_TransformAddLanguageSpecificTextSet("LST2C41A2C1\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Transform__ctor.htm) | Initializes a new instance of the GH\_Transform class |
| Public method | [GH\_Transform(GH\_Transform)](M_Grasshopper_Kernel_Types_GH_Transform__ctor_1.htm) | Initializes a new instance of the GH\_Transform class |
| Public method | [GH\_Transform(ITransform)](M_Grasshopper_Kernel_Types_GH_Transform__ctor_2.htm) | Initializes a new instance of the GH\_Transform class |
| Public method | [GH\_Transform(Transform)](M_Grasshopper_Kernel_Types_GH_Transform__ctor_3.htm) | Initializes a new instance of the GH\_Transform class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [CompoundTransforms](P_Grasshopper_Kernel_Types_GH_Transform_CompoundTransforms.htm) | Gets the internal set of transforms. If you modify the compound transformations, you *must* call ClearCaches(). |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Transform_IsValid.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Transform_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Transform_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Transform_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Transform_Value.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_18?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_19?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_20?cs=.|vb=.|cpp=::|nu=.|fs=.");Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Transform_CastFrom.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_21?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_22?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_23?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST2C41A2C1\_24?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST2C41A2C1\_25?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST2C41A2C1\_26?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_27?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_28?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST2C41A2C1\_29?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST2C41A2C1\_30?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST2C41A2C1\_31?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Transform_CastTo__1.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_32?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_33?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_34?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST2C41A2C1\_35?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST2C41A2C1\_36?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST2C41A2C1\_37?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).) |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_Transform_ClearCaches.htm) | Erase the compound transformation caches. |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_Transform_Duplicate.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_38?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_39?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_40?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST2C41A2C1\_41?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).) |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Transform_EmitProxy.htm) | Returns a proxy that represents this transform. Do not call this function unless you're (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_42?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_43?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_44?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LST2C41A2C1\_45?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).) |
| Public method | [GetInverse](M_Grasshopper_Kernel_Types_GH_Transform_GetInverse.htm) |  |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Transform_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_46?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_47?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_48?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Transform_ScriptVariable.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_49?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_50?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_51?cs=.|vb=.|cpp=::|nu=.|fs=.");ScriptVariableAddLanguageSpecificTextSet("LST2C41A2C1\_52?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Transform_ToString.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_53?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_54?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_55?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST2C41A2C1\_56?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Transform_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_57?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_58?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2C41A2C1\_59?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST2C41A2C1\_60?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2C41A2C1\_61?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)