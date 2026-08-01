# T_Grasshopper_Rhinoceros_Drafting_ModelLinetype

﻿ ModelLinetype Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Drafting](../html/N_Grasshopper_Rhinoceros_Drafting.htm "Grasshopper.Rhinoceros.Drafting")

[ModelLinetype Class](../html/T_Grasshopper_Rhinoceros_Drafting_ModelLinetype.htm "ModelLinetype Class")

[ModelLinetype Constructor](../html/Overload_Grasshopper_Rhinoceros_Drafting_ModelLinetype__ctor.htm "ModelLinetype Constructor ")

[ModelLinetype Properties](../html/Properties_T_Grasshopper_Rhinoceros_Drafting_ModelLinetype.htm "ModelLinetype Properties")

[ModelLinetype Methods](../html/Methods_T_Grasshopper_Rhinoceros_Drafting_ModelLinetype.htm "ModelLinetype Methods")

[ModelLinetype Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Drafting_ModelLinetype.htm "ModelLinetype Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelLinetype Class |

Represents a Rhino model linetype. Wraps the functionality of the Linetype type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST506A6593\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST506A6593\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST506A6593\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
      [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST506A6593\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm)  
        Grasshopper.Rhinoceros.DraftingAddLanguageSpecificTextSet("LST506A6593\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelLinetype

**Namespace:**
 [Grasshopper.Rhinoceros.Drafting](N_Grasshopper_Rhinoceros_Drafting.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelLinetype : ModelComponentContent, 
	IGH_BakeAwareData
```

```
Public NotInheritable Class ModelLinetype
	Inherits ModelComponentContent
	Implements IGH_BakeAwareData
```

AddLanguageTabSet("ID1EBCA");

The ModelLinetype type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelLinetypeAddLanguageSpecificTextSet("LST506A6593\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype__ctor.htm) | Initializes a new instance of the ModelLinetype class |
| Public method | [ModelLinetype(ModelLinetypeAddLanguageSpecificTextSet("LST506A6593\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes)](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype__ctor_1.htm) | Initializes a new instance of the ModelLinetype class |
| Public method | [ModelLinetype(Guid)](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype__ctor_3.htm) | Initializes a new instance of the ModelLinetype class |
| Public method | [ModelLinetype(Linetype)](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype__ctor_2.htm) | Initializes a new instance of the ModelLinetype class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [CapStyle](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_CapStyle.htm) |  |
| Public property | [Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [JoinStyle](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_JoinStyle.htm) |  |
| Public property | [Name](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_Name.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LST506A6593\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm).) |
| Public property | [Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Segments](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_Segments.htm) |  |
| Public property | [Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [TaperPoints](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_TaperPoints.htm) |  |
| Public propertyStatic member | [Unset](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_Unset.htm) |  |
| Public property | [UserText](P_Grasshopper_Rhinoceros_ModelComponentContent_UserText.htm) | (Inherited from [ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm).) |
| Public property | [Width](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_Width.htm) |  |
| Public property | [WidthUnits](P_Grasshopper_Rhinoceros_Drafting_ModelLinetype_WidthUnits.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype_Cast.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LST506A6593\_8?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST506A6593\_9?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST506A6593\_10?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST506A6593\_11?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST506A6593\_12?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST506A6593\_13?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST506A6593\_14?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ModelLinetypeAddLanguageSpecificTextSet("LST506A6593\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes to ModelLinetype)](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype_op_Implicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST506A6593\_16?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(Linetype to ModelLinetype)](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype_op_Implicit_1.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST506A6593\_17?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(String to ModelLinetype)](M_Grasshopper_Rhinoceros_Drafting_ModelLinetype_op_Implicit_2.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Drafting Namespace](N_Grasshopper_Rhinoceros_Drafting.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)