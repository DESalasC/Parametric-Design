# T_Grasshopper_Rhinoceros_Display_ModelDisplayMode

﻿ ModelDisplayMode Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Display](../html/N_Grasshopper_Rhinoceros_Display.htm "Grasshopper.Rhinoceros.Display")

[ModelDisplayMode Class](../html/T_Grasshopper_Rhinoceros_Display_ModelDisplayMode.htm "ModelDisplayMode Class")

[ModelDisplayMode Constructor](../html/Overload_Grasshopper_Rhinoceros_Display_ModelDisplayMode__ctor.htm "ModelDisplayMode Constructor ")

[ModelDisplayMode Properties](../html/Properties_T_Grasshopper_Rhinoceros_Display_ModelDisplayMode.htm "ModelDisplayMode Properties")

[ModelDisplayMode Methods](../html/Methods_T_Grasshopper_Rhinoceros_Display_ModelDisplayMode.htm "ModelDisplayMode Methods")

[ModelDisplayMode Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Display_ModelDisplayMode.htm "ModelDisplayMode Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelDisplayMode Class |

Represents a Rhino display mode. Wraps the functionality of the DisplayModeDescription type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST5D5CE8A6\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST5D5CE8A6\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST5D5CE8A6\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
      Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LST5D5CE8A6\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelDisplayMode

**Namespace:**
 [Grasshopper.Rhinoceros.Display](N_Grasshopper_Rhinoceros_Display.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelDisplayMode : ModelContent, 
	IGH_BakeAwareData
```

```
Public NotInheritable Class ModelDisplayMode
	Inherits ModelContent
	Implements IGH_BakeAwareData
```

AddLanguageTabSet("ID1EBCA");

The ModelDisplayMode type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelDisplayModeAddLanguageSpecificTextSet("LST5D5CE8A6\_4?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode__ctor.htm) | Initializes a new instance of the ModelDisplayMode class |
| Public method | [ModelDisplayMode(ModelDisplayModeAddLanguageSpecificTextSet("LST5D5CE8A6\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode__ctor_1.htm) | Initializes a new instance of the ModelDisplayMode class |
| Public method | [ModelDisplayMode(DisplayModeDescription)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode__ctor_2.htm) | Initializes a new instance of the ModelDisplayMode class |
| Public method | [ModelDisplayMode(Guid)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode__ctor_3.htm) | Initializes a new instance of the ModelDisplayMode class |

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
| Public propertyStatic member | [Unset](P_Grasshopper_Rhinoceros_Display_ModelDisplayMode_Unset.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_Cast.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LST5D5CE8A6\_6?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST5D5CE8A6\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST5D5CE8A6\_8?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST5D5CE8A6\_9?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST5D5CE8A6\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST5D5CE8A6\_11?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_TooltipString.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LST5D5CE8A6\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");TooltipStringAddLanguageSpecificTextSet("LST5D5CE8A6\_13?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_ToString.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LST5D5CE8A6\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST5D5CE8A6\_15?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST5D5CE8A6\_16?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ModelDisplayModeAddLanguageSpecificTextSet("LST5D5CE8A6\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes to ModelDisplayMode)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_op_Implicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST5D5CE8A6\_18?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(DisplayModeDescription to ModelDisplayMode)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_op_Implicit_1.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST5D5CE8A6\_19?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(Guid to ModelDisplayMode)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_op_Implicit_2.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST5D5CE8A6\_20?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(String to ModelDisplayMode)](M_Grasshopper_Rhinoceros_Display_ModelDisplayMode_op_Implicit_3.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Display Namespace](N_Grasshopper_Rhinoceros_Display.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)