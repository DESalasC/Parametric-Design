# T_Grasshopper_Kernel_Types_GH_OrdinateDimension

﻿ GH\_OrdinateDimension Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_OrdinateDimension Class](../html/T_Grasshopper_Kernel_Types_GH_OrdinateDimension.htm "GH_OrdinateDimension Class")

[GH\_OrdinateDimension Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_OrdinateDimension__ctor.htm "GH_OrdinateDimension Constructor ")

[GH\_OrdinateDimension Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_OrdinateDimension.htm "GH_OrdinateDimension Properties")

[GH\_OrdinateDimension Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_OrdinateDimension.htm "GH_OrdinateDimension Methods")

[GH\_OrdinateDimension Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_OrdinateDimension.htm "GH_OrdinateDimension Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_OrdinateDimension Class |

Represents an implementation of a Rhino ordinate dimension.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTDCCC04A8\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTDCCC04A8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LSTDCCC04A8\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");AnnotationBaseAddLanguageSpecificTextSet("LSTDCCC04A8\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTDCCC04A8\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)AddLanguageSpecificTextSet("LSTDCCC04A8\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");AnnotationBaseAddLanguageSpecificTextSet("LSTDCCC04A8\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTDCCC04A8\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm)  
        [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTDCCC04A8\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Dimension](T_Grasshopper_Kernel_Types_GH_Dimension.htm)  
          Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTDCCC04A8\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_OrdinateDimension

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_OrdinateDimension : GH_Dimension
```

```
Public Class GH_OrdinateDimension
	Inherits GH_Dimension
```

AddLanguageTabSet("ID1EBCA");

The GH\_OrdinateDimension type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_OrdinateDimensionAddLanguageSpecificTextSet("LSTDCCC04A8\_10?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_OrdinateDimension__ctor.htm) | Default constructor, creates an invalid ordinate dimension. |
| Public method | [GH\_OrdinateDimension(GH\_OrdinateDimension)](M_Grasshopper_Kernel_Types_GH_OrdinateDimension__ctor_1.htm) | Create a duplicate of another GH\_OrdinateDimension. This constructor also copies reference data. |
| Public method | [GH\_OrdinateDimension(Guid)](M_Grasshopper_Kernel_Types_GH_OrdinateDimension__ctor_4.htm) | Create a new referenced ordinate dimension that references a Rhino dimension with the specified ID. |
| Public method | [GH\_OrdinateDimension(OrdinateDimension)](M_Grasshopper_Kernel_Types_GH_OrdinateDimension__ctor_2.htm) | Create a duplicate of an existing ordinate dimension. |
| Public method | [GH\_OrdinateDimension(OrdinateDimension, ModelAnnotationStyle)](M_Grasshopper_Kernel_Types_GH_OrdinateDimension__ctor_3.htm) | Create a duplicate of an existing ordinate dimension. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundingbox](P_Grasshopper_Kernel_Types_GH_AnnotationBase_Boundingbox.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_AnnotationBase_ClippingBox.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_AnnotationBase_IsGeometryLoaded.htm) | Gets the load state of this annotation object. The annotation is considered to be loaded when the local annotation instance is not null. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm) | Gets a value indicating whether or not this geometry is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTDCCC04A8\_11?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDCCC04A8\_12?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_AnnotationBase_IsValid.htm) | Gets the validity of this dimension. If the dimension is referenced but cannot be loaded, then the dimension is not valid. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_AnnotationBase_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [Overrides](P_Grasshopper_Kernel_Types_GH_AnnotationBase_Overrides.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [ReferenceID](P_Grasshopper_Kernel_Types_GH_AnnotationBase_ReferenceID.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [Style](P_Grasshopper_Kernel_Types_GH_AnnotationBase_Style.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_OrdinateDimension_TypeDescription.htm) | (Overrides [GH\_AnnotationBaseAddLanguageSpecificTextSet("LSTDCCC04A8\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_AnnotationBase_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_OrdinateDimension_TypeName.htm) | (Overrides [GH\_AnnotationBaseAddLanguageSpecificTextSet("LSTDCCC04A8\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_AnnotationBase_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_OrdinateDimension_Value.htm) |  |
| Protected property | [ValueType](P_Grasshopper_Kernel_Types_GH_OrdinateDimension_ValueType.htm) | (Overrides [GH\_DimensionAddLanguageSpecificTextSet("LSTDCCC04A8\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");ValueType](P_Grasshopper_Kernel_Types_GH_Dimension_ValueType.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry](M_Grasshopper_Kernel_Types_GH_AnnotationBase_BakeGeometry.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_OrdinateDimension_CastFrom.htm) | Remote to Local caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTDCCC04A8\_16?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDCCC04A8\_17?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTDCCC04A8\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTDCCC04A8\_19?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTDCCC04A8\_20?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTDCCC04A8\_21?cpp=%");)](M_Grasshopper_Kernel_Types_GH_AnnotationBase_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTDCCC04A8\_22?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTDCCC04A8\_23?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTDCCC04A8\_24?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Dimension_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Inherited from [GH\_Dimension](T_Grasshopper_Kernel_Types_GH_Dimension.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTDCCC04A8\_25?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTDCCC04A8\_26?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTDCCC04A8\_27?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm) | Attempt a cast to type T. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTDCCC04A8\_28?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDCCC04A8\_29?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTDCCC04A8\_30?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTDCCC04A8\_31?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTDCCC04A8\_32?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTDCCC04A8\_33?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDCCC04A8\_34?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTDCCC04A8\_35?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTDCCC04A8\_36?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTDCCC04A8\_37?cpp=%");)](M_Grasshopper_Kernel_Types_GH_OrdinateDimension_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_DimensionAddLanguageSpecificTextSet("LSTDCCC04A8\_38?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LSTDCCC04A8\_39?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTDCCC04A8\_40?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTDCCC04A8\_41?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Dimension_CastTo__1.htm).) |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_AnnotationBase_ClearCaches.htm) | Clears all volatile caches for this instance. The boundingbox is cleared, and if the annotation is referenced, the local instance of the annotation is erased. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DrawViewportMeshes.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DrawViewportWires.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Duplicate.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [DuplicateAnnotation](M_Grasshopper_Kernel_Types_GH_OrdinateDimension_DuplicateAnnotation.htm) | Create a duplicate of this annotation. (Overrides [GH\_AnnotationBaseAddLanguageSpecificTextSet("LSTDCCC04A8\_42?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAnnotationAddLanguageSpecificTextSet("LSTDCCC04A8\_43?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DuplicateAnnotation.htm).) |
| Public method | [DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DuplicateGeometry.htm) | Create a duplicate of this annotation. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [DuplicateOrdinateDimension](M_Grasshopper_Kernel_Types_GH_OrdinateDimension_DuplicateOrdinateDimension.htm) | Create a duplicate of this ordinate dimension. |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Dimension_EmitProxy.htm) | (Inherited from [GH\_Dimension](T_Grasshopper_Kernel_Types_GH_Dimension.htm).) |
| Public method | [GetBoundingBox](M_Grasshopper_Kernel_Types_GH_AnnotationBase_GetBoundingBox.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [LoadGeometryAddLanguageSpecificTextSet("LSTDCCC04A8\_44?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_AnnotationBase_LoadGeometry.htm) | If the geometry is referenced and not yet loaded, attempts to load the geometry. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_AnnotationBase_LoadGeometry_1.htm) | If the annotation is referenced and not yet loaded, attempts to load the leader. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Morph](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Morph.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Read.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_AnnotationBase_ScriptVariable.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_OrdinateDimension_ToString.htm) | Format the dimension using default grasshopper formatting logic. (Overrides [GH\_AnnotationBaseAddLanguageSpecificTextSet("LSTDCCC04A8\_45?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTDCCC04A8\_46?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_AnnotationBase_ToString.htm).) |
| Public method | [Transform](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Transform.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Write.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTDCCC04A8\_47?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDCCC04A8\_48?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)