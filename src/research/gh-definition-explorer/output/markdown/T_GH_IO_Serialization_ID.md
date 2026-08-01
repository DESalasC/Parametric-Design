# T_GH_IO_Serialization_ID

﻿ ID Structure

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[ID Structure](../html/T_GH_IO_Serialization_ID.htm "ID Structure")

[ID Constructor](../html/Overload_GH_IO_Serialization_ID__ctor.htm "ID Constructor ")

[ID Properties](../html/Properties_T_GH_IO_Serialization_ID.htm "ID Properties")

[ID Methods](../html/Methods_T_GH_IO_Serialization_ID.htm "ID Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ID Structure |

An ID is used to uniquely identify a specific item.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public struct ID : IComparable<ID>, IEquatable<ID>
```

```
Public Structure ID
	Implements IComparable(Of ID), IEquatable(Of ID)
```

AddLanguageTabSet("ID0EBCA");

The ID type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ID(String)](M_GH_IO_Serialization_ID__ctor.htm) | Constuctor for IDs. |
| Public method | [ID(String, Int32)](M_GH_IO_Serialization_ID__ctor_1.htm) | Constructor for IDs. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Hash](P_GH_IO_Serialization_ID_Hash.htm) | Gets the hash code. |
| Public property | [HasIndex](P_GH_IO_Serialization_ID_HasIndex.htm) | Gets whether the index has been set. |
| Public property | [HasName](P_GH_IO_Serialization_ID_HasName.htm) | Gets whether the name has been set. Every valid ID must have a name. |
| Public property | [Index](P_GH_IO_Serialization_ID_Index.htm) | Gets the index of this ID, if there is no valid index then -1 is returned. |
| Public property | [Name](P_GH_IO_Serialization_ID_Name.htm) | Gets the name of this ID. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CompareTo](M_GH_IO_Serialization_ID_CompareTo.htm) | Compares this ID to another ID. |
| Public method | [Equals](M_GH_IO_Serialization_ID_Equals.htm) | Determines if two IDs are equal. |
| Public method | [GetHashCode](M_GH_IO_Serialization_ID_GetHashCode.htm) | Gets the hash code. (Overrides [ValueTypeAddLanguageSpecificTextSet("LSTA99C62D6\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");GetHashCodeAddLanguageSpecificTextSet("LSTA99C62D6\_1?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-valuetype-gethashcode).) |
| Public method | [ToString](M_GH_IO_Serialization_ID_ToString.htm) | Gets a string representation for this ID. (Overrides [ValueTypeAddLanguageSpecificTextSet("LSTA99C62D6\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTA99C62D6\_3?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.valuetype.tostring#system-valuetype-tostring).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)