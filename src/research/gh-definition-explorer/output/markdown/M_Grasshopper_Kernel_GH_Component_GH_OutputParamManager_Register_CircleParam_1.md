# M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_CircleParam_1

﻿ GH\_Component.GH\_OutputParamManager.Register\_CircleParam Method (String, String, String, GH\_ParamAccess)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component.GH\_OutputParamManager Class](../html/T_Grasshopper_Kernel_GH_Component_GH_OutputParamManager.htm "GH_Component.GH_OutputParamManager Class")

[GH\_OutputParamManager Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_OutputParamManager.htm "GH_OutputParamManager Methods")

[Register\_CircleParam Method](../html/Overload_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_CircleParam.htm "Register_CircleParam Method ")

[Register\_CircleParam Method (String, String, String)](../html/M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_CircleParam.htm "Register_CircleParam Method (String, String, String)")

[Register\_CircleParam Method (String, String, String, GH\_ParamAccess)](../html/M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_CircleParam_1.htm "Register_CircleParam Method (String, String, String, GH_ParamAccess)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAddLanguageSpecificTextSet("LST1EDE8BA0\_0?cpp=::|nu=.");GH\_OutputParamManagerAddLanguageSpecificTextSet("LST1EDE8BA0\_1?cpp=::|nu=.");Register\_CircleParam Method (String, String, String, GH\_ParamAccess) |

Register a new 3D circle parameter

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void Register_CircleParam(
	string name,
	string nickname,
	string description,
	GH_ParamAccess access
)
```

```
Public Sub Register_CircleParam ( 
	name As String,
	nickname As String,
	description As String,
	access As GH_ParamAccess
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST1EDE8BA0\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The name of the parameter. Keep it short, single words are best.

nickname
:   Type: [SystemAddLanguageSpecificTextSet("LST1EDE8BA0\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The nickname of the parameter. Keep it short, single characters are best.

description
:   Type: [SystemAddLanguageSpecificTextSet("LST1EDE8BA0\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The description of the parameter. Be succinct but clear.

access
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST1EDE8BA0\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParamAccess](T_Grasshopper_Kernel_GH_ParamAccess.htm)  
    Parameter access, you should set this field if you intend to output lists here.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentAddLanguageSpecificTextSet("LST1EDE8BA0\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_OutputParamManager Class](T_Grasshopper_Kernel_GH_Component_GH_OutputParamManager.htm)

[Register\_CircleParam Overload](Overload_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_CircleParam.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)