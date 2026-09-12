# M_Grasshopper_Kernel_Parameters_IGH_TypeHint_Cast

﻿ IGH\_TypeHint.Cast Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Parameters](../html/N_Grasshopper_Kernel_Parameters.htm "Grasshopper.Kernel.Parameters")

[IGH\_TypeHint Interface](../html/T_Grasshopper_Kernel_Parameters_IGH_TypeHint.htm "IGH_TypeHint Interface")

[IGH\_TypeHint Methods](../html/Methods_T_Grasshopper_Kernel_Parameters_IGH_TypeHint.htm "IGH_TypeHint Methods")

[Cast Method](../html/M_Grasshopper_Kernel_Parameters_IGH_TypeHint_Cast.htm "Cast Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_TypeHintAddLanguageSpecificTextSet("LST1CF5DE17\_0?cpp=::|nu=.");Cast Method |

Apply conversion logic to a specific object. This function should not throw exceptions.

**Namespace:**
 [Grasshopper.Kernel.Parameters](N_Grasshopper_Kernel_Parameters.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool Cast(
	Object data,
	out Object target
)
```

```
Function Cast ( 
	data As Object,
	<OutAttribute> ByRef target As Object
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

data
:   Type: [SystemAddLanguageSpecificTextSet("LST1CF5DE17\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
    Data to convert.

target
:   Type: [SystemAddLanguageSpecificTextSet("LST1CF5DE17\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)AddLanguageSpecificTextSet("LST1CF5DE17\_3?cpp=%");  
    Output instance.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure. If False is returned, target may be null.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_TypeHint Interface](T_Grasshopper_Kernel_Parameters_IGH_TypeHint.htm)

[Grasshopper.Kernel.Parameters Namespace](N_Grasshopper_Kernel_Parameters.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)