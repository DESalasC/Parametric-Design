# T_Grasshopper_Kernel_Types_GH_Matrix

﻿ GH\_Matrix Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Matrix Class](../html/T_Grasshopper_Kernel_Types_GH_Matrix.htm "GH_Matrix Class")

[GH\_Matrix Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Matrix__ctor.htm "GH_Matrix Constructor ")

[GH\_Matrix Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Matrix.htm "GH_Matrix Properties")

[GH\_Matrix Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Matrix.htm "GH_Matrix Methods")

[GH\_Matrix Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Matrix.htm "GH_Matrix Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Matrix Class |

Represents a rectangular numeric matrix. GH\_Integer re-implements Rhino.Geometry.Matrix.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST43D1F80D\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST43D1F80D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST43D1F80D\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");MatrixAddLanguageSpecificTextSet("LST43D1F80D\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST43D1F80D\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Matrix

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Matrix : GH_Goo<Matrix>
```

```
Public Class GH_Matrix
	Inherits GH_Goo(Of Matrix)
```

AddLanguageTabSet("ID1EBCA");

The GH\_Matrix type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_MatrixAddLanguageSpecificTextSet("LST43D1F80D\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Matrix__ctor.htm) | Blank constructor |
| Public method | [GH\_Matrix(GH\_Matrix)](M_Grasshopper_Kernel_Types_GH_Matrix__ctor_1.htm) | Initializes a new instance of the GH\_Matrix class |
| Public method | [GH\_Matrix(Matrix)](M_Grasshopper_Kernel_Types_GH_Matrix__ctor_2.htm) | Initializes a new instance of the GH\_Matrix class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Matrix_IsValid.htm) | Gets the validity of this instance. Integers are always valid. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST43D1F80D\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Matrix_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_11?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_12?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST43D1F80D\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Matrix_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_14?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_15?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST43D1F80D\_16?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm) | Gets or sets the internal data. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_17?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_18?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Matrix_CastFrom.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST43D1F80D\_21?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST43D1F80D\_22?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST43D1F80D\_23?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST43D1F80D\_24?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_25?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_26?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST43D1F80D\_27?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST43D1F80D\_28?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST43D1F80D\_29?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Matrix_CastTo__1.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_30?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_31?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST43D1F80D\_32?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST43D1F80D\_33?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST43D1F80D\_34?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST43D1F80D\_35?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).) |
| Public methodStatic member | [CloneMatrix](M_Grasshopper_Kernel_Types_GH_Matrix_CloneMatrix.htm) | Duplicates a Matrix. |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_Matrix_Duplicate.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_36?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_37?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST43D1F80D\_38?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST43D1F80D\_39?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).) |
| Public method | [DuplicateMatrix](M_Grasshopper_Kernel_Types_GH_Matrix_DuplicateMatrix.htm) |  |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm) | Create a new proxy for this instance. Return Null if this class does not support proxies. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_40?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_41?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Matrix_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_42?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_43?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST43D1F80D\_44?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Matrix_ScriptVariable.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_45?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_46?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST43D1F80D\_47?cs=.|vb=.|cpp=::|nu=.|fs=.");ScriptVariableAddLanguageSpecificTextSet("LST43D1F80D\_48?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Matrix_ToString.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_49?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_50?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST43D1F80D\_51?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST43D1F80D\_52?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Matrix_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_53?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_54?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST43D1F80D\_55?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST43D1F80D\_56?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST43D1F80D\_57?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)