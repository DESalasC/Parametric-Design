# M_GH_IO_Serialization_GH_Archive_MessageCount_1

﻿ GH\_Archive.MessageCount Method (Boolean, Boolean, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Archive Class](../html/T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Class")

[GH\_Archive Methods](../html/Methods_T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Methods")

[MessageCount Method](../html/Overload_GH_IO_Serialization_GH_Archive_MessageCount.htm "MessageCount Method ")

[MessageCount Method](../html/M_GH_IO_Serialization_GH_Archive_MessageCount.htm "MessageCount Method ")

[MessageCount Method (Boolean, Boolean, Boolean)](../html/M_GH_IO_Serialization_GH_Archive_MessageCount_1.htm "MessageCount Method (Boolean, Boolean, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ArchiveAddLanguageSpecificTextSet("LSTADCA444E\_0?cpp=::|nu=.");MessageCount Method (Boolean, Boolean, Boolean) |

Gets the number of messages recorded since the most recent IO operation began.
Message count can be filtered by message type.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int MessageCount(
	bool includeInfo,
	bool includeWarnings,
	bool includeErrors
)
```

```
Public Function MessageCount ( 
	includeInfo As Boolean,
	includeWarnings As Boolean,
	includeErrors As Boolean
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

includeInfo
:   Type: [SystemAddLanguageSpecificTextSet("LSTADCA444E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, info messages will be included in the count.

includeWarnings
:   Type: [SystemAddLanguageSpecificTextSet("LSTADCA444E\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, warnings will be included in the count.

includeErrors
:   Type: [SystemAddLanguageSpecificTextSet("LSTADCA444E\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, errors will be included in the count.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
The number of recoded messages that pass the type filters.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Archive Class](T_GH_IO_Serialization_GH_Archive.htm)

[MessageCount Overload](Overload_GH_IO_Serialization_GH_Archive_MessageCount.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)