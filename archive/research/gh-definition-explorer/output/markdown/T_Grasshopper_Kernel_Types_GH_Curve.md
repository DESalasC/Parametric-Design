# T_Grasshopper_Kernel_Types_GH_Curve

﻿ GH\_Curve Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Curve Class](../html/T_Grasshopper_Kernel_Types_GH_Curve.htm "GH_Curve Class")

[GH\_Curve Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Curve__ctor.htm "GH_Curve Constructor ")

[GH\_Curve Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Curve.htm "GH_Curve Properties")

[GH\_Curve Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Curve.htm "GH_Curve Methods")

[GH\_Curve Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Curve.htm "GH_Curve Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Curve Class |

Represents a 3D spline curve.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST795CC5ED\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST795CC5ED\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST795CC5ED\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");CurveAddLanguageSpecificTextSet("LST795CC5ED\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST795CC5ED\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)AddLanguageSpecificTextSet("LST795CC5ED\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");CurveAddLanguageSpecificTextSet("LST795CC5ED\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
      Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST795CC5ED\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Curve

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Curve : GH_GeometricGoo<Curve>, 
	IGH_BakeAwareData, IGH_PreviewData
```

```
Public Class GH_Curve
	Inherits GH_GeometricGoo(Of Curve)
	Implements IGH_BakeAwareData, IGH_PreviewData
```

AddLanguageTabSet("ID1EBCA");

The GH\_Curve type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_CurveAddLanguageSpecificTextSet("LST795CC5ED\_8?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Curve__ctor.htm) | Default constructor, creates an invalid curve. |
| Public method | [GH\_Curve(Curve)](M_Grasshopper_Kernel_Types_GH_Curve__ctor_2.htm) | Create a duplicate of an existing curve. |
| Public method | [GH\_Curve(GH\_Curve)](M_Grasshopper_Kernel_Types_GH_Curve__ctor_1.htm) | Create a duplicate of another GH\_Curve. This constructor also copies reference data. |
| Public method | [GH\_Curve(Guid)](M_Grasshopper_Kernel_Types_GH_Curve__ctor_3.htm) | Create a new referenced curve that references a Rhino curve object with the specified ID. |
| Public method | [GH\_Curve(Guid, Int32)](M_Grasshopper_Kernel_Types_GH_Curve__ctor_4.htm) | Create a new references edge curve that references an edge index in a Rhino Brep object. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundingbox](P_Grasshopper_Kernel_Types_GH_Curve_Boundingbox.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");Boundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Boundingbox.htm).) |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_Curve_ClippingBox.htm) |  |
| Public property | [IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_Curve_IsGeometryLoaded.htm) | Gets the load state of this curve object. The curve is considered to be loaded when the local OnCurve instance is not null. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsGeometryLoaded.htm).) |
| Public property | [IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm) | Gets a value indicating whether or not this geometry is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Curve_IsValid.htm) | Gets the validity of this curve. If the curve is referenced but cannot be loaded, the curve is not valid. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_17?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_18?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_19?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Curve_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST795CC5ED\_20?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_21?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [ReferenceEdge](P_Grasshopper_Kernel_Types_GH_Curve_ReferenceEdge.htm) | Gets or sets the edge index for a referenced curve. If the index >= 0 then an edge reference is implied. |
| Public property | [ReferenceID](P_Grasshopper_Kernel_Types_GH_Curve_ReferenceID.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_23?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_24?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_25?cs=.|vb=.|cpp=::|nu=.|fs=.");ReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Curve_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST795CC5ED\_26?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_27?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_28?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Curve_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST795CC5ED\_29?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_30?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_31?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Curve_Value.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_32?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_33?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_34?cs=.|vb=.|cpp=::|nu=.|fs=.");Value](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Value.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry](M_Grasshopper_Kernel_Types_GH_Curve_BakeGeometry.htm) |  |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Curve_CastFrom.htm) | Remote to Local caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_35?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_36?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_37?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST795CC5ED\_38?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST795CC5ED\_39?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST795CC5ED\_40?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Curve_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_41?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_42?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_43?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST795CC5ED\_44?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST795CC5ED\_45?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST795CC5ED\_46?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST795CC5ED\_47?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST795CC5ED\_48?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST795CC5ED\_49?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm) | Attempt a cast to type T. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_50?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_51?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST795CC5ED\_52?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST795CC5ED\_53?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST795CC5ED\_54?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST795CC5ED\_55?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_56?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_Curve_ClearCaches.htm) | Clears all volatile caches for this instance. The boundingbox is cleared, and if the curve is referenced, the local instance of the curve is erased. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_57?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_58?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_59?cs=.|vb=.|cpp=::|nu=.|fs=.");ClearCachesAddLanguageSpecificTextSet("LST795CC5ED\_60?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ClearCaches.htm).) |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_Curve_DrawViewportMeshes.htm) |  |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_Curve_DrawViewportWires.htm) |  |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_Curve_Duplicate.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_61?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_62?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_63?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST795CC5ED\_64?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Duplicate.htm).) |
| Public method | [DuplicateCurve](M_Grasshopper_Kernel_Types_GH_Curve_DuplicateCurve.htm) | Create a duplicate of this curve. |
| Public method | [DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_Curve_DuplicateGeometry.htm) | Create a duplicate of this curve. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_65?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_66?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_67?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateGeometryAddLanguageSpecificTextSet("LST795CC5ED\_68?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_DuplicateGeometry.htm).) |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Curve_EmitProxy.htm) | Returns a proxy that represents this curve. Do not call this function unless you're (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_69?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_70?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_71?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LST795CC5ED\_72?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_EmitProxy.htm).) |
| Public method | [GetBoundingBox](M_Grasshopper_Kernel_Types_GH_Curve_GetBoundingBox.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_73?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_74?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_75?cs=.|vb=.|cpp=::|nu=.|fs=.");GetBoundingBox(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_GetBoundingBox.htm).) |
| Public method | [LoadGeometryAddLanguageSpecificTextSet("LST795CC5ED\_76?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Curve_LoadGeometry.htm) | If the geometry is referenced and not yet loaded, attempts to load the geometry. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_77?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_78?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_79?cs=.|vb=.|cpp=::|nu=.|fs=.");LoadGeometryAddLanguageSpecificTextSet("LST795CC5ED\_80?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm).) |
| Public method | [LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_Curve_LoadGeometry_1.htm) | If the curve is referenced and not yet loaded, attempts to load the curve. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_81?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_82?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_83?cs=.|vb=.|cpp=::|nu=.|fs=.");LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1.htm).) |
| Public method | [MakeDeformable](M_Grasshopper_Kernel_Types_GH_Curve_MakeDeformable.htm) | Converts the local geometry into deformable nurbs curve geometry. This method will not destroy Reference data. |
| Public method | [Morph](M_Grasshopper_Kernel_Types_GH_Curve_Morph.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_84?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_85?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_86?cs=.|vb=.|cpp=::|nu=.|fs=.");Morph(SpaceMorph)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Morph.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Curve_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST795CC5ED\_87?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_88?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_89?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Curve_ScriptVariable.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST795CC5ED\_90?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_91?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_92?cs=.|vb=.|cpp=::|nu=.|fs=.");ScriptVariableAddLanguageSpecificTextSet("LST795CC5ED\_93?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Curve_ToString.htm) | Format the curve using default grasshopper formatting logic. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST795CC5ED\_94?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_95?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_96?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST795CC5ED\_97?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Transform](M_Grasshopper_Kernel_Types_GH_Curve_Transform.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST795CC5ED\_98?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_99?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_100?cs=.|vb=.|cpp=::|nu=.|fs=.");Transform(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Curve_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST795CC5ED\_101?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_102?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST795CC5ED\_103?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST795CC5ED\_104?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST795CC5ED\_105?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)