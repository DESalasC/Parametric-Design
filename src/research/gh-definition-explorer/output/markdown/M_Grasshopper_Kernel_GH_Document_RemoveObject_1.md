# M_Grasshopper_Kernel_GH_Document_RemoveObject_1

﻿ GH\_Document.RemoveObject Method (IGH\_DocumentObject, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[RemoveObject Method](../html/Overload_Grasshopper_Kernel_GH_Document_RemoveObject.htm "RemoveObject Method ")

[RemoveObject Method (IGH\_Attributes, Boolean)](../html/M_Grasshopper_Kernel_GH_Document_RemoveObject.htm "RemoveObject Method (IGH_Attributes, Boolean)")

[RemoveObject Method (IGH\_DocumentObject, Boolean)](../html/M_Grasshopper_Kernel_GH_Document_RemoveObject_1.htm "RemoveObject Method (IGH_DocumentObject, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LST4CF2FE16\_0?cpp=::|nu=.");RemoveObject Method (IGH\_DocumentObject, Boolean) |

Remove the object from the document. This removal is the precursor to object deletion.
Do not call this function if you intend to transfer the object to another GH\_Document.
This method does not add an Undo event, that is the responsibility of the caller.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool RemoveObject(
	IGH_DocumentObject docObject,
	bool update
)
```

```
Public Function RemoveObject ( 
	docObject As IGH_DocumentObject,
	update As Boolean
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

docObject
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST4CF2FE16\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm)  
    Object to remove.

update
:   Type: [SystemAddLanguageSpecificTextSet("LST4CF2FE16\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[RemoveObject Overload](Overload_Grasshopper_Kernel_GH_Document_RemoveObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)