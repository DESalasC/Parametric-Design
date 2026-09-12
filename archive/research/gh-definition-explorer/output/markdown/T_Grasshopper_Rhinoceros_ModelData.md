# T_Grasshopper_Rhinoceros_ModelData

﻿ ModelData Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm "Grasshopper.Rhinoceros")

[ModelData Class](../html/T_Grasshopper_Rhinoceros_ModelData.htm "ModelData Class")

[ModelData Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelData.htm "ModelData Properties")

[ModelData Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelData.htm "ModelData Methods")

[ModelData Fields](../html/Fields_T_Grasshopper_Rhinoceros_ModelData.htm "ModelData Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelData Class |

Represents a Rhino model chunk of data.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST2997A1E1\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST2997A1E1\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData  
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
public abstract class ModelData : IGH_ModelData, 
	ICloneable, IComparable, IEquatable<ModelData>, IStructuralEquatable
```

```
Public MustInherit Class ModelData
	Implements IGH_ModelData, ICloneable, IComparable, IEquatable(Of ModelData), 
	IStructuralEquatable
```

AddLanguageTabSet("ID1EBCA");

The ModelData type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Protected property | [Attribs](P_Grasshopper_Rhinoceros_ModelData_Attribs.htm) |  |
| Protected property | [DefaultAttributes](P_Grasshopper_Rhinoceros_ModelData_DefaultAttributes.htm) |  |
| Protected property | [IsValidWhyNot](P_Grasshopper_Rhinoceros_ModelData_IsValidWhyNot.htm) |  |
| Protected property | [TypeDescription](P_Grasshopper_Rhinoceros_ModelData_TypeDescription.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected methodStatic member | [CastAddLanguageSpecificTextSet("LST2997A1E1\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");A, TAddLanguageSpecificTextSet("LST2997A1E1\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Rhinoceros_ModelData_Cast__2.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LST2997A1E1\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST2997A1E1\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) |  |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) |  |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelData_Equals_1.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST2997A1E1\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Equals(Object)](https://docs.microsoft.com/dotnet/api/system.object.equals#system-object-equals(system-object)).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelData_GetHashCode.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST2997A1E1\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GetHashCodeAddLanguageSpecificTextSet("LST2997A1E1\_8?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-object-gethashcode).) |
| Protected method | [Read](M_Grasshopper_Rhinoceros_ModelData_Read.htm) |  |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_ModelData_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) |  |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_ModelData_TooltipString.htm) |  |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelData_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST2997A1E1\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST2997A1E1\_10?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |
| Protected method | [Write](M_Grasshopper_Rhinoceros_ModelData_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [Serial](F_Grasshopper_Rhinoceros_ModelData_Serial.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Remarks

This type is the base type of a family of immutable types.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST2997A1E1\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST2997A1E1\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData  
    [Grasshopper.Rhinoceros.AnnotationsAddLanguageSpecificTextSet("LST2997A1E1\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");AnnotationArrow](T_Grasshopper_Rhinoceros_Annotations_AnnotationArrow.htm)  
    [Grasshopper.Rhinoceros.AnnotationsAddLanguageSpecificTextSet("LST2997A1E1\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");AnnotationArrowSettings](T_Grasshopper_Rhinoceros_Annotations_AnnotationArrowSettings.htm)  
    [Grasshopper.Rhinoceros.AnnotationsAddLanguageSpecificTextSet("LST2997A1E1\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");AnnotationDimensionSettings](T_Grasshopper_Rhinoceros_Annotations_AnnotationDimensionSettings.htm)  
    [Grasshopper.Rhinoceros.AnnotationsAddLanguageSpecificTextSet("LST2997A1E1\_16?cs=.|vb=.|cpp=::|nu=.|fs=.");AnnotationLeaderSettings](T_Grasshopper_Rhinoceros_Annotations_AnnotationLeaderSettings.htm)  
    [Grasshopper.Rhinoceros.AnnotationsAddLanguageSpecificTextSet("LST2997A1E1\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");AnnotationTextSettings](T_Grasshopper_Rhinoceros_Annotations_AnnotationTextSettings.htm)  
    [Grasshopper.Rhinoceros.AnnotationsAddLanguageSpecificTextSet("LST2997A1E1\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");AnnotationToleranceSettings](T_Grasshopper_Rhinoceros_Annotations_AnnotationToleranceSettings.htm)  
    [Grasshopper.Rhinoceros.AnnotationsAddLanguageSpecificTextSet("LST2997A1E1\_19?cs=.|vb=.|cpp=::|nu=.|fs=.");AnnotationUnitsSettings](T_Grasshopper_Rhinoceros_Annotations_AnnotationUnitsSettings.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST2997A1E1\_20?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)