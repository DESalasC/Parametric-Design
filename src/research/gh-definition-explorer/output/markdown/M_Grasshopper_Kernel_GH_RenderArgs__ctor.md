# M_Grasshopper_Kernel_GH_RenderArgs__ctor

﻿ GH\_RenderArgs Constructor (RhinoDoc, ViewportInfo, RenderPrimitiveList, Guid, RenderMaterial, RenderMaterial)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_RenderArgs Class](../html/T_Grasshopper_Kernel_GH_RenderArgs.htm "GH_RenderArgs Class")

[GH\_RenderArgs Constructor](../html/Overload_Grasshopper_Kernel_GH_RenderArgs__ctor.htm "GH_RenderArgs Constructor ")

[GH\_RenderArgs Constructor (RhinoDoc, ViewportInfo, RenderPrimitiveList, Guid, Dictionary(Int32, RenderMaterial))](../html/M_Grasshopper_Kernel_GH_RenderArgs__ctor_1.htm "GH_RenderArgs Constructor (RhinoDoc, ViewportInfo, RenderPrimitiveList, Guid, Dictionary(Int32, RenderMaterial))")

[GH\_RenderArgs Constructor (RhinoDoc, ViewportInfo, RenderPrimitiveList, Guid, RenderMaterial, RenderMaterial)](../html/M_Grasshopper_Kernel_GH_RenderArgs__ctor.htm "GH_RenderArgs Constructor (RhinoDoc, ViewportInfo, RenderPrimitiveList, Guid, RenderMaterial, RenderMaterial)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_RenderArgs Constructor (RhinoDoc, ViewportInfo, RenderPrimitiveList, Guid, RenderMaterial, RenderMaterial) |

**Note: This API is now obsolete.**

Create new render arguments.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
[ObsoleteAttribute]
public GH_RenderArgs(
	RhinoDoc doc,
	ViewportInfo vp,
	RenderPrimitiveList geometry,
	Guid id,
	RenderMaterial matNormal,
	RenderMaterial matSelected
)
```

```
<ObsoleteAttribute>
Public Sub New ( 
	doc As RhinoDoc,
	vp As ViewportInfo,
	geometry As RenderPrimitiveList,
	id As Guid,
	matNormal As RenderMaterial,
	matSelected As RenderMaterial
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

doc
:   Type: RhinoDoc  
    Rhino document.

vp
:   Type: ViewportInfo  
    Viewport.

geometry
:   Type: RenderPrimitiveList  
    Geometry list.

id
:   Type: [SystemAddLanguageSpecificTextSet("LSTC58A5E75\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    Render plugin id.

matNormal
:   Type: RenderMaterial  
    Material for unselected objects.

matSelected
:   Type: RenderMaterial  
    Material for selected objects.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_RenderArgs Class](T_Grasshopper_Kernel_GH_RenderArgs.htm)

[GH\_RenderArgs Overload](Overload_Grasshopper_Kernel_GH_RenderArgs__ctor.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)