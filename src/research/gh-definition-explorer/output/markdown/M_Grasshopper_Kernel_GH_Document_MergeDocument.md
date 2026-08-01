# M_Grasshopper_Kernel_GH_Document_MergeDocument

﻿ GH\_Document.MergeDocument Method (GH\_Document)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[MergeDocument Method](../html/Overload_Grasshopper_Kernel_GH_Document_MergeDocument.htm "MergeDocument Method ")

[MergeDocument Method (GH\_Document)](../html/M_Grasshopper_Kernel_GH_Document_MergeDocument.htm "MergeDocument Method (GH_Document)")

[MergeDocument Method (GH\_Document, Boolean)](../html/M_Grasshopper_Kernel_GH_Document_MergeDocument_1.htm "MergeDocument Method (GH_Document, Boolean)")

[MergeDocument Method (GH\_Document, Boolean, Boolean)](../html/M_Grasshopper_Kernel_GH_Document_MergeDocument_2.htm "MergeDocument Method (GH_Document, Boolean, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LSTF3ACCC47\_0?cpp=::|nu=.");MergeDocument Method (GH\_Document) |

Hoist all objects from another document into this one.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool MergeDocument(
	GH_Document other
)
```

```
Public Function MergeDocument ( 
	other As GH_Document
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

other
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTF3ACCC47\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Document](T_Grasshopper_Kernel_GH_Document.htm)  
    The other document. Cannot be Null or

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)Remarks

The objects will be moved, not copied. The other document ends up being empty since objects can only belong to one document at a time.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[MergeDocument Overload](Overload_Grasshopper_Kernel_GH_Document_MergeDocument.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)