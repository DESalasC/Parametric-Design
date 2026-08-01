# M_GH_IO_VersionNumber_CompareTo_1

﻿ VersionNumber.CompareTo Method (Object)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO](../html/N_GH_IO.htm "GH_IO")

[VersionNumber Structure](../html/T_GH_IO_VersionNumber.htm "VersionNumber Structure")

[VersionNumber Methods](../html/Methods_T_GH_IO_VersionNumber.htm "VersionNumber Methods")

[CompareTo Method](../html/Overload_GH_IO_VersionNumber_CompareTo.htm "CompareTo Method ")

[CompareTo Method (Object)](../html/M_GH_IO_VersionNumber_CompareTo_1.htm "CompareTo Method (Object)")

[CompareTo Method (VersionNumber)](../html/M_GH_IO_VersionNumber_CompareTo.htm "CompareTo Method (VersionNumber)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| VersionNumberAddLanguageSpecificTextSet("LSTF88FA8BB\_0?cpp=::|nu=.");CompareTo Method (Object) |

Compares the value of this instance to a specified VersionNumber value and returns an integer that indicates whether this instance is earlier than, the same as, or later than the specified VersionNumber value.

**Namespace:**
 [GH\_IO](N_GH_IO.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int CompareTo(
	Object value
)
```

```
Public Function CompareTo ( 
	value As Object
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

value
:   Type: [SystemAddLanguageSpecificTextSet("LSTF88FA8BB\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
    The object to compare to the current instance.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
A signed number indicating the relative values of this instance and the value parameter.
Less than zero indicates this instance is earier than value.
Zero indicates this instance is the same as value.
Greater than zero indicates this instance is later than value.

#### Implements

[IComparableAddLanguageSpecificTextSet("LSTF88FA8BB\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");CompareTo(Object)](https://docs.microsoft.com/dotnet/api/system.icomparable.compareto#system-icomparable-compareto(system-object))

![](../icons/SectionExpanded.png)See Also

#### Reference

[VersionNumber Structure](T_GH_IO_VersionNumber.htm)

[CompareTo Overload](Overload_GH_IO_VersionNumber_CompareTo.htm)

[GH\_IO Namespace](N_GH_IO.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)