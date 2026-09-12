# T_Grasshopper_Rhinoceros_Model_ModelLayer

﻿ ModelLayer Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Model](../html/N_Grasshopper_Rhinoceros_Model.htm "Grasshopper.Rhinoceros.Model")

[ModelLayer Class](../html/T_Grasshopper_Rhinoceros_Model_ModelLayer.htm "ModelLayer Class")

[ModelLayer Constructor](../html/Overload_Grasshopper_Rhinoceros_Model_ModelLayer__ctor.htm "ModelLayer Constructor ")

[ModelLayer Properties](../html/Properties_T_Grasshopper_Rhinoceros_Model_ModelLayer.htm "ModelLayer Properties")

[ModelLayer Methods](../html/Methods_T_Grasshopper_Rhinoceros_Model_ModelLayer.htm "ModelLayer Methods")

[ModelLayer Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Model_ModelLayer.htm "ModelLayer Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelLayer Class |

Represents a Rhino model layer. Wraps the functionality of the Layer type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTF6E360E6\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTF6E360E6\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTF6E360E6\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
      [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTF6E360E6\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm)  
        Grasshopper.Rhinoceros.ModelAddLanguageSpecificTextSet("LSTF6E360E6\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelLayer

**Namespace:**
 [Grasshopper.Rhinoceros.Model](N_Grasshopper_Rhinoceros_Model.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelLayer : ModelComponentContent, 
	IGH_BakeAwareData
```

```
Public NotInheritable Class ModelLayer
	Inherits ModelComponentContent
	Implements IGH_BakeAwareData
```

AddLanguageTabSet("ID1EBCA");

The ModelLayer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelLayerAddLanguageSpecificTextSet("LSTF6E360E6\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Model_ModelLayer__ctor.htm) | Initializes a new instance of the ModelLayer class |
| Public method | [ModelLayer(ModelLayerAddLanguageSpecificTextSet("LSTF6E360E6\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes)](M_Grasshopper_Rhinoceros_Model_ModelLayer__ctor_1.htm) | Initializes a new instance of the ModelLayer class |
| Public method | [ModelLayer(Guid)](M_Grasshopper_Rhinoceros_Model_ModelLayer__ctor_3.htm) | Initializes a new instance of the ModelLayer class |
| Public method | [ModelLayer(Layer)](M_Grasshopper_Rhinoceros_Model_ModelLayer__ctor_2.htm) | Initializes a new instance of the ModelLayer class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [DisplayColor](P_Grasshopper_Rhinoceros_Model_ModelLayer_DisplayColor.htm) |  |
| Public property | [DraftingColor](P_Grasshopper_Rhinoceros_Model_ModelLayer_DraftingColor.htm) |  |
| Public property | [Hidden](P_Grasshopper_Rhinoceros_Model_ModelLayer_Hidden.htm) |  |
| Public property | [HiddenOnModel](P_Grasshopper_Rhinoceros_Model_ModelLayer_HiddenOnModel.htm) |  |
| Public property | [HiddenOnNewDetail](P_Grasshopper_Rhinoceros_Model_ModelLayer_HiddenOnNewDetail.htm) |  |
| Public property | [Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Linetype](P_Grasshopper_Rhinoceros_Model_ModelLayer_Linetype.htm) |  |
| Public property | [LineWeight](P_Grasshopper_Rhinoceros_Model_ModelLayer_LineWeight.htm) |  |
| Public property | [Locked](P_Grasshopper_Rhinoceros_Model_ModelLayer_Locked.htm) |  |
| Public property | [Material](P_Grasshopper_Rhinoceros_Model_ModelLayer_Material.htm) |  |
| Public property | [Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public propertyStatic member | [Unset](P_Grasshopper_Rhinoceros_Model_ModelLayer_Unset.htm) |  |
| Public property | [UserText](P_Grasshopper_Rhinoceros_ModelComponentContent_UserText.htm) | (Inherited from [ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_Model_ModelLayer_Cast.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LSTF6E360E6\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTF6E360E6\_8?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTF6E360E6\_9?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTF6E360E6\_10?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTF6E360E6\_11?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTF6E360E6\_12?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_Model_ModelLayer_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTF6E360E6\_13?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ModelLayerAddLanguageSpecificTextSet("LSTF6E360E6\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes to ModelLayer)](M_Grasshopper_Rhinoceros_Model_ModelLayer_op_Implicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTF6E360E6\_15?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(Layer to ModelLayer)](M_Grasshopper_Rhinoceros_Model_ModelLayer_op_Implicit_1.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTF6E360E6\_16?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(String to ModelLayer)](M_Grasshopper_Rhinoceros_Model_ModelLayer_op_Implicit_2.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Model Namespace](N_Grasshopper_Rhinoceros_Model.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)