# M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPointParameter_2

﻿ GH\_Component.GH\_InputParamManager.AddPointParameter Method (String, String, String, GH\_ParamAccess, IEnumerable(Point3d))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component.GH\_InputParamManager Class](../html/T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_Component.GH_InputParamManager Class")

[GH\_InputParamManager Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_InputParamManager Methods")

[AddPointParameter Method](../html/Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPointParameter.htm "AddPointParameter Method ")

[AddPointParameter Method (String, String, String, GH\_ParamAccess)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPointParameter.htm "AddPointParameter Method (String, String, String, GH_ParamAccess)")

[AddPointParameter Method (String, String, String, GH\_ParamAccess, Point3d)](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPointParameter_1.htm "AddPointParameter Method (String, String, String, GH_ParamAccess, Point3d)")

[AddPointParameter Method (String, String, String, GH\_ParamAccess, IEnumerable(Point3d))](../html/M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPointParameter_2.htm "AddPointParameter Method (String, String, String, GH_ParamAccess, IEnumerable(Point3d))")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAddLanguageSpecificTextSet("LST612D095C\_0?cpp=::|nu=.");GH\_InputParamManagerAddLanguageSpecificTextSet("LST612D095C\_1?cpp=::|nu=.");AddPointParameter Method (String, String, String, GH\_ParamAccess, IEnumerableAddLanguageSpecificTextSet("LST612D095C\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");Point3dAddLanguageSpecificTextSet("LST612D095C\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Register a new 3D point param with multiple default coordinates.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int AddPointParameter(
	string name,
	string nickname,
	string description,
	GH_ParamAccess access,
	IEnumerable<Point3d> default
)
```

```
Public Function AddPointParameter ( 
	name As String,
	nickname As String,
	description As String,
	access As GH_ParamAccess,
	default As IEnumerable(Of Point3d)
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST612D095C\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The name of the parameter. Keep it short, single words are best.

nickname
:   Type: [SystemAddLanguageSpecificTextSet("LST612D095C\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The nickname of the parameter. Keep it short, single characters are best.

description
:   Type: [SystemAddLanguageSpecificTextSet("LST612D095C\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The description of the parameter. Be succinct but clear, single sentences are best.

access
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST612D095C\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParamAccess](T_Grasshopper_Kernel_GH_ParamAccess.htm)  
    Parameter access type. You must provide a correct access code in order to use GetData(), GetDataList() or GetDataTree() respectively.

default
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST612D095C\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LST612D095C\_9?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");Point3dAddLanguageSpecificTextSet("LST612D095C\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    A collection of default values to store in the parameter Persistent Data.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentAddLanguageSpecificTextSet("LST612D095C\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InputParamManager Class](T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm)

[AddPointParameter Overload](Overload_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPointParameter.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)