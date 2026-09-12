# M_Grasshopper_Kernel_IGH_BakeAwareData_BakeGeometry

﻿ IGH\_BakeAwareData.BakeGeometry Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_BakeAwareData Interface](../html/T_Grasshopper_Kernel_IGH_BakeAwareData.htm "IGH_BakeAwareData Interface")

[IGH\_BakeAwareData Methods](../html/Methods_T_Grasshopper_Kernel_IGH_BakeAwareData.htm "IGH_BakeAwareData Methods")

[BakeGeometry Method](../html/M_Grasshopper_Kernel_IGH_BakeAwareData_BakeGeometry.htm "BakeGeometry Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_BakeAwareDataAddLanguageSpecificTextSet("LST561F7E85\_0?cpp=::|nu=.");BakeGeometry Method |

Bake an object in the given Rhino document.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool BakeGeometry(
	RhinoDoc doc,
	ObjectAttributes att,
	out Guid obj_guid
)
```

```
Function BakeGeometry ( 
	doc As RhinoDoc,
	att As ObjectAttributes,
	<OutAttribute> ByRef obj_guid As Guid
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

doc
:   Type: RhinoDoc  
    Document to bake into.

att
:   Type: ObjectAttributes  
    Attributes to bake with (should not be null).

obj\_guid
:   Type: [SystemAddLanguageSpecificTextSet("LST561F7E85\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)AddLanguageSpecificTextSet("LST561F7E85\_2?cpp=%");  
    The id of the baked object.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success. If False, obj\_guid and obj\_inst are not guaranteed to be valid pointers.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_BakeAwareData Interface](T_Grasshopper_Kernel_IGH_BakeAwareData.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)