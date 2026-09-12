# T_Grasshopper_Kernel_GH_DocumentTree

﻿ GH\_DocumentTree Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentTree Class](../html/T_Grasshopper_Kernel_GH_DocumentTree.htm "GH_DocumentTree Class")

[GH\_DocumentTree Constructor](../html/M_Grasshopper_Kernel_GH_DocumentTree__ctor.htm "GH_DocumentTree Constructor ")

[GH\_DocumentTree Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocumentTree.htm "GH_DocumentTree Properties")

[GH\_DocumentTree Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentTree.htm "GH_DocumentTree Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentTree Class |

Represents a hierarchical tree of documents that are subsidiary to one another.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST59713422\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST59713422\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocumentTree

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DocumentTree : IGH_DebugDescription
```

```
Public Class GH_DocumentTree
	Implements IGH_DebugDescription
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocumentTree type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DocumentTree](M_Grasshopper_Kernel_GH_DocumentTree__ctor.htm) | Create a new document tree. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [FlatCollection](P_Grasshopper_Kernel_GH_DocumentTree_FlatCollection.htm) | Gets a flat collection of all documents. The most subsidiary documents are at the start of the collection. |
| Public property | [Root](P_Grasshopper_Kernel_GH_DocumentTree_Root.htm) | Gets the root node for this document. |
| Public property | [RootDocument](P_Grasshopper_Kernel_GH_DocumentTree_RootDocument.htm) | Gets the document inside the root node of this tree. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendToDebugLog](M_Grasshopper_Kernel_GH_DocumentTree_AppendToDebugLog.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)