# T_Grasshopper_Rhinoceros_Display_DisplayColorGradient

﻿ DisplayColorGradient Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Display](../html/N_Grasshopper_Rhinoceros_Display.htm "Grasshopper.Rhinoceros.Display")

[DisplayColorGradient Class](../html/T_Grasshopper_Rhinoceros_Display_DisplayColorGradient.htm "DisplayColorGradient Class")

[DisplayColorGradient Constructor](../html/Overload_Grasshopper_Rhinoceros_Display_DisplayColorGradient__ctor.htm "DisplayColorGradient Constructor ")

[DisplayColorGradient Properties](../html/Properties_T_Grasshopper_Rhinoceros_Display_DisplayColorGradient.htm "DisplayColorGradient Properties")

[DisplayColorGradient Methods](../html/Methods_T_Grasshopper_Rhinoceros_Display_DisplayColorGradient.htm "DisplayColorGradient Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| DisplayColorGradient Class |

Represents a gradient colour stop. Wraps the functionality of the ColorGradient type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST5FF18C41\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST5FF18C41\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST5FF18C41\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");ColorGradientAddLanguageSpecificTextSet("LST5FF18C41\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LST5FF18C41\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");DisplayColorGradient

**Namespace:**
 [Grasshopper.Rhinoceros.Display](N_Grasshopper_Rhinoceros_Display.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class DisplayColorGradient : GH_Goo<ColorGradient>, 
	IGH_PreviewData
```

```
Public NotInheritable Class DisplayColorGradient
	Inherits GH_Goo(Of ColorGradient)
	Implements IGH_PreviewData
```

AddLanguageTabSet("ID1EBCA");

The DisplayColorGradient type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [DisplayColorGradientAddLanguageSpecificTextSet("LST5FF18C41\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient__ctor.htm) | Blank constructor |
| Public method | [DisplayColorGradient(ColorGradient)](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient__ctor_2.htm) | Initializes a new instance of the DisplayColorGradient class |
| Public method | [DisplayColorGradient(DisplayColorGradient)](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient__ctor_1.htm) | Initializes a new instance of the DisplayColorGradient class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ClippingBox](P_Grasshopper_Rhinoceros_Display_DisplayColorGradient_ClippingBox.htm) |  |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_Display_DisplayColorGradient_IsValid.htm) | Gets the validity of this instance. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST5FF18C41\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Rhinoceros_Display_DisplayColorGradient_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST5FF18C41\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Rhinoceros_Display_DisplayColorGradient_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST5FF18C41\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Rhinoceros_Display_DisplayColorGradient_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST5FF18C41\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm) | Gets or sets the internal data. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_18?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_19?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_CastFrom.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_20?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_21?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST5FF18C41\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST5FF18C41\_23?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST5FF18C41\_24?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST5FF18C41\_25?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_26?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_27?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST5FF18C41\_28?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST5FF18C41\_29?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST5FF18C41\_30?cpp=%");)](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_CastTo__1.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_31?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_32?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST5FF18C41\_33?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST5FF18C41\_34?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST5FF18C41\_35?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST5FF18C41\_36?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).) |
| Public method | [DrawViewportMeshes](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_DrawViewportMeshes.htm) |  |
| Public method | [DrawViewportWires](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_DrawViewportWires.htm) |  |
| Public method | [Duplicate](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_Duplicate.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_37?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_38?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST5FF18C41\_39?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST5FF18C41\_40?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).) |
| Public method | [DuplicateColourGradient](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_DuplicateColourGradient.htm) |  |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm) | Create a new proxy for this instance. Return Null if this class does not support proxies. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_41?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_42?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [Read](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_43?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_44?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST5FF18C41\_45?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disappears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_46?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_47?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ToString](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_ToString.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_48?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_49?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST5FF18C41\_50?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST5FF18C41\_51?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Write](M_Grasshopper_Rhinoceros_Display_DisplayColorGradient_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST5FF18C41\_52?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5FF18C41\_53?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST5FF18C41\_54?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Display Namespace](N_Grasshopper_Rhinoceros_Display.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)