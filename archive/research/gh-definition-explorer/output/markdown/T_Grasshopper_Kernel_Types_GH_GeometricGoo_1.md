# T_Grasshopper_Kernel_Types_GH_GeometricGoo_1

﻿ GH\_GeometricGoo(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_GeometricGoo(T) Class](../html/T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm "GH_GeometricGoo(T) Class")

[GH\_GeometricGoo(T) Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_GeometricGoo_1__ctor.htm "GH_GeometricGoo(T) Constructor ")

[GH\_GeometricGoo(T) Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm "GH_GeometricGoo(T) Properties")

[GH\_GeometricGoo(T) Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm "GH_GeometricGoo(T) Methods")

[GH\_GeometricGoo(T) Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm "GH_GeometricGoo(T) Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GeometricGooAddLanguageSpecificTextSet("LST74B7094F\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST74B7094F\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

Abstract base implementation of IGH\_GeometricGoo. If you implement IGH\_GeometricGoo, use this for a booster.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST74B7094F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST74B7094F\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST74B7094F\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGooAddLanguageSpecificTextSet("LST74B7094F\_7?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_8?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");  
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
public abstract class GH_GeometricGoo<T> : GH_Goo<T>, 
	IGH_GeometricGoo
```

```
Public MustInherit Class GH_GeometricGoo(Of T)
	Inherits GH_Goo(Of T)
	Implements IGH_GeometricGoo
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T

The GH\_GeometricGooAddLanguageSpecificTextSet("LST74B7094F\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_GeometricGooAddLanguageSpecificTextSet("LST74B7094F\_11?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_12?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST74B7094F\_13?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1__ctor.htm) | Blank constructor, m\_value will be set to default (null for reference types, zeroes for value types) |
| Protected method | [GH\_GeometricGooAddLanguageSpecificTextSet("LST74B7094F\_14?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_15?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(T)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1__ctor_1.htm) | Data constructor, m\_value will be set to internal\_data. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Boundingbox.htm) | Gets the boundingbox for this geometry. |
| Public property | [IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsGeometryLoaded.htm) | Gets a value indicating whether or not this geometry is currently loaded (assuming it is referenced). Not all IGH\_GeometricGoo implementations support referenced geometry. The default is to always return True. |
| Public property | [IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm) | Gets a value indicating whether or not this geometry is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsValid.htm) | Gets a value indicating whether or not the current value is valid. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_16?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_17?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST74B7094F\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public property | [ReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID.htm) | Gets or sets the Guid of the object that is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. The default implementation is to always return Guid.Empty. |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm) | Gets a description of the type of the implementation. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_21?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_22?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm) | Gets the name of the type of the implementation. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_23?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_24?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Value.htm) | Gets or sets the value of this type. Note that if the type has a ReferenceID this value might get destroyed in the future. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_25?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_26?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST74B7094F\_27?cs=.|vb=.|cpp=::|nu=.|fs=.");Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm) | Attempt a cast from generic object. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_28?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_29?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST74B7094F\_30?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST74B7094F\_31?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST74B7094F\_32?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST74B7094F\_33?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm) | Attempt a cast to type T. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_34?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_35?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST74B7094F\_36?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST74B7094F\_37?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST74B7094F\_38?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST74B7094F\_39?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST74B7094F\_40?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST74B7094F\_41?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST74B7094F\_42?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_43?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_44?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ClearCaches.htm) | Clears all caches. Typically if the geometry is referenced, this will erase the local copy. If your T is a value-type, you must override this function and specifically unset the local value. |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Duplicate.htm) | Make a complete duplicate of this instance. No shallow copies. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_45?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_46?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST74B7094F\_47?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST74B7094F\_48?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).) |
| Public method | [DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_DuplicateGeometry.htm) | Make a complete duplicate of this geometry. No shallow copies. |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_EmitProxy.htm) | Create a new proxy for this instance. Return Null if this class does not support proxies. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_49?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_50?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST74B7094F\_51?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LST74B7094F\_52?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).) |
| Public method | [GetBoundingBox](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_GetBoundingBox.htm) | Compute an aligned boundingbox. |
| Public method | [LoadGeometryAddLanguageSpecificTextSet("LST74B7094F\_53?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm) | If the geometry is referenced and currently unloaded, forces loading of the geometry. Not all IGH\_GeometricGoo implementations support referenced geometry. |
| Public method | [LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1.htm) | If the geometry is referenced and currently unloaded, forces loading of the geometry. Not all IGH\_GeometricGoo implementations support referenced geometry. The default is to always return True. |
| Public method | [Morph](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Morph.htm) | Morph the object or a deformable representation of the object. |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm) | Default behaviour is to return True. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_54?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_55?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disappears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_56?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_57?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm) | Creates a string description of the current instance value. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_58?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_59?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [Transform](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform.htm) | Transforms the object or a deformable representation of the object. |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm) | Default behaviour is to return True. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_60?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_61?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST74B7094F\_62?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_63?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST74B7094F\_64?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_65?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST74B7094F\_66?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST74B7094F\_67?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_68?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGooAddLanguageSpecificTextSet("LST74B7094F\_69?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST74B7094F\_70?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_71?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_72?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Arc](T_Grasshopper_Kernel_Types_GH_Arc.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_73?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Box](T_Grasshopper_Kernel_Types_GH_Box.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_74?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Brep](T_Grasshopper_Kernel_Types_GH_Brep.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_75?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Circle](T_Grasshopper_Kernel_Types_GH_Circle.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_76?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Curve](T_Grasshopper_Kernel_Types_GH_Curve.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_77?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DetailView](T_Grasshopper_Kernel_Types_GH_DetailView.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_78?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Extrusion](T_Grasshopper_Kernel_Types_GH_Extrusion.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_79?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Hatch](T_Grasshopper_Kernel_Types_GH_Hatch.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_80?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InstanceReference](T_Grasshopper_Kernel_Types_GH_InstanceReference.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_81?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Light](T_Grasshopper_Kernel_Types_GH_Light.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_82?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Line](T_Grasshopper_Kernel_Types_GH_Line.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_83?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Mesh](T_Grasshopper_Kernel_Types_GH_Mesh.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_84?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Plane](T_Grasshopper_Kernel_Types_GH_Plane.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_85?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PointCloud](T_Grasshopper_Kernel_Types_GH_PointCloud.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_86?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Rectangle](T_Grasshopper_Kernel_Types_GH_Rectangle.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_87?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SubD](T_Grasshopper_Kernel_Types_GH_SubD.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_88?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Surface](T_Grasshopper_Kernel_Types_GH_Surface.htm)  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST74B7094F\_89?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_TextDot](T_Grasshopper_Kernel_Types_GH_TextDot.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)