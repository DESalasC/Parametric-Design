# M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddParameter_1

﻿ GH\_Component.GH\_InputParamManager.AddParameter Method (IGH\_Param, String, String, String, GH\_ParamAccess)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component.GH\_InputParamManager Class](../html/T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_Component.GH_InputParamManager Class")

[GH\_InputParamManager Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_InputParamManager Methods")

[AddParameter Method](../html/Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddParameter.htm "AddParameter Method ")

[AddParameter Method (IGH\_Param)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddParameter.htm "AddParameter Method (IGH_Param)")

[AddParameter Method (IGH\_Param, String, String, String, GH\_ParamAccess)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddParameter_1.htm "AddParameter Method (IGH_Param, String, String, String, GH_ParamAccess)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAddLanguageSpecificTextSet("LST78DE5D7F\_0?cpp=::|nu=.");GH\_InputParamManagerAddLanguageSpecificTextSet("LST78DE5D7F\_1?cpp=::|nu=.");AddParameter Method (IGH\_Param, String, String, String, GH\_ParamAccess) |

Generic parameter addition. If you cannot use one of the utility methods provided
by this class, you can register a customized parameter using this method.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int AddParameter(
	IGH_Param param,
	string name,
	string nickname,
	string description,
	GH_ParamAccess access
)
```

```
Public Function AddParameter ( 
	param As IGH_Param,
	name As String,
	nickname As String,
	description As String,
	access As GH_ParamAccess
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

param
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST78DE5D7F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Param](T_Grasshopper_Kernel_IGH_Param.htm)  
    The parameter to add.

name
:   Type: [SystemAddLanguageSpecificTextSet("LST78DE5D7F\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The name of the parameter. Keep it short, single words are best.

nickname
:   Type: [SystemAddLanguageSpecificTextSet("LST78DE5D7F\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The nickname of the parameter. Keep it short, single characters are best.

description
:   Type: [SystemAddLanguageSpecificTextSet("LST78DE5D7F\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The description of the parameter. Be succinct but clear, single sentences are best.

access
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST78DE5D7F\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParamAccess](T_Grasshopper_Kernel_GH_ParamAccess.htm)  
    Parameter access type. You must provide a correct access code in order to use GetData(), GetDataList() or GetDataTree() respectively.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
Index of the newly added parameter.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentAddLanguageSpecificTextSet("LST78DE5D7F\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InputParamManager Class](T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm)

[AddParameter Overload](Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddParameter.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)