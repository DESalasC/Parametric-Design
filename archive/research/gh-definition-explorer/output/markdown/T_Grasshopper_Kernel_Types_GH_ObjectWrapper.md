# T_Grasshopper_Kernel_Types_GH_ObjectWrapper

﻿ GH\_ObjectWrapper Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_ObjectWrapper Class](../html/T_Grasshopper_Kernel_Types_GH_ObjectWrapper.htm "GH_ObjectWrapper Class")

[GH\_ObjectWrapper Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_ObjectWrapper__ctor.htm "GH_ObjectWrapper Constructor ")

[GH\_ObjectWrapper Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_ObjectWrapper.htm "GH_ObjectWrapper Properties")

[GH\_ObjectWrapper Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_ObjectWrapper.htm "GH_ObjectWrapper Methods")

[GH\_ObjectWrapper Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_ObjectWrapper.htm "GH_ObjectWrapper Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ObjectWrapper Class |

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST8F5FA012\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST8F5FA012\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST8F5FA012\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Object](https://docs.microsoft.com/dotnet/api/system.object)AddLanguageSpecificTextSet("LST8F5FA012\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST8F5FA012\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ObjectWrapper

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ObjectWrapper : GH_Goo<Object>, 
	IGH_BakeAwareData, IGH_PreviewData
```

```
Public Class GH_ObjectWrapper
	Inherits GH_Goo(Of Object)
	Implements IGH_BakeAwareData, IGH_PreviewData
```

AddLanguageTabSet("ID1EBCA");

The GH\_ObjectWrapper type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ObjectWrapperAddLanguageSpecificTextSet("LST8F5FA012\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_ObjectWrapper__ctor.htm) | Initializes a new instance of the GH\_ObjectWrapper class |
| Public method | [GH\_ObjectWrapper(Object)](M_Grasshopper_Kernel_Types_GH_ObjectWrapper__ctor_1.htm) | Initializes a new instance of the GH\_ObjectWrapper class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_ObjectWrapper_ClippingBox.htm) |  |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_ObjectWrapper_IsValid.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8F5FA012\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_ObjectWrapper_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_11?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_12?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8F5FA012\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_ObjectWrapper_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_14?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_15?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8F5FA012\_16?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm) | Gets or sets the internal data. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_17?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_18?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry](M_Grasshopper_Kernel_Types_GH_ObjectWrapper_BakeGeometry.htm) |  |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_ObjectWrapper_CastFrom.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8F5FA012\_21?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST8F5FA012\_22?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST8F5FA012\_23?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST8F5FA012\_24?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_25?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_26?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST8F5FA012\_27?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST8F5FA012\_28?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST8F5FA012\_29?cpp=%");)](M_Grasshopper_Kernel_Types_GH_ObjectWrapper_CastTo__1.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_30?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_31?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8F5FA012\_32?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST8F5FA012\_33?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST8F5FA012\_34?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST8F5FA012\_35?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).) |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_ObjectWrapper_DrawViewportMeshes.htm) |  |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_ObjectWrapper_DrawViewportWires.htm) |  |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_ObjectWrapper_Duplicate.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_36?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_37?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8F5FA012\_38?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST8F5FA012\_39?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).) |
| Public method | [DuplicateObject](M_Grasshopper_Kernel_Types_GH_ObjectWrapper_DuplicateObject.htm) |  |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_ObjectWrapper_EmitProxy.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_40?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_41?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8F5FA012\_42?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LST8F5FA012\_43?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_ObjectWrapper_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_44?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_45?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8F5FA012\_46?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_ObjectWrapper_ScriptVariable.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_47?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_48?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8F5FA012\_49?cs=.|vb=.|cpp=::|nu=.|fs=.");ScriptVariableAddLanguageSpecificTextSet("LST8F5FA012\_50?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_ObjectWrapper_ToString.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_51?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_52?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8F5FA012\_53?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST8F5FA012\_54?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm) | Default behaviour is to return True. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_55?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_56?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST8F5FA012\_57?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8F5FA012\_58?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)