# T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle

﻿ ModelAnnotationStyle Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Annotations](../html/N_Grasshopper_Rhinoceros_Annotations.htm "Grasshopper.Rhinoceros.Annotations")

[ModelAnnotationStyle Class](../html/T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle.htm "ModelAnnotationStyle Class")

[ModelAnnotationStyle Constructor](../html/Overload_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle__ctor.htm "ModelAnnotationStyle Constructor ")

[ModelAnnotationStyle Properties](../html/Properties_T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle.htm "ModelAnnotationStyle Properties")

[ModelAnnotationStyle Methods](../html/Methods_T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle.htm "ModelAnnotationStyle Methods")

[ModelAnnotationStyle Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle.htm "ModelAnnotationStyle Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelAnnotationStyle Class |

Represents a Rhino model annotation style. Wraps the functionality of the DimensionStyle type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST1ACD39B5\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST1ACD39B5\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST1ACD39B5\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
      [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST1ACD39B5\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm)  
        Grasshopper.Rhinoceros.AnnotationsAddLanguageSpecificTextSet("LST1ACD39B5\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelAnnotationStyle

**Namespace:**
 [Grasshopper.Rhinoceros.Annotations](N_Grasshopper_Rhinoceros_Annotations.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelAnnotationStyle : ModelComponentContent, 
	IGH_BakeAwareData
```

```
Public NotInheritable Class ModelAnnotationStyle
	Inherits ModelComponentContent
	Implements IGH_BakeAwareData
```

AddLanguageTabSet("ID1EBCA");

The ModelAnnotationStyle type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelAnnotationStyleAddLanguageSpecificTextSet("LST1ACD39B5\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle__ctor.htm) | Initializes a new instance of the ModelAnnotationStyle class |
| Public method | [ModelAnnotationStyle(ModelAnnotationStyleAddLanguageSpecificTextSet("LST1ACD39B5\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle__ctor_1.htm) | Initializes a new instance of the ModelAnnotationStyle class |
| Public method | [ModelAnnotationStyle(DimensionStyle)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle__ctor_2.htm) | Initializes a new instance of the ModelAnnotationStyle class |
| Public method | [ModelAnnotationStyle(Guid)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle__ctor_3.htm) | Initializes a new instance of the ModelAnnotationStyle class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ArrowSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_ArrowSettings.htm) |  |
| Public property | [DimensionScale](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_DimensionScale.htm) |  |
| Public property | [DimensionSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_DimensionSettings.htm) |  |
| Public property | [Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [LeaderSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_LeaderSettings.htm) |  |
| Public property | [Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [TextSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_TextSettings.htm) |  |
| Public property | [ToleranceSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_ToleranceSettings.htm) |  |
| Public property | [UnitsSettings](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_UnitsSettings.htm) |  |
| Public propertyStatic member | [Unset](P_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Unset.htm) |  |
| Public property | [UserText](P_Grasshopper_Rhinoceros_ModelComponentContent_UserText.htm) | (Inherited from [ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_Cast.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LST1ACD39B5\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST1ACD39B5\_8?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST1ACD39B5\_9?cpp=%");)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_CastTo__1.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LST1ACD39B5\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST1ACD39B5\_11?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST1ACD39B5\_12?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST1ACD39B5\_13?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST1ACD39B5\_14?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST1ACD39B5\_15?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST1ACD39B5\_16?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST1ACD39B5\_17?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST1ACD39B5\_18?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST1ACD39B5\_19?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST1ACD39B5\_20?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ModelAnnotationStyleAddLanguageSpecificTextSet("LST1ACD39B5\_21?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes to ModelAnnotationStyle)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_op_Implicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST1ACD39B5\_22?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(DimensionStyle to ModelAnnotationStyle)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_op_Implicit_1.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST1ACD39B5\_23?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(String to ModelAnnotationStyle)](M_Grasshopper_Rhinoceros_Annotations_ModelAnnotationStyle_op_Implicit_2.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Annotations Namespace](N_Grasshopper_Rhinoceros_Annotations.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)