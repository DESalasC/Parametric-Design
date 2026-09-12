# T_Grasshopper_Kernel_Types_GH_Dimension

﻿ GH\_Dimension Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Dimension Class](../html/T_Grasshopper_Kernel_Types_GH_Dimension.htm "GH_Dimension Class")

[GH\_Dimension Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Dimension__ctor.htm "GH_Dimension Constructor ")

[GH\_Dimension Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Dimension.htm "GH_Dimension Properties")

[GH\_Dimension Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Dimension.htm "GH_Dimension Methods")

[GH\_Dimension Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Dimension.htm "GH_Dimension Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Dimension Class |

Represents an implementation of a Rhino dimension base class.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST91E5B919\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST91E5B919\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LST91E5B919\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");AnnotationBaseAddLanguageSpecificTextSet("LST91E5B919\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST91E5B919\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)AddLanguageSpecificTextSet("LST91E5B919\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");AnnotationBaseAddLanguageSpecificTextSet("LST91E5B919\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
      [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST91E5B919\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm)  
        Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST91E5B919\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Dimension  
          [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST91E5B919\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AngularDimension](T_Grasshopper_Kernel_Types_GH_AngularDimension.htm)  
          [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST91E5B919\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Centermark](T_Grasshopper_Kernel_Types_GH_Centermark.htm)  
          [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST91E5B919\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_LinearDimension](T_Grasshopper_Kernel_Types_GH_LinearDimension.htm)  
          [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST91E5B919\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_OrdinateDimension](T_Grasshopper_Kernel_Types_GH_OrdinateDimension.htm)  
          [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST91E5B919\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RadialDimension](T_Grasshopper_Kernel_Types_GH_RadialDimension.htm)

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_Dimension : GH_AnnotationBase
```

```
Public MustInherit Class GH_Dimension
	Inherits GH_AnnotationBase
```

AddLanguageTabSet("ID1EBCA");

The GH\_Dimension type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DimensionAddLanguageSpecificTextSet("LST91E5B919\_14?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Dimension__ctor.htm) | Default constructor, creates an invalid dimension. |
| Protected method | [GH\_Dimension(Dimension)](M_Grasshopper_Kernel_Types_GH_Dimension__ctor_3.htm) | Create a duplicate of an existing dimension. |
| Protected method | [GH\_Dimension(GH\_Dimension)](M_Grasshopper_Kernel_Types_GH_Dimension__ctor_1.htm) | Create a duplicate of another GH\_Dimension. This constructor also copies reference data. |
| Public method | [GH\_Dimension(Guid)](M_Grasshopper_Kernel_Types_GH_Dimension__ctor_5.htm) | Create a new referenced dimension that references a Rhino dimension with the specified ID. |
| Protected method | [GH\_Dimension(ObjRef)](M_Grasshopper_Kernel_Types_GH_Dimension__ctor_2.htm) | Initializes a new instance of the GH\_Dimension class |
| Protected method | [GH\_Dimension(Dimension, ModelAnnotationStyle)](M_Grasshopper_Kernel_Types_GH_Dimension__ctor_4.htm) | Create a duplicate of an existing dimension. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundingbox](P_Grasshopper_Kernel_Types_GH_AnnotationBase_Boundingbox.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_AnnotationBase_ClippingBox.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_AnnotationBase_IsGeometryLoaded.htm) | Gets the load state of this annotation object. The annotation is considered to be loaded when the local annotation instance is not null. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm) | Gets a value indicating whether or not this geometry is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST91E5B919\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST91E5B919\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_AnnotationBase_IsValid.htm) | Gets the validity of this dimension. If the dimension is referenced but cannot be loaded, then the dimension is not valid. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_AnnotationBase_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [Overrides](P_Grasshopper_Kernel_Types_GH_AnnotationBase_Overrides.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [ReferenceID](P_Grasshopper_Kernel_Types_GH_AnnotationBase_ReferenceID.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [Style](P_Grasshopper_Kernel_Types_GH_AnnotationBase_Style.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_AnnotationBase_TypeDescription.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_AnnotationBase_TypeName.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Dimension_Value.htm) |  |
| Protected property | [ValueType](P_Grasshopper_Kernel_Types_GH_Dimension_ValueType.htm) | (Overrides [GH\_AnnotationBaseAddLanguageSpecificTextSet("LST91E5B919\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");ValueType](P_Grasshopper_Kernel_Types_GH_AnnotationBase_ValueType.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry](M_Grasshopper_Kernel_Types_GH_AnnotationBase_BakeGeometry.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm) | Attempt a cast from generic object. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST91E5B919\_18?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST91E5B919\_19?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST91E5B919\_20?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST91E5B919\_21?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST91E5B919\_22?cpp=%");)](M_Grasshopper_Kernel_Types_GH_AnnotationBase_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST91E5B919\_23?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST91E5B919\_24?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST91E5B919\_25?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Dimension_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_AnnotationBaseAddLanguageSpecificTextSet("LST91E5B919\_26?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST91E5B919\_27?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST91E5B919\_28?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST91E5B919\_29?cpp=%");)](M_Grasshopper_Kernel_Types_GH_AnnotationBase_CastTo__1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST91E5B919\_30?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST91E5B919\_31?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST91E5B919\_32?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm) | Attempt a cast to type T. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LST91E5B919\_33?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST91E5B919\_34?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LST91E5B919\_35?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST91E5B919\_36?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LST91E5B919\_37?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST91E5B919\_38?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST91E5B919\_39?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_AnnotationBase_ClearCaches.htm) | Clears all volatile caches for this instance. The boundingbox is cleared, and if the annotation is referenced, the local instance of the annotation is erased. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DrawViewportMeshes.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DrawViewportWires.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Duplicate.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [DuplicateAnnotation](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DuplicateAnnotation.htm) | Create a duplicate of this annotation. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_AnnotationBase_DuplicateGeometry.htm) | Create a duplicate of this annotation. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_Dimension_EmitProxy.htm) | (Overrides [GH\_AnnotationBaseAddLanguageSpecificTextSet("LST91E5B919\_40?cs=.|vb=.|cpp=::|nu=.|fs=.");EmitProxyAddLanguageSpecificTextSet("LST91E5B919\_41?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_AnnotationBase_EmitProxy.htm).) |
| Public method | [GetBoundingBox](M_Grasshopper_Kernel_Types_GH_AnnotationBase_GetBoundingBox.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [LoadGeometryAddLanguageSpecificTextSet("LST91E5B919\_42?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_AnnotationBase_LoadGeometry.htm) | If the geometry is referenced and not yet loaded, attempts to load the geometry. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_AnnotationBase_LoadGeometry_1.htm) | If the annotation is referenced and not yet loaded, attempts to load the leader. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Morph](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Morph.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Read.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_AnnotationBase_ScriptVariable.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_AnnotationBase_ToString.htm) | Format the dimension using default grasshopper formatting logic. (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Transform](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Transform.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_AnnotationBase_Write.htm) | (Inherited from [GH\_AnnotationBase](T_Grasshopper_Kernel_Types_GH_AnnotationBase.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LST91E5B919\_43?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST91E5B919\_44?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)