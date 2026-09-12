# M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_RegisterParam_2

﻿ GH\_Component.GH\_OutputParamManager.RegisterParam Method (IGH\_Param, String, String, String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component.GH\_OutputParamManager Class](../html/T_Grasshopper_Kernel_GH_Component_GH_OutputParamManager.htm "GH_Component.GH_OutputParamManager Class")

[GH\_OutputParamManager Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_OutputParamManager.htm "GH_OutputParamManager Methods")

[RegisterParam Method](../html/Overload_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_RegisterParam.htm "RegisterParam Method ")

[RegisterParam Method (IGH\_Param)](../html/M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_RegisterParam.htm "RegisterParam Method (IGH_Param)")

[RegisterParam Method (IGH\_Param, GH\_ParamAccess)](../html/M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_RegisterParam_1.htm "RegisterParam Method (IGH_Param, GH_ParamAccess)")

[RegisterParam Method (IGH\_Param, String, String, String)](../html/M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_RegisterParam_2.htm "RegisterParam Method (IGH_Param, String, String, String)")

[RegisterParam Method (IGH\_Param, String, String, String, GH\_ParamAccess)](../html/M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_RegisterParam_3.htm "RegisterParam Method (IGH_Param, String, String, String, GH_ParamAccess)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAddLanguageSpecificTextSet("LSTD0C67272\_0?cpp=::|nu=.");GH\_OutputParamManagerAddLanguageSpecificTextSet("LSTD0C67272\_1?cpp=::|nu=.");RegisterParam Method (IGH\_Param, String, String, String) |

Generic parameter registration. This class provides methods to register standard parameters,
but if you have a special type you're in charge of setting it all up yourself.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void RegisterParam(
	IGH_Param param,
	string name,
	string nickname,
	string description
)
```

```
Public Sub RegisterParam ( 
	param As IGH_Param,
	name As String,
	nickname As String,
	description As String
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

param
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTD0C67272\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Param](T_Grasshopper_Kernel_IGH_Param.htm)  
    The parameter to add

name
:   Type: [SystemAddLanguageSpecificTextSet("LSTD0C67272\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The name of the parameter. Keep it short, single words are best.

nickname
:   Type: [SystemAddLanguageSpecificTextSet("LSTD0C67272\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The nickname of the parameter. Keep it short, single characters are best.

description
:   Type: [SystemAddLanguageSpecificTextSet("LSTD0C67272\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The description of the parameter. Be succinct but clear.

![](../icons/SectionExpanded.png)Remarks

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentAddLanguageSpecificTextSet("LSTD0C67272\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_OutputParamManager Class](T_Grasshopper_Kernel_GH_Component_GH_OutputParamManager.htm)

[RegisterParam Overload](Overload_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_RegisterParam.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)