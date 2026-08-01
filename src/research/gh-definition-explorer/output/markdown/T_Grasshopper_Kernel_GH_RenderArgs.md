# T_Grasshopper_Kernel_GH_RenderArgs

﻿ GH\_RenderArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_RenderArgs Class](../html/T_Grasshopper_Kernel_GH_RenderArgs.htm "GH_RenderArgs Class")

[GH\_RenderArgs Constructor](../html/Overload_Grasshopper_Kernel_GH_RenderArgs__ctor.htm "GH_RenderArgs Constructor ")

[GH\_RenderArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_RenderArgs.htm "GH_RenderArgs Properties")

[GH\_RenderArgs Methods](../html/Methods_T_Grasshopper_Kernel_GH_RenderArgs.htm "GH_RenderArgs Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_RenderArgs Class |

This class is passed to objects that implement IGH\_RenderAwareData or IGH\_RenderAwareObject during render queue operations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTAFAB3613\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTAFAB3613\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RenderArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_RenderArgs
```

```
Public Class GH_RenderArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_RenderArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_RenderArgs(RhinoDoc, ViewportInfo, RenderPrimitiveList, Guid, DictionaryAddLanguageSpecificTextSet("LSTAFAB3613\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");Int32, RenderMaterialAddLanguageSpecificTextSet("LSTAFAB3613\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_RenderArgs__ctor_1.htm) | **Obsolete.**  Create new render arguments. |
| Public method | [GH\_RenderArgs(RhinoDoc, ViewportInfo, RenderPrimitiveList, Guid, RenderMaterial, RenderMaterial)](M_Grasshopper_Kernel_GH_RenderArgs__ctor.htm) | **Obsolete.**  Create new render arguments. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Document](P_Grasshopper_Kernel_GH_RenderArgs_Document.htm) | Gets the rhino document from whence the render originated. |
| Public property | [MaterialNormal](P_Grasshopper_Kernel_GH_RenderArgs_MaterialNormal.htm) | **Obsolete.**  Gets the material hint to use for unselected objects. |
| Public property | [MaterialSelected](P_Grasshopper_Kernel_GH_RenderArgs_MaterialSelected.htm) | **Obsolete.**  Gets the material hint to use for selected objects. |
| Public property | [ModelTransform](P_Grasshopper_Kernel_GH_RenderArgs_ModelTransform.htm) | Gets the current model transform. |
| Public property | [PluginId](P_Grasshopper_Kernel_GH_RenderArgs_PluginId.htm) | Gets the render plugin id that is about to render this geometry. |
| Public property | [Viewport](P_Grasshopper_Kernel_GH_RenderArgs_Viewport.htm) | Gets the viewport details involved in this rendering. |
| Public property | [ViewportName](P_Grasshopper_Kernel_GH_RenderArgs_ViewportName.htm) | Gets the viewport name involved in this rendering. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [PopModelTransform](M_Grasshopper_Kernel_GH_RenderArgs_PopModelTransform.htm) |  |
| Public method | [PushModelTransform](M_Grasshopper_Kernel_GH_RenderArgs_PushModelTransform.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)