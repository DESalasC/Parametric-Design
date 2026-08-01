# T_Grasshopper_Rhinoceros_Model_ModelObject

﻿ ModelObject Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Model](../html/N_Grasshopper_Rhinoceros_Model.htm "Grasshopper.Rhinoceros.Model")

[ModelObject Class](../html/T_Grasshopper_Rhinoceros_Model_ModelObject.htm "ModelObject Class")

[ModelObject Constructor](../html/Overload_Grasshopper_Rhinoceros_Model_ModelObject__ctor.htm "ModelObject Constructor ")

[ModelObject Properties](../html/Properties_T_Grasshopper_Rhinoceros_Model_ModelObject.htm "ModelObject Properties")

[ModelObject Methods](../html/Methods_T_Grasshopper_Rhinoceros_Model_ModelObject.htm "ModelObject Methods")

[ModelObject Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Model_ModelObject.htm "ModelObject Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelObject Class |

Represents a Rhino model object. Wraps the functionality of the RhinoObject type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST9E807D1\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST9E807D1\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST9E807D1\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
      [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST9E807D1\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm)  
        Grasshopper.Rhinoceros.ModelAddLanguageSpecificTextSet("LST9E807D1\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelObject

**Namespace:**
 [Grasshopper.Rhinoceros.Model](N_Grasshopper_Rhinoceros_Model.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelObject : ModelComponentContent, 
	IGH_BakeAwareData, IGH_PreviewData, IGH_PreviewMeshData, IGH_RenderAwareData
```

```
Public NotInheritable Class ModelObject
	Inherits ModelComponentContent
	Implements IGH_BakeAwareData, IGH_PreviewData, IGH_PreviewMeshData, IGH_RenderAwareData
```

AddLanguageTabSet("ID1EBCA");

The ModelObject type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelObjectAddLanguageSpecificTextSet("LST9E807D1\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Model_ModelObject__ctor.htm) | Initializes a new instance of the ModelObject class |
| Public method | [ModelObject(ModelObjectAddLanguageSpecificTextSet("LST9E807D1\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes)](M_Grasshopper_Rhinoceros_Model_ModelObject__ctor_1.htm) | Initializes a new instance of the ModelObject class |
| Public method | [ModelObject(Guid)](M_Grasshopper_Rhinoceros_Model_ModelObject__ctor_5.htm) | Initializes a new instance of the ModelObject class |
| Public method | [ModelObject(RhinoObject)](M_Grasshopper_Rhinoceros_Model_ModelObject__ctor_2.htm) | Initializes a new instance of the ModelObject class |
| Public method | [ModelObject(RhinoDoc, ObjectAttributes)](M_Grasshopper_Rhinoceros_Model_ModelObject__ctor_3.htm) | Initializes a new instance of the ModelObject class |
| Public method | [ModelObject(RhinoDoc, ObjectAttributes, GeometryBase)](M_Grasshopper_Rhinoceros_Model_ModelObject__ctor_4.htm) | Initializes a new instance of the ModelObject class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Display](P_Grasshopper_Rhinoceros_Model_ModelObject_Display.htm) |  |
| Public property | [Drafting](P_Grasshopper_Rhinoceros_Model_ModelObject_Drafting.htm) |  |
| Public property | [Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_Model_ModelObject_IsValid.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LST9E807D1\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm).) |
| Public property | [Layer](P_Grasshopper_Rhinoceros_Model_ModelObject_Layer.htm) |  |
| Public property | [Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [ObjectType](P_Grasshopper_Rhinoceros_Model_ModelObject_ObjectType.htm) |  |
| Public property | [Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Render](P_Grasshopper_Rhinoceros_Model_ModelObject_Render.htm) |  |
| Public property | [Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [TypeName](P_Grasshopper_Rhinoceros_Model_ModelObject_TypeName.htm) | (Overrides ModelData.TypeName.) |
| Public property | [Url](P_Grasshopper_Rhinoceros_Model_ModelObject_Url.htm) |  |
| Public property | [UserText](P_Grasshopper_Rhinoceros_ModelComponentContent_UserText.htm) | (Inherited from [ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm).) |
| Public property | [Visibility](P_Grasshopper_Rhinoceros_Model_ModelObject_Visibility.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_Model_ModelObject_Cast.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LST9E807D1\_8?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST9E807D1\_9?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST9E807D1\_10?cpp=%");)](M_Grasshopper_Rhinoceros_Model_ModelObject_CastTo__1.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LST9E807D1\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST9E807D1\_12?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST9E807D1\_13?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST9E807D1\_14?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST9E807D1\_15?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST9E807D1\_16?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST9E807D1\_17?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST9E807D1\_18?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST9E807D1\_19?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST9E807D1\_20?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [GetBoundingBox](M_Grasshopper_Rhinoceros_Model_ModelObject_GetBoundingBox.htm) |  |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_Model_ModelObject_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_Model_ModelObject_TooltipString.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LST9E807D1\_21?cs=.|vb=.|cpp=::|nu=.|fs=.");TooltipStringAddLanguageSpecificTextSet("LST9E807D1\_22?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_Model_ModelObject_ToString.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LST9E807D1\_23?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST9E807D1\_24?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST9E807D1\_25?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ModelObjectAddLanguageSpecificTextSet("LST9E807D1\_26?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes to ModelObject)](M_Grasshopper_Rhinoceros_Model_ModelObject_op_Implicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST9E807D1\_27?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(RhinoObject to ModelObject)](M_Grasshopper_Rhinoceros_Model_ModelObject_op_Implicit_1.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Model Namespace](N_Grasshopper_Rhinoceros_Model.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)