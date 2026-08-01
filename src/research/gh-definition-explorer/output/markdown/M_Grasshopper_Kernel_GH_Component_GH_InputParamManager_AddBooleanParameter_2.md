# M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBooleanParameter_2

﻿ GH\_Component.GH\_InputParamManager.AddBooleanParameter Method (String, String, String, GH\_ParamAccess, IEnumerable(Boolean))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component.GH\_InputParamManager Class](../html/T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_Component.GH_InputParamManager Class")

[GH\_InputParamManager Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_InputParamManager Methods")

[AddBooleanParameter Method](../html/Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBooleanParameter.htm "AddBooleanParameter Method ")

[AddBooleanParameter Method (String, String, String, GH\_ParamAccess)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBooleanParameter.htm "AddBooleanParameter Method (String, String, String, GH_ParamAccess)")

[AddBooleanParameter Method (String, String, String, GH\_ParamAccess, Boolean)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBooleanParameter_1.htm "AddBooleanParameter Method (String, String, String, GH_ParamAccess, Boolean)")

[AddBooleanParameter Method (String, String, String, GH\_ParamAccess, IEnumerable(Boolean))](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBooleanParameter_2.htm "AddBooleanParameter Method (String, String, String, GH_ParamAccess, IEnumerable(Boolean))")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAddLanguageSpecificTextSet("LSTEB910B61\_0?cpp=::|nu=.");GH\_InputParamManagerAddLanguageSpecificTextSet("LSTEB910B61\_1?cpp=::|nu=.");AddBooleanParameter Method (String, String, String, GH\_ParamAccess, IEnumerableAddLanguageSpecificTextSet("LSTEB910B61\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");BooleanAddLanguageSpecificTextSet("LSTEB910B61\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Add a Boolean parameter to the input list of this component.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int AddBooleanParameter(
	string name,
	string nickname,
	string description,
	GH_ParamAccess access,
	IEnumerable<bool> default
)
```

```
Public Function AddBooleanParameter ( 
	name As String,
	nickname As String,
	description As String,
	access As GH_ParamAccess,
	default As IEnumerable(Of Boolean)
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LSTEB910B61\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The name of the parameter. Keep it short, single words are best.

nickname
:   Type: [SystemAddLanguageSpecificTextSet("LSTEB910B61\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The nickname of the parameter. Keep it short, single characters are best.

description
:   Type: [SystemAddLanguageSpecificTextSet("LSTEB910B61\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The description of the parameter. Be succinct but clear, single sentences are best.

access
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTEB910B61\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParamAccess](T_Grasshopper_Kernel_GH_ParamAccess.htm)  
    Parameter access type. You must provide a correct access code in order to use GetData(), GetDataList() or GetDataTree() respectively.

default
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LSTEB910B61\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LSTEB910B61\_9?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)AddLanguageSpecificTextSet("LSTEB910B61\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    A collection of default values to store in the parameter Persistent Data.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentAddLanguageSpecificTextSet("LSTEB910B61\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InputParamManager Class](T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm)

[AddBooleanParameter Overload](Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBooleanParameter.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)