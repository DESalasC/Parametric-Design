# T_Grasshopper_Kernel_Types_GH_SubD

﻿ GH\_SubD Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_SubD Class](../html/T_Grasshopper_Kernel_Types_GH_SubD.htm "GH_SubD Class")

[GH\_SubD Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_SubD__ctor.htm "GH_SubD Constructor ")

[GH\_SubD Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_SubD.htm "GH_SubD Properties")

[GH\_SubD Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_SubD.htm "GH_SubD Methods")

[GH\_SubD Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_SubD.htm "GH_SubD Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SubD Class |

Represents a 3D subdivision surface.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTC0E6F7A4\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTC0E6F7A4\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LSTC0E6F7A4\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");SubDAddLanguageSpecificTextSet("LSTC0E6F7A4\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTC0E6F7A4\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)AddLanguageSpecificTextSet("LSTC0E6F7A4\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");SubDAddLanguageSpecificTextSet("LSTC0E6F7A4\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
      Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTC0E6F7A4\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SubD

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_SubD : GH_GeometricGoo<SubD>, 
	IGH_BakeAwareData, IGH_PreviewData, IGH_PreviewMeshData, IGH_RenderAwareData
```

```
Public Class GH_SubD
	Inherits GH_GeometricGoo(Of SubD)
	Implements IGH_BakeAwareData, IGH_PreviewData, IGH_PreviewMeshData, IGH_RenderAwareData
```

AddLanguageTabSet("ID1EBCA");

The GH\_SubD type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_SubDAddLanguageSpecificTextSet("LSTC0E6F7A4\_8?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_SubD__ctor.htm) | Initializes a new instance of the GH\_SubD class |
| Public method | [GH\_SubD(GH\_SubD)](M_Grasshopper_Kernel_Types_GH_SubD__ctor_1.htm) | Initializes a new instance of the GH\_SubD class |
| Public method | [GH\_SubD(Guid)](M_Grasshopper_Kernel_Types_GH_SubD__ctor_3.htm) | Initializes a new instance of the GH\_SubD class |
| Public method | [GH\_SubD(SubD)](M_Grasshopper_Kernel_Types_GH_SubD__ctor_2.htm) | Initializes a new instance of the GH\_SubD class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundingbox](P_Grasshopper_Kernel_Types_GH_SubD_Boundingbox.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");Boundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Boundingbox.htm).) |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_SubD_ClippingBox.htm) |  |
| Public property | [IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_SubD_IsGeometryLoaded.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsGeometryLoaded.htm).) |
| Public property | [IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm) | Gets a value indicating whether or not this geometry is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_SubD_IsValid.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_17?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_18?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_19?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_SubD_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC0E6F7A4\_20?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_21?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [ReferenceID](P_Grasshopper_Kernel_Types_GH_SubD_ReferenceID.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_23?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_24?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_25?cs=.|vb=.|cpp=::|nu=.|fs=.");ReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_SubD_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC0E6F7A4\_26?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_27?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_28?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_SubD_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC0E6F7A4\_29?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_30?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_31?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_SubD_Value.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_32?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_33?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_34?cs=.|vb=.|cpp=::|nu=.|fs=.");Value](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Value.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendRenderGeometry](M_Grasshopper_Kernel_Types_GH_SubD_AppendRenderGeometry.htm) |  |
| Public method | [BakeGeometry](M_Grasshopper_Kernel_Types_GH_SubD_BakeGeometry.htm) |  |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_SubD_CastFrom.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_35?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_36?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_37?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTC0E6F7A4\_38?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTC0E6F7A4\_39?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTC0E6F7A4\_40?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm) | Attempt a cast to type T. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_41?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_42?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTC0E6F7A4\_43?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTC0E6F7A4\_44?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTC0E6F7A4\_45?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTC0E6F7A4\_46?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_47?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTC0E6F7A4\_48?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_49?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTC0E6F7A4\_50?cpp=%");)](M_Grasshopper_Kernel_Types_GH_SubD_CastTo__1.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_51?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_52?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_53?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LSTC0E6F7A4\_54?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTC0E6F7A4\_55?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTC0E6F7A4\_56?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm).) |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_SubD_ClearCaches.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_57?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_58?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_59?cs=.|vb=.|cpp=::|nu=.|fs=.");ClearCachesAddLanguageSpecificTextSet("LSTC0E6F7A4\_60?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ClearCaches.htm).) |
| Public method | [DestroyPreviewMeshes](M_Grasshopper_Kernel_Types_GH_SubD_DestroyPreviewMeshes.htm) |  |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_SubD_DrawViewportMeshes.htm) |  |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_SubD_DrawViewportWires.htm) |  |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_SubD_Duplicate.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_61?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_62?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_63?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LSTC0E6F7A4\_64?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Duplicate.htm).) |
| Public method | [DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_SubD_DuplicateGeometry.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_65?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_66?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_67?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateGeometryAddLanguageSpecificTextSet("LSTC0E6F7A4\_68?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_DuplicateGeometry.htm).) |
| Public method | [DuplicateSubD](M_Grasshopper_Kernel_Types_GH_SubD_DuplicateSubD.htm) |  |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_SubD_EmitProxy.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_69?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_70?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_71?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LSTC0E6F7A4\_72?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_EmitProxy.htm).) |
| Public method | [GetBoundingBox](M_Grasshopper_Kernel_Types_GH_SubD_GetBoundingBox.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_73?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_74?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_75?cs=.|vb=.|cpp=::|nu=.|fs=.");GetBoundingBox(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_GetBoundingBox.htm).) |
| Public method | [GetPreviewMeshes](M_Grasshopper_Kernel_Types_GH_SubD_GetPreviewMeshes.htm) |  |
| Public method | [LoadGeometryAddLanguageSpecificTextSet("LSTC0E6F7A4\_76?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_SubD_LoadGeometry.htm) | If the geometry is referenced and not yet loaded, attempts to load the geometry. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_77?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_78?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_79?cs=.|vb=.|cpp=::|nu=.|fs=.");LoadGeometryAddLanguageSpecificTextSet("LSTC0E6F7A4\_80?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm).) |
| Public method | [LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_SubD_LoadGeometry_1.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_81?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_82?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_83?cs=.|vb=.|cpp=::|nu=.|fs=.");LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1.htm).) |
| Public method | [Morph](M_Grasshopper_Kernel_Types_GH_SubD_Morph.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_84?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_85?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_86?cs=.|vb=.|cpp=::|nu=.|fs=.");Morph(SpaceMorph)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Morph.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_SubD_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC0E6F7A4\_87?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_88?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_89?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_SubD_ScriptVariable.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC0E6F7A4\_90?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_91?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_92?cs=.|vb=.|cpp=::|nu=.|fs=.");ScriptVariableAddLanguageSpecificTextSet("LSTC0E6F7A4\_93?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_SubD_ToString.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC0E6F7A4\_94?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_95?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_96?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTC0E6F7A4\_97?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Transform](M_Grasshopper_Kernel_Types_GH_SubD_Transform.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTC0E6F7A4\_98?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_99?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_100?cs=.|vb=.|cpp=::|nu=.|fs=.");Transform(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_SubD_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTC0E6F7A4\_101?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_102?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTC0E6F7A4\_103?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTC0E6F7A4\_104?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC0E6F7A4\_105?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)