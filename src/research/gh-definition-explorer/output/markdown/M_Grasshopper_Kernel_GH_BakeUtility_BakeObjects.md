# M_Grasshopper_Kernel_GH_BakeUtility_BakeObjects

﻿ GH\_BakeUtility.BakeObjects Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_BakeUtility Class](../html/T_Grasshopper_Kernel_GH_BakeUtility.htm "GH_BakeUtility Class")

[GH\_BakeUtility Methods](../html/Methods_T_Grasshopper_Kernel_GH_BakeUtility.htm "GH_BakeUtility Methods")

[BakeObject Method](../html/M_Grasshopper_Kernel_GH_BakeUtility_BakeObject.htm "BakeObject Method ")

[BakeObjects Method](../html/M_Grasshopper_Kernel_GH_BakeUtility_BakeObjects.htm "BakeObjects Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_BakeUtilityAddLanguageSpecificTextSet("LST383C5149\_0?cpp=::|nu=.");BakeObjects Method |

Bake a bunch of objects.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int BakeObjects(
	IEnumerable objects,
	ObjectAttributes att,
	RhinoDoc doc
)
```

```
Public Function BakeObjects ( 
	objects As IEnumerable,
	att As ObjectAttributes,
	doc As RhinoDoc
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

objects
:   Type: [System.CollectionsAddLanguageSpecificTextSet("LST383C5149\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.ienumerable)  
    Objects to bake.

att
:   Type: ObjectAttributes  
    Attributes.

doc
:   Type: RhinoDoc  
    Document.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
Number of successful bake operations.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_BakeUtility Class](T_Grasshopper_Kernel_GH_BakeUtility.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)