# T_Grasshopper_Kernel_Data_GH_PathOffset

﻿ GH\_PathOffset Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_PathOffset Class](../html/T_Grasshopper_Kernel_Data_GH_PathOffset.htm "GH_PathOffset Class")

[GH\_PathOffset Constructor](../html/Overload_Grasshopper_Kernel_Data_GH_PathOffset__ctor.htm "GH_PathOffset Constructor ")

[GH\_PathOffset Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_PathOffset.htm "GH_PathOffset Properties")

[GH\_PathOffset Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_PathOffset.htm "GH_PathOffset Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PathOffset Class |

Represents a relative offset within a data structure.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTFCF94BFE\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LSTFCF94BFE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PathOffset

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_PathOffset
```

```
Public Class GH_PathOffset
```

AddLanguageTabSet("ID1EBCA");

The GH\_PathOffset type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_PathOffsetAddLanguageSpecificTextSet("LSTFCF94BFE\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Data_GH_PathOffset__ctor.htm) | Initializes a new instance of the GH\_PathOffset class |
| Public method | [GH\_PathOffset(IEnumerableAddLanguageSpecificTextSet("LSTFCF94BFE\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");Int32AddLanguageSpecificTextSet("LSTFCF94BFE\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_Data_GH_PathOffset__ctor_1.htm) | Initializes a new instance of the GH\_PathOffset class |
| Public method | [GH\_PathOffset(IEnumerableAddLanguageSpecificTextSet("LSTFCF94BFE\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");Int32AddLanguageSpecificTextSet("LSTFCF94BFE\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Int32)](M_Grasshopper_Kernel_Data_GH_PathOffset__ctor_2.htm) | Initializes a new instance of the GH\_PathOffset class |
| Public method | [GH\_PathOffset(IEnumerableAddLanguageSpecificTextSet("LSTFCF94BFE\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");Int32AddLanguageSpecificTextSet("LSTFCF94BFE\_8?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Int32, Boolean, Boolean)](M_Grasshopper_Kernel_Data_GH_PathOffset__ctor_3.htm) | Initializes a new instance of the GH\_PathOffset class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ItemOffset](P_Grasshopper_Kernel_Data_GH_PathOffset_ItemOffset.htm) | Gets or sets the relative offset for branch items. |
| Public property | [ItemWrap](P_Grasshopper_Kernel_Data_GH_PathOffset_ItemWrap.htm) | Gets or sets the ItemWrap flag. |
| Public property | [PathOffset](P_Grasshopper_Kernel_Data_GH_PathOffset_PathOffset.htm) | Gets access to the relative offsets for path indices. |
| Public property | [PathWrap](P_Grasshopper_Kernel_Data_GH_PathOffset_PathWrap.htm) | Gets or sets the PathWrap flag. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [OffsetPath(GH\_Path, Int32, GH\_PathAddLanguageSpecificTextSet("LSTFCF94BFE\_9?cpp=%");, Int32AddLanguageSpecificTextSet("LSTFCF94BFE\_10?cpp=%");)](M_Grasshopper_Kernel_Data_GH_PathOffset_OffsetPath.htm) | Offset a path + index value without wrapping. |
| Public method | [OffsetPath(GH\_Path, Int32, IGH\_Structure, GH\_PathAddLanguageSpecificTextSet("LSTFCF94BFE\_11?cpp=%");, Int32AddLanguageSpecificTextSet("LSTFCF94BFE\_12?cpp=%");)](M_Grasshopper_Kernel_Data_GH_PathOffset_OffsetPath_1.htm) | Offset a path + index value with wrapping and bounds checking. |
| Public methodStatic member | [ParseString](M_Grasshopper_Kernel_Data_GH_PathOffset_ParseString.htm) |  |
| Public method | [ToString](M_Grasshopper_Kernel_Data_GH_PathOffset_ToString.htm) | Format the Path Offset. (Overrides [ObjectAddLanguageSpecificTextSet("LSTFCF94BFE\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTFCF94BFE\_14?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)