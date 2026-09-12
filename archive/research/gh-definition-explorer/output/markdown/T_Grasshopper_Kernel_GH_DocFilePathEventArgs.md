# T_Grasshopper_Kernel_GH_DocFilePathEventArgs

﻿ GH\_DocFilePathEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocFilePathEventArgs Class](../html/T_Grasshopper_Kernel_GH_DocFilePathEventArgs.htm "GH_DocFilePathEventArgs Class")

[GH\_DocFilePathEventArgs Constructor](../html/M_Grasshopper_Kernel_GH_DocFilePathEventArgs__ctor.htm "GH_DocFilePathEventArgs Constructor ")

[GH\_DocFilePathEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocFilePathEventArgs.htm "GH_DocFilePathEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocFilePathEventArgs Class |

These arguments are passed along with FilePathChanged events on GH\_Document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST4E43747F\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST4E43747F\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LST4E43747F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocFilePathEventArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DocFilePathEventArgs : EventArgs
```

```
Public Class GH_DocFilePathEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocFilePathEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DocFilePathEventArgs](M_Grasshopper_Kernel_GH_DocFilePathEventArgs__ctor.htm) | Create a new instance of the GH\_DocFilePathEventArgs class. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Document](P_Grasshopper_Kernel_GH_DocFilePathEventArgs_Document.htm) | Gets the document that raised this event. |
| Public property | [NewFilePath](P_Grasshopper_Kernel_GH_DocFilePathEventArgs_NewFilePath.htm) | Gets the new filepath, the one currently assigned to this document. |
| Public property | [OldFilePath](P_Grasshopper_Kernel_GH_DocFilePathEventArgs_OldFilePath.htm) | Gets the old filepath, prior to the change that triggered this event. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)