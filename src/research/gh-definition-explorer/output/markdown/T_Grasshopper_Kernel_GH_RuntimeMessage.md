# T_Grasshopper_Kernel_GH_RuntimeMessage

﻿ GH\_RuntimeMessage Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_RuntimeMessage Class](../html/T_Grasshopper_Kernel_GH_RuntimeMessage.htm "GH_RuntimeMessage Class")

[GH\_RuntimeMessage Constructor](../html/M_Grasshopper_Kernel_GH_RuntimeMessage__ctor.htm "GH_RuntimeMessage Constructor ")

[GH\_RuntimeMessage Properties](../html/Properties_T_Grasshopper_Kernel_GH_RuntimeMessage.htm "GH_RuntimeMessage Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_RuntimeMessage Class |

Contains all fields that together define a RuntimeMessage. Runtime Messages
are created and recorded by document objects during Grasshopper solutions.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST3F365EEE\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST3F365EEE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RuntimeMessage

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_RuntimeMessage
```

```
Public Class GH_RuntimeMessage
```

AddLanguageTabSet("ID1EBCA");

The GH\_RuntimeMessage type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_RuntimeMessage](M_Grasshopper_Kernel_GH_RuntimeMessage__ctor.htm) | Initializes a new instance of the GH\_RuntimeMessage class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Event](P_Grasshopper_Kernel_GH_RuntimeMessage_Event.htm) | Gets the time at which the message was recorded. |
| Public property | [HasSource](P_Grasshopper_Kernel_GH_RuntimeMessage_HasSource.htm) | Gets a value indicating whether or not this message has a source. |
| Public property | [Message](P_Grasshopper_Kernel_GH_RuntimeMessage_Message.htm) | Gets the contents of the message. |
| Public property | [Source](P_Grasshopper_Kernel_GH_RuntimeMessage_Source.htm) | Gets a string describing the source object that created the message. |
| Public property | [Type](P_Grasshopper_Kernel_GH_RuntimeMessage_Type.htm) | Gets the type qualifier of the message. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)