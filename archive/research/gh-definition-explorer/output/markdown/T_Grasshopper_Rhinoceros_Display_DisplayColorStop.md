# T_Grasshopper_Rhinoceros_Display_DisplayColorStop

﻿ DisplayColorStop Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Display](../html/N_Grasshopper_Rhinoceros_Display.htm "Grasshopper.Rhinoceros.Display")

[DisplayColorStop Class](../html/T_Grasshopper_Rhinoceros_Display_DisplayColorStop.htm "DisplayColorStop Class")

[DisplayColorStop Constructor](../html/Overload_Grasshopper_Rhinoceros_Display_DisplayColorStop__ctor.htm "DisplayColorStop Constructor ")

[DisplayColorStop Properties](../html/Properties_T_Grasshopper_Rhinoceros_Display_DisplayColorStop.htm "DisplayColorStop Properties")

[DisplayColorStop Methods](../html/Methods_T_Grasshopper_Rhinoceros_Display_DisplayColorStop.htm "DisplayColorStop Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| DisplayColorStop Class |

Represents a gradient colour stop. Wraps the functionality of the ColorStop type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTCF100C91\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTCF100C91\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LSTCF100C91\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");ColorStopAddLanguageSpecificTextSet("LSTCF100C91\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LSTCF100C91\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");DisplayColorStop

**Namespace:**
 [Grasshopper.Rhinoceros.Display](N_Grasshopper_Rhinoceros_Display.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class DisplayColorStop : GH_Goo<ColorStop>
```

```
Public NotInheritable Class DisplayColorStop
	Inherits GH_Goo(Of ColorStop)
```

AddLanguageTabSet("ID1EBCA");

The DisplayColorStop type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [DisplayColorStopAddLanguageSpecificTextSet("LSTCF100C91\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Display_DisplayColorStop__ctor.htm) | Blank constructor |
| Public method | [DisplayColorStop(ColorStop)](M_Grasshopper_Rhinoceros_Display_DisplayColorStop__ctor_2.htm) | Initializes a new instance of the DisplayColorStop class |
| Public method | [DisplayColorStop(DisplayColorStop)](M_Grasshopper_Rhinoceros_Display_DisplayColorStop__ctor_1.htm) | Initializes a new instance of the DisplayColorStop class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_Display_DisplayColorStop_IsValid.htm) | Gets the validity of this instance. (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCF100C91\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Rhinoceros_Display_DisplayColorStop_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCF100C91\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Rhinoceros_Display_DisplayColorStop_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCF100C91\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Rhinoceros_Display_DisplayColorStop_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCF100C91\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm) | Gets or sets the internal data. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_18?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_19?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Rhinoceros_Display_DisplayColorStop_CastFrom.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_20?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_21?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCF100C91\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTCF100C91\_23?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTCF100C91\_24?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTCF100C91\_25?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_26?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_27?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTCF100C91\_28?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTCF100C91\_29?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTCF100C91\_30?cpp=%");)](M_Grasshopper_Rhinoceros_Display_DisplayColorStop_CastTo__1.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_31?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_32?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCF100C91\_33?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LSTCF100C91\_34?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTCF100C91\_35?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTCF100C91\_36?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).) |
| Public method | [Duplicate](M_Grasshopper_Rhinoceros_Display_DisplayColorStop_Duplicate.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_37?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_38?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCF100C91\_39?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LSTCF100C91\_40?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).) |
| Public method | [DuplicateColorStop](M_Grasshopper_Rhinoceros_Display_DisplayColorStop_DuplicateColorStop.htm) |  |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm) | Create a new proxy for this instance. Return Null if this class does not support proxies. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_41?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_42?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [Read](M_Grasshopper_Rhinoceros_Display_DisplayColorStop_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_43?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_44?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCF100C91\_45?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disappears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_46?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_47?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_Display_DisplayColorStop_ToString.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_48?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_49?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCF100C91\_50?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTCF100C91\_51?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Write](M_Grasshopper_Rhinoceros_Display_DisplayColorStop_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTCF100C91\_52?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTCF100C91\_53?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTCF100C91\_54?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Display Namespace](N_Grasshopper_Rhinoceros_Display.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)