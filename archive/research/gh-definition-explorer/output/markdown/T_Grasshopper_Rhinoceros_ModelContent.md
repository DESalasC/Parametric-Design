# T_Grasshopper_Rhinoceros_ModelContent

﻿ ModelContent Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm "Grasshopper.Rhinoceros")

[ModelContent Class](../html/T_Grasshopper_Rhinoceros_ModelContent.htm "ModelContent Class")

[ModelContent Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelContent.htm "ModelContent Properties")

[ModelContent Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelContent.htm "ModelContent Methods")

[ModelContent Fields](../html/Fields_T_Grasshopper_Rhinoceros_ModelContent.htm "ModelContent Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelContent Class |

Represents a Rhino model element.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTEA63FE7\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTEA63FE7\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTEA63FE7\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent  
      [More...](#fullInheritance)

**Namespace:**
 [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class ModelContent : ModelData, 
	IGH_ModelContentData, IEquatable<ModelContent>
```

```
Public MustInherit Class ModelContent
	Inherits ModelData
	Implements IGH_ModelContentData, IEquatable(Of ModelContent)
```

AddLanguageTabSet("ID1EBCA");

The ModelContent type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Protected property | [Attribs](P_Grasshopper_Rhinoceros_ModelContent_Attribs.htm) |  |
| Protected property | [DefaultAttributes](P_Grasshopper_Rhinoceros_ModelData_DefaultAttributes.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public property | [Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm) |  |
| Protected property | [IsReferencedData](P_Grasshopper_Rhinoceros_ModelContent_IsReferencedData.htm) |  |
| Protected property | [IsReferencedDataLoaded](P_Grasshopper_Rhinoceros_ModelContent_IsReferencedDataLoaded.htm) |  |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm) | (Overrides ModelData.IsValid.) |
| Protected property | [IsValidWhyNot](P_Grasshopper_Rhinoceros_ModelContent_IsValidWhyNot.htm) | (Overrides [ModelDataAddLanguageSpecificTextSet("LSTEA63FE7\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Rhinoceros_ModelData_IsValidWhyNot.htm).) |
| Public property | [Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm) |  |
| Public property | [Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm) |  |
| Public property | [Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm) |  |
| Public property | [Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm) |  |
| Public property | [Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm) |  |
| Protected property | [TypeDescription](P_Grasshopper_Rhinoceros_ModelData_TypeDescription.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [AsFrozen](M_Grasshopper_Rhinoceros_ModelContent_AsFrozen.htm) | Try to obtain a dereferenced snapshot of itself. |
| Public methodStatic member | [Cast(Object)](M_Grasshopper_Rhinoceros_ModelContent_Cast.htm) |  |
| Protected methodStatic member | [CastAddLanguageSpecificTextSet("LSTEA63FE7\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");A, TAddLanguageSpecificTextSet("LSTEA63FE7\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(Object)](M_Grasshopper_Rhinoceros_ModelContent_Cast__2.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LSTEA63FE7\_6?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTEA63FE7\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTEA63FE7\_8?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Overrides [ModelDataAddLanguageSpecificTextSet("LSTEA63FE7\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LSTEA63FE7\_10?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTEA63FE7\_11?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTEA63FE7\_12?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTEA63FE7\_13?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTEA63FE7\_14?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTEA63FE7\_15?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) |  |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Overrides [ModelDataAddLanguageSpecificTextSet("LSTEA63FE7\_16?cs=.|vb=.|cpp=::|nu=.|fs=.");Equals(Object)](M_Grasshopper_Rhinoceros_ModelData_Equals_1.htm).) |
| Public methodStatic member | [FromId](M_Grasshopper_Rhinoceros_ModelContent_FromId.htm) |  |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Overrides [ModelDataAddLanguageSpecificTextSet("LSTEA63FE7\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");GetHashCodeAddLanguageSpecificTextSet("LSTEA63FE7\_18?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_ModelData_GetHashCode.htm).) |
| Protected method | [InternaliseData](M_Grasshopper_Rhinoceros_ModelContent_InternaliseData.htm) |  |
| Protected method | [LoadReferencedData](M_Grasshopper_Rhinoceros_ModelContent_LoadReferencedData.htm) |  |
| Protected method | [Read](M_Grasshopper_Rhinoceros_ModelContent_Read.htm) | (Overrides [ModelDataAddLanguageSpecificTextSet("LSTEA63FE7\_19?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Rhinoceros_ModelData_Read.htm).) |
| Protected method | [RuntimeId](M_Grasshopper_Rhinoceros_ModelContent_RuntimeId.htm) |  |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_ModelContent_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm) | (Overrides [ModelDataAddLanguageSpecificTextSet("LSTEA63FE7\_20?cs=.|vb=.|cpp=::|nu=.|fs=.");TooltipStringAddLanguageSpecificTextSet("LSTEA63FE7\_21?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_ModelData_TooltipString.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm) | (Overrides [ModelDataAddLanguageSpecificTextSet("LSTEA63FE7\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTEA63FE7\_23?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_ModelData_ToString.htm).) |
| Protected method | [UnloadReferencedData](M_Grasshopper_Rhinoceros_ModelContent_UnloadReferencedData.htm) |  |
| Protected method | [Write](M_Grasshopper_Rhinoceros_ModelContent_Write.htm) | (Overrides [ModelDataAddLanguageSpecificTextSet("LSTEA63FE7\_24?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Rhinoceros_ModelData_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [Serial](F_Grasshopper_Rhinoceros_ModelData_Serial.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTEA63FE7\_25?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTEA63FE7\_26?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTEA63FE7\_27?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent  
      [Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LSTEA63FE7\_28?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelDisplayMode](T_Grasshopper_Rhinoceros_Display_ModelDisplayMode.htm)  
      [Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LSTEA63FE7\_29?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelNamedView](T_Grasshopper_Rhinoceros_Display_ModelNamedView.htm)  
      [Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LSTEA63FE7\_30?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelViewport](T_Grasshopper_Rhinoceros_Display_ModelViewport.htm)  
      [Grasshopper.Rhinoceros.ModelAddLanguageSpecificTextSet("LSTEA63FE7\_31?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelEarthAnchorPoint](T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint.htm)  
      [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTEA63FE7\_32?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm)  
      [Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LSTEA63FE7\_33?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelRenderContent](T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm)  
      [Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LSTEA63FE7\_34?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelRenderSkylight](T_Grasshopper_Rhinoceros_Render_ModelRenderSkylight.htm)  
      [Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LSTEA63FE7\_35?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelRenderSun](T_Grasshopper_Rhinoceros_Render_ModelRenderSun.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)