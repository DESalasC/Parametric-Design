# Methods_T_Grasshopper_Kernel_GH_DocumentServer

﻿ GH\_DocumentServer Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentServer Class](../html/T_Grasshopper_Kernel_GH_DocumentServer.htm "GH_DocumentServer Class")

[GH\_DocumentServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentServer.htm "GH_DocumentServer Methods")

[AddDocument Method](../html/Overload_Grasshopper_Kernel_GH_DocumentServer_AddDocument.htm "AddDocument Method ")

[AddNewDocument Method](../html/M_Grasshopper_Kernel_GH_DocumentServer_AddNewDocument.htm "AddNewDocument Method ")

[Contains Method](../html/M_Grasshopper_Kernel_GH_DocumentServer_Contains.htm "Contains Method ")

[GetEnumerator Method](../html/M_Grasshopper_Kernel_GH_DocumentServer_GetEnumerator.htm "GetEnumerator Method ")

[GetEnumerator\_Generic Method](../html/M_Grasshopper_Kernel_GH_DocumentServer_GetEnumerator_Generic.htm "GetEnumerator_Generic Method ")

[IndexOf Method](../html/Overload_Grasshopper_Kernel_GH_DocumentServer_IndexOf.htm "IndexOf Method ")

[IndexOfAutoSave Method](../html/M_Grasshopper_Kernel_GH_DocumentServer_IndexOfAutoSave.htm "IndexOfAutoSave Method ")

[NextAvailableDocument Method](../html/M_Grasshopper_Kernel_GH_DocumentServer_NextAvailableDocument.htm "NextAvailableDocument Method ")

[PromoteDocument Method](../html/M_Grasshopper_Kernel_GH_DocumentServer_PromoteDocument.htm "PromoteDocument Method ")

[RemoveAllDocuments Method](../html/M_Grasshopper_Kernel_GH_DocumentServer_RemoveAllDocuments.htm "RemoveAllDocuments Method ")

[RemoveDocument Method](../html/M_Grasshopper_Kernel_GH_DocumentServer_RemoveDocument.htm "RemoveDocument Method ")

[SafeRemoveDocument Method](../html/M_Grasshopper_Kernel_GH_DocumentServer_SafeRemoveDocument.htm "SafeRemoveDocument Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentServer Methods |

The [GH\_DocumentServer](T_Grasshopper_Kernel_GH_DocumentServer.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddDocument(GH\_Document)](M_Grasshopper_Kernel_GH_DocumentServer_AddDocument.htm) | Add a new document to the global list. If the document is already registered nothing will happen. This also applies to a different document which points to the same file path |
| Public method | [AddDocument(GH\_Document, BooleanAddLanguageSpecificTextSet("LST653A3D22\_0?cpp=%");)](M_Grasshopper_Kernel_GH_DocumentServer_AddDocument_1.htm) | Add a new document to the global list. If the document is already registered nothing will happen. This also applies to a different document which points to the same file path |
| Public method | [AddDocument(String, Boolean)](M_Grasshopper_Kernel_GH_DocumentServer_AddDocument_2.htm) | Add a new document to the global list. If there already is a document with the given path, it will be made active. |
| Public method | [AddNewDocument](M_Grasshopper_Kernel_GH_DocumentServer_AddNewDocument.htm) | Adds a new document to the global list. If a template file has been set, this document will be based on the template. |
| Public method | [Contains](M_Grasshopper_Kernel_GH_DocumentServer_Contains.htm) | Gets a value indicating whether or not the given document is inside the list. |
| Public method | [GetEnumerator](M_Grasshopper_Kernel_GH_DocumentServer_GetEnumerator.htm) |  |
| Public method | [GetEnumerator\_Generic](M_Grasshopper_Kernel_GH_DocumentServer_GetEnumerator_Generic.htm) |  |
| Public method | [IndexOf(GH\_Document)](M_Grasshopper_Kernel_GH_DocumentServer_IndexOf.htm) | Gets the index of the given document. |
| Public method | [IndexOf(String)](M_Grasshopper_Kernel_GH_DocumentServer_IndexOf_1.htm) | Gets the index of the document that matches the filepath. |
| Public method | [IndexOfAutoSave](M_Grasshopper_Kernel_GH_DocumentServer_IndexOfAutoSave.htm) | Gets the document index that is associated with the specified autosave location. |
| Public method | [NextAvailableDocument](M_Grasshopper_Kernel_GH_DocumentServer_NextAvailableDocument.htm) | Gets the most important, non-active document. |
| Public method | [PromoteDocument](M_Grasshopper_Kernel_GH_DocumentServer_PromoteDocument.htm) | Push a document to the top of the list, meaning it will be first in line when a new default document needs to be selected. |
| Public method | [RemoveAllDocuments](M_Grasshopper_Kernel_GH_DocumentServer_RemoveAllDocuments.htm) | Remove all documents in the global list. |
| Public method | [RemoveDocument](M_Grasshopper_Kernel_GH_DocumentServer_RemoveDocument.htm) | Removes a specific document from the global list. If the document isn't registered nothing will happen. If the document is owned by an IGH\_DocumentOwner, the owner will be informed of the removal. |
| Public method | [SafeRemoveDocument](M_Grasshopper_Kernel_GH_DocumentServer_SafeRemoveDocument.htm) | Remove a document correctly from the server. This method shows user-interface prompts if there is unsaved data and will also save if needed. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentServer Class](T_Grasshopper_Kernel_GH_DocumentServer.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)