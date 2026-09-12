# M_Grasshopper_Kernel_GH_DocumentServer_IndexOf

﻿ GH\_DocumentServer.IndexOf Method (GH\_Document)

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
| GH\_DocumentServerAddLanguageSpecificTextSet("LSTDAD08512\_0?cpp=::|nu=.");IndexOf Method (GH\_Document) |

Gets the index of the given document.

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
	GH_Document doc
)
```

```
Public Function IndexOf ( 
	doc As GH_Document
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

doc
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTDAD08512\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Document](T_Grasshopper_Kernel_GH_Document.htm)  
    Document to search for.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
The index of the given document or -1 if the document is not in the global list.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentServer Class](T_Grasshopper_Kernel_GH_DocumentServer.htm)

[IndexOf Overload](Overload_Grasshopper_Kernel_GH_DocumentServer_IndexOf.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)