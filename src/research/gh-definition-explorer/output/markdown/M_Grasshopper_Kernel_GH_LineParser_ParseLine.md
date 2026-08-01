# M_Grasshopper_Kernel_GH_LineParser_ParseLine

﻿ GH\_LineParser.ParseLine Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_LineParser Class](../html/T_Grasshopper_Kernel_GH_LineParser.htm "GH_LineParser Class")

[GH\_LineParser Methods](../html/Methods_T_Grasshopper_Kernel_GH_LineParser.htm "GH_LineParser Methods")

[ParseLine Method](../html/M_Grasshopper_Kernel_GH_LineParser_ParseLine.htm "ParseLine Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_LineParserAddLanguageSpecificTextSet("LST856B5207\_0?cpp=::|nu=.");ParseLine Method |

Parse a line of text and convert it to custom data.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract Object ParseLine(
	string line,
	ref GH_LineParserAction action
)
```

```
Public MustOverride Function ParseLine ( 
	line As String,
	ByRef action As GH_LineParserAction
) As Object
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

line
:   Type: [SystemAddLanguageSpecificTextSet("LST856B5207\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Line to parse.

action
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST856B5207\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_LineParserAction](T_Grasshopper_Kernel_GH_LineParserAction.htm)AddLanguageSpecificTextSet("LST856B5207\_3?cpp=%");  
    Set the action to take after this function returns. The default is Include.

#### Return Value

Type: [Object](https://docs.microsoft.com/dotnet/api/system.object)  
The data represented by the line.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_LineParser Class](T_Grasshopper_Kernel_GH_LineParser.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)