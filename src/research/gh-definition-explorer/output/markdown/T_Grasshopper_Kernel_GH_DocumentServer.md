# T_Grasshopper_Kernel_GH_DocumentServer

﻿ GH\_DocumentServer Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentServer Class](../html/T_Grasshopper_Kernel_GH_DocumentServer.htm "GH_DocumentServer Class")

[GH\_DocumentServer Constructor](../html/M_Grasshopper_Kernel_GH_DocumentServer__ctor.htm "GH_DocumentServer Constructor ")

[GH\_DocumentServer Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocumentServer.htm "GH_DocumentServer Properties")

[GH\_DocumentServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentServer.htm "GH_DocumentServer Methods")

[GH\_DocumentServer Events](../html/Events_T_Grasshopper_Kernel_GH_DocumentServer.htm "GH_DocumentServer Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentServer Class |

Manages and maintains a collection of GH\_Documents.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST1F2D8CC4\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST1F2D8CC4\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocumentServer

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_DocumentServer : IEnumerable<GH_Document>
```

```
Public NotInheritable Class GH_DocumentServer
	Implements IEnumerable(Of GH_Document)
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocumentServer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DocumentServer](M_Grasshopper_Kernel_GH_DocumentServer__ctor.htm) | Initializes a new instance of the GH\_DocumentServer class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Document](P_Grasshopper_Kernel_GH_DocumentServer_Document.htm) | Gets the document at the given index. |
| Public property | [DocumentCount](P_Grasshopper_Kernel_GH_DocumentServer_DocumentCount.htm) | Gets the number of documents stored in the global list. |
| Public property | [DocumentNames](P_Grasshopper_Kernel_GH_DocumentServer_DocumentNames.htm) | Gets a string collection containing all the names of the documents in the global list. |
| Public property | [ModifiedDocumentCount](P_Grasshopper_Kernel_GH_DocumentServer_ModifiedDocumentCount.htm) | Gets the total number of modified (unsaved) documents. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddDocument(GH\_Document)](M_Grasshopper_Kernel_GH_DocumentServer_AddDocument.htm) | Add a new document to the global list. If the document is already registered nothing will happen. This also applies to a different document which points to the same file path |
| Public method | [AddDocument(GH\_Document, BooleanAddLanguageSpecificTextSet("LST1F2D8CC4\_2?cpp=%");)](M_Grasshopper_Kernel_GH_DocumentServer_AddDocument_1.htm) | Add a new document to the global list. If the document is already registered nothing will happen. This also applies to a different document which points to the same file path |
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

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [DocumentAdded](E_Grasshopper_Kernel_GH_DocumentServer_DocumentAdded.htm) |  |
| Public event | [DocumentRemoved](E_Grasshopper_Kernel_GH_DocumentServer_DocumentRemoved.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)