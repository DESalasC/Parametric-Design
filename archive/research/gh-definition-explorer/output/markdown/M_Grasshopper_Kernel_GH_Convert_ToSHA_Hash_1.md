# M_Grasshopper_Kernel_GH_Convert_ToSHA_Hash_1

﻿ GH\_Convert.ToSHA\_Hash Method (Stream)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Convert Class](../html/T_Grasshopper_Kernel_GH_Convert.htm "GH_Convert Class")

[GH\_Convert Methods](../html/Methods_T_Grasshopper_Kernel_GH_Convert.htm "GH_Convert Methods")

[ToSHA\_Hash Method](../html/Overload_Grasshopper_Kernel_GH_Convert_ToSHA_Hash.htm "ToSHA_Hash Method ")

[ToSHA\_Hash Method (Byte[])](../html/M_Grasshopper_Kernel_GH_Convert_ToSHA_Hash.htm "ToSHA_Hash Method (Byte[])")

[ToSHA\_Hash Method (Stream)](../html/M_Grasshopper_Kernel_GH_Convert_ToSHA_Hash_1.htm "ToSHA_Hash Method (Stream)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ConvertAddLanguageSpecificTextSet("LST78AF42E3\_0?cpp=::|nu=.");ToSHA\_Hash Method (Stream) |

Create a SHA hash. The hash algorithm is only guaranteed to yield
the same results from within a unique application domain.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static Guid ToSHA_Hash(
	Stream data
)
```

```
Public Shared Function ToSHA_Hash ( 
	data As Stream
) As Guid
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

data
:   Type: [System.IOAddLanguageSpecificTextSet("LST78AF42E3\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Stream](https://docs.microsoft.com/dotnet/api/system.io.stream)  
    Data to hash.

#### Return Value

Type: [Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
A guid representing the (partial) SHA hash.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Convert Class](T_Grasshopper_Kernel_GH_Convert.htm)

[ToSHA\_Hash Overload](Overload_Grasshopper_Kernel_GH_Convert_ToSHA_Hash.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)