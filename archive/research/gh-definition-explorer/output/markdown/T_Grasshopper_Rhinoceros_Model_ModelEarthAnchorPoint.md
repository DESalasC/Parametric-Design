# T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint

﻿ ModelEarthAnchorPoint Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Model](../html/N_Grasshopper_Rhinoceros_Model.htm "Grasshopper.Rhinoceros.Model")

[ModelEarthAnchorPoint Class](../html/T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint.htm "ModelEarthAnchorPoint Class")

[ModelEarthAnchorPoint Constructor](../html/Overload_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint__ctor.htm "ModelEarthAnchorPoint Constructor ")

[ModelEarthAnchorPoint Properties](../html/Properties_T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint.htm "ModelEarthAnchorPoint Properties")

[ModelEarthAnchorPoint Methods](../html/Methods_T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint.htm "ModelEarthAnchorPoint Methods")

[ModelEarthAnchorPoint Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint.htm "ModelEarthAnchorPoint Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelEarthAnchorPoint Class |

Represents a Rhino Earth anchor point. Wraps the functionality of the EarthAnchorPoint type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTF7C3DC39\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTF7C3DC39\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTF7C3DC39\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
      Grasshopper.Rhinoceros.ModelAddLanguageSpecificTextSet("LSTF7C3DC39\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelEarthAnchorPoint

**Namespace:**
 [Grasshopper.Rhinoceros.Model](N_Grasshopper_Rhinoceros_Model.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelEarthAnchorPoint : ModelContent, 
	IGH_BakeAwareData
```

```
Public NotInheritable Class ModelEarthAnchorPoint
	Inherits ModelContent
	Implements IGH_BakeAwareData
```

AddLanguageTabSet("ID1EBCA");

The ModelEarthAnchorPoint type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelEarthAnchorPointAddLanguageSpecificTextSet("LSTF7C3DC39\_4?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint__ctor.htm) | Initializes a new instance of the ModelEarthAnchorPoint class |
| Public method | [ModelEarthAnchorPoint(ModelEarthAnchorPointAddLanguageSpecificTextSet("LSTF7C3DC39\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes)](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint__ctor_1.htm) | Initializes a new instance of the ModelEarthAnchorPoint class |
| Public method | [ModelEarthAnchorPoint(EarthAnchorPoint)](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint__ctor_2.htm) | Initializes a new instance of the ModelEarthAnchorPoint class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Elevation](P_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_Elevation.htm) | Gets a point elevation on earth, in meters. |
| Public property | [ElevationCoordinateSystem](P_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_ElevationCoordinateSystem.htm) | Gets the value indicating the zero level convention relating to a location on Earth |
| Public property | [Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Latitude](P_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_Latitude.htm) | Gets a point latitude on earth, in degrees. [-90, +90] |
| Public property | [Longitude](P_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_Longitude.htm) | Gets a point longitude on earth, in degrees. [-180, +180] |
| Public property | [ModelCompass](P_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_ModelCompass.htm) | Gets the corresponding compass plane in model coordinates |
| Public property | [Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_Cast.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LSTF7C3DC39\_6?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTF7C3DC39\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTF7C3DC39\_8?cpp=%");)](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_CastTo__1.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LSTF7C3DC39\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LSTF7C3DC39\_10?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTF7C3DC39\_11?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTF7C3DC39\_12?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTF7C3DC39\_13?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTF7C3DC39\_14?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTF7C3DC39\_15?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTF7C3DC39\_16?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTF7C3DC39\_17?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTF7C3DC39\_18?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_TooltipString.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LSTF7C3DC39\_19?cs=.|vb=.|cpp=::|nu=.|fs=.");TooltipStringAddLanguageSpecificTextSet("LSTF7C3DC39\_20?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_ToString.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LSTF7C3DC39\_21?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTF7C3DC39\_22?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTF7C3DC39\_23?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ModelEarthAnchorPointAddLanguageSpecificTextSet("LSTF7C3DC39\_24?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes to ModelEarthAnchorPoint)](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_op_Implicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTF7C3DC39\_25?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(EarthAnchorPoint to ModelEarthAnchorPoint)](M_Grasshopper_Rhinoceros_Model_ModelEarthAnchorPoint_op_Implicit_1.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Model Namespace](N_Grasshopper_Rhinoceros_Model.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)