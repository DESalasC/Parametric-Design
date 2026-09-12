# T_Grasshopper_Kernel_Types_GH_Circle

﻿ GH\_Circle Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Circle Class](../html/T_Grasshopper_Kernel_Types_GH_Circle.htm "GH_Circle Class")

[GH\_Circle Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Circle__ctor.htm "GH_Circle Constructor ")

[GH\_Circle Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Circle.htm "GH_Circle Properties")

[GH\_Circle Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Circle.htm "GH_Circle Methods")

[GH\_Circle Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Circle.htm "GH_Circle Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Circle Class |

Represents a 3D circle. GH\_Circle re-implements the OpenNURBS OnCircle class.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTC201DF60\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTC201DF60\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LSTC201DF60\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");CircleAddLanguageSpecificTextSet("LSTC201DF60\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTC201DF60\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)AddLanguageSpecificTextSet("LSTC201DF60\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");CircleAddLanguageSpecificTextSet("LSTC201DF60\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
      Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTC201DF60\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Circle

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Circle : GH_GeometricGoo<Circle>, 
	IGH_BakeAwareData, IGH_PreviewData
```

```
Public Class GH_Circle
	Inherits GH_GeometricGoo(Of Circle)
	Implements IGH_BakeAwareData, IGH_PreviewData
```

AddLanguageTabSet("ID1EBCA");

The GH\_Circle type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_CircleAddLanguageSpecificTextSet("LSTC201DF60\_8?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Circle__ctor.htm) | Default constructor |
| Public method | [GH\_Circle(Circle)](M_Grasshopper_Kernel_Types_GH_Circle__ctor_2.htm) | Create a duplicate of another circle |
| Public method | [GH\_Circle(GH\_Circle)](M_Grasshopper_Kernel_Types_GH_Circle__ctor_1.htm) | Create a duplicate of another circle. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundingbox](P_Grasshopper_Kernel_Types_GH_Circle_Boundingbox.htm) | Gets the boundingbox for this geometry. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");Boundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Boundingbox.htm).) |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_Circle_ClippingBox.htm) |  |
| Public property | [IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsGeometryLoaded.htm) | Gets a value indicating whether or not this geometry is currently loaded (assuming it is referenced). Not all IGH\_GeometricGoo implementations support referenced geometry. The default is to always return True. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm) | Gets a value indicating whether or not this geometry is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_14?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_15?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Circle_IsValid.htm) | Gets the validity of this instance. Circles are valid when their base planes are valid and when the radius is larger than zero. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_16?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_17?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Circle_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC201DF60\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_21?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [ReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID.htm) | Gets or sets the Guid of the object that is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. The default implementation is to always return Guid.Empty. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_22?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_23?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Circle_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC201DF60\_24?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_25?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_26?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Circle_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC201DF60\_27?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_28?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_29?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Value.htm) | Gets or sets the value of this type. Note that if the type has a ReferenceID this value might get destroyed in the future. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_30?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_31?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry](M_Grasshopper_Kernel_Types_GH_Circle_BakeGeometry.htm) |  |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Circle_CastFrom.htm) | Remote to Local caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_32?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_33?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_34?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTC201DF60\_35?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTC201DF60\_36?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTC201DF60\_37?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Circle_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_38?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_39?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_40?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LSTC201DF60\_41?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTC201DF60\_42?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTC201DF60\_43?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTC201DF60\_44?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTC201DF60\_45?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTC201DF60\_46?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm) | Attempt a cast to type T. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_47?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_48?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTC201DF60\_49?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTC201DF60\_50?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTC201DF60\_51?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTC201DF60\_52?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_53?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ClearCaches.htm) | Clears all caches. Typically if the geometry is referenced, this will erase the local copy. If your T is a value-type, you must override this function and specifically unset the local value. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_54?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_55?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_Circle_DrawViewportMeshes.htm) |  |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_Circle_DrawViewportWires.htm) |  |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_Circle_Duplicate.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_56?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_57?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_58?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LSTC201DF60\_59?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Duplicate.htm).) |
| Public method | [DuplicateCircle](M_Grasshopper_Kernel_Types_GH_Circle_DuplicateCircle.htm) | Create a duplicate of this circle. |
| Public method | [DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_Circle_DuplicateGeometry.htm) | Create a duplicate of this circle. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_60?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_61?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_62?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateGeometryAddLanguageSpecificTextSet("LSTC201DF60\_63?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_DuplicateGeometry.htm).) |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Circle_EmitProxy.htm) | Returns a proxy that represents this circle. Do not call this function unless you're (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_64?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_65?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_66?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LSTC201DF60\_67?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_EmitProxy.htm).) |
| Public method | [GetBoundingBox](M_Grasshopper_Kernel_Types_GH_Circle_GetBoundingBox.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_68?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_69?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_70?cs=.|vb=.|cpp=::|nu=.|fs=.");GetBoundingBox(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_GetBoundingBox.htm).) |
| Public method | [LoadGeometryAddLanguageSpecificTextSet("LSTC201DF60\_71?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm) | If the geometry is referenced and currently unloaded, forces loading of the geometry. Not all IGH\_GeometricGoo implementations support referenced geometry. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_72?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_73?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1.htm) | If the geometry is referenced and currently unloaded, forces loading of the geometry. Not all IGH\_GeometricGoo implementations support referenced geometry. The default is to always return True. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_74?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_75?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [Morph](M_Grasshopper_Kernel_Types_GH_Circle_Morph.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_76?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_77?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_78?cs=.|vb=.|cpp=::|nu=.|fs=.");Morph(SpaceMorph)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Morph.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Circle_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC201DF60\_79?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_80?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_81?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disappears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTC201DF60\_82?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_83?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Circle_ToString.htm) | Format the circle using default grasshopper formatting logic. (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC201DF60\_84?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_85?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_86?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTC201DF60\_87?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Transform](M_Grasshopper_Kernel_Types_GH_Circle_Transform.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC201DF60\_88?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_89?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_90?cs=.|vb=.|cpp=::|nu=.|fs=.");Transform(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Circle_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC201DF60\_91?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_92?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC201DF60\_93?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTC201DF60\_94?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC201DF60\_95?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)