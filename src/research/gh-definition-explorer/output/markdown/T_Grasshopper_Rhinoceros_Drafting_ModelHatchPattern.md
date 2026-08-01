# T_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern

﻿ ModelHatchPattern Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Drafting](../html/N_Grasshopper_Rhinoceros_Drafting.htm "Grasshopper.Rhinoceros.Drafting")

[ModelHatchPattern Class](../html/T_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern.htm "ModelHatchPattern Class")

[ModelHatchPattern Constructor](../html/Overload_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern__ctor.htm "ModelHatchPattern Constructor ")

[ModelHatchPattern Properties](../html/Properties_T_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern.htm "ModelHatchPattern Properties")

[ModelHatchPattern Methods](../html/Methods_T_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern.htm "ModelHatchPattern Methods")

[ModelHatchPattern Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern.htm "ModelHatchPattern Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelHatchPattern Class |

Represents a Rhino model hatch pattern. Wraps the functionality of the HatchPattern type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTDE7BCBDE\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTDE7BCBDE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTDE7BCBDE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
      [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTDE7BCBDE\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm)  
        Grasshopper.Rhinoceros.DraftingAddLanguageSpecificTextSet("LSTDE7BCBDE\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelHatchPattern

**Namespace:**
 [Grasshopper.Rhinoceros.Drafting](N_Grasshopper_Rhinoceros_Drafting.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelHatchPattern : ModelComponentContent, 
	IGH_BakeAwareData
```

```
Public NotInheritable Class ModelHatchPattern
	Inherits ModelComponentContent
	Implements IGH_BakeAwareData
```

AddLanguageTabSet("ID1EBCA");

The ModelHatchPattern type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelHatchPatternAddLanguageSpecificTextSet("LSTDE7BCBDE\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern__ctor.htm) | Initializes a new instance of the ModelHatchPattern class |
| Public method | [ModelHatchPattern(ModelHatchPatternAddLanguageSpecificTextSet("LSTDE7BCBDE\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes)](M_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern__ctor_1.htm) | Initializes a new instance of the ModelHatchPattern class |
| Public method | [ModelHatchPattern(Guid)](M_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern__ctor_3.htm) | Initializes a new instance of the ModelHatchPattern class |
| Public method | [ModelHatchPattern(HatchPattern)](M_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern__ctor_2.htm) | Initializes a new instance of the ModelHatchPattern class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [FillType](P_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern_FillType.htm) |  |
| Public property | [Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Lines](P_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern_Lines.htm) |  |
| Public property | [Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public propertyStatic member | [Unset](P_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern_Unset.htm) |  |
| Public property | [UserText](P_Grasshopper_Rhinoceros_ModelComponentContent_UserText.htm) | (Inherited from [ModelComponentContent](T_Grasshopper_Rhinoceros_ModelComponentContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern_Cast.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LSTDE7BCBDE\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTDE7BCBDE\_8?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTDE7BCBDE\_9?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTDE7BCBDE\_10?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTDE7BCBDE\_11?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTDE7BCBDE\_12?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTDE7BCBDE\_13?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ModelHatchPatternAddLanguageSpecificTextSet("LSTDE7BCBDE\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes to ModelHatchPattern)](M_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern_op_Implicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTDE7BCBDE\_15?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(HatchPattern to ModelHatchPattern)](M_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern_op_Implicit_1.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTDE7BCBDE\_16?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(String to ModelHatchPattern)](M_Grasshopper_Rhinoceros_Drafting_ModelHatchPattern_op_Implicit_2.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Drafting Namespace](N_Grasshopper_Rhinoceros_Drafting.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)