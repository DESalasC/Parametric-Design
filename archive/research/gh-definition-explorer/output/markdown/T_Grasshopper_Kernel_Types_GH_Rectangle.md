# T_Grasshopper_Kernel_Types_GH_Rectangle

﻿ GH\_Rectangle Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Rectangle Class](../html/T_Grasshopper_Kernel_Types_GH_Rectangle.htm "GH_Rectangle Class")

[GH\_Rectangle Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Rectangle__ctor.htm "GH_Rectangle Constructor ")

[GH\_Rectangle Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Rectangle.htm "GH_Rectangle Properties")

[GH\_Rectangle Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Rectangle.htm "GH_Rectangle Methods")

[GH\_Rectangle Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Rectangle.htm "GH_Rectangle Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Rectangle Class |

Represents a 3D rectangle. GH\_Rectangle re-implements the RhinoCommon Rectangle3d.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST165752FF\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST165752FF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST165752FF\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");Rectangle3dAddLanguageSpecificTextSet("LST165752FF\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST165752FF\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)AddLanguageSpecificTextSet("LST165752FF\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");Rectangle3dAddLanguageSpecificTextSet("LST165752FF\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
      Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST165752FF\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Rectangle

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Rectangle : GH_GeometricGoo<Rectangle3d>, 
	IGH_BakeAwareData, IGH_PreviewData
```

```
Public Class GH_Rectangle
	Inherits GH_GeometricGoo(Of Rectangle3d)
	Implements IGH_BakeAwareData, IGH_PreviewData
```

AddLanguageTabSet("ID1EBCA");

The GH\_Rectangle type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_RectangleAddLanguageSpecificTextSet("LST165752FF\_8?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Rectangle__ctor.htm) | Default constructor |
| Public method | [GH\_Rectangle(GH\_Rectangle)](M_Grasshopper_Kernel_Types_GH_Rectangle__ctor_1.htm) | Create a duplicate of another circle. |
| Public method | [GH\_Rectangle(Rectangle3d)](M_Grasshopper_Kernel_Types_GH_Rectangle__ctor_2.htm) | Create a duplicate of another rectangle. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundingbox](P_Grasshopper_Kernel_Types_GH_Rectangle_Boundingbox.htm) | Gets the boundingbox for this geometry. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");Boundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Boundingbox.htm).) |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_Rectangle_ClippingBox.htm) |  |
| Public property | [IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsGeometryLoaded.htm) | Gets a value indicating whether or not this geometry is currently loaded (assuming it is referenced). Not all IGH\_GeometricGoo implementations support referenced geometry. The default is to always return True. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm) | Gets a value indicating whether or not this geometry is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_14?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_15?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Rectangle_IsValid.htm) | Gets the validity of this instance. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_16?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_17?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Rectangle_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST165752FF\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_21?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [ReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID.htm) | Gets or sets the Guid of the object that is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. The default implementation is to always return Guid.Empty. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_22?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_23?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Rectangle_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST165752FF\_24?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_25?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_26?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Rectangle_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST165752FF\_27?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_28?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_29?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Value.htm) | Gets or sets the value of this type. Note that if the type has a ReferenceID this value might get destroyed in the future. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_30?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_31?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry](M_Grasshopper_Kernel_Types_GH_Rectangle_BakeGeometry.htm) |  |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Rectangle_CastFrom.htm) | Remote to Local caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_32?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_33?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_34?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST165752FF\_35?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST165752FF\_36?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST165752FF\_37?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm) | Attempt a cast to type T. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_38?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_39?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST165752FF\_40?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST165752FF\_41?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST165752FF\_42?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST165752FF\_43?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_44?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST165752FF\_45?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST165752FF\_46?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST165752FF\_47?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Rectangle_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_48?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_49?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_50?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST165752FF\_51?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST165752FF\_52?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST165752FF\_53?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm).) |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ClearCaches.htm) | Clears all caches. Typically if the geometry is referenced, this will erase the local copy. If your T is a value-type, you must override this function and specifically unset the local value. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_54?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_55?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_Rectangle_DrawViewportMeshes.htm) |  |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_Rectangle_DrawViewportWires.htm) |  |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_Rectangle_Duplicate.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_56?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_57?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_58?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST165752FF\_59?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Duplicate.htm).) |
| Public method | [DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_Rectangle_DuplicateGeometry.htm) | Create a duplicate of this rectangle. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_60?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_61?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_62?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateGeometryAddLanguageSpecificTextSet("LST165752FF\_63?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_DuplicateGeometry.htm).) |
| Public method | [DuplicateRectangle](M_Grasshopper_Kernel_Types_GH_Rectangle_DuplicateRectangle.htm) | Create a duplicate of this rectangle. |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Rectangle_EmitProxy.htm) | Returns a proxy that represents this rectangle. Do not call this function unless you're (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_64?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_65?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_66?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LST165752FF\_67?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_EmitProxy.htm).) |
| Public method | [GetBoundingBox](M_Grasshopper_Kernel_Types_GH_Rectangle_GetBoundingBox.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_68?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_69?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_70?cs=.|vb=.|cpp=::|nu=.|fs=.");GetBoundingBox(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_GetBoundingBox.htm).) |
| Public method | [LoadGeometryAddLanguageSpecificTextSet("LST165752FF\_71?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm) | If the geometry is referenced and currently unloaded, forces loading of the geometry. Not all IGH\_GeometricGoo implementations support referenced geometry. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_72?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_73?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1.htm) | If the geometry is referenced and currently unloaded, forces loading of the geometry. Not all IGH\_GeometricGoo implementations support referenced geometry. The default is to always return True. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_74?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_75?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [Morph](M_Grasshopper_Kernel_Types_GH_Rectangle_Morph.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_76?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_77?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_78?cs=.|vb=.|cpp=::|nu=.|fs=.");Morph(SpaceMorph)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Morph.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Rectangle_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST165752FF\_79?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_80?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_81?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disappears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST165752FF\_82?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_83?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Rectangle_ToString.htm) | Format the circle using default grasshopper formatting logic. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST165752FF\_84?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_85?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_86?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST165752FF\_87?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Transform](M_Grasshopper_Kernel_Types_GH_Rectangle_Transform.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST165752FF\_88?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_89?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_90?cs=.|vb=.|cpp=::|nu=.|fs=.");Transform(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Rectangle_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST165752FF\_91?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_92?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST165752FF\_93?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST165752FF\_94?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST165752FF\_95?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)