# T_Grasshopper_Kernel_GH_ConnectivityDisparity

﻿ GH\_ConnectivityDisparity Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ConnectivityDisparity Class](../html/T_Grasshopper_Kernel_GH_ConnectivityDisparity.htm "GH_ConnectivityDisparity Class")

[GH\_ConnectivityDisparity Constructor](../html/M_Grasshopper_Kernel_GH_ConnectivityDisparity__ctor.htm "GH_ConnectivityDisparity Constructor ")

[GH\_ConnectivityDisparity Properties](../html/Properties_T_Grasshopper_Kernel_GH_ConnectivityDisparity.htm "GH_ConnectivityDisparity Properties")

[GH\_ConnectivityDisparity Methods](../html/Methods_T_Grasshopper_Kernel_GH_ConnectivityDisparity.htm "GH_ConnectivityDisparity Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ConnectivityDisparity Class |

Maintains two connectivity diagrams, one of which is a subset of the other.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTD632C388\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTD632C388\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ConnectivityDisparity

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ConnectivityDisparity
```

```
Public Class GH_ConnectivityDisparity
```

AddLanguageTabSet("ID1EBCA");

The GH\_ConnectivityDisparity type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ConnectivityDisparity](M_Grasshopper_Kernel_GH_ConnectivityDisparity__ctor.htm) | Create a new instance of the Connectivity Disparity utility class. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [SubNodes](P_Grasshopper_Kernel_GH_ConnectivityDisparity_SubNodes.htm) | Gets a proxy for all the Nodes in the Subset diagram. |
| Public property | [SubSet](P_Grasshopper_Kernel_GH_ConnectivityDisparity_SubSet.htm) | Gets a pointer to the subset diagram stored in this disparity class. |
| Public property | [TopNodes](P_Grasshopper_Kernel_GH_ConnectivityDisparity_TopNodes.htm) | Gets a proxy for all the Nodes in the Top Level diagram. |
| Public property | [TopSet](P_Grasshopper_Kernel_GH_ConnectivityDisparity_TopSet.htm) | Gets a pointer to the complete diagram stored in this disparity class. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [ExternalInputs](M_Grasshopper_Kernel_GH_ConnectivityDisparity_ExternalInputs.htm) | Find all external sources for a given id in the subset. |
| Public method | [ExternalOutputs](M_Grasshopper_Kernel_GH_ConnectivityDisparity_ExternalOutputs.htm) | Find all external recipients for a given id in the subset. |
| Public method | [InternalInputs](M_Grasshopper_Kernel_GH_ConnectivityDisparity_InternalInputs.htm) | Find all internal sources for a given id in the subset. |
| Public method | [InternalOutputs](M_Grasshopper_Kernel_GH_ConnectivityDisparity_InternalOutputs.htm) | Find all external recipients for a given id in the subset. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)