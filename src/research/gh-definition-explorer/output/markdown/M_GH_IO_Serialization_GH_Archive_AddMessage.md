# M_GH_IO_Serialization_GH_Archive_AddMessage

﻿ GH\_Archive.AddMessage Method (GH\_Message)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Archive Class](../html/T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Class")

[GH\_Archive Methods](../html/Methods_T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Methods")

[AddMessage Method](../html/Overload_GH_IO_Serialization_GH_Archive_AddMessage.htm "AddMessage Method ")

[AddMessage Method (GH\_Message)](../html/M_GH_IO_Serialization_GH_Archive_AddMessage.htm "AddMessage Method (GH_Message)")

[AddMessage Method (String, GH\_Message\_Type)](../html/M_GH_IO_Serialization_GH_Archive_AddMessage_1.htm "AddMessage Method (String, GH_Message_Type)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ArchiveAddLanguageSpecificTextSet("LSTA2AD84C7\_0?cpp=::|nu=.");AddMessage Method (GH\_Message) |

Add a new message to the record.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void AddMessage(
	GH_Message message
)
```

```
Public Sub AddMessage ( 
	message As GH_Message
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

message
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LSTA2AD84C7\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Message](T_GH_IO_Serialization_GH_Message.htm)  
    Message to add

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](https://docs.microsoft.com/dotnet/api/system.argumentnullexception) | Thrown if the message is a null reference. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Archive Class](T_GH_IO_Serialization_GH_Archive.htm)

[AddMessage Overload](Overload_GH_IO_Serialization_GH_Archive_AddMessage.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)