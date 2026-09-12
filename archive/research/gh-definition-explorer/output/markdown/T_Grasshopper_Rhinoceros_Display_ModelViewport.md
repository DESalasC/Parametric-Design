# T_Grasshopper_Rhinoceros_Display_ModelViewport

﻿ ModelViewport Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Display](../html/N_Grasshopper_Rhinoceros_Display.htm "Grasshopper.Rhinoceros.Display")

[ModelViewport Class](../html/T_Grasshopper_Rhinoceros_Display_ModelViewport.htm "ModelViewport Class")

[ModelViewport Properties](../html/Properties_T_Grasshopper_Rhinoceros_Display_ModelViewport.htm "ModelViewport Properties")

[ModelViewport Methods](../html/Methods_T_Grasshopper_Rhinoceros_Display_ModelViewport.htm "ModelViewport Methods")

[ModelViewport Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_Display_ModelViewport.htm "ModelViewport Type Conversions")

[ModelViewport Fields](../html/Fields_T_Grasshopper_Rhinoceros_Display_ModelViewport.htm "ModelViewport Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelViewport Class |

Represents a Rhino viewport. Wraps the main viewport of a RhinoView instance.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST96805230\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST96805230\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelData](T_Grasshopper_Rhinoceros_ModelData.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST96805230\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm)  
      Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LST96805230\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelViewport  
        [Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LST96805230\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelPageViewport](T_Grasshopper_Rhinoceros_Display_ModelPageViewport.htm)  
        [Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LST96805230\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelStandardViewport](T_Grasshopper_Rhinoceros_Display_ModelStandardViewport.htm)

**Namespace:**
 [Grasshopper.Rhinoceros.Display](N_Grasshopper_Rhinoceros_Display.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class ModelViewport : ModelContent, 
	IGH_BakeAwareData
```

```
Public Class ModelViewport
	Inherits ModelContent
	Implements IGH_BakeAwareData
```

AddLanguageTabSet("ID1EBCA");

The ModelViewport type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Protected property | [Attribs](P_Grasshopper_Rhinoceros_Display_ModelViewport_Attribs.htm) |  |
| Protected property | [DefaultAttributes](P_Grasshopper_Rhinoceros_Display_ModelViewport_DefaultAttributes.htm) | (Overrides [ModelDataAddLanguageSpecificTextSet("LST96805230\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");DefaultAttributes](P_Grasshopper_Rhinoceros_ModelData_DefaultAttributes.htm).) |
| Public property | [DisplayMode](P_Grasshopper_Rhinoceros_Display_ModelViewport_DisplayMode.htm) |  |
| Public property | [Id](P_Grasshopper_Rhinoceros_ModelContent_Id.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected property | [IsReferencedData](P_Grasshopper_Rhinoceros_ModelContent_IsReferencedData.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected property | [IsReferencedDataLoaded](P_Grasshopper_Rhinoceros_ModelContent_IsReferencedDataLoaded.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_ModelContent_IsValid.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected property | [IsValidWhyNot](P_Grasshopper_Rhinoceros_ModelContent_IsValidWhyNot.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Name](P_Grasshopper_Rhinoceros_ModelContent_Name.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Notes](P_Grasshopper_Rhinoceros_ModelContent_Notes.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Parent](P_Grasshopper_Rhinoceros_ModelContent_Parent.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Path](P_Grasshopper_Rhinoceros_ModelContent_Path.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public property | [Space](P_Grasshopper_Rhinoceros_Display_ModelViewport_Space.htm) |  |
| Public property | [Tags](P_Grasshopper_Rhinoceros_ModelContent_Tags.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected property | [TypeDescription](P_Grasshopper_Rhinoceros_ModelData_TypeDescription.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public propertyStatic member | [Unset](P_Grasshopper_Rhinoceros_Display_ModelViewport_Unset.htm) |  |
| Public property | [ViewportType](P_Grasshopper_Rhinoceros_Display_ModelViewport_ViewportType.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [AsFrozen](M_Grasshopper_Rhinoceros_ModelContent_AsFrozen.htm) | Try to obtain a dereferenced snapshot of itself. (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_Display_ModelViewport_Cast.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LST96805230\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST96805230\_8?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST96805230\_9?cpp=%");)](M_Grasshopper_Rhinoceros_Display_ModelViewport_CastTo__1.htm) | (Overrides [ModelContentAddLanguageSpecificTextSet("LST96805230\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST96805230\_11?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST96805230\_12?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST96805230\_13?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST96805230\_14?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST96805230\_15?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST96805230\_16?cpp=%");)](M_Grasshopper_Rhinoceros_ModelContent_CastTo__1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST96805230\_17?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST96805230\_18?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST96805230\_19?cpp=%");)](M_Grasshopper_Rhinoceros_ModelData_CastTo__1.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(ModelContent)](M_Grasshopper_Rhinoceros_ModelContent_Equals.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [Equals(ModelData)](M_Grasshopper_Rhinoceros_ModelData_Equals.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelContent_Equals_1.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelContent_GetHashCode.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected method | [InternaliseData](M_Grasshopper_Rhinoceros_ModelContent_InternaliseData.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected method | [LoadReferencedData](M_Grasshopper_Rhinoceros_ModelContent_LoadReferencedData.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected method | [Read](M_Grasshopper_Rhinoceros_ModelContent_Read.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected method | [RuntimeId](M_Grasshopper_Rhinoceros_ModelContent_RuntimeId.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToAttributes](M_Grasshopper_Rhinoceros_Display_ModelViewport_ToAttributes.htm) |  |
| Public method | [ToDetails](M_Grasshopper_Rhinoceros_ModelData_ToDetails.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_ModelContent_TooltipString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelContent_ToString.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected method | [UnloadReferencedData](M_Grasshopper_Rhinoceros_ModelContent_UnloadReferencedData.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |
| Protected method | [Write](M_Grasshopper_Rhinoceros_ModelContent_Write.htm) | (Inherited from [ModelContent](T_Grasshopper_Rhinoceros_ModelContent.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST96805230\_20?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(ModelViewportAddLanguageSpecificTextSet("LST96805230\_21?cs=.|vb=.|cpp=::|nu=.|fs=.");Attributes to ModelViewport)](M_Grasshopper_Rhinoceros_Display_ModelViewport_op_Implicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LST96805230\_22?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(RhinoViewport to ModelViewport)](M_Grasshopper_Rhinoceros_Display_ModelViewport_op_Implicit_1.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [Serial](F_Grasshopper_Rhinoceros_ModelData_Serial.htm) | (Inherited from [ModelData](T_Grasshopper_Rhinoceros_ModelData.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Display Namespace](N_Grasshopper_Rhinoceros_Display.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)