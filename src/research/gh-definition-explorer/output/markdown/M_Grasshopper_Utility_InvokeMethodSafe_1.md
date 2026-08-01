# M_Grasshopper_Utility_InvokeMethodSafe_1

﻿ Utility.InvokeMethodSafe Method (Object, String, Object[])

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Utility Class](../html/T_Grasshopper_Utility.htm "Utility Class")

[Utility Methods](../html/Methods_T_Grasshopper_Utility.htm "Utility Methods")

[InvokeMethodSafe Method](../html/Overload_Grasshopper_Utility_InvokeMethodSafe.htm "InvokeMethodSafe Method ")

[InvokeMethodSafe Method (Object, String)](../html/M_Grasshopper_Utility_InvokeMethodSafe.htm "InvokeMethodSafe Method (Object, String)")

[InvokeMethodSafe Method (Object, String, Object[])](../html/M_Grasshopper_Utility_InvokeMethodSafe_1.htm "InvokeMethodSafe Method (Object, String, Object[])")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| UtilityAddLanguageSpecificTextSet("LSTEF4D0134\_0?cpp=::|nu=.");InvokeMethodSafe Method (Object, String, AddLanguageSpecificTextSet("LSTEF4D0134\_1?cpp=array&lt;");ObjectAddLanguageSpecificTextSet("LSTEF4D0134\_2?cpp=&gt;|vb=()|nu=[]");) |

Call a method via its name. No exceptions are thrown.

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static Object InvokeMethodSafe(
	Object target,
	string method,
	params Object[] params
)
```

```
Public Shared Function InvokeMethodSafe ( 
	target As Object,
	method As String,
	ParamArray params As Object()
) As Object
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

target
:   Type: [SystemAddLanguageSpecificTextSet("LSTEF4D0134\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
    Object to invoke on.

method
:   Type: [SystemAddLanguageSpecificTextSet("LSTEF4D0134\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of method to invoke.

params
:   Type: AddLanguageSpecificTextSet("LSTEF4D0134\_5?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LSTEF4D0134\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)AddLanguageSpecificTextSet("LSTEF4D0134\_7?cpp=&gt;|vb=()|nu=[]");  
    Arguments for method.

#### Return Value

Type: [Object](https://docs.microsoft.com/dotnet/api/system.object)  
The return value of the method.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Utility Class](T_Grasshopper_Utility.htm)

[InvokeMethodSafe Overload](Overload_Grasshopper_Utility_InvokeMethodSafe.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)