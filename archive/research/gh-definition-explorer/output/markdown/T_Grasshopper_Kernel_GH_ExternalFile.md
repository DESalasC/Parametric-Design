# T_Grasshopper_Kernel_GH_ExternalFile

﻿ GH\_ExternalFile Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ExternalFile Class](../html/T_Grasshopper_Kernel_GH_ExternalFile.htm "GH_ExternalFile Class")

[GH\_ExternalFile Constructor](../html/M_Grasshopper_Kernel_GH_ExternalFile__ctor.htm "GH_ExternalFile Constructor ")

[GH\_ExternalFile Properties](../html/Properties_T_Grasshopper_Kernel_GH_ExternalFile.htm "GH_ExternalFile Properties")

[GH\_ExternalFile Methods](../html/Methods_T_Grasshopper_Kernel_GH_ExternalFile.htm "GH_ExternalFile Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ExternalFile Class |

Represents information about external files to be loaded.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTF4CC04F8\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTF4CC04F8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ExternalFile

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ExternalFile
```

```
Public Class GH_ExternalFile
```

AddLanguageTabSet("ID1EBCA");

The GH\_ExternalFile type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ExternalFile](M_Grasshopper_Kernel_GH_ExternalFile__ctor.htm) | Create a new instance of the file info class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [FileHash](P_Grasshopper_Kernel_GH_ExternalFile_FileHash.htm) | Gets the file hash. |
| Public property | [FileName](P_Grasshopper_Kernel_GH_ExternalFile_FileName.htm) | Gets the file name (without the extension). |
| Public property | [FilePath](P_Grasshopper_Kernel_GH_ExternalFile_FilePath.htm) | Gets the file path. |
| Public property | [FileSize](P_Grasshopper_Kernel_GH_ExternalFile_FileSize.htm) | Gets the file size (in bytes). |
| Public property | [FileType](P_Grasshopper_Kernel_GH_ExternalFile_FileType.htm) | Gets the file type as indicated by the extension. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [IsIdenticalTo](M_Grasshopper_Kernel_GH_ExternalFile_IsIdenticalTo.htm) | Compares two files for content. If the size and the hash or the other file are equal to this one, the files are considered identical. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)