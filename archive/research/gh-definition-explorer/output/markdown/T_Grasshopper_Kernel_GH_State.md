# T_Grasshopper_Kernel_GH_State

﻿ GH\_State Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_State Class](../html/T_Grasshopper_Kernel_GH_State.htm "GH_State Class")

[GH\_State Constructor](../html/Overload_Grasshopper_Kernel_GH_State__ctor.htm "GH_State Constructor ")

[GH\_State Properties](../html/Properties_T_Grasshopper_Kernel_GH_State.htm "GH_State Properties")

[GH\_State Methods](../html/Methods_T_Grasshopper_Kernel_GH_State.htm "GH_State Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_State Class |

Represents a single recorded document state.
A state contains values for an arbitrary set of objects inside the document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST97D6D302\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST97D6D302\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_State

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_State : GH_ISerializable
```

```
Public Class GH_State
	Implements GH_ISerializable
```

AddLanguageTabSet("ID1EBCA");

The GH\_State type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_StateAddLanguageSpecificTextSet("LST97D6D302\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_State__ctor.htm) | Initializes a new instance of the GH\_State class |
| Public method | [GH\_State(GH\_State)](M_Grasshopper_Kernel_GH_State__ctor_1.htm) | Initializes a new instance of the GH\_State class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [DataAddLanguageSpecificTextSet("LST97D6D302\_3?cs=[|vb=(|cpp=[|nu=(|fs= ");GuidAddLanguageSpecificTextSet("LST97D6D302\_4?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_GH_State_Data.htm) | Gets the state data stored under the specified ID |
| Public property | [DataAddLanguageSpecificTextSet("LST97D6D302\_5?cs=[|vb=(|cpp=[|nu=(|fs= ");Int32AddLanguageSpecificTextSet("LST97D6D302\_6?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_GH_State_Data_1.htm) | Gets the state data stored under the specified index |
| Public property | [LastModified](P_Grasshopper_Kernel_GH_State_LastModified.htm) | Gets the date at which this state was last modified. |
| Public property | [Name](P_Grasshopper_Kernel_GH_State_Name.htm) | Gets or sets the name of this state. |
| Public property | [StateCount](P_Grasshopper_Kernel_GH_State_StateCount.htm) | Gets the number of items stored in the state database. |
| Public property | [StateData](P_Grasshopper_Kernel_GH_State_StateData.htm) | Gets a pointer to the internal database of states. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddStateObject](M_Grasshopper_Kernel_GH_State_AddStateObject.htm) | Append a new object to the database. |
| Public method | [ClearStates](M_Grasshopper_Kernel_GH_State_ClearStates.htm) | Removes all items from the state database. |
| Public method | [CreateStateFromDocument](M_Grasshopper_Kernel_GH_State_CreateStateFromDocument.htm) | Creates a state database from a document. |
| Public method | [Read](M_Grasshopper_Kernel_GH_State_Read.htm) |  |
| Public method | [RemoveStateObject](M_Grasshopper_Kernel_GH_State_RemoveStateObject.htm) | Remove an object from the database. |
| Public method | [Write](M_Grasshopper_Kernel_GH_State_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)