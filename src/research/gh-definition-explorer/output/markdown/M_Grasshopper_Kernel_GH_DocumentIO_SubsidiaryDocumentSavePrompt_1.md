# M_Grasshopper_Kernel_GH_DocumentIO_SubsidiaryDocumentSavePrompt_1

﻿ GH\_DocumentIO.SubsidiaryDocumentSavePrompt Method (String, Boolean, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentIO Class](../html/T_Grasshopper_Kernel_GH_DocumentIO.htm "GH_DocumentIO Class")

[GH\_DocumentIO Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentIO.htm "GH_DocumentIO Methods")

[SubsidiaryDocumentSavePrompt Method](../html/Overload_Grasshopper_Kernel_GH_DocumentIO_SubsidiaryDocumentSavePrompt.htm "SubsidiaryDocumentSavePrompt Method ")

[SubsidiaryDocumentSavePrompt Method (GH\_Document)](../html/M_Grasshopper_Kernel_GH_DocumentIO_SubsidiaryDocumentSavePrompt.htm "SubsidiaryDocumentSavePrompt Method (GH_Document)")

[SubsidiaryDocumentSavePrompt Method (String, Boolean, Int32)](../html/M_Grasshopper_Kernel_GH_DocumentIO_SubsidiaryDocumentSavePrompt_1.htm "SubsidiaryDocumentSavePrompt Method (String, Boolean, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentIOAddLanguageSpecificTextSet("LST952D3C0D\_0?cpp=::|nu=.");SubsidiaryDocumentSavePrompt Method (String, Boolean, Int32) |

Display a 'stuff has changed do you want to save' message box with Yes/No/Cancel options.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static DialogResult SubsidiaryDocumentSavePrompt(
	string documentName,
	bool modified,
	int modifiedSubsidiaries
)
```

```
Public Shared Function SubsidiaryDocumentSavePrompt ( 
	documentName As String,
	modified As Boolean,
	modifiedSubsidiaries As Integer
) As DialogResult
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

documentName
:   Type: [SystemAddLanguageSpecificTextSet("LST952D3C0D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of top level document.

modified
:   Type: [SystemAddLanguageSpecificTextSet("LST952D3C0D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    Boolean indicating whether top-level document is modified.

modifiedSubsidiaries
:   Type: [SystemAddLanguageSpecificTextSet("LST952D3C0D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Number of modified subsidiary documents.

#### Return Value

Type: [DialogResult](https://docs.microsoft.com/dotnet/api/system.windows.forms.dialogresult)  
Yes, No, Cancel or None state.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentIO Class](T_Grasshopper_Kernel_GH_DocumentIO.htm)

[SubsidiaryDocumentSavePrompt Overload](Overload_Grasshopper_Kernel_GH_DocumentIO_SubsidiaryDocumentSavePrompt.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)