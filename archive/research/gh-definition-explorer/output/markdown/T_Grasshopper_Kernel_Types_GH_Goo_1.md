# T_Grasshopper_Kernel_Types_GH_Goo_1

﻿ GH\_Goo(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Goo(T) Class](../html/T_Grasshopper_Kernel_Types_GH_Goo_1.htm "GH_Goo(T) Class")

[GH\_Goo(T) Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Goo_1__ctor.htm "GH_Goo(T) Constructor ")

[GH\_Goo(T) Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Goo_1.htm "GH_Goo(T) Properties")

[GH\_Goo(T) Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Goo_1.htm "GH_Goo(T) Methods")

[GH\_Goo(T) Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Goo_1.htm "GH_Goo(T) Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GooAddLanguageSpecificTextSet("LST1D21365A\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST1D21365A\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

Base class for IGH\_Goo implementation. Takes care of some default behaviour.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST1D21365A\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GooAddLanguageSpecificTextSet("LST1D21365A\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1D21365A\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");  
    [More...](#fullInheritance)

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_Goo<T> : IGH_Goo
```

```
Public MustInherit Class GH_Goo(Of T)
	Implements IGH_Goo
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T

The GH\_GooAddLanguageSpecificTextSet("LST1D21365A\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1D21365A\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_GooAddLanguageSpecificTextSet("LST1D21365A\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1D21365A\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST1D21365A\_10?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1__ctor.htm) | Blank constructor, m\_value will be set to default (null for reference types, zeroes for value types) |
| Protected method | [GH\_GooAddLanguageSpecificTextSet("LST1D21365A\_11?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1D21365A\_12?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(T)](M_Grasshopper_Kernel_Types_GH_Goo_1__ctor_2.htm) | Data constructor, m\_value will be set to internal\_data. |
| Protected method | [GH\_GooAddLanguageSpecificTextSet("LST1D21365A\_13?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1D21365A\_14?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(GH\_GooAddLanguageSpecificTextSet("LST1D21365A\_15?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST1D21365A\_16?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_Types_GH_Goo_1__ctor_1.htm) | Copy constructor, copies the data from another GH\_Goo(Of T) instance. Reference types will not be duplicated. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm) | Gets a value indicating whether or not the current value is valid. |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm) | Gets a description of the type of the implementation. |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm) | Gets the name of the type of the implementation. |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm) | Gets or sets the internal data. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm) | Attempt a cast from generic data. |
| Public method | [CastToAddLanguageSpecificTextSet("LST1D21365A\_17?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST1D21365A\_18?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm) | Make a complete duplicate of this instance. No shallow copies. |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm) | Create a new proxy for this instance. Return Null if this class does not support proxies. |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm) | Default behaviour is to return True. |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disappears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm) | Creates a string description of the current instance value. (Overrides [ObjectAddLanguageSpecificTextSet("LST1D21365A\_19?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST1D21365A\_20?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm) | Default behaviour is to return True. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Remarks

Feel free to implement IGH\_Goo directly though.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST1D21365A\_21?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GooAddLanguageSpecificTextSet("LST1D21365A\_23?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1D21365A\_24?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_25?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Boolean](T_Grasshopper_Kernel_Types_GH_Boolean.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_26?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Colour](T_Grasshopper_Kernel_Types_GH_Colour.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_27?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ComplexNumber](T_Grasshopper_Kernel_Types_GH_ComplexNumber.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_28?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Culture](T_Grasshopper_Kernel_Types_GH_Culture.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_29?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGooAddLanguageSpecificTextSet("LST1D21365A\_30?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1D21365A\_31?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_32?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Guid](T_Grasshopper_Kernel_Types_GH_Guid.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_33?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Integer](T_Grasshopper_Kernel_Types_GH_Integer.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_34?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Interval](T_Grasshopper_Kernel_Types_GH_Interval.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_35?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Interval2D](T_Grasshopper_Kernel_Types_GH_Interval2D.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_36?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Material](T_Grasshopper_Kernel_Types_GH_Material.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_37?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Matrix](T_Grasshopper_Kernel_Types_GH_Matrix.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_38?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MeshFace](T_Grasshopper_Kernel_Types_GH_MeshFace.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_39?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MeshingParameters](T_Grasshopper_Kernel_Types_GH_MeshingParameters.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_40?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Number](T_Grasshopper_Kernel_Types_GH_Number.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_41?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ObjectWrapper](T_Grasshopper_Kernel_Types_GH_ObjectWrapper.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_42?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_String](T_Grasshopper_Kernel_Types_GH_String.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_43?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_StructurePath](T_Grasshopper_Kernel_Types_GH_StructurePath.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_44?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Time](T_Grasshopper_Kernel_Types_GH_Time.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_45?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Transform](T_Grasshopper_Kernel_Types_GH_Transform.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1D21365A\_46?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Vector](T_Grasshopper_Kernel_Types_GH_Vector.htm)  
    [Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LST1D21365A\_47?cs=.|vb=.|cpp=::|nu=.|fs=.");DisplayColorGradient](T_Grasshopper_Rhinoceros_Display_DisplayColorGradient.htm)  
    [Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LST1D21365A\_48?cs=.|vb=.|cpp=::|nu=.|fs=.");DisplayColorStop](T_Grasshopper_Rhinoceros_Display_DisplayColorStop.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LST1D21365A\_49?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelFont](T_Grasshopper_Rhinoceros_ModelFont.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)