# T_Grasshopper_Rhinoceros_Drafting_ModelLineWidth

﻿ ModelLineWidth Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Drafting](../html/N_Grasshopper_Rhinoceros_Drafting.htm "Grasshopper.Rhinoceros.Drafting")

[ModelLineWidth Class](../html/T_Grasshopper_Rhinoceros_Drafting_ModelLineWidth.htm "ModelLineWidth Class")

[ModelLineWidth Constructor](../html/Overload_Grasshopper_Rhinoceros_Drafting_ModelLineWidth__ctor.htm "ModelLineWidth Constructor ")

[ModelLineWidth Properties](../html/Properties_T_Grasshopper_Rhinoceros_Drafting_ModelLineWidth.htm "ModelLineWidth Properties")

[ModelLineWidth Methods](../html/Methods_T_Grasshopper_Rhinoceros_Drafting_ModelLineWidth.htm "ModelLineWidth Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelLineWidth Class |

Represents a Rhino model linetype.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST1CE4A758\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1CE4A758\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST1CE4A758\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Double](https://docs.microsoft.com/dotnet/api/system.double)AddLanguageSpecificTextSet("LST1CE4A758\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1CE4A758\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Number](T_Grasshopper_Kernel_Types_GH_Number.htm)  
      Grasshopper.Rhinoceros.DraftingAddLanguageSpecificTextSet("LST1CE4A758\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelLineWidth

**Namespace:**
 [Grasshopper.Rhinoceros.Drafting](N_Grasshopper_Rhinoceros_Drafting.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelLineWidth : GH_Number, 
	IEquatable<ModelLineWidth>
```

```
Public NotInheritable Class ModelLineWidth
	Inherits GH_Number
	Implements IEquatable(Of ModelLineWidth)
```

AddLanguageTabSet("ID1EBCA");

The ModelLineWidth type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelLineWidthAddLanguageSpecificTextSet("LST1CE4A758\_6?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth__ctor.htm) | Initializes a new instance of the ModelLineWidth class |
| Public method | [ModelLineWidth(Double)](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth__ctor_1.htm) | Initializes a new instance of the ModelLineWidth class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Number_IsValid.htm) | Gets the validity of this instance. If the number is NaN, then it is considered invalid (Inherited from [GH\_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Number_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Inherited from [GH\_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_TypeDescription.htm) | (Overrides [GH\_NumberAddLanguageSpecificTextSet("LST1CE4A758\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Number_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_TypeName.htm) | (Overrides [GH\_NumberAddLanguageSpecificTextSet("LST1CE4A758\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Number_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm) | Gets or sets the internal data. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST1CE4A758\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1CE4A758\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_CastFrom.htm) | (Overrides [GH\_NumberAddLanguageSpecificTextSet("LST1CE4A758\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Number_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST1CE4A758\_12?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST1CE4A758\_13?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST1CE4A758\_14?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST1CE4A758\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1CE4A758\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST1CE4A758\_17?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST1CE4A758\_18?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST1CE4A758\_19?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Number_CastTo__1.htm) | (Inherited from [GH\_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).) |
| Public method | [Duplicate](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_Duplicate.htm) | (Overrides [GH\_NumberAddLanguageSpecificTextSet("LST1CE4A758\_20?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST1CE4A758\_21?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Number_Duplicate.htm).) |
| Public method | [DuplicateNumber](M_Grasshopper_Kernel_Types_GH_Number_DuplicateNumber.htm) | (Inherited from [GH\_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).) |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Number_EmitProxy.htm) | (Inherited from [GH\_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).) |
| Public method | [Equals(ModelLineWidth)](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_Equals.htm) |  |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_Equals_1.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST1CE4A758\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");Equals(Object)](https://docs.microsoft.com/dotnet/api/system.object.equals#system-object-equals(system-object)).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_GetHashCode.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST1CE4A758\_23?cs=.|vb=.|cpp=::|nu=.|fs=.");GetHashCodeAddLanguageSpecificTextSet("LST1CE4A758\_24?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-object-gethashcode).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Number_Read.htm) | (Inherited from [GH\_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disappears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST1CE4A758\_25?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1CE4A758\_26?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_Drafting_ModelLineWidth_ToString.htm) | (Overrides [GH\_NumberAddLanguageSpecificTextSet("LST1CE4A758\_27?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST1CE4A758\_28?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Number_ToString.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Number_Write.htm) | (Inherited from [GH\_Number](T_Grasshopper_Kernel_Types_GH_Number.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Drafting Namespace](N_Grasshopper_Rhinoceros_Drafting.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)