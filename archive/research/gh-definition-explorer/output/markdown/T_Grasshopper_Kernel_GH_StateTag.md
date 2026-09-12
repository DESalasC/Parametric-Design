# T_Grasshopper_Kernel_GH_StateTag

﻿ GH\_StateTag Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_StateTag Class](../html/T_Grasshopper_Kernel_GH_StateTag.htm "GH_StateTag Class")

[GH\_StateTag Constructor](../html/M_Grasshopper_Kernel_GH_StateTag__ctor.htm "GH_StateTag Constructor ")

[GH\_StateTag Properties](../html/Properties_T_Grasshopper_Kernel_GH_StateTag.htm "GH_StateTag Properties")

[GH\_StateTag Methods](../html/Methods_T_Grasshopper_Kernel_GH_StateTag.htm "GH_StateTag Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StateTag Class |

Abstract implementation of the IGH\_StateTag interface.
Derive from this class rather than implementing IGH\_StateTag.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTB6A391C6\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTB6A391C6\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_StateTag

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_StateTag : IGH_StateTag
```

```
Public MustInherit Class GH_StateTag
	Implements IGH_StateTag
```

AddLanguageTabSet("ID1EBCA");

The GH\_StateTag type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_StateTag](M_Grasshopper_Kernel_GH_StateTag__ctor.htm) | Initializes a new instance of the GH\_StateTag class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Description](P_Grasshopper_Kernel_GH_StateTag_Description.htm) |  |
| Public property | [Icon](P_Grasshopper_Kernel_GH_StateTag_Icon.htm) |  |
| Public property | [Name](P_Grasshopper_Kernel_GH_StateTag_Name.htm) |  |
| Public property | [Stage](P_Grasshopper_Kernel_GH_StateTag_Stage.htm) | Gets or sets the stage rectangle for this tag. |
| Public property | [StateDescription](P_Grasshopper_Kernel_GH_StateTag_StateDescription.htm) | Gets or sets the state description for this tag. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Render](M_Grasshopper_Kernel_GH_StateTag_Render.htm) |  |
| Protected method | [RenderFreeformIcon](M_Grasshopper_Kernel_GH_StateTag_RenderFreeformIcon.htm) | Render a filled path with default shading. |
| Protected method | [RenderTagBlankIcon(Graphics)](M_Grasshopper_Kernel_GH_StateTag_RenderTagBlankIcon.htm) | Render a blank rectangle icon. |
| Protected method | [RenderTagBlankIcon(Graphics, GH\_StateTagAddLanguageSpecificTextSet("LSTB6A391C6\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");DrawCallback)](M_Grasshopper_Kernel_GH_StateTag_RenderTagBlankIcon_1.htm) | Render a blank rectangle icon. |
| Protected method | [RenderTagPolygonIcon](M_Grasshopper_Kernel_GH_StateTag_RenderTagPolygonIcon.htm) | Render a filled polygon with default shading. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)