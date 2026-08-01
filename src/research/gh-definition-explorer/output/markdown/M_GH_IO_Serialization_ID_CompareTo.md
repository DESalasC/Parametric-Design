# M_GH_IO_Serialization_ID_CompareTo

﻿ ID.CompareTo Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[ID Structure](../html/T_GH_IO_Serialization_ID.htm "ID Structure")

[ID Methods](../html/Methods_T_GH_IO_Serialization_ID.htm "ID Methods")

[CompareTo Method](../html/M_GH_IO_Serialization_ID_CompareTo.htm "CompareTo Method ")

[Equals Method](../html/M_GH_IO_Serialization_ID_Equals.htm "Equals Method ")

[GetHashCode Method](../html/M_GH_IO_Serialization_ID_GetHashCode.htm "GetHashCode Method ")

[ToString Method](../html/M_GH_IO_Serialization_ID_ToString.htm "ToString Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IDAddLanguageSpecificTextSet("LSTFF4CA9B2\_0?cpp=::|nu=.");CompareTo Method |

Compares this ID to another ID.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int CompareTo(
	ID other
)
```

```
Public Function CompareTo ( 
	other As ID
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

other
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LSTFF4CA9B2\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ID](T_GH_IO_Serialization_ID.htm)  
    The other ID.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
Less than 0, if other comes before this. 0 is other is at the same place. More than zero otherwise.

#### Implements

[IComparableAddLanguageSpecificTextSet("LSTFF4CA9B2\_2?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTFF4CA9B2\_3?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTFF4CA9B2\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");CompareTo(T)](https://docs.microsoft.com/dotnet/api/system.icomparable-1.compareto#system-icomparable-1-compareto(-0))

![](../icons/SectionExpanded.png)See Also

#### Reference

[ID Structure](T_GH_IO_Serialization_ID.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)