# T_Grasshopper_Kernel_Types_GH_Light

﻿ GH\_Light Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Light Class](../html/T_Grasshopper_Kernel_Types_GH_Light.htm "GH_Light Class")

[GH\_Light Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_Light__ctor.htm "GH_Light Constructor ")

[GH\_Light Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Light.htm "GH_Light Properties")

[GH\_Light Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Light.htm "GH_Light Methods")

[GH\_Light Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Light.htm "GH_Light Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Light Class |

Represents an implementation of a Rhino Light class.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTB6CD1418\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTB6CD1418\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)AddLanguageSpecificTextSet("LSTB6CD1418\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");LightAddLanguageSpecificTextSet("LSTB6CD1418\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTB6CD1418\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGoo](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)AddLanguageSpecificTextSet("LSTB6CD1418\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");LightAddLanguageSpecificTextSet("LSTB6CD1418\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
      Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTB6CD1418\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Light

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Light : GH_GeometricGoo<Light>, 
	IGH_PreviewData, IGH_BakeAwareData
```

```
Public Class GH_Light
	Inherits GH_GeometricGoo(Of Light)
	Implements IGH_PreviewData, IGH_BakeAwareData
```

AddLanguageTabSet("ID1EBCA");

The GH\_Light type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_LightAddLanguageSpecificTextSet("LSTB6CD1418\_8?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Light__ctor.htm) | Default constructor, creates an new light |
| Public method | [GH\_Light(GH\_Light)](M_Grasshopper_Kernel_Types_GH_Light__ctor_1.htm) | Create a duplicate of another GH\_Light. This constructor also copies reference data. |
| Public method | [GH\_Light(Guid)](M_Grasshopper_Kernel_Types_GH_Light__ctor_3.htm) | Create a new referenced light that references a Rhino light with the specified ID. |
| Public method | [GH\_Light(Light)](M_Grasshopper_Kernel_Types_GH_Light__ctor_2.htm) | Create a duplicate of an existing light. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundingbox](P_Grasshopper_Kernel_Types_GH_Light_Boundingbox.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");Boundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Boundingbox.htm).) |
| Public property | [ClippingBox](P_Grasshopper_Kernel_Types_GH_Light_ClippingBox.htm) |  |
| Public property | [IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_Light_IsGeometryLoaded.htm) | Gets the load state of this light object. The light is considered to be loaded when the local light instance is not null. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsGeometryLoaded.htm).) |
| Public property | [IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm) | Gets a value indicating whether or not this geometry is referenced. Not all IGH\_GeometricGoo implementations support referenced geometry. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_15?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_16?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_Light_IsValid.htm) | Gets the validity of this light. If the light is referenced but cannot be loaded, then the light is not valid. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_17?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_18?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_19?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValid](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsValid.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Light_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTB6CD1418\_20?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_21?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).) |
| Public property | [ReferenceID](P_Grasshopper_Kernel_Types_GH_Light_ReferenceID.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_23?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_24?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_25?cs=.|vb=.|cpp=::|nu=.|fs=.");ReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_Light_TypeDescription.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTB6CD1418\_26?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_27?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_28?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_Light_TypeName.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTB6CD1418\_29?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_30?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_31?cs=.|vb=.|cpp=::|nu=.|fs=.");TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).) |
| Public property | [Value](P_Grasshopper_Kernel_Types_GH_Light_Value.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_32?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_33?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_34?cs=.|vb=.|cpp=::|nu=.|fs=.");Value](P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Value.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry](M_Grasshopper_Kernel_Types_GH_Light_BakeGeometry.htm) |  |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_Light_CastFrom.htm) | Remote to Local caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_35?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_36?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_37?cs=.|vb=.|cpp=::|nu=.|fs=.");CastFrom(Object)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastFrom.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTB6CD1418\_38?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTB6CD1418\_39?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTB6CD1418\_40?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm) | Attempt a cast to type T. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_41?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_42?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTB6CD1418\_43?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTB6CD1418\_44?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTB6CD1418\_45?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm) | Attempt a cast to type Q. (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTB6CD1418\_46?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_47?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTB6CD1418\_48?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTB6CD1418\_49?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LSTB6CD1418\_50?cpp=%");)](M_Grasshopper_Kernel_Types_GH_Light_CastTo__1.htm) | Local to Remote caster function. This stuff is complex, don't concern yourself with casting logic. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_51?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_52?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_53?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LSTB6CD1418\_54?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTB6CD1418\_55?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(QAddLanguageSpecificTextSet("LSTB6CD1418\_56?cpp=%");)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm).) |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_Light_ClearCaches.htm) | Clears all volatile caches for this instance. The boundingbox is cleared, and if the light is referenced, the local instance of the light is erased. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_57?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_58?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_59?cs=.|vb=.|cpp=::|nu=.|fs=.");ClearCachesAddLanguageSpecificTextSet("LSTB6CD1418\_60?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ClearCaches.htm).) |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_Types_GH_Light_DrawViewportMeshes.htm) |  |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_Types_GH_Light_DrawViewportWires.htm) |  |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_Light_Duplicate.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_61?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_62?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_63?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateAddLanguageSpecificTextSet("LSTB6CD1418\_64?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Duplicate.htm).) |
| Public method | [DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_Light_DuplicateGeometry.htm) | Create a duplicate of this light. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_65?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_66?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_67?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateGeometryAddLanguageSpecificTextSet("LSTB6CD1418\_68?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_DuplicateGeometry.htm).) |
| Public method | [DuplicateLight](M_Grasshopper_Kernel_Types_GH_Light_DuplicateLight.htm) | Create a duplicate of this light. |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_EmitProxy.htm) | Create a new proxy for this instance. Return Null if this class does not support proxies. (Inherited from [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_69?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_70?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm).) |
| Public method | [GetBoundingBox](M_Grasshopper_Kernel_Types_GH_Light_GetBoundingBox.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_71?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_72?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_73?cs=.|vb=.|cpp=::|nu=.|fs=.");GetBoundingBox(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_GetBoundingBox.htm).) |
| Public method | [LoadGeometryAddLanguageSpecificTextSet("LSTB6CD1418\_74?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Light_LoadGeometry.htm) | If the geometry is referenced and not yet loaded, attempts to load the geometry. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_75?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_76?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_77?cs=.|vb=.|cpp=::|nu=.|fs=.");LoadGeometryAddLanguageSpecificTextSet("LSTB6CD1418\_78?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm).) |
| Public method | [LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_Light_LoadGeometry_1.htm) | If the light is referenced and not yet loaded, attempts to load the light. (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_79?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_80?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_81?cs=.|vb=.|cpp=::|nu=.|fs=.");LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1.htm).) |
| Public method | [Morph](M_Grasshopper_Kernel_Types_GH_Light_Morph.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_82?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_83?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_84?cs=.|vb=.|cpp=::|nu=.|fs=.");Morph(SpaceMorph)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Morph.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_Light_Read.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTB6CD1418\_85?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_86?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_87?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_Light_ScriptVariable.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTB6CD1418\_88?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_89?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_90?cs=.|vb=.|cpp=::|nu=.|fs=.");ScriptVariableAddLanguageSpecificTextSet("LSTB6CD1418\_91?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_Light_ToString.htm) | Format the dimension using default grasshopper formatting logic. (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTB6CD1418\_92?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_93?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_94?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTB6CD1418\_95?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).) |
| Public method | [Transform](M_Grasshopper_Kernel_Types_GH_Light_Transform.htm) | (Overrides [GH\_GeometricGooAddLanguageSpecificTextSet("LSTB6CD1418\_96?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_97?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_98?cs=.|vb=.|cpp=::|nu=.|fs=.");Transform(Transform)](M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Transform.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_Light_Write.htm) | (Overrides [GH\_GooAddLanguageSpecificTextSet("LSTB6CD1418\_99?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_100?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTB6CD1418\_101?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm) | (Inherited from [GH\_GooAddLanguageSpecificTextSet("LSTB6CD1418\_102?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB6CD1418\_103?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)