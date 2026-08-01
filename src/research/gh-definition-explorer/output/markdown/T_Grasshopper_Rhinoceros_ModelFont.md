# T_Grasshopper_Rhinoceros_ModelFont

﻿ ModelFont Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm "Grasshopper.Rhinoceros")

[ModelFont Class](../html/T_Grasshopper_Rhinoceros_ModelFont.htm "ModelFont Class")

[ModelFont Constructor](../html/Overload_Grasshopper_Rhinoceros_ModelFont__ctor.htm "ModelFont Constructor ")

[ModelFont Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelFont.htm "ModelFont Properties")

[ModelFont Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelFont.htm "ModelFont Methods")

[ModelFont Type Conversions](../html/Operators_T_Grasshopper_Rhinoceros_ModelFont.htm "ModelFont Type Conversions")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelFont Class |

Represents a typography font. Wraps the functionality of the Font type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTCD89B895\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTCD89B895\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LSTCD89B895\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");FontAddLanguageSpecificTextSet("LSTCD89B895\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTCD89B895\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelFont

**Namespace:**
 [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelFont : GH_Goo<Font>, 
	IEquatable<ModelFont>
```

```
Public NotInheritable Class ModelFont
	Inherits GH_Goo(Of Font)
	Implements IEquatable(Of ModelFont)
```

AddLanguageTabSet("ID1EBCA");

The ModelFont type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelFontAddLanguageSpecificTextSet("LSTCD89B895\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_ModelFont__ctor.htm) | Initializes a new instance of the ModelFont class |
| Public method | [ModelFont(Font)](M_Grasshopper_Rhinoceros_ModelFont__ctor_1.htm) | Initializes a new instance of the ModelFont class |
| Public method | [ModelFont(String)](M_Grasshopper_Rhinoceros_ModelFont__ctor_2.htm) | Initializes a new instance of the ModelFont class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [FamilyName](P_Grasshopper_Rhinoceros_ModelFont_FamilyName.htm) |  |
| Public propertyStatic member | [InstalledFamilies](P_Grasshopper_Rhinoceros_ModelFont_InstalledFamilies.htm) |  |
| Public propertyStatic member | [InstalledFonts](P_Grasshopper_Rhinoceros_ModelFont_InstalledFonts.htm) |  |
| Public property | [IsInstalled](P_Grasshopper_Rhinoceros_ModelFont_IsInstalled.htm) |  |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_ModelFont_IsValid.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCD89B895\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Rhinoceros_ModelFont_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_11?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_12?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCD89B895\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Rhinoceros_ModelFont_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_14?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_15?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCD89B895\_16?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm) | Gets or sets the internal data. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_17?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_18?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_ModelFont_Cast.htm) |  |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm) | Attempt a cast from generic data. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTCD89B895\_21?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTCD89B895\_22?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_23?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_24?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [Duplicate](M_Grasshopper_Rhinoceros_ModelFont_Duplicate.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_25?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_26?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCD89B895\_27?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LSTCD89B895\_28?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).) |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm) | Create a new proxy for this instance. Return Null if this class does not support proxies. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_29?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_30?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [Equals(ModelFont)](M_Grasshopper_Rhinoceros_ModelFont_Equals.htm) |  |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_ModelFont_Equals_1.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LSTCD89B895\_31?cs=.|vb=.|cpp=::|nu=.|fs=.");Equals(Object)](https://docs.microsoft.com/dotnet/api/system.object.equals#system-object-equals(system-object)).) |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_ModelFont_GetHashCode.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LSTCD89B895\_32?cs=.|vb=.|cpp=::|nu=.|fs=.");GetHashCodeAddLanguageSpecificTextSet("LSTCD89B895\_33?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-object-gethashcode).) |
| Public methodStatic member | [IsFamilyNameInstalled](M_Grasshopper_Rhinoceros_ModelFont_IsFamilyNameInstalled.htm) |  |
| Public method | [Read](M_Grasshopper_Rhinoceros_ModelFont_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_34?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_35?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCD89B895\_36?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disappears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_37?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_38?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelFont_ToString.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_39?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_40?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCD89B895\_41?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTCD89B895\_42?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Write](M_Grasshopper_Rhinoceros_ModelFont_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCD89B895\_43?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCD89B895\_44?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCD89B895\_45?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTCD89B895\_46?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(Font to ModelFont)](M_Grasshopper_Rhinoceros_ModelFont_op_Implicit.htm) |  |
| Public operatorStatic member | [AddLanguageSpecificTextSet("LSTCD89B895\_47?cs=Implicit|vb=Widening|cpp=Implicit|nu=Implicit|fs=Implicit");(String to ModelFont)](M_Grasshopper_Rhinoceros_ModelFont_op_Implicit_1.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)