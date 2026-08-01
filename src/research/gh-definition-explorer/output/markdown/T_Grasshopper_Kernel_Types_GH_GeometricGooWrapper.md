# T_Grasshopper_Kernel_Types_GH_GeometricGooWrapper

﻿ GH\_GeometricGooWrapper Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_GeometricGooWrapper Class](../html/T_Grasshopper_Kernel_Types_GH_GeometricGooWrapper.htm "GH_GeometricGooWrapper Class")

[GH\_GeometricGooWrapper Constructor](../html/Overload_Grasshopper_Kernel_Types_GH_GeometricGooWrapper__ctor.htm "GH_GeometricGooWrapper Constructor ")

[GH\_GeometricGooWrapper Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_GeometricGooWrapper.htm "GH_GeometricGooWrapper Properties")

[GH\_GeometricGooWrapper Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_GeometricGooWrapper.htm "GH_GeometricGooWrapper Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GeometricGooWrapper Class |

Utility class for maintaining all kinds of IGH\_GeometricGoo types.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST59EA8208\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST59EA8208\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometricGooWrapper

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_GeometricGooWrapper : IGH_GeometricGoo
```

```
Public NotInheritable Class GH_GeometricGooWrapper
	Implements IGH_GeometricGoo
```

AddLanguageTabSet("ID1EBCA");

The GH\_GeometricGooWrapper type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_GeometricGooWrapperAddLanguageSpecificTextSet("LST59EA8208\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper__ctor.htm) | Initializes a new instance of the GH\_GeometricGooWrapper class |
| Public method | [GH\_GeometricGooWrapper(IGH\_GeometricGoo)](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper__ctor_1.htm) | Initializes a new instance of the GH\_GeometricGooWrapper class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundingbox](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_Boundingbox.htm) |  |
| Public property | [InternalGoo](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_InternalGoo.htm) |  |
| Public property | [IsGeometryLoaded](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_IsGeometryLoaded.htm) |  |
| Public property | [IsReferencedGeometry](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_IsReferencedGeometry.htm) |  |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_IsValid.htm) |  |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_IsValidWhyNot.htm) |  |
| Public property | [ReferenceID](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_ReferenceID.htm) |  |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_TypeDescription.htm) |  |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_TypeName.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_CastFrom.htm) |  |
| Public method | [CastToAddLanguageSpecificTextSet("LST59EA8208\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST59EA8208\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_CastTo__1.htm) |  |
| Public method | [ClearCaches](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_ClearCaches.htm) |  |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_Duplicate.htm) |  |
| Public method | [DuplicateGeometry](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_DuplicateGeometry.htm) |  |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_EmitProxy.htm) |  |
| Public method | [GetBoundingBox](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_GetBoundingBox.htm) |  |
| Public method | [LoadGeometryAddLanguageSpecificTextSet("LST59EA8208\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_LoadGeometry.htm) |  |
| Public method | [LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_LoadGeometry_1.htm) |  |
| Public method | [Morph](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_Morph.htm) |  |
| Public method | [Read](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_Read.htm) |  |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disapears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST59EA8208\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST59EA8208\_7?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |
| Public method | [Transform](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_Transform.htm) |  |
| Public method | [Write](M_Grasshopper_Kernel_Types_GH_GeometricGooWrapper_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)