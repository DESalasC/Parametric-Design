# Overload_Grasshopper_Kernel_GH_Document_RemoveObject

﻿ GH\_Document.RemoveObject Method 

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
| GH\_DocumentAddLanguageSpecificTextSet("LST2307F496\_0?cpp=::|nu=.");RemoveObject Method |

![](../icons/SectionExpanded.png)Overload List

|  | Name | Description |
| --- | --- | --- |
| Public method | [RemoveObject(IGH\_Attributes, Boolean)](M_Grasshopper_Kernel_GH_Document_RemoveObject.htm) | Remove the top-level object in the attribute tree from the document. This method does not add an Undo event, that is the responsibility of the caller. |
| Public method | [RemoveObject(IGH\_DocumentObject, Boolean)](M_Grasshopper_Kernel_GH_Document_RemoveObject_1.htm) | Remove the object from the document. This removal is the precursor to object deletion. Do not call this function if you intend to transfer the object to another GH\_Document. This method does not add an Undo event, that is the responsibility of the caller. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)