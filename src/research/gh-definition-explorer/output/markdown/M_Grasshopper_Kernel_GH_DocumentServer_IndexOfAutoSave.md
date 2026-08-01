# M_Grasshopper_Kernel_GH_DocumentServer_IndexOfAutoSave

﻿ GH\_DocumentServer.IndexOfAutoSave Method 

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
| GH\_DocumentServerAddLanguageSpecificTextSet("LST35F1E03B\_0?cpp=::|nu=.");IndexOfAutoSave Method |

Gets the document index that is associated with the specified autosave location.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int IndexOfAutoSave(
	string autoSavePath
)
```

```
Public Function IndexOfAutoSave ( 
	autoSavePath As String
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

autoSavePath
:   Type: [SystemAddLanguageSpecificTextSet("LST35F1E03B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The full path (directory, filename and extension) of the autosave file to test against.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
The index of the document that matches the given autosave path or -1 if no document match is found.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentServer Class](T_Grasshopper_Kernel_GH_DocumentServer.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)