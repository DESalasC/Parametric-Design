# T_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment

﻿ ModelRenderEnvironment Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Render](../html/N_Grasshopper_Rhinoceros_Render.htm "Grasshopper.Rhinoceros.Render")

[ModelRenderEnvironment Class](../html/T_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment.htm "ModelRenderEnvironment Class")

[ModelRenderEnvironment Constructor](../html/Overload_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment__ctor.htm "ModelRenderEnvironment Constructor ")

[ModelRenderEnvironment Properties](../html/Properties_T_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment.htm "ModelRenderEnvironment Properties")

[ModelRenderEnvironment Methods](../html/Methods_T_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment.htm "ModelRenderEnvironment Methods")

[ModelRenderEnvironment Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment.htm "ModelRenderEnvironment Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelRenderEnvironment Class |

Represents a Rhino render environment. Wraps the functionality of the RenderEnvironment type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST2A1CF38E\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST2A1CF38E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST2A1CF38E\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
      [Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LST2A1CF38E\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelRenderContent](T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm)  
        Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LST2A1CF38E\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelRenderEnvironment

**Namespace:**
 [Grasshopper.Rhinoceros.Render](N_Grasshopper_Rhinoceros_Render.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelRenderEnvironment : ModelRenderContent, 
	IGH_BakeAwareData
```

```
Public NotInheritable Class ModelRenderEnvironment
	Inherits ModelRenderContent
	Implements IGH_BakeAwareData
```

AddLanguageTabSet("ID1EBCA");

The ModelRenderEnvironment type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelRenderEnvironmentAddLanguageSpecificTextSet("LST2A1CF38E\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment__ctor.htm) | Initializes a new instance of the ModelRenderEnvironment class |
| Public method | [ModelRenderEnvironment(ModelRenderEnvironmentAddLanguageSpecificTextSet("LST2A1CF38E\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes)](M_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment__ctor_1.htm) | Initializes a new instance of the ModelRenderEnvironment class |
| Public method | [ModelRenderEnvironment(Guid)](M_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment__ctor_3.htm) | Initializes a new instance of the ModelRenderEnvironment class |
| Public method | [ModelRenderEnvironment(RenderEnvironment)](M_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment__ctor_2.htm) | Initializes a new instance of the ModelRenderEnvironment class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [TypeName](P_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment_TypeName.htm) | (Overrides [ModelRenderContentAddLanguageSpecificTextSet("LST2A1CF38E\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Rhinoceros_Render_ModelRenderContent_TypeName.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment_Cast.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LST2A1CF38E\_8?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST2A1CF38E\_9?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST2A1CF38E\_10?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST2A1CF38E\_11?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST2A1CF38E\_12?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST2A1CF38E\_13?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST2A1CF38E\_14?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST2A1CF38E\_15?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST2A1CF38E\_16?cpp=%");)](M_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment_CastTo__1.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LST2A1CF38E\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST2A1CF38E\_18?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST2A1CF38E\_19?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST2A1CF38E\_20?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm).) |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST2A1CF38E\_21?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ModelRenderEnvironmentAddLanguageSpecificTextSet("LST2A1CF38E\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes to ModelRenderEnvironment)](M_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment_op_Implicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST2A1CF38E\_23?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ColorRGBA to ModelRenderEnvironment)](M_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment_op_Implicit_1.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST2A1CF38E\_24?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(RenderEnvironment to ModelRenderEnvironment)](M_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment_op_Implicit_2.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST2A1CF38E\_25?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(String to ModelRenderEnvironment)](M_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment_op_Implicit_3.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Render Namespace](N_Grasshopper_Rhinoceros_Render.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)