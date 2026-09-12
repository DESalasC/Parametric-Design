# M_Grasshopper_Kernel_GH_DocumentServer_IndexOf_1

﻿ GH\_DocumentServer.IndexOf Method (String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentServer Class](../html/T_Grasshopper_Kernel_GH_DocumentServer.htm "GH_DocumentServer Class")

[GH\_DocumentServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentServer.htm "GH_DocumentServer Methods")

[IndexOf Method](../html/Overload_Grasshopper_Kernel_GH_DocumentServer_IndexOf.htm "IndexOf Method ")

[IndexOf Method (GH\_Document)](../html/M_Grasshopper_Kernel_GH_DocumentServer_IndexOf.htm "IndexOf Method (GH_Document)")

[IndexOf Method (String)](../html/M_Grasshopper_Kernel_GH_DocumentServer_IndexOf_1.htm "IndexOf Method (String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentServerAddLanguageSpecificTextSet("LSTB610D1CC\_0?cpp=::|nu=.");IndexOf Method (String) |

Gets the index of the document that matches the filepath.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int IndexOf(
	string filepath
)
```

```
Public Function IndexOf ( 
	filepath As String
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

filepath
:   Type: [SystemAddLanguageSpecificTextSet("LSTB610D1CC\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    File path URI to match.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
The index of the document that matches the given path or -1 if no document match is found.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentServer Class](T_Grasshopper_Kernel_GH_DocumentServer.htm)

[IndexOf Overload](Overload_Grasshopper_Kernel_GH_DocumentServer_IndexOf.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)