# M_Grasshopper_Kernel_GH_InstanceDescription_Write

﻿ GH\_InstanceDescription.Write Method 

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
| GH\_InstanceDescriptionAddLanguageSpecificTextSet("LSTF6E6140F\_0?cpp=::|nu=.");Write Method |

Default serialization. Only stores Name, NickName, Description and InstanceGuid fields.
If you want to store additional fields use WriteFull() instead.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual bool Write(
	GH_IWriter writer
)
```

```
Public Overridable Function Write ( 
	writer As GH_IWriter
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

writer
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LSTF6E6140F\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IWriter](T_GH_IO_Serialization_GH_IWriter.htm)  
    Object to serialize with.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
Always True.

#### Implements

[GH\_ISerializableAddLanguageSpecificTextSet("LSTF6E6140F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_GH_IO_GH_ISerializable_Write.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_InstanceDescription Class](T_Grasshopper_Kernel_GH_InstanceDescription.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)