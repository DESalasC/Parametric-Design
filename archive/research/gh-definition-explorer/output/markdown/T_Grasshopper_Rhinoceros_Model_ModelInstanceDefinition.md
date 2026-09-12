# T_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition

﻿ ModelInstanceDefinition Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Model](../html/N_Grasshopper_Rhinoceros_Model.htm "Grasshopper.Rhinoceros.Model")

[ModelInstanceDefinition Class](../html/T_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition.htm "ModelInstanceDefinition Class")

[ModelInstanceDefinition Constructor](../html/Overload_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition__ctor.htm "ModelInstanceDefinition Constructor ")

[ModelInstanceDefinition Properties](../html/Properties_T_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition.htm "ModelInstanceDefinition Properties")

[ModelInstanceDefinition Methods](../html/Methods_T_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition.htm "ModelInstanceDefinition Methods")

[ModelInstanceDefinition Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition.htm "ModelInstanceDefinition Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelInstanceDefinition Class |

Represents a Rhino block definition. Wraps the functionality of the InstanceDefinition type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST6B2EABDA\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST6B2EABDA\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST6B2EABDA\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
      [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST6B2EABDA\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm)  
        Grasshopper.Rhinoceros.ModelAddLanguageSpecificTextSet("LST6B2EABDA\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelInstanceDefinition

**Namespace:**
 [Grasshopper.Rhinoceros.Model](N_Grasshopper_Rhinoceros_Model.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelInstanceDefinition : ModelComponentContent, 
	IGH_BakeAwareData, IGH_PreviewData
```

```
Public NotInheritable Class ModelInstanceDefinition
	Inherits ModelComponentContent
	Implements IGH_BakeAwareData, IGH_PreviewData
```

AddLanguageTabSet("ID1EBCA");

The ModelInstanceDefinition type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelInstanceDefinitionAddLanguageSpecificTextSet("LST6B2EABDA\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition__ctor.htm) | Initializes a new instance of the ModelInstanceDefinition class |
| Public method | [ModelInstanceDefinition(ModelInstanceDefinitionAddLanguageSpecificTextSet("LST6B2EABDA\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes)](M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition__ctor_1.htm) | Initializes a new instance of the ModelInstanceDefinition class |
| Public method | [ModelInstanceDefinition(Guid)](M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition__ctor_3.htm) | Initializes a new instance of the ModelInstanceDefinition class |
| Public method | [ModelInstanceDefinition(InstanceDefinition)](M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition__ctor_2.htm) | Initializes a new instance of the ModelInstanceDefinition class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [FilePath](P_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_FilePath.htm) |  |
| Public property | [Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_IsValid.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LST6B2EABDA\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm).) |
| Public property | [Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Objects](P_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_Objects.htm) |  |
| Public property | [Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public propertyStatic member | [Unset](P_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_Unset.htm) |  |
| Public property | [UpdateType](P_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_UpdateType.htm) |  |
| Public property | [Url](P_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_Url.htm) |  |
| Public property | [UrlDescription](P_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_UrlDescription.htm) |  |
| Public property | [UserText](P_Grasshopper_Rhinoceros_ModelComponentContent_UserText.htm) | (Inherited from [ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry](M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_BakeGeometry.htm) |  |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_Cast.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LST6B2EABDA\_8?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST6B2EABDA\_9?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST6B2EABDA\_10?cpp=%");)](M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_CastTo__1.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LST6B2EABDA\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST6B2EABDA\_12?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST6B2EABDA\_13?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST6B2EABDA\_14?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST6B2EABDA\_15?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST6B2EABDA\_16?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST6B2EABDA\_17?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST6B2EABDA\_18?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST6B2EABDA\_19?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST6B2EABDA\_20?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [GetBoundingBox](M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_GetBoundingBox.htm) |  |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST6B2EABDA\_21?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ModelInstanceDefinitionAddLanguageSpecificTextSet("LST6B2EABDA\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes to ModelInstanceDefinition)](M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_op_Implicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST6B2EABDA\_23?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(InstanceDefinition to ModelInstanceDefinition)](M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_op_Implicit_1.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST6B2EABDA\_24?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(String to ModelInstanceDefinition)](M_Grasshopper_Rhinoceros_Model_ModelInstanceDefinition_op_Implicit_2.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Model Namespace](N_Grasshopper_Rhinoceros_Model.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)