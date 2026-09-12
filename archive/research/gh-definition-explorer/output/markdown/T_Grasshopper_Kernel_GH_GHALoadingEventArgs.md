# T_Grasshopper_Kernel_GH_GHALoadingEventArgs

﻿ GH\_GHALoadingEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_GHALoadingEventArgs Class](../html/T_Grasshopper_Kernel_GH_GHALoadingEventArgs.htm "GH_GHALoadingEventArgs Class")

[GH\_GHALoadingEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_GHALoadingEventArgs.htm "GH_GHALoadingEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GHALoadingEventArgs Class |

Event arguments used in the GH\_GHALoaded event on GH\_ComponentServer.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTFFAA281A\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTFFAA281A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LSTFFAA281A\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GHALoadingEventArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_GHALoadingEventArgs : EventArgs
```

```
Public Class GH_GHALoadingEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_GHALoadingEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Assembly](P_Grasshopper_Kernel_GH_GHALoadingEventArgs_Assembly.htm) | Gets the assembly that was loaded from the GHA file. |
| Public property | [FileName](P_Grasshopper_Kernel_GH_GHALoadingEventArgs_FileName.htm) | Gets the location of the gha file. |
| Public property | [Icon](P_Grasshopper_Kernel_GH_GHALoadingEventArgs_Icon.htm) | Gets the official icon of the GHA file. |
| Public property | [Id](P_Grasshopper_Kernel_GH_GHALoadingEventArgs_Id.htm) | Gets the Id of the GHA file. |
| Public property | [LoadingMechanism](P_Grasshopper_Kernel_GH_GHALoadingEventArgs_LoadingMechanism.htm) | Gets the mechanism that was used to load the file. |
| Public property | [Name](P_Grasshopper_Kernel_GH_GHALoadingEventArgs_Name.htm) | Gets the official name of the GHA file. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)