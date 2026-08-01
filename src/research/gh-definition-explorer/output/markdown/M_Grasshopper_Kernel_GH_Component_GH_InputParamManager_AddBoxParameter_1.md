# M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBoxParameter_1

﻿ GH\_Component.GH\_InputParamManager.AddBoxParameter Method (String, String, String, GH\_ParamAccess, Box)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component.GH\_InputParamManager Class](../html/T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_Component.GH_InputParamManager Class")

[GH\_InputParamManager Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_InputParamManager Methods")

[AddBoxParameter Method](../html/Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBoxParameter.htm "AddBoxParameter Method ")

[AddBoxParameter Method (String, String, String, GH\_ParamAccess)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBoxParameter.htm "AddBoxParameter Method (String, String, String, GH_ParamAccess)")

[AddBoxParameter Method (String, String, String, GH\_ParamAccess, Box)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBoxParameter_1.htm "AddBoxParameter Method (String, String, String, GH_ParamAccess, Box)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAddLanguageSpecificTextSet("LSTA83A3186\_0?cpp=::|nu=.");GH\_InputParamManagerAddLanguageSpecificTextSet("LSTA83A3186\_1?cpp=::|nu=.");AddBoxParameter Method (String, String, String, GH\_ParamAccess, Box) |

Add a 3D Box parameter to the input list of this component.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int AddBoxParameter(
	string name,
	string nickname,
	string description,
	GH_ParamAccess access,
	Box default
)
```

```
Public Function AddBoxParameter ( 
	name As String,
	nickname As String,
	description As String,
	access As GH_ParamAccess,
	default As Box
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LSTA83A3186\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The name of the parameter. Keep it short, single words are best.

nickname
:   Type: [SystemAddLanguageSpecificTextSet("LSTA83A3186\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The nickname of the parameter. Keep it short, single characters are best.

description
:   Type: [SystemAddLanguageSpecificTextSet("LSTA83A3186\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The description of the parameter. Be succinct but clear, single sentences are best.

access
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTA83A3186\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParamAccess](T_Grasshopper_Kernel_GH_ParamAccess.htm)  
    Parameter access type. You must provide a correct access code in order to use GetData(), GetDataList() or GetDataTree() respectively.

default
:   Type: Box  
    A default value to store in the parameter Persistent Data.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentAddLanguageSpecificTextSet("LSTA83A3186\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InputParamManager Class](T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm)

[AddBoxParameter Overload](Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBoxParameter.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)