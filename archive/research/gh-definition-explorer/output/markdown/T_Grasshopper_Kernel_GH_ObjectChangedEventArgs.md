# T_Grasshopper_Kernel_GH_ObjectChangedEventArgs

﻿ GH\_ObjectChangedEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ObjectChangedEventArgs Class](../html/T_Grasshopper_Kernel_GH_ObjectChangedEventArgs.htm "GH_ObjectChangedEventArgs Class")

[GH\_ObjectChangedEventArgs Constructor](../html/Overload_Grasshopper_Kernel_GH_ObjectChangedEventArgs__ctor.htm "GH_ObjectChangedEventArgs Constructor ")

[GH\_ObjectChangedEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_ObjectChangedEventArgs.htm "GH_ObjectChangedEventArgs Properties")

[GH\_ObjectChangedEventArgs Fields](../html/Fields_T_Grasshopper_Kernel_GH_ObjectChangedEventArgs.htm "GH_ObjectChangedEventArgs Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ObjectChangedEventArgs Class |

Event arguments passed during ObjectChanged events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST1D64772E\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST1D64772E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LST1D64772E\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ObjectChangedEventArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ObjectChangedEventArgs : EventArgs
```

```
Public Class GH_ObjectChangedEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_ObjectChangedEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ObjectChangedEventArgs(IGH\_DocumentObject, GH\_ObjectEventType)](M_Grasshopper_Kernel_GH_ObjectChangedEventArgs__ctor.htm) | Initializes a new instance of the GH\_ObjectChangedEventArgs class |
| Public method | [GH\_ObjectChangedEventArgs(IGH\_DocumentObject, String)](M_Grasshopper_Kernel_GH_ObjectChangedEventArgs__ctor_2.htm) | Initializes a new instance of the GH\_ObjectChangedEventArgs class |
| Public method | [GH\_ObjectChangedEventArgs(IGH\_DocumentObject, GH\_ObjectEventType, Object)](M_Grasshopper_Kernel_GH_ObjectChangedEventArgs__ctor_1.htm) | Initializes a new instance of the GH\_ObjectChangedEventArgs class |
| Public method | [GH\_ObjectChangedEventArgs(IGH\_DocumentObject, String, Object)](M_Grasshopper_Kernel_GH_ObjectChangedEventArgs__ctor_3.htm) | Initializes a new instance of the GH\_ObjectChangedEventArgs class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [CustomType](P_Grasshopper_Kernel_GH_ObjectChangedEventArgs_CustomType.htm) | Gets the customised type description of this event. This field is only set when the Type is GH\_ObjectEventType.Custom. |
| Public property | [Sender](P_Grasshopper_Kernel_GH_ObjectChangedEventArgs_Sender.htm) | Gets the object which raised this event. |
| Public property | [Tag](P_Grasshopper_Kernel_GH_ObjectChangedEventArgs_Tag.htm) | Gets the tag for this event. |
| Public property | [Type](P_Grasshopper_Kernel_GH_ObjectChangedEventArgs_Type.htm) | Gets the type of this event. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_custom](F_Grasshopper_Kernel_GH_ObjectChangedEventArgs_m_custom.htm) |  |
| Protected field | [m\_sender](F_Grasshopper_Kernel_GH_ObjectChangedEventArgs_m_sender.htm) |  |
| Protected field | [m\_tag](F_Grasshopper_Kernel_GH_ObjectChangedEventArgs_m_tag.htm) |  |
| Protected field | [m\_type](F_Grasshopper_Kernel_GH_ObjectChangedEventArgs_m_type.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)