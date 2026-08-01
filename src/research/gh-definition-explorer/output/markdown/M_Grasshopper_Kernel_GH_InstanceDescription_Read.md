# M_Grasshopper_Kernel_GH_InstanceDescription_Read

﻿ GH\_InstanceDescription.Read Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_InstanceDescription Class](../html/T_Grasshopper_Kernel_GH_InstanceDescription.htm "GH_InstanceDescription Class")

[GH\_InstanceDescription Methods](../html/Methods_T_Grasshopper_Kernel_GH_InstanceDescription.htm "GH_InstanceDescription Methods")

[CopyFrom Method](../html/M_Grasshopper_Kernel_GH_InstanceDescription_CopyFrom.htm "CopyFrom Method ")

[NewInstanceGuid Method](../html/Overload_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid.htm "NewInstanceGuid Method ")

[Read Method](../html/M_Grasshopper_Kernel_GH_InstanceDescription_Read.htm "Read Method ")

[ReadFull Method](../html/M_Grasshopper_Kernel_GH_InstanceDescription_ReadFull.htm "ReadFull Method ")

[Write Method](../html/M_Grasshopper_Kernel_GH_InstanceDescription_Write.htm "Write Method ")

[WriteFull Method](../html/M_Grasshopper_Kernel_GH_InstanceDescription_WriteFull.htm "WriteFull Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_InstanceDescriptionAddLanguageSpecificTextSet("LSTABD67F45\_0?cpp=::|nu=.");Read Method |

Default deserialization. Only retrieves Name, NickName, Description and InstanceGuid fields.
If you want to retrieve additional fields use ReadFull() instead. However, ReadFull() will only
work if the archive was written using WriteFull().

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual bool Read(
	GH_IReader reader
)
```

```
Public Overridable Function Read ( 
	reader As GH_IReader
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

reader
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LSTABD67F45\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IReader](T_GH_IO_Serialization_GH_IReader.htm)  
    Object to deserialize with.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
Always True.

#### Implements

[GH\_ISerializableAddLanguageSpecificTextSet("LSTABD67F45\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_GH_IO_GH_ISerializable_Read.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_InstanceDescription Class](T_Grasshopper_Kernel_GH_InstanceDescription.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)