# T_Grasshopper_Kernel_GH_AssemblyPriority

﻿ GH\_AssemblyPriority Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_AssemblyPriority Class](../html/T_Grasshopper_Kernel_GH_AssemblyPriority.htm "GH_AssemblyPriority Class")

[GH\_AssemblyPriority Constructor](../html/M_Grasshopper_Kernel_GH_AssemblyPriority__ctor.htm "GH_AssemblyPriority Constructor ")

[GH\_AssemblyPriority Methods](../html/Methods_T_Grasshopper_Kernel_GH_AssemblyPriority.htm "GH_AssemblyPriority Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AssemblyPriority Class |

Derive from this class if you wish to perform additional steps before any of your components are loaded.
Any class in your project which inherits from GH\_AssemblyPriority and which has an
empty constructor will be instantiated prior to any GH\_Component or IGH\_DocumentObject classes.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTFF147E46\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTFF147E46\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AssemblyPriority  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTFF147E46\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelContentEnablerLoader](T_Grasshopper_Rhinoceros_ModelContentEnablerLoader.htm)

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_AssemblyPriority
```

```
Public MustInherit Class GH_AssemblyPriority
```

AddLanguageTabSet("ID1EBCA");

The GH\_AssemblyPriority type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_AssemblyPriority](M_Grasshopper_Kernel_GH_AssemblyPriority__ctor.htm) | Initializes a new instance of the GH\_AssemblyPriority class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [PriorityLoad](M_Grasshopper_Kernel_GH_AssemblyPriority_PriorityLoad.htm) | This method will be called exactly once before any of the Components in your project are loaded. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)