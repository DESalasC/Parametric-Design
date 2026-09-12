# M_Grasshopper_Kernel_GH_DocumentIO_Copy_2

﻿ GH\_DocumentIO.Copy Method (GH\_ClipboardType, IEnumerable(Guid))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentIO Class](../html/T_Grasshopper_Kernel_GH_DocumentIO.htm "GH_DocumentIO Class")

[GH\_DocumentIO Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentIO.htm "GH_DocumentIO Methods")

[Copy Method](../html/Overload_Grasshopper_Kernel_GH_DocumentIO_Copy.htm "Copy Method ")

[Copy Method (GH\_ClipboardType)](../html/M_Grasshopper_Kernel_GH_DocumentIO_Copy.htm "Copy Method (GH_ClipboardType)")

[Copy Method (GH\_ClipboardType, Boolean)](../html/M_Grasshopper_Kernel_GH_DocumentIO_Copy_1.htm "Copy Method (GH_ClipboardType, Boolean)")

[Copy Method (GH\_ClipboardType, IEnumerable(Guid))](../html/M_Grasshopper_Kernel_GH_DocumentIO_Copy_2.htm "Copy Method (GH_ClipboardType, IEnumerable(Guid))")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentIOAddLanguageSpecificTextSet("LST235986B3\_0?cpp=::|nu=.");Copy Method (GH\_ClipboardType, IEnumerableAddLanguageSpecificTextSet("LST235986B3\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GuidAddLanguageSpecificTextSet("LST235986B3\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Copy the specified objects in the internal document into the clipboard.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool Copy(
	GH_ClipboardType clipboard,
	IEnumerable<Guid> guids
)
```

```
Public Function Copy ( 
	clipboard As GH_ClipboardType,
	guids As IEnumerable(Of Guid)
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

clipboard
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST235986B3\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ClipboardType](T_Grasshopper_Kernel_GH_ClipboardType.htm)  
    Specifies the clipboard type to use.

guids
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST235986B3\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LST235986B3\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Guid](https://docs.microsoft.com/dotnet/api/system.guid)AddLanguageSpecificTextSet("LST235986B3\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    List of object ids to copy.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentIO Class](T_Grasshopper_Kernel_GH_DocumentIO.htm)

[Copy Overload](Overload_Grasshopper_Kernel_GH_DocumentIO_Copy.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)