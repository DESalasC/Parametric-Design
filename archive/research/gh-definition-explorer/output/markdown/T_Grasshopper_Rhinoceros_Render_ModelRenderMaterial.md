# T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial

﻿ ModelRenderMaterial Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Render](../html/N_Grasshopper_Rhinoceros_Render.htm "Grasshopper.Rhinoceros.Render")

[ModelRenderMaterial Class](../html/T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm "ModelRenderMaterial Class")

[ModelRenderMaterial Constructor](../html/Overload_Grasshopper_Rhinoceros_Render_ModelRenderMaterial__ctor.htm "ModelRenderMaterial Constructor ")

[ModelRenderMaterial Properties](../html/Properties_T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm "ModelRenderMaterial Properties")

[ModelRenderMaterial Methods](../html/Methods_T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm "ModelRenderMaterial Methods")

[ModelRenderMaterial Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm "ModelRenderMaterial Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelRenderMaterial Class |

Represents a Rhino render material. Wraps the functionality of the RenderMaterial type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTA74D3F02\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTA74D3F02\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTA74D3F02\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
      [Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LSTA74D3F02\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelRenderContent](T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm)  
        Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LSTA74D3F02\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelRenderMaterial

**Namespace:**
 [Grasshopper.Rhinoceros.Render](N_Grasshopper_Rhinoceros_Render.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelRenderMaterial : ModelRenderContent, 
	IGH_BakeAwareData
```

```
Public NotInheritable Class ModelRenderMaterial
	Inherits ModelRenderContent
	Implements IGH_BakeAwareData
```

AddLanguageTabSet("ID1EBCA");

The ModelRenderMaterial type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelRenderMaterialAddLanguageSpecificTextSet("LSTA74D3F02\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial__ctor.htm) | Initializes a new instance of the ModelRenderMaterial class |
| Public method | [ModelRenderMaterial(ModelRenderMaterialAddLanguageSpecificTextSet("LSTA74D3F02\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial__ctor_1.htm) | Initializes a new instance of the ModelRenderMaterial class |
| Public method | [ModelRenderMaterial(Guid)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial__ctor_4.htm) | Initializes a new instance of the ModelRenderMaterial class |
| Public method | [ModelRenderMaterial(Material)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial__ctor_2.htm) | Initializes a new instance of the ModelRenderMaterial class |
| Public method | [ModelRenderMaterial(RenderMaterial)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial__ctor_3.htm) | Initializes a new instance of the ModelRenderMaterial class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Name](P_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_Name.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LSTA74D3F02\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm).) |
| Public property | [Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [TypeName](P_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_TypeName.htm) | (Overrides [ModelRenderContentAddLanguageSpecificTextSet("LSTA74D3F02\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Rhinoceros_Render_ModelRenderContent_TypeName.htm).) |
| Public propertyStatic member | [Unset](P_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_Unset.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_Cast.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LSTA74D3F02\_9?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTA74D3F02\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTA74D3F02\_11?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTA74D3F02\_12?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTA74D3F02\_13?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTA74D3F02\_14?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTA74D3F02\_15?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTA74D3F02\_16?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTA74D3F02\_17?cpp=%");)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_CastTo__1.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LSTA74D3F02\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LSTA74D3F02\_19?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTA74D3F02\_20?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTA74D3F02\_21?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm).) |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTA74D3F02\_22?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ModelRenderMaterialAddLanguageSpecificTextSet("LSTA74D3F02\_23?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes to ModelRenderMaterial)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_op_Implicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTA74D3F02\_24?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ColorRGBA to ModelRenderMaterial)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_op_Implicit_1.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTA74D3F02\_25?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(Material to ModelRenderMaterial)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_op_Implicit_2.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTA74D3F02\_26?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(RenderMaterial to ModelRenderMaterial)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_op_Implicit_3.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTA74D3F02\_27?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(String to ModelRenderMaterial)](M_Grasshopper_Rhinoceros_Render_ModelRenderMaterial_op_Implicit_4.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Render Namespace](N_Grasshopper_Rhinoceros_Render.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)