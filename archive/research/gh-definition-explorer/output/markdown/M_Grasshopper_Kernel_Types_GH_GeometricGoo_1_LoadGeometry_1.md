# M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1

﻿ GH\_GeometricGoo(T).LoadGeometry Method (RhinoDoc)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_GeometricGoo(T) Class](../html/T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm "GH_GeometricGoo(T) Class")

[GH\_GeometricGoo(T) Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm "GH_GeometricGoo(T) Methods")

[LoadGeometry Method](../html/Overload_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm "LoadGeometry Method ")

[LoadGeometry Method](../html/M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm "LoadGeometry Method ")

[LoadGeometry Method (RhinoDoc)](../html/M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry_1.htm "LoadGeometry Method (RhinoDoc)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GeometricGooAddLanguageSpecificTextSet("LSTD0C91091\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD0C91091\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTD0C91091\_2?cpp=::|nu=.");LoadGeometry Method (RhinoDoc) |

If the geometry is referenced and currently unloaded, forces loading of the geometry.
Not all IGH\_GeometricGoo implementations support referenced geometry. The default is to always return True.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual bool LoadGeometry(
	RhinoDoc doc
)
```

```
Public Overridable Function LoadGeometry ( 
	doc As RhinoDoc
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

doc
:   Type: RhinoDoc  
    Document to use for loading.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

#### Implements

[IGH\_GeometricGooAddLanguageSpecificTextSet("LSTD0C91091\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");LoadGeometry(RhinoDoc)](M_Grasshopper_Kernel_Types_IGH_GeometricGoo_LoadGeometry_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GeometricGooAddLanguageSpecificTextSet("LSTD0C91091\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD0C91091\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)

[LoadGeometry Overload](Overload_Grasshopper_Kernel_Types_GH_GeometricGoo_1_LoadGeometry.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)