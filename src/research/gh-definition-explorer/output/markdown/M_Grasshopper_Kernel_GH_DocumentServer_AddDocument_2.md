# M_Grasshopper_Kernel_GH_DocumentServer_AddDocument_2

﻿ GH\_DocumentServer.AddDocument Method (String, Boolean)

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
| GH\_DocumentServerAddLanguageSpecificTextSet("LSTCA4F90A5\_0?cpp=::|nu=.");AddDocument Method (String, Boolean) |

Add a new document to the global list. If there already is a document with the
given path, it will be made active.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_Document AddDocument(
	string filepath,
	bool makeActive
)
```

```
Public Function AddDocument ( 
	filepath As String,
	makeActive As Boolean
) As GH_Document
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

filepath
:   Type: [SystemAddLanguageSpecificTextSet("LSTCA4F90A5\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Filepath to document.

makeActive
:   Type: [SystemAddLanguageSpecificTextSet("LSTCA4F90A5\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, the document will be loaded into the main canvas.

#### Return Value

Type: [GH\_Document](T_Grasshopper_Kernel_GH_Document.htm)  
The document that was added or activated, or null on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentServer Class](T_Grasshopper_Kernel_GH_DocumentServer.htm)

[AddDocument Overload](Overload_Grasshopper_Kernel_GH_DocumentServer_AddDocument.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)