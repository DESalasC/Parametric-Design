# M_Grasshopper_Kernel_GH_DocumentObject_GetValue_4

﻿ GH\_DocumentObject.GetValue Method (String, String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentObject Class](../html/T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Class")

[GH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Methods")

[GetValue Method](../html/Overload_Grasshopper_Kernel_GH_DocumentObject_GetValue.htm "GetValue Method ")

[GetValue Method (String, Boolean)](../html/M_Grasshopper_Kernel_GH_DocumentObject_GetValue.htm "GetValue Method (String, Boolean)")

[GetValue Method (String, Double)](../html/M_Grasshopper_Kernel_GH_DocumentObject_GetValue_1.htm "GetValue Method (String, Double)")

[GetValue Method (String, Color)](../html/M_Grasshopper_Kernel_GH_DocumentObject_GetValue_2.htm "GetValue Method (String, Color)")

[GetValue Method (String, Int32)](../html/M_Grasshopper_Kernel_GH_DocumentObject_GetValue_3.htm "GetValue Method (String, Int32)")

[GetValue Method (String, String)](../html/M_Grasshopper_Kernel_GH_DocumentObject_GetValue_4.htm "GetValue Method (String, String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentObjectAddLanguageSpecificTextSet("LST7071EFFE\_0?cpp=::|nu=.");GetValue Method (String, String) |

Get a string value from the component value table.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected string GetValue(
	string valueName,
	string default
)
```

```
Protected Function GetValue ( 
	valueName As String,
	default As String
) As String
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

valueName
:   Type: [SystemAddLanguageSpecificTextSet("LST7071EFFE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of string to retrieve.

default
:   Type: [SystemAddLanguageSpecificTextSet("LST7071EFFE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Default value to return in case of missing named value.

#### Return Value

Type: [String](https://docs.microsoft.com/dotnet/api/system.string)  
The string value with the given name of the default value.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentObject Class](T_Grasshopper_Kernel_GH_DocumentObject.htm)

[GetValue Overload](Overload_Grasshopper_Kernel_GH_DocumentObject_GetValue.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)