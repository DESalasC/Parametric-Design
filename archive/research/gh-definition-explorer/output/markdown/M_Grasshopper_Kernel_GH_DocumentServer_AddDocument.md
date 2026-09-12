# M_Grasshopper_Kernel_GH_DocumentServer_AddDocument

﻿ GH\_DocumentServer.AddDocument Method (GH\_Document)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentServer Class](../html/T_Grasshopper_Kernel_GH_DocumentServer.htm "GH_DocumentServer Class")

[GH\_DocumentServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentServer.htm "GH_DocumentServer Methods")

[AddDocument Method](../html/Overload_Grasshopper_Kernel_GH_DocumentServer_AddDocument.htm "AddDocument Method ")

[AddDocument Method (GH\_Document)](../html/M_Grasshopper_Kernel_GH_DocumentServer_AddDocument.htm "AddDocument Method (GH_Document)")

[AddDocument Method (GH\_Document, Boolean)](../html/M_Grasshopper_Kernel_GH_DocumentServer_AddDocument_1.htm "AddDocument Method (GH_Document, Boolean)")

[AddDocument Method (String, Boolean)](../html/M_Grasshopper_Kernel_GH_DocumentServer_AddDocument_2.htm "AddDocument Method (String, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentServerAddLanguageSpecificTextSet("LSTFAC11A8A\_0?cpp=::|nu=.");AddDocument Method (GH\_Document) |

Add a new document to the global list. If the document is already registered nothing will happen.
This also applies to a different document which points to the same file path

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void AddDocument(
	GH_Document document
)
```

```
Public Sub AddDocument ( 
	document As GH_Document
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

document
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTFAC11A8A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Document](T_Grasshopper_Kernel_GH_Document.htm)  
    Document to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](https://docs.microsoft.com/dotnet/api/system.argumentnullexception) | Thrown when the document is a null reference. |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown when the document doesn't have top-level rank. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentServer Class](T_Grasshopper_Kernel_GH_DocumentServer.htm)

[AddDocument Overload](Overload_Grasshopper_Kernel_GH_DocumentServer_AddDocument.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)