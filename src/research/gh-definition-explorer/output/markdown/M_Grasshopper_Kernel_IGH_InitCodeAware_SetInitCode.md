# M_Grasshopper_Kernel_IGH_InitCodeAware_SetInitCode

﻿ IGH\_InitCodeAware.SetInitCode Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_InitCodeAware Interface](../html/T_Grasshopper_Kernel_IGH_InitCodeAware.htm "IGH_InitCodeAware Interface")

[IGH\_InitCodeAware Methods](../html/Methods_T_Grasshopper_Kernel_IGH_InitCodeAware.htm "IGH_InitCodeAware Methods")

[SetInitCode Method](../html/M_Grasshopper_Kernel_IGH_InitCodeAware_SetInitCode.htm "SetInitCode Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_InitCodeAwareAddLanguageSpecificTextSet("LST50E4FE4E\_0?cpp=::|nu=.");SetInitCode Method |

This method will be called when the user inserts an object via the
Canvas Search popup and supplies an "=XXXX" string init code.
Do not throw exceptions in this method! Either handle the code correctly or ignore it.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void SetInitCode(
	string code
)
```

```
Sub SetInitCode ( 
	code As String
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

code
:   Type: [SystemAddLanguageSpecificTextSet("LST50E4FE4E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The portion after the first "=" symbol.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_InitCodeAware Interface](T_Grasshopper_Kernel_IGH_InitCodeAware.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)