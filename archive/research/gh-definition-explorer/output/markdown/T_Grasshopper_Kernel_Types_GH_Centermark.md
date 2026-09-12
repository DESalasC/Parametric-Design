# T_Grasshopper_Kernel_Types_GH_Centermark

﻿ GH\_Centermark Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Centermark Class](../html/T_Grasshopper_Kernel_Types_GH_Centermark.htm "GH_Centermark Class")

[GH\_Centermark Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Centermark__ctor.htm "GH_Centermark Constructor ")

[GH\_Centermark Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Centermark.htm "GH_Centermark Properties")

[GH\_Centermark Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Centermark.htm "GH_Centermark Methods")

[GH\_Centermark Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Centermark.htm "GH_Centermark Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Centermark Class |

Represents an implementation of a Rhino centermark.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST5029324C\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST5029324C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST5029324C\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");AnnotationBaseAddLanguageSpecificTextSet("LST5029324C\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST5029324C\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)AddLanguageSpecificTextSet("LST5029324C\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");AnnotationBaseAddLanguageSpecificTextSet("LST5029324C\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST5029324C\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm)  
        [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST5029324C\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Dimension](T_Grasshopper_Kernel_Types_GH_Dimension.htm)  
          Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST5029324C\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Centermark

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Centermark : GH_Dimension
```

```
Public Class GH_Centermark
	Inherits GH_Dimension
```

AddLanguageTabSet("ID1EBCA");

The GH\_Centermark type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_CentermarkAddLanguageSpecificTextSet("LST5029324C\_10?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Centermark__ctor.htm) | Default constructor, creates an invalid centermark. |
| Public method | [GH\_Centermark(Centermark)](M_Grasshopper_Kernel_Types_GH_Centermark__ctor_2.htm) | Create a duplicate of an existing centermark. |
| Public method | [GH\_Centermark(GH\_Centermark)](M_Grasshopper_Kernel_Types_GH_Centermark__ctor_1.htm) | Create a duplicate of another GH\_Centermark. This constructor also copies reference data. |
| Public method | [GH\_Centermark(Guid)](M_Grasshopper_Kernel_Types_GH_Centermark__ctor_4.htm) | Create a new referenced centermark that references a Rhino centermark with the specified ID. |
| Public method | [GH\_Centermark(Centermark, ModelAnnotationStyle)](M_Grasshopper_Kernel_Types_GH_Centermark__ctor_3.htm) | Create a duplicate of an existing centermark. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundingbox](P_Grasshopper_Kernel_Types_GH_AnnotationBase_Boundingbox.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_AnnotationBase_ClippingBox.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_AnnotationBase_IsGeometryLoaded.htm) | Gets the load state of this annotation object. The annotation is considered to be loaded when the local annotation instance is not null. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm) | Gets a value indicating whether or not this geometry is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST5029324C\_11?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5029324C\_12?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_AnnotationBase_IsValid.htm) | Gets the validity of this dimension. If the dimension is referenced but cannot be loaded, then the dimension is not valid. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_AnnotationBase_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [Overrides](P_Grasshopper_Kernel_Types_GH_AnnotationBase_Overrides.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [ReferenceID](P_Grasshopper_Kernel_Types_GH_AnnotationBase_ReferenceID.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [Style](P_Grasshopper_Kernel_Types_GH_AnnotationBase_Style.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Centermark_TypeDescription.htm) | (Overrides [GH\_AnnotationBaseAddLanguageSpecificTextSet("LST5029324C\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_AnnotationBase_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Centermark_TypeName.htm) | (Overrides [GH\_AnnotationBaseAddLanguageSpecificTextSet("LST5029324C\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_AnnotationBase_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Centermark_Value.htm) |  |
| Protected property | [ValueType](P_Grasshopper_Kernel_Types_GH_Centermark_ValueType.htm) | (Overrides [GH\_DimensionAddLanguageSpecificTextSet("LST5029324C\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");ValueType](P_Grasshopper_Kernel_Types_GH_Dimension_ValueType.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry](M_Grasshopper_Kernel_Types_GH_AnnotationBase_BakeGeometry.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Centermark_CastFrom.htm) | Remote to Local caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LST5029324C\_16?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5029324C\_17?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST5029324C\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST5029324C\_19?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST5029324C\_20?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST5029324C\_21?cpp=%");)](M_Grasshopper_Kernel_Types_GH_AnnotationBase_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST5029324C\_22?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST5029324C\_23?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST5029324C\_24?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Centermark_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_DimensionAddLanguageSpecificTextSet("LST5029324C\_25?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST5029324C\_26?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST5029324C\_27?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST5029324C\_28?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Dimension_CastTo__1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST5029324C\_29?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST5029324C\_30?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST5029324C\_31?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Dimension_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Inherited from [GH\_Dimension](T_Grasshopper_Kernel_Types_GH_Dimension.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST5029324C\_32?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST5029324C\_33?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST5029324C\_34?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm) | Attempt a cast to type T. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST5029324C\_35?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5029324C\_36?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST5029324C\_37?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST5029324C\_38?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST5029324C\_39?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST5029324C\_40?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5029324C\_41?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_AnnotationBase_ClearCaches.htm) | Clears all volatile caches for this instance. The boundingbox is cleared, and if the annotation is referenced, the local instance of the annotation is erased. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DrawViewportMeshes.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DrawViewportWires.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Duplicate.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [DuplicateAnnotation](M_Grasshopper_Kernel_Types_GH_Centermark_DuplicateAnnotation.htm) | Create a duplicate of this annotation. (Overrides [GH\_AnnotationBaseAddLanguageSpecificTextSet("LST5029324C\_42?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAnnotationAddLanguageSpecificTextSet("LST5029324C\_43?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DuplicateAnnotation.htm).) |
| Public method | [DuplicateCentermark](M_Grasshopper_Kernel_Types_GH_Centermark_DuplicateCentermark.htm) | Create a duplicate of this centermark. |
| Public method | [DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DuplicateGeometry.htm) | Create a duplicate of this annotation. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Dimension_EmitProxy.htm) | (Inherited from [GH\_Dimension](T_Grasshopper_Kernel_Types_GH_Dimension.htm).) |
| Public method | [GetBoundingBox](M_Grasshopper_Kernel_Types_GH_AnnotationBase_GetBoundingBox.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [LoadGeometryAddLanguageSpecificTextSet("LST5029324C\_44?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_AnnotationBase_LoadGeometry.htm) | If the geometry is referenced and not yet loaded, attempts to load the geometry. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_AnnotationBase_LoadGeometry_1.htm) | If the annotation is referenced and not yet loaded, attempts to load the leader. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Morph](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Morph.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Read.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_AnnotationBase_ScriptVariable.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Centermark_ToString.htm) | Format the centermark using default grasshopper formatting logic. (Overrides [GH\_AnnotationBaseAddLanguageSpecificTextSet("LST5029324C\_45?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST5029324C\_46?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_AnnotationBase_ToString.htm).) |
| Public method | [Transform](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Transform.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Write.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST5029324C\_47?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5029324C\_48?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)