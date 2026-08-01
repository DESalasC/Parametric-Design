# T_Grasshopper_Kernel_GH_DocumentIO

﻿ GH\_DocumentIO Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentIO Class](../html/T_Grasshopper_Kernel_GH_DocumentIO.htm "GH_DocumentIO Class")

[GH\_DocumentIO Constructor](../html/Overload_Grasshopper_Kernel_GH_DocumentIO__ctor.htm "GH_DocumentIO Constructor ")

[GH\_DocumentIO Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocumentIO.htm "GH_DocumentIO Properties")

[GH\_DocumentIO Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentIO.htm "GH_DocumentIO Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentIO Class |

Provides basic IO operations for GH\_Documents.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTD6852543\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTD6852543\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocumentIO

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_DocumentIO
```

```
Public NotInheritable Class GH_DocumentIO
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocumentIO type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DocumentIOAddLanguageSpecificTextSet("LSTD6852543\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_DocumentIO__ctor.htm) | Create a new instance of GH\_DocumentIO without an internal document. |
| Public method | [GH\_DocumentIO(GH\_Document)](M_Grasshopper_Kernel_GH_DocumentIO__ctor_1.htm) | Create a new instance of GH\_DocumentIO with an internal document. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public propertyStatic member | [DisableOverwriteProtection](P_Grasshopper_Kernel_GH_DocumentIO_DisableOverwriteProtection.htm) | Gets or sets whether the file overwrite protection dialog ought to be shown during risky saves. |
| Public property | [Document](P_Grasshopper_Kernel_GH_DocumentIO_Document.htm) | Gets or sets the internal document. |
| Public property | [IsDocument](P_Grasshopper_Kernel_GH_DocumentIO_IsDocument.htm) | Gets a value indicating whether or not this instance of GH\_DocumentIO contains an internal document. |
| Public property | [LocalClipboardContent](P_Grasshopper_Kernel_GH_DocumentIO_LocalClipboardContent.htm) | Gets the contents of the local clipboard. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [ClearClipboard](M_Grasshopper_Kernel_GH_DocumentIO_ClearClipboard.htm) | Clear the Clipboard Text content. This function wipes both the Text and UnicodeText clipboard fields. |
| Public method | [Copy(GH\_ClipboardType)](M_Grasshopper_Kernel_GH_DocumentIO_Copy.htm) | Copy the internal document into the clipboard. |
| Public method | [Copy(GH\_ClipboardType, Boolean)](M_Grasshopper_Kernel_GH_DocumentIO_Copy_1.htm) | Copy the internal document into the clipboard. |
| Public method | [Copy(GH\_ClipboardType, IEnumerableAddLanguageSpecificTextSet("LSTD6852543\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GuidAddLanguageSpecificTextSet("LSTD6852543\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_DocumentIO_Copy_2.htm) | Copy the specified objects in the internal document into the clipboard. |
| Public methodStatic member | [GetDocumentIcon](M_Grasshopper_Kernel_GH_DocumentIO_GetDocumentIcon.htm) | Try and extract the icon image of a document. Not all gh/ghx files contain an icon so this function may return null. The document itself is not loaded and rendered, so the icon really has to be part of the file already. |
| Public methodStatic member | [GetDocumentThumbnail](M_Grasshopper_Kernel_GH_DocumentIO_GetDocumentThumbnail.htm) | Try and extract the preview image of a document. Not all gh/ghx files contain a thumbnail so this function may return null. The document itself is not loaded and rendered, so the thumbnail really has to be part of the file already. |
| Public method | [OpenAddLanguageSpecificTextSet("LSTD6852543\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_DocumentIO_Open.htm) | Perform a default Open operation and store the result as the internal document. |
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

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)