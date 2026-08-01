# M_Grasshopper_Kernel_GDL_GH_GDLParser_ParseGDL

﻿ GH\_GDLParser.ParseGDL Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.GDL](../html/N_Grasshopper_Kernel_GDL.htm "Grasshopper.Kernel.GDL")

[GH\_GDLParser Class](../html/T_Grasshopper_Kernel_GDL_GH_GDLParser.htm "GH_GDLParser Class")

[GH\_GDLParser Methods](../html/Methods_T_Grasshopper_Kernel_GDL_GH_GDLParser.htm "GH_GDLParser Methods")

[ParseGDL Method](../html/M_Grasshopper_Kernel_GDL_GH_GDLParser_ParseGDL.htm "ParseGDL Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GDLParserAddLanguageSpecificTextSet("LST420B3EB0\_0?cpp=::|nu=.");ParseGDL Method |

Convert a GDL text into an actual document.

**Namespace:**
 [Grasshopper.Kernel.GDL](N_Grasshopper_Kernel_GDL.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_Document ParseGDL(
	string[] lines,
	out string[] messages
)
```

```
Public Shared Function ParseGDL ( 
	lines As String(),
	<OutAttribute> ByRef messages As String()
) As GH_Document
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

lines
:   Type: AddLanguageSpecificTextSet("LST420B3EB0\_1?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LST420B3EB0\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LST420B3EB0\_3?cpp=&gt;|vb=()|nu=[]");  
    Lines to parse.

messages
:   Type: AddLanguageSpecificTextSet("LST420B3EB0\_4?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LST420B3EB0\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LST420B3EB0\_6?cpp=&gt;|vb=()|nu=[]");AddLanguageSpecificTextSet("LST420B3EB0\_7?cpp=%");  
    Messages encountered.

#### Return Value

Type: [GH\_Document](T_Grasshopper_Kernel_GH_Document.htm)  
A document on success or null on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GDLParser Class](T_Grasshopper_Kernel_GDL_GH_GDLParser.htm)

[Grasshopper.Kernel.GDL Namespace](N_Grasshopper_Kernel_GDL.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)