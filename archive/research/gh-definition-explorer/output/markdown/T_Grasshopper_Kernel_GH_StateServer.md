# T_Grasshopper_Kernel_GH_StateServer

﻿ GH\_StateServer Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_StateServer Class](../html/T_Grasshopper_Kernel_GH_StateServer.htm "GH_StateServer Class")

[GH\_StateServer Constructor](../html/M_Grasshopper_Kernel_GH_StateServer__ctor.htm "GH_StateServer Constructor ")

[GH\_StateServer Properties](../html/Properties_T_Grasshopper_Kernel_GH_StateServer.htm "GH_StateServer Properties")

[GH\_StateServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_StateServer.htm "GH_StateServer Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StateServer Class |

Maintains all the recorded states for this document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST165D7409\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [System.Collections.GenericAddLanguageSpecificTextSet("LST165D7409\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST165D7409\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[GH\_State](T_Grasshopper_Kernel_GH_State.htm)AddLanguageSpecificTextSet("LST165D7409\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.KernelAddLanguageSpecificTextSet("LST165D7409\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_StateServer

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_StateServer : List<GH_State>, 
	GH_ISerializable
```

```
Public Class GH_StateServer
	Inherits List(Of GH_State)
	Implements GH_ISerializable
```

AddLanguageTabSet("ID1EBCA");

The GH\_StateServer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_StateServer](M_Grasshopper_Kernel_GH_StateServer__ctor.htm) | Initializes a new instance of the GH\_StateServer class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Names](P_Grasshopper_Kernel_GH_StateServer_Names.htm) | Gets a list of all the state names in this server. |
| Public property | [Owner](P_Grasshopper_Kernel_GH_StateServer_Owner.htm) | Gets the document that owns this server. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [NewStateFromDocument](M_Grasshopper_Kernel_GH_StateServer_NewStateFromDocument.htm) | Displays UI for new state creation. If the user aborts, then null is returned. If the user successfully defines a new state, it is appended to this server. |
| Public method | [Read](M_Grasshopper_Kernel_GH_StateServer_Read.htm) |  |
| Public method | [RemoveState](M_Grasshopper_Kernel_GH_StateServer_RemoveState.htm) | Remove a certain state. This method adds an undo record to the document. |
| Public method | [RestoreState(Int32, Int32AddLanguageSpecificTextSet("LST165D7409\_5?cpp=%");, Int32AddLanguageSpecificTextSet("LST165D7409\_6?cpp=%");)](M_Grasshopper_Kernel_GH_StateServer_RestoreState_1.htm) | Restore a certain state. |
| Public method | [RestoreState(String, Int32AddLanguageSpecificTextSet("LST165D7409\_7?cpp=%");, Int32AddLanguageSpecificTextSet("LST165D7409\_8?cpp=%");)](M_Grasshopper_Kernel_GH_StateServer_RestoreState_2.htm) | Restore a certain state. |
| Public method | [RestoreState(Int32, Boolean, Int32AddLanguageSpecificTextSet("LST165D7409\_9?cpp=%");, Int32AddLanguageSpecificTextSet("LST165D7409\_10?cpp=%");)](M_Grasshopper_Kernel_GH_StateServer_RestoreState.htm) | Restore a certain state. |
| Public method | [Write](M_Grasshopper_Kernel_GH_StateServer_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)