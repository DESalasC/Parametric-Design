# T_Grasshopper_Kernel_Types_GH_PointCloud

﻿ GH\_PointCloud Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_PointCloud Class](../html/T_Grasshopper_Kernel_Types_GH_PointCloud.htm "GH_PointCloud Class")

[GH\_PointCloud Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_PointCloud__ctor.htm "GH_PointCloud Constructor ")

[GH\_PointCloud Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_PointCloud.htm "GH_PointCloud Properties")

[GH\_PointCloud Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_PointCloud.htm "GH_PointCloud Methods")

[GH\_PointCloud Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_PointCloud.htm "GH_PointCloud Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PointCloud Class |

Represents a point cloud.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST2EAB9A6D\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST2EAB9A6D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST2EAB9A6D\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");PointCloudAddLanguageSpecificTextSet("LST2EAB9A6D\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST2EAB9A6D\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)AddLanguageSpecificTextSet("LST2EAB9A6D\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");PointCloudAddLanguageSpecificTextSet("LST2EAB9A6D\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
      Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST2EAB9A6D\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PointCloud

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_PointCloud : GH_GeometricGoo<PointCloud>, 
	IGH_BakeAwareData, IGH_PreviewData
```

```
Public Class GH_PointCloud
	Inherits GH_GeometricGoo(Of PointCloud)
	Implements IGH_BakeAwareData, IGH_PreviewData
```

AddLanguageTabSet("ID1EBCA");

The GH\_PointCloud type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_PointCloudAddLanguageSpecificTextSet("LST2EAB9A6D\_8?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_PointCloud__ctor.htm) | Default constructor, creates an invalid curve. |
| Public method | [GH\_PointCloud(GH\_PointCloud)](M_Grasshopper_Kernel_Types_GH_PointCloud__ctor_1.htm) | Create a duplicate of another GH\_PointCloud. This constructor also copies reference data. |
| Public method | [GH\_PointCloud(Guid)](M_Grasshopper_Kernel_Types_GH_PointCloud__ctor_3.htm) | Create a new referenced curve that references a Rhino curve object with the specified ID. |
| Public method | [GH\_PointCloud(PointCloud)](M_Grasshopper_Kernel_Types_GH_PointCloud__ctor_2.htm) | Create a duplicate of an existing point-cloud. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundingbox](P_Grasshopper_Kernel_Types_GH_PointCloud_Boundingbox.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");Boundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Boundingbox.htm).) |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_PointCloud_ClippingBox.htm) |  |
| Public property | [IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_PointCloud_IsGeometryLoaded.htm) | Gets the load state of this curve object. The curve is considered to be loaded when the local OnCurve instance is not null. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsGeometryLoaded.htm).) |
| Public property | [IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm) | Gets a value indicating whether or not this geometry is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_PointCloud_IsValid.htm) | Gets the validity of this curve. If the curve is referenced but cannot be loaded, the curve is not valid. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_17?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_18?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_19?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_PointCloud_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2EAB9A6D\_20?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_21?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [ReferenceID](P_Grasshopper_Kernel_Types_GH_PointCloud_ReferenceID.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_23?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_24?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_25?cs=.|vb=.|cpp=::|nu=.|fs=.");ReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_PointCloud_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2EAB9A6D\_26?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_27?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_28?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_PointCloud_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2EAB9A6D\_29?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_30?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_31?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_PointCloud_Value.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_32?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_33?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_34?cs=.|vb=.|cpp=::|nu=.|fs=.");Value](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Value.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry](M_Grasshopper_Kernel_Types_GH_PointCloud_BakeGeometry.htm) |  |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_PointCloud_CastFrom.htm) | Remote to Local caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_35?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_36?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_37?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST2EAB9A6D\_38?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST2EAB9A6D\_39?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST2EAB9A6D\_40?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm) | Attempt a cast to type T. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_41?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_42?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST2EAB9A6D\_43?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST2EAB9A6D\_44?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST2EAB9A6D\_45?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST2EAB9A6D\_46?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_47?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST2EAB9A6D\_48?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST2EAB9A6D\_49?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST2EAB9A6D\_50?cpp=%");)](M_Grasshopper_Kernel_Types_GH_PointCloud_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_51?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_52?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_53?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST2EAB9A6D\_54?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST2EAB9A6D\_55?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST2EAB9A6D\_56?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm).) |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_PointCloud_ClearCaches.htm) | Clears all volatile caches for this instance. The boundingbox is cleared, and if the curve is referenced, the local instance of the curve is erased. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_57?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_58?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_59?cs=.|vb=.|cpp=::|nu=.|fs=.");ClearCachesAddLanguageSpecificTextSet("LST2EAB9A6D\_60?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ClearCaches.htm).) |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_PointCloud_DrawViewportMeshes.htm) |  |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_PointCloud_DrawViewportWires.htm) |  |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_PointCloud_Duplicate.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_61?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_62?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_63?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LST2EAB9A6D\_64?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Duplicate.htm).) |
| Public method | [DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_PointCloud_DuplicateGeometry.htm) | Create a duplicate of this curve. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_65?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_66?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_67?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateGeometryAddLanguageSpecificTextSet("LST2EAB9A6D\_68?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_DuplicateGeometry.htm).) |
| Public method | [DuplicatePointCloud](M_Grasshopper_Kernel_Types_GH_PointCloud_DuplicatePointCloud.htm) | Create a duplicate of this curve. |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_PointCloud_EmitProxy.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_69?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_70?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_71?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LST2EAB9A6D\_72?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_EmitProxy.htm).) |
| Public method | [GetBoundingBox](M_Grasshopper_Kernel_Types_GH_PointCloud_GetBoundingBox.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_73?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_74?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_75?cs=.|vb=.|cpp=::|nu=.|fs=.");GetBoundingBox(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_GetBoundingBox.htm).) |
| Public method | [LoadGeometryAddLanguageSpecificTextSet("LST2EAB9A6D\_76?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_PointCloud_LoadGeometry.htm) | If the geometry is referenced and not yet loaded, attempts to load the geometry. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_77?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_78?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_79?cs=.|vb=.|cpp=::|nu=.|fs=.");LoadGeometryAddLanguageSpecificTextSet("LST2EAB9A6D\_80?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm).) |
| Public method | [LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_PointCloud_LoadGeometry_1.htm) | If the curve is referenced and not yet loaded, attempts to load the curve. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_81?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_82?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_83?cs=.|vb=.|cpp=::|nu=.|fs=.");LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1.htm).) |
| Public method | [Morph](M_Grasshopper_Kernel_Types_GH_PointCloud_Morph.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_84?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_85?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_86?cs=.|vb=.|cpp=::|nu=.|fs=.");Morph(SpaceMorph)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Morph.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_PointCloud_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2EAB9A6D\_87?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_88?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_89?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_PointCloud_ScriptVariable.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2EAB9A6D\_90?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_91?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_92?cs=.|vb=.|cpp=::|nu=.|fs=.");ScriptVariableAddLanguageSpecificTextSet("LST2EAB9A6D\_93?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_PointCloud_ToString.htm) | Format the curve using default grasshopper formatting logic. (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2EAB9A6D\_94?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_95?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_96?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST2EAB9A6D\_97?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Transform](M_Grasshopper_Kernel_Types_GH_PointCloud_Transform.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST2EAB9A6D\_98?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_99?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_100?cs=.|vb=.|cpp=::|nu=.|fs=.");Transform(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_PointCloud_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LST2EAB9A6D\_101?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_102?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST2EAB9A6D\_103?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST2EAB9A6D\_104?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST2EAB9A6D\_105?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)