# Methods_T_Grasshopper_Kernel_GH_DocumentIO

﻿ GH\_DocumentIO Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentIO Class](../html/T_Grasshopper_Kernel_GH_DocumentIO.htm "GH_DocumentIO Class")

[GH\_DocumentIO Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentIO.htm "GH_DocumentIO Methods")

[ClearClipboard Method](../html/M_Grasshopper_Kernel_GH_DocumentIO_ClearClipboard.htm "ClearClipboard Method ")

[Copy Method](../html/Overload_Grasshopper_Kernel_GH_DocumentIO_Copy.htm "Copy Method ")

[GetDocumentIcon Method](../html/M_Grasshopper_Kernel_GH_DocumentIO_GetDocumentIcon.htm "GetDocumentIcon Method ")

[GetDocumentThumbnail Method](../html/M_Grasshopper_Kernel_GH_DocumentIO_GetDocumentThumbnail.htm "GetDocumentThumbnail Method ")

[Open Method](../html/Overload_Grasshopper_Kernel_GH_DocumentIO_Open.htm "Open Method ")

[OpenDocumentDialog Method](../html/M_Grasshopper_Kernel_GH_DocumentIO_OpenDocumentDialog.htm "OpenDocumentDialog Method ")

[Paste Method](../html/M_Grasshopper_Kernel_GH_DocumentIO_Paste.htm "Paste Method ")

[Save Method](../html/M_Grasshopper_Kernel_GH_DocumentIO_Save.htm "Save Method ")

[SaveAs Method](../html/M_Grasshopper_Kernel_GH_DocumentIO_SaveAs.htm "SaveAs Method ")

[SaveAsCopyDocumentDialog Method](../html/M_Grasshopper_Kernel_GH_DocumentIO_SaveAsCopyDocumentDialog.htm "SaveAsCopyDocumentDialog Method ")

[SaveAsDocumentDialog Method](../html/M_Grasshopper_Kernel_GH_DocumentIO_SaveAsDocumentDialog.htm "SaveAsDocumentDialog Method ")

[SaveBackup Method](../html/M_Grasshopper_Kernel_GH_DocumentIO_SaveBackup.htm "SaveBackup Method ")

[SaveDocumentDialog Method](../html/M_Grasshopper_Kernel_GH_DocumentIO_SaveDocumentDialog.htm "SaveDocumentDialog Method ")

[SaveQuiet Method](../html/M_Grasshopper_Kernel_GH_DocumentIO_SaveQuiet.htm "SaveQuiet Method ")

[ShowOverwriteDialog Method](../html/Overload_Grasshopper_Kernel_GH_DocumentIO_ShowOverwriteDialog.htm "ShowOverwriteDialog Method ")

[SubsidiaryDocumentSavePrompt Method](../html/Overload_Grasshopper_Kernel_GH_DocumentIO_SubsidiaryDocumentSavePrompt.htm "SubsidiaryDocumentSavePrompt Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentIO Methods |

The [GH\_DocumentIO](T_Grasshopper_Kernel_GH_DocumentIO.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [ClearClipboard](M_Grasshopper_Kernel_GH_DocumentIO_ClearClipboard.htm) | Clear the Clipboard Text content. This function wipes both the Text and UnicodeText clipboard fields. |
| Public method | [Copy(GH\_ClipboardType)](M_Grasshopper_Kernel_GH_DocumentIO_Copy.htm) | Copy the internal document into the clipboard. |
| Public method | [Copy(GH\_ClipboardType, Boolean)](M_Grasshopper_Kernel_GH_DocumentIO_Copy_1.htm) | Copy the internal document into the clipboard. |
| Public method | [Copy(GH\_ClipboardType, IEnumerableAddLanguageSpecificTextSet("LSTDE27732B\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GuidAddLanguageSpecificTextSet("LSTDE27732B\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_DocumentIO_Copy_2.htm) | Copy the specified objects in the internal document into the clipboard. |
| Public methodStatic member | [GetDocumentIcon](M_Grasshopper_Kernel_GH_DocumentIO_GetDocumentIcon.htm) | Try and extract the icon image of a document. Not all gh/ghx files contain an icon so this function may return null. The document itself is not loaded and rendered, so the icon really has to be part of the file already. |
| Public methodStatic member | [GetDocumentThumbnail](M_Grasshopper_Kernel_GH_DocumentIO_GetDocumentThumbnail.htm) | Try and extract the preview image of a document. Not all gh/ghx files contain a thumbnail so this function may return null. The document itself is not loaded and rendered, so the thumbnail really has to be part of the file already. |
| Public method | [OpenAddLanguageSpecificTextSet("LSTDE27732B\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_DocumentIO_Open.htm) | Perform a default Open operation and store the result as the internal document. |
| Public method | [Open(String)](M_Grasshopper_Kernel_GH_DocumentIO_Open_1.htm) | Open the file at the given location. |
| Public method | [OpenDocumentDialog](M_Grasshopper_Kernel_GH_DocumentIO_OpenDocumentDialog.htm) | Display the Open GH/GHX dialog. |
| Public method | [Paste](M_Grasshopper_Kernel_GH_DocumentIO_Paste.htm) | Deserialize a Grasshopper document from the clipboard. On success, the internal document of this GH\_DocumentIO instance will be set. |
| Public method | [Save](M_Grasshopper_Kernel_GH_DocumentIO_Save.htm) | Perform a default Save operation on the internal document. |
| Public method | [SaveAs](M_Grasshopper_Kernel_GH_DocumentIO_SaveAs.htm) | Perform a default Save As operation on the internal document. |
| Public method | [SaveAsCopyDocumentDialog](M_Grasshopper_Kernel_GH_DocumentIO_SaveAsCopyDocumentDialog.htm) | Display the Save As Copy GH/GHX dialog. |
| Public method | [SaveAsDocumentDialog](M_Grasshopper_Kernel_GH_DocumentIO_SaveAsDocumentDialog.htm) | Display the Save As GH/GHX dialog. |
| Public method | [SaveBackup](M_Grasshopper_Kernel_GH_DocumentIO_SaveBackup.htm) | Save a time-stamped copy of the current file. |
| Public method | [SaveDocumentDialog](M_Grasshopper_Kernel_GH_DocumentIO_SaveDocumentDialog.htm) | Display the Save GH/GHX dialog. |
| Public method | [SaveQuiet](M_Grasshopper_Kernel_GH_DocumentIO_SaveQuiet.htm) | Quietly save a file to a given location. |
| Public methodStatic member | [ShowOverwriteDialog(String)](M_Grasshopper_Kernel_GH_DocumentIO_ShowOverwriteDialog.htm) |  |
| Public methodStatic member | [ShowOverwriteDialog(String, DateTime, DateTime)](M_Grasshopper_Kernel_GH_DocumentIO_ShowOverwriteDialog_1.htm) |  |
| Public methodStatic member | [SubsidiaryDocumentSavePrompt(GH\_Document)](M_Grasshopper_Kernel_GH_DocumentIO_SubsidiaryDocumentSavePrompt.htm) | Display a 'stuff has changed do you want to save' message box with Yes/No/Cancel options. |
| Public methodStatic member | [SubsidiaryDocumentSavePrompt(String, Boolean, Int32)](M_Grasshopper_Kernel_GH_DocumentIO_SubsidiaryDocumentSavePrompt_1.htm) | Display a 'stuff has changed do you want to save' message box with Yes/No/Cancel options. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentIO Class](T_Grasshopper_Kernel_GH_DocumentIO.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)