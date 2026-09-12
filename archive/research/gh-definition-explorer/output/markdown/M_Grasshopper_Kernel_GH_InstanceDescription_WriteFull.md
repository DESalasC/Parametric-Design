# M_Grasshopper_Kernel_GH_InstanceDescription_WriteFull

﻿ GH\_InstanceDescription.WriteFull Method 

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
| GH\_InstanceDescriptionAddLanguageSpecificTextSet("LST6D4AA200\_0?cpp=::|nu=.");WriteFull Method |

GH\_InstanceDescription does not by default serialize all fields.
Use this function to write *all* fields to the archive.
This method is compatible with the default Write()/Read() operations.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual bool WriteFull(
	GH_IWriter writer
)
```

```
Public Overridable Function WriteFull ( 
	writer As GH_IWriter
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

writer
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LST6D4AA200\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IWriter](T_GH_IO_Serialization_GH_IWriter.htm)  
    Writer for serialization.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_InstanceDescription Class](T_Grasshopper_Kernel_GH_InstanceDescription.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)