# M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddRectangleParameter_1

﻿ GH\_Component.GH\_InputParamManager.AddRectangleParameter Method (String, String, String, GH\_ParamAccess, Rectangle3d)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component.GH\_InputParamManager Class](../html/T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_Component.GH_InputParamManager Class")

[GH\_InputParamManager Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_InputParamManager Methods")

[AddRectangleParameter Method](../html/Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddRectangleParameter.htm "AddRectangleParameter Method ")

[AddRectangleParameter Method (String, String, String, GH\_ParamAccess)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddRectangleParameter.htm "AddRectangleParameter Method (String, String, String, GH_ParamAccess)")

[AddRectangleParameter Method (String, String, String, GH\_ParamAccess, Rectangle3d)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddRectangleParameter_1.htm "AddRectangleParameter Method (String, String, String, GH_ParamAccess, Rectangle3d)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAddLanguageSpecificTextSet("LST540EB94F\_0?cpp=::|nu=.");GH\_InputParamManagerAddLanguageSpecificTextSet("LST540EB94F\_1?cpp=::|nu=.");AddRectangleParameter Method (String, String, String, GH\_ParamAccess, Rectangle3d) |

Add a 3D Rectangle parameter to the input list of this component.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int AddRectangleParameter(
	string name,
	string nickname,
	string description,
	GH_ParamAccess access,
	Rectangle3d default
)
```

```
Public Function AddRectangleParameter ( 
	name As String,
	nickname As String,
	description As String,
	access As GH_ParamAccess,
	default As Rectangle3d
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST540EB94F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The name of the parameter. Keep it short, single words are best.

nickname
:   Type: [SystemAddLanguageSpecificTextSet("LST540EB94F\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The nickname of the parameter. Keep it short, single characters are best.

description
:   Type: [SystemAddLanguageSpecificTextSet("LST540EB94F\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The description of the parameter. Be succinct but clear, single sentences are best.

access
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST540EB94F\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParamAccess](T_Grasshopper_Kernel_GH_ParamAccess.htm)  
    Parameter access type. You must provide a correct access code in order to use GetData(), GetDataList() or GetDataTree() respectively.

default
:   Type: Rectangle3d  
    A default value to store in the parameter Persistent Data.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentAddLanguageSpecificTextSet("LST540EB94F\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InputParamManager Class](T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm)

[AddRectangleParameter Overload](Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddRectangleParameter.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)