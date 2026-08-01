# T_Grasshopper_Kernel_IGH_BakeAwareObject

﻿ IGH\_BakeAwareObject Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_BakeAwareObject Interface](../html/T_Grasshopper_Kernel_IGH_BakeAwareObject.htm "IGH_BakeAwareObject Interface")

[IGH\_BakeAwareObject Properties](../html/Properties_T_Grasshopper_Kernel_IGH_BakeAwareObject.htm "IGH_BakeAwareObject Properties")

[IGH\_BakeAwareObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_BakeAwareObject.htm "IGH_BakeAwareObject Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_BakeAwareObject Interface |

Implement this interface on your IGH\_ActiveObject if you want to participate
in the Bake GUI.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_BakeAwareObject
```

```
Public Interface IGH_BakeAwareObject
```

AddLanguageTabSet("ID0EBCA");

The IGH\_BakeAwareObject type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsBakeCapable](P_Grasshopper_Kernel_IGH_BakeAwareObject_IsBakeCapable.htm) | Gets a value indicating whether or not the object can potentially Bake data in its current state. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry(RhinoDoc, ListAddLanguageSpecificTextSet("LSTEA2AD5FE\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GuidAddLanguageSpecificTextSet("LSTEA2AD5FE\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry_1.htm) | Bake all the goemetry in this object in the given Rhino document. |
| Public method | [BakeGeometry(RhinoDoc, ObjectAttributes, ListAddLanguageSpecificTextSet("LSTEA2AD5FE\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GuidAddLanguageSpecificTextSet("LSTEA2AD5FE\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry.htm) | Bake all the goemetry in this object in the given Rhino document. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)