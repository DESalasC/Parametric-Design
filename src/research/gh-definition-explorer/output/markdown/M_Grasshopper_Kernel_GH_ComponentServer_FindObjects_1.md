# M_Grasshopper_Kernel_GH_ComponentServer_FindObjects_1

﻿ GH\_ComponentServer.FindObjects Method (String[], Int32, IGH\_ObjectProxy[], Double[])

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentServer Class](../html/T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Class")

[GH\_ComponentServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Methods")

[FindObjects Method](../html/Overload_Grasshopper_Kernel_GH_ComponentServer_FindObjects.htm "FindObjects Method ")

[FindObjects Method (Guid)](../html/M_Grasshopper_Kernel_GH_ComponentServer_FindObjects.htm "FindObjects Method (Guid)")

[FindObjects Method (String[], Int32, IGH\_ObjectProxy[], Double[])](../html/M_Grasshopper_Kernel_GH_ComponentServer_FindObjects_1.htm "FindObjects Method (String[], Int32, IGH_ObjectProxy[], Double[])")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentServerAddLanguageSpecificTextSet("LSTAE4651B7\_0?cpp=::|nu=.");FindObjects Method (AddLanguageSpecificTextSet("LSTAE4651B7\_1?cpp=array&lt;");StringAddLanguageSpecificTextSet("LSTAE4651B7\_2?cpp=&gt;|vb=()|nu=[]");, Int32, AddLanguageSpecificTextSet("LSTAE4651B7\_3?cpp=array&lt;");IGH\_ObjectProxyAddLanguageSpecificTextSet("LSTAE4651B7\_4?cpp=&gt;|vb=()|nu=[]");AddLanguageSpecificTextSet("LSTAE4651B7\_5?cpp=%");, AddLanguageSpecificTextSet("LSTAE4651B7\_6?cpp=array&lt;");DoubleAddLanguageSpecificTextSet("LSTAE4651B7\_7?cpp=&gt;|vb=()|nu=[]");AddLanguageSpecificTextSet("LSTAE4651B7\_8?cpp=%");) |

Searches the list of cached object proxies for objects that might be implied by a search term.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int FindObjects(
	string[] terms,
	int maximumResults,
	ref IGH_ObjectProxy[] results,
	ref double[] resultWeights
)
```

```
Public Function FindObjects ( 
	terms As String(),
	maximumResults As Integer,
	ByRef results As IGH_ObjectProxy(),
	ByRef resultWeights As Double()
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

terms
:   Type: AddLanguageSpecificTextSet("LSTAE4651B7\_9?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LSTAE4651B7\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LSTAE4651B7\_11?cpp=&gt;|vb=()|nu=[]");  
    Search terms to use.

maximumResults
:   Type: [SystemAddLanguageSpecificTextSet("LSTAE4651B7\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Maximum number of allowed hits.

results
:   Type: AddLanguageSpecificTextSet("LSTAE4651B7\_13?cpp=array&lt;");[Grasshopper.KernelAddLanguageSpecificTextSet("LSTAE4651B7\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_ObjectProxy](T_Grasshopper_Kernel_IGH_ObjectProxy.htm)AddLanguageSpecificTextSet("LSTAE4651B7\_15?cpp=&gt;|vb=()|nu=[]");AddLanguageSpecificTextSet("LSTAE4651B7\_16?cpp=%");

resultWeights
:   Type: AddLanguageSpecificTextSet("LSTAE4651B7\_17?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LSTAE4651B7\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)AddLanguageSpecificTextSet("LSTAE4651B7\_19?cpp=&gt;|vb=()|nu=[]");AddLanguageSpecificTextSet("LSTAE4651B7\_20?cpp=%");

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
A sorted list of search results.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentServer Class](T_Grasshopper_Kernel_GH_ComponentServer.htm)

[FindObjects Overload](Overload_Grasshopper_Kernel_GH_ComponentServer_FindObjects.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)