# T_Grasshopper_Kernel_GH_StateTagList

﻿ GH\_StateTagList Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_StateTagList Class](../html/T_Grasshopper_Kernel_GH_StateTagList.htm "GH_StateTagList Class")

[GH\_StateTagList Constructor](../html/M_Grasshopper_Kernel_GH_StateTagList__ctor.htm "GH_StateTagList Constructor ")

[GH\_StateTagList Properties](../html/Properties_T_Grasshopper_Kernel_GH_StateTagList.htm "GH_StateTagList Properties")

[GH\_StateTagList Methods](../html/Methods_T_Grasshopper_Kernel_GH_StateTagList.htm "GH_StateTagList Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StateTagList Class |

Maintains a collection of IGH\_StateTag objects.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST8E601F30\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [System.Collections.GenericAddLanguageSpecificTextSet("LST8E601F30\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST8E601F30\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_StateTag](T_Grasshopper_Kernel_IGH_StateTag.htm)AddLanguageSpecificTextSet("LST8E601F30\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Grasshopper.KernelAddLanguageSpecificTextSet("LST8E601F30\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_StateTagList

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_StateTagList : List<IGH_StateTag>, 
	IGH_TooltipAwareObject
```

```
Public Class GH_StateTagList
	Inherits List(Of IGH_StateTag)
	Implements IGH_TooltipAwareObject
```

AddLanguageTabSet("ID1EBCA");

The GH\_StateTagList type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_StateTagList](M_Grasshopper_Kernel_GH_StateTagList__ctor.htm) | Initializes a new instance of the GH\_StateTagList class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BoundingBox](P_Grasshopper_Kernel_GH_StateTagList_BoundingBox.htm) | Gets the boundingbox of all StateTags. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Layout](M_Grasshopper_Kernel_GH_StateTagList_Layout.htm) | Layout the StateTags. |
| Public method | [RenderStateTags](M_Grasshopper_Kernel_GH_StateTagList_RenderStateTags.htm) | Render all StateTags in this list to the designated Graphics surface. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)