# T_Grasshopper_Kernel_Types_GH_Material

﻿ GH\_Material Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Material Class](../html/T_Grasshopper_Kernel_Types_GH_Material.htm "GH_Material Class")

[GH\_Material Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Material__ctor.htm "GH_Material Constructor ")

[GH\_Material Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Material.htm "GH_Material Properties")

[GH\_Material Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Material.htm "GH_Material Methods")

[GH\_Material Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Material.htm "GH_Material Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Material Class |

Represents a implementation of the Rhino material

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST8C3CEFD9\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST8C3CEFD9\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST8C3CEFD9\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");DisplayMaterialAddLanguageSpecificTextSet("LST8C3CEFD9\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST8C3CEFD9\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Material

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Material : GH_Goo<DisplayMaterial>
```

```
Public Class GH_Material
	Inherits GH_Goo(Of DisplayMaterial)
```

AddLanguageTabSet("ID1EBCA");

The GH\_Material type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_MaterialAddLanguageSpecificTextSet("LST8C3CEFD9\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Material__ctor.htm) | Initializes a new instance of the GH\_Material class |
| Public method | [GH\_Material(Color)](M_Grasshopper_Kernel_Types_GH_Material__ctor_4.htm) | Create a new material based on a colour. The colour is used to control Diffuse, Emission and Transparency. Ambient, Specular and Shine are always default. |
| Public method | [GH\_Material(DisplayMaterial)](M_Grasshopper_Kernel_Types_GH_Material__ctor_2.htm) | Create a new Material. |
| Public method | [GH\_Material(GH\_Material)](M_Grasshopper_Kernel_Types_GH_Material__ctor_1.htm) | Copy another GH\_Material instance. |
| Public method | [GH\_Material(Guid)](M_Grasshopper_Kernel_Types_GH_Material__ctor_5.htm) | Create a new Material from an RDK material ID. |
| Public method | [GH\_Material(RenderMaterial)](M_Grasshopper_Kernel_Types_GH_Material__ctor_3.htm) | Create a new Material. |
| Public method | [GH\_Material(String)](M_Grasshopper_Kernel_Types_GH_Material__ctor_6.htm) | Create a new Material from an RDK xml string. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Material_IsValid.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8C3CEFD9\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Material_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8C3CEFD9\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [RdkMaterialId](P_Grasshopper_Kernel_Types_GH_Material_RdkMaterialId.htm) | Gets or sets the RDK material ID this material is associated with. |
| Public property | [RdkMaterialRmtl](P_Grasshopper_Kernel_Types_GH_Material_RdkMaterialRmtl.htm) | Gets or sets the RDK material RMTL file path. |
| Public property | [RdkMaterialXml](P_Grasshopper_Kernel_Types_GH_Material_RdkMaterialXml.htm) | Gets or sets the RDK material Xml string. |
| Public property | [Type](P_Grasshopper_Kernel_Types_GH_Material_Type.htm) | Gets the implied type based on what fields have been assigned. |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Material_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8C3CEFD9\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Material_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8C3CEFD9\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm) | Gets or sets the internal data. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_18?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_19?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Material_CastFrom.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_20?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_21?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8C3CEFD9\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST8C3CEFD9\_23?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST8C3CEFD9\_24?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST8C3CEFD9\_25?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_26?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_27?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST8C3CEFD9\_28?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST8C3CEFD9\_29?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST8C3CEFD9\_30?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Material_CastTo__1.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_31?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_32?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8C3CEFD9\_33?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST8C3CEFD9\_34?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST8C3CEFD9\_35?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST8C3CEFD9\_36?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).) |
| Public methodStatic member | [CreateRhinoMaterial](M_Grasshopper_Kernel_Types_GH_Material_CreateRhinoMaterial.htm) | Creates a standard Rhino material from a colour. |
| Public methodStatic member | [CreateStandardMaterial](M_Grasshopper_Kernel_Types_GH_Material_CreateStandardMaterial.htm) | Creates a standard Grasshopper material from a colour. |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_Material_Duplicate.htm) | Duplicate this material. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_37?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_38?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8C3CEFD9\_39?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST8C3CEFD9\_40?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).) |
| Public method | [DuplicateMaterial](M_Grasshopper_Kernel_Types_GH_Material_DuplicateMaterial.htm) | Duplicate this material. |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Material_EmitProxy.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_41?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_42?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8C3CEFD9\_43?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LST8C3CEFD9\_44?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).) |
| Public method | [MaterialBestGuess](M_Grasshopper_Kernel_Types_GH_Material_MaterialBestGuess.htm) | Gets the best guess RenderMaterial for this shader. |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Material_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_45?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_46?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8C3CEFD9\_47?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Material_ScriptVariable.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_48?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_49?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8C3CEFD9\_50?cs=.|vb=.|cpp=::|nu=.|fs=.");ScriptVariableAddLanguageSpecificTextSet("LST8C3CEFD9\_51?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Material_ToString.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_52?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_53?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8C3CEFD9\_54?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST8C3CEFD9\_55?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Material_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_56?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_57?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST8C3CEFD9\_58?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST8C3CEFD9\_59?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST8C3CEFD9\_60?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)