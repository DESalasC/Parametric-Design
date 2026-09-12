# M_Grasshopper_Kernel_Types_GH_TextDot_LoadGeometry_1

﻿ GH\_TextDot.LoadGeometry Method (RhinoDoc)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_TextDot Class](../html/T_Grasshopper_Kernel_Types_GH_TextDot.htm "GH_TextDot Class")

[GH\_TextDot Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_TextDot.htm "GH_TextDot Methods")

[LoadGeometry Method](../html/Overload_Grasshopper_Kernel_Types_GH_TextDot_LoadGeometry.htm "LoadGeometry Method ")

[LoadGeometry Method](../html/M_Grasshopper_Kernel_Types_GH_TextDot_LoadGeometry.htm "LoadGeometry Method ")

[LoadGeometry Method (RhinoDoc)](../html/M_Grasshopper_Kernel_Types_GH_TextDot_LoadGeometry_1.htm "LoadGeometry Method (RhinoDoc)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TextDotAddLanguageSpecificTextSet("LST34739EC5\_0?cpp=::|nu=.");LoadGeometry Method (RhinoDoc) |

If the text dot is referenced and not yet loaded, attempts to load the text dot.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public override bool LoadGeometry(
	RhinoDoc doc
)
```

```
Public Overrides Function LoadGeometry ( 
	doc As RhinoDoc
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

doc
:   Type: RhinoDoc

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the text dot is loaded (or if it was already loaded), False on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TextDot Class](T_Grasshopper_Kernel_Types_GH_TextDot.htm)

[LoadGeometry Overload](Overload_Grasshopper_Kernel_Types_GH_TextDot_LoadGeometry.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)