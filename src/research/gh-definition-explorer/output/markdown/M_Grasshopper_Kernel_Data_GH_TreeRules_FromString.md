# M_Grasshopper_Kernel_Data_GH_TreeRules_FromString

﻿ GH\_TreeRules.FromString Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_TreeRules Class](../html/T_Grasshopper_Kernel_Data_GH_TreeRules.htm "GH_TreeRules Class")

[GH\_TreeRules Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_TreeRules.htm "GH_TreeRules Methods")

[Apply Method](../html/Overload_Grasshopper_Kernel_Data_GH_TreeRules_Apply.htm "Apply Method ")

[FromString Method](../html/M_Grasshopper_Kernel_Data_GH_TreeRules_FromString.htm "FromString Method ")

[ToString Method](../html/M_Grasshopper_Kernel_Data_GH_TreeRules_ToString.htm "ToString Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TreeRulesAddLanguageSpecificTextSet("LSTFCE298A\_0?cpp=::|nu=.");FromString Method |

Attempt to parse a Pattern string.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_TreeRules FromString(
	string text,
	ref string message = null
)
```

```
Public Shared Function FromString ( 
	text As String,
	Optional ByRef message As String = Nothing
) As GH_TreeRules
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

text
:   Type: [SystemAddLanguageSpecificTextSet("LSTFCE298A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    String to parse.

message (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LSTFCE298A\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LSTFCE298A\_3?cpp=%");  
    If this function fails, msg will contain a message describing the error.

#### Return Value

Type: [GH\_TreeRules](T_Grasshopper_Kernel_Data_GH_TreeRules.htm)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TreeRules Class](T_Grasshopper_Kernel_Data_GH_TreeRules.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)