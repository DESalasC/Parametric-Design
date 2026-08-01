# M_Grasshopper_Kernel_GH_RuntimeMessage__ctor

﻿ GH\_RuntimeMessage Constructor 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_RuntimeMessage Class](../html/T_Grasshopper_Kernel_GH_RuntimeMessage.htm "GH_RuntimeMessage Class")

[GH\_RuntimeMessage Constructor](../html/M_Grasshopper_Kernel_GH_RuntimeMessage__ctor.htm "GH_RuntimeMessage Constructor ")

[GH\_RuntimeMessage Properties](../html/Properties_T_Grasshopper_Kernel_GH_RuntimeMessage.htm "GH_RuntimeMessage Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_RuntimeMessage Constructor |

Initializes a new instance of the [GH\_RuntimeMessage](T_Grasshopper_Kernel_GH_RuntimeMessage.htm) class

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_RuntimeMessage(
	string nMessage,
	GH_RuntimeMessageLevel nType = GH_RuntimeMessageLevel.Remark,
	string nSource = null
)
```

```
Public Sub New ( 
	nMessage As String,
	Optional nType As GH_RuntimeMessageLevel = GH_RuntimeMessageLevel.Remark,
	Optional nSource As String = Nothing
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

nMessage
:   Type: [SystemAddLanguageSpecificTextSet("LSTE9300552\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)

nType (Optional)
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTE9300552\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RuntimeMessageLevel](T_Grasshopper_Kernel_GH_RuntimeMessageLevel.htm)

nSource (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LSTE9300552\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_RuntimeMessage Class](T_Grasshopper_Kernel_GH_RuntimeMessage.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)