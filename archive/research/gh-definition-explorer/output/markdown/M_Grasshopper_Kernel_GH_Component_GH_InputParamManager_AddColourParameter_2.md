# M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddColourParameter_2

﻿ GH\_Component.GH\_InputParamManager.AddColourParameter Method (String, String, String, GH\_ParamAccess, Color)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component.GH\_InputParamManager Class](../html/T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_Component.GH_InputParamManager Class")

[GH\_InputParamManager Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_InputParamManager Methods")

[AddColourParameter Method](../html/Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddColourParameter.htm "AddColourParameter Method ")

[AddColourParameter Method (String, String, String, GH\_ParamAccess)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddColourParameter.htm "AddColourParameter Method (String, String, String, GH_ParamAccess)")

[AddColourParameter Method (String, String, String, GH\_ParamAccess, IEnumerable(Color))](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddColourParameter_1.htm "AddColourParameter Method (String, String, String, GH_ParamAccess, IEnumerable(Color))")

[AddColourParameter Method (String, String, String, GH\_ParamAccess, Color)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddColourParameter_2.htm "AddColourParameter Method (String, String, String, GH_ParamAccess, Color)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAddLanguageSpecificTextSet("LST41B65263\_0?cpp=::|nu=.");GH\_InputParamManagerAddLanguageSpecificTextSet("LST41B65263\_1?cpp=::|nu=.");AddColourParameter Method (String, String, String, GH\_ParamAccess, Color) |

Add an ARGB Colour parameter to the input list of this component.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int AddColourParameter(
	string name,
	string nickname,
	string description,
	GH_ParamAccess access,
	Color default
)
```

```
Public Function AddColourParameter ( 
	name As String,
	nickname As String,
	description As String,
	access As GH_ParamAccess,
	default As Color
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST41B65263\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The name of the parameter. Keep it short, single words are best.

nickname
:   Type: [SystemAddLanguageSpecificTextSet("LST41B65263\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The nickname of the parameter. Keep it short, single characters are best.

description
:   Type: [SystemAddLanguageSpecificTextSet("LST41B65263\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The description of the parameter. Be succinct but clear, single sentences are best.

access
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST41B65263\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParamAccess](T_Grasshopper_Kernel_GH_ParamAccess.htm)  
    Parameter access type. You must provide a correct access code in order to use GetData(), GetDataList() or GetDataTree() respectively.

default
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST41B65263\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    A default value to store in the parameter Persistent Data.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentAddLanguageSpecificTextSet("LST41B65263\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InputParamManager Class](T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm)

[AddColourParameter Overload](Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddColourParameter.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)