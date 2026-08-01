# T_Grasshopper_Rhinoceros_Render_ModelRenderContent

﻿ ModelRenderContent Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Render](../html/N_Grasshopper_Rhinoceros_Render.htm "Grasshopper.Rhinoceros.Render")

[ModelRenderContent Class](../html/T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm "ModelRenderContent Class")

[ModelRenderContent Properties](../html/Properties_T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm "ModelRenderContent Properties")

[ModelRenderContent Methods](../html/Methods_T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm "ModelRenderContent Methods")

[ModelRenderContent Fields](../html/Fields_T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm "ModelRenderContent Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelRenderContent Class |

Represents a Rhino render content. Wraps the functionality of the RenderContent type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST472337BC\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST472337BC\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST472337BC\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
      Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LST472337BC\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelRenderContent  
        [Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LST472337BC\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelRenderEnvironment](T_Grasshopper_Rhinoceros_Render_ModelRenderEnvironment.htm)  
        [Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LST472337BC\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelRenderMaterial](T_Grasshopper_Rhinoceros_Render_ModelRenderMaterial.htm)  
        [Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LST472337BC\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelRenderTexture](T_Grasshopper_Rhinoceros_Render_ModelRenderTexture.htm)

**Namespace:**
 [Grasshopper.Rhinoceros.Render](N_Grasshopper_Rhinoceros_Render.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class ModelRenderContent : ModelContent
```

```
Public MustInherit Class ModelRenderContent
	Inherits ModelContent
```

AddLanguageTabSet("ID1EBCA");

The ModelRenderContent type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Protected property | [Attribs](P_Grasshopper_Rhinoceros_Render_ModelRenderContent_Attribs.htm) |  |
| Protected property | [DefaultAttributes](P_Grasshopper_Rhinoceros_ModelData_DefaultAttributes.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public property | [Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected property | [IsReferencedData](P_Grasshopper_Rhinoceros_ModelContent_IsReferencedData.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected property | [IsReferencedDataLoaded](P_Grasshopper_Rhinoceros_ModelContent_IsReferencedDataLoaded.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected property | [IsValidWhyNot](P_Grasshopper_Rhinoceros_ModelContent_IsValidWhyNot.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected property | [TypeDescription](P_Grasshopper_Rhinoceros_ModelData_TypeDescription.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public property | [TypeName](P_Grasshopper_Rhinoceros_Render_ModelRenderContent_TypeName.htm) | (Overrides ModelData.TypeName.) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [AsFrozen](M_Grasshopper_Rhinoceros_ModelContent_AsFrozen.htm) | Try to obtain a dereferenced snapshot of itself. (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST472337BC\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST472337BC\_8?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST472337BC\_9?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST472337BC\_10?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST472337BC\_11?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST472337BC\_12?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Protected methodStatic member | [DuplicateContentAddLanguageSpecificTextSet("LST472337BC\_13?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TContentAddLanguageSpecificTextSet("LST472337BC\_14?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Rhinoceros_Render_ModelRenderContent_DuplicateContent__1.htm) |  |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected method | [InternaliseData](M_Grasshopper_Rhinoceros_ModelContent_InternaliseData.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected method | [LoadReferencedData](M_Grasshopper_Rhinoceros_ModelContent_LoadReferencedData.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected method | [Read](M_Grasshopper_Rhinoceros_ModelContent_Read.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected method | [RuntimeId](M_Grasshopper_Rhinoceros_ModelContent_RuntimeId.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_Render_ModelRenderContent_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected method | [UnloadReferencedData](M_Grasshopper_Rhinoceros_ModelContent_UnloadReferencedData.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected method | [Write](M_Grasshopper_Rhinoceros_ModelContent_Write.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [Serial](F_Grasshopper_Rhinoceros_ModelData_Serial.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Render Namespace](N_Grasshopper_Rhinoceros_Render.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)