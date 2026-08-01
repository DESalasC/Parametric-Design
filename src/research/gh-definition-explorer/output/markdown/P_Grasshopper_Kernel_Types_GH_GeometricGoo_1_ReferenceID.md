# P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID

﻿ GH\_GeometricGoo(T).ReferenceID Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_GeometricGoo(T) Class](../html/T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm "GH_GeometricGoo(T) Class")

[GH\_GeometricGoo(T) Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm "GH_GeometricGoo(T) Properties")

[Boundingbox Property](../html/P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Boundingbox.htm "Boundingbox Property ")

[IsGeometryLoaded Property](../html/P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsGeometryLoaded.htm "IsGeometryLoaded Property ")

[IsReferencedGeometry Property](../html/P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsReferencedGeometry.htm "IsReferencedGeometry Property ")

[IsValid Property](../html/P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_IsValid.htm "IsValid Property ")

[ReferenceID Property](../html/P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_ReferenceID.htm "ReferenceID Property ")

[Value Property](../html/P_Grasshopper_Kernel_Types_GH_GeometricGoo_1_Value.htm "Value Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GeometricGooAddLanguageSpecificTextSet("LST5C5FDA98\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST5C5FDA98\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST5C5FDA98\_2?cpp=::|nu=.");ReferenceID Property |

Gets or sets the Guid of the object that is referenced.
Not all IGH\_GeometricGoo implementations support referenced geometry.
The default implementation is to always return Guid.Empty.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual Guid ReferenceID { get; set; }
```

```
Public Overridable Property ReferenceID As Guid
	Get
	Set
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Guid](https://docs.microsoft.com/dotnet/api/system.guid)  

[Missing <value> documentation for "P:Grasshopper.Kernel.Types.GH\_GeometricGoo`1.ReferenceID"]

#### Implements

[IGH\_GeometricGooAddLanguageSpecificTextSet("LST5C5FDA98\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ReferenceID](P_Grasshopper_Kernel_Types_IGH_GeometricGoo_ReferenceID.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GeometricGooAddLanguageSpecificTextSet("LST5C5FDA98\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST5C5FDA98\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)