# M_Grasshopper_Kernel_GH_DocumentIO_GetDocumentThumbnail

﻿ GH\_DocumentIO.GetDocumentThumbnail Method 

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
| GH\_DocumentIOAddLanguageSpecificTextSet("LSTA38EFEAD\_0?cpp=::|nu=.");GetDocumentThumbnail Method |

Try and extract the preview image of a document. Not all gh/ghx files contain a thumbnail
so this function may return null. The document itself is not loaded and rendered, so the
thumbnail really has to be part of the file already.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static Bitmap GetDocumentThumbnail(
	string filePath
)
```

```
Public Shared Function GetDocumentThumbnail ( 
	filePath As String
) As Bitmap
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

filePath
:   Type: [SystemAddLanguageSpecificTextSet("LSTA38EFEAD\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Filepath to examine.

#### Return Value

Type: [Bitmap](https://docs.microsoft.com/dotnet/api/system.drawing.bitmap)  
A preview bitmap on success or null on failure.
Caller is responsible for disposing of the image.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentIO Class](T_Grasshopper_Kernel_GH_DocumentIO.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)