# M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntegerParameter_1

﻿ GH\_Component.GH\_InputParamManager.AddIntegerParameter Method (String, String, String, GH\_ParamAccess, IEnumerable(Int32))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component.GH\_InputParamManager Class](../html/T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_Component.GH_InputParamManager Class")

[GH\_InputParamManager Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_InputParamManager Methods")

[AddIntegerParameter Method](../html/Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntegerParameter.htm "AddIntegerParameter Method ")

[AddIntegerParameter Method (String, String, String, GH\_ParamAccess)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntegerParameter.htm "AddIntegerParameter Method (String, String, String, GH_ParamAccess)")

[AddIntegerParameter Method (String, String, String, GH\_ParamAccess, IEnumerable(Int32))](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntegerParameter_1.htm "AddIntegerParameter Method (String, String, String, GH_ParamAccess, IEnumerable(Int32))")

[AddIntegerParameter Method (String, String, String, GH\_ParamAccess, Int32)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntegerParameter_2.htm "AddIntegerParameter Method (String, String, String, GH_ParamAccess, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAddLanguageSpecificTextSet("LST2935ADC0\_0?cpp=::|nu=.");GH\_InputParamManagerAddLanguageSpecificTextSet("LST2935ADC0\_1?cpp=::|nu=.");AddIntegerParameter Method (String, String, String, GH\_ParamAccess, IEnumerableAddLanguageSpecificTextSet("LST2935ADC0\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");Int32AddLanguageSpecificTextSet("LST2935ADC0\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Add a Integer parameter to the input list of this component.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int AddIntegerParameter(
	string name,
	string nickname,
	string description,
	GH_ParamAccess access,
	IEnumerable<int> default
)
```

```
Public Function AddIntegerParameter ( 
	name As String,
	nickname As String,
	description As String,
	access As GH_ParamAccess,
	default As IEnumerable(Of Integer)
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST2935ADC0\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The name of the parameter. Keep it short, single words are best.

nickname
:   Type: [SystemAddLanguageSpecificTextSet("LST2935ADC0\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The nickname of the parameter. Keep it short, single characters are best.

description
:   Type: [SystemAddLanguageSpecificTextSet("LST2935ADC0\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The description of the parameter. Be succinct but clear, single sentences are best.

access
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST2935ADC0\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParamAccess](T_Grasshopper_Kernel_GH_ParamAccess.htm)  
    Parameter access type. You must provide a correct access code in order to use GetData(), GetDataList() or GetDataTree() respectively.

default
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST2935ADC0\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LST2935ADC0\_9?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LST2935ADC0\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    A collection of default values to store in the parameter Persistent Data.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentAddLanguageSpecificTextSet("LST2935ADC0\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InputParamManager Class](T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm)

[AddIntegerParameter Overload](Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntegerParameter.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)