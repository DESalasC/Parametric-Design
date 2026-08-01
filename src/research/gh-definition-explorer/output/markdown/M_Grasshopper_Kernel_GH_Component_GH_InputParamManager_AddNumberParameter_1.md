# M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddNumberParameter_1

﻿ GH\_Component.GH\_InputParamManager.AddNumberParameter Method (String, String, String, GH\_ParamAccess, IEnumerable(Double))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component.GH\_InputParamManager Class](../html/T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_Component.GH_InputParamManager Class")

[GH\_InputParamManager Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_InputParamManager Methods")

[AddNumberParameter Method](../html/Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddNumberParameter.htm "AddNumberParameter Method ")

[AddNumberParameter Method (String, String, String, GH\_ParamAccess)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddNumberParameter.htm "AddNumberParameter Method (String, String, String, GH_ParamAccess)")

[AddNumberParameter Method (String, String, String, GH\_ParamAccess, IEnumerable(Double))](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddNumberParameter_1.htm "AddNumberParameter Method (String, String, String, GH_ParamAccess, IEnumerable(Double))")

[AddNumberParameter Method (String, String, String, GH\_ParamAccess, Double)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddNumberParameter_2.htm "AddNumberParameter Method (String, String, String, GH_ParamAccess, Double)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAddLanguageSpecificTextSet("LSTB3E4C76E\_0?cpp=::|nu=.");GH\_InputParamManagerAddLanguageSpecificTextSet("LSTB3E4C76E\_1?cpp=::|nu=.");AddNumberParameter Method (String, String, String, GH\_ParamAccess, IEnumerableAddLanguageSpecificTextSet("LSTB3E4C76E\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");DoubleAddLanguageSpecificTextSet("LSTB3E4C76E\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Add a floating point Number parameter to the input list of this component.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int AddNumberParameter(
	string name,
	string nickname,
	string description,
	GH_ParamAccess access,
	IEnumerable<double> default
)
```

```
Public Function AddNumberParameter ( 
	name As String,
	nickname As String,
	description As String,
	access As GH_ParamAccess,
	default As IEnumerable(Of Double)
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LSTB3E4C76E\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The name of the parameter. Keep it short, single words are best.

nickname
:   Type: [SystemAddLanguageSpecificTextSet("LSTB3E4C76E\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The nickname of the parameter. Keep it short, single characters are best.

description
:   Type: [SystemAddLanguageSpecificTextSet("LSTB3E4C76E\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The description of the parameter. Be succinct but clear, single sentences are best.

access
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTB3E4C76E\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParamAccess](T_Grasshopper_Kernel_GH_ParamAccess.htm)  
    Parameter access type. You must provide a correct access code in order to use GetData(), GetDataList() or GetDataTree() respectively.

default
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LSTB3E4C76E\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LSTB3E4C76E\_9?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Double](https://docs.microsoft.com/dotnet/api/system.double)AddLanguageSpecificTextSet("LSTB3E4C76E\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    A collection of default values to store in the parameter Persistent Data.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentAddLanguageSpecificTextSet("LSTB3E4C76E\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InputParamManager Class](T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm)

[AddNumberParameter Overload](Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddNumberParameter.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)