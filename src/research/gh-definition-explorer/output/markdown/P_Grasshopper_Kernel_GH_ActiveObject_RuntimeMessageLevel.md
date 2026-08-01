# P_Grasshopper_Kernel_GH_ActiveObject_RuntimeMessageLevel

﻿ GH\_ActiveObject.RuntimeMessageLevel Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ActiveObject Class](../html/T_Grasshopper_Kernel_GH_ActiveObject.htm "GH_ActiveObject Class")

[GH\_ActiveObject Properties](../html/Properties_T_Grasshopper_Kernel_GH_ActiveObject.htm "GH_ActiveObject Properties")

[IconCapableUI Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_IconCapableUI.htm "IconCapableUI Property ")

[IsDataProvider Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_IsDataProvider.htm "IsDataProvider Property ")

[Locked Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_Locked.htm "Locked Property ")

[MutableNickName Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_MutableNickName.htm "MutableNickName Property ")

[Phase Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_Phase.htm "Phase Property ")

[ProcessorTime Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_ProcessorTime.htm "ProcessorTime Property ")

[RuntimeMessageLevel Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_RuntimeMessageLevel.htm "RuntimeMessageLevel Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ActiveObjectAddLanguageSpecificTextSet("LST14018D28\_0?cpp=::|nu=.");RuntimeMessageLevel Property |

Returns the worst case flag for the current object

If the object contains at least 1 error, the result is Error.

If the object contains at least 1 warning, the result is Warning.

If the object contains at least 1 message, the result is Remark.

If the object contains no errors, no warnings and no messages, the result is Blank.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual GH_RuntimeMessageLevel RuntimeMessageLevel { get; }
```

```
Public Overridable ReadOnly Property RuntimeMessageLevel As GH_RuntimeMessageLevel
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [GH\_RuntimeMessageLevel](T_Grasshopper_Kernel_GH_RuntimeMessageLevel.htm)  

[Missing <value> documentation for "P:Grasshopper.Kernel.GH\_ActiveObject.RuntimeMessageLevel"]

#### Implements

[IGH\_ActiveObjectAddLanguageSpecificTextSet("LST14018D28\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");RuntimeMessageLevel](P_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessageLevel.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ActiveObject Class](T_Grasshopper_Kernel_GH_ActiveObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)