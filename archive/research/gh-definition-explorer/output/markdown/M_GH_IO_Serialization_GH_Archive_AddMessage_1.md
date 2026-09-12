# M_GH_IO_Serialization_GH_Archive_AddMessage_1

﻿ GH\_Archive.AddMessage Method (String, GH\_Message\_Type)

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
| GH\_ArchiveAddLanguageSpecificTextSet("LSTAC086C1C\_0?cpp=::|nu=.");AddMessage Method (String, GH\_Message\_Type) |

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
	string messageText,
	GH_Message_Type messageType
)
```

```
Public Sub AddMessage ( 
	messageText As String,
	messageType As GH_Message_Type
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

messageText
:   Type: [SystemAddLanguageSpecificTextSet("LSTAC086C1C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Message text.

messageType
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LSTAC086C1C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Message\_Type](T_GH_IO_Serialization_GH_Message_Type.htm)  
    Message type.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](https://docs.microsoft.com/dotnet/api/system.argumentnullexception) | Thrown if message text is null or empty. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Archive Class](T_GH_IO_Serialization_GH_Archive.htm)

[AddMessage Overload](Overload_GH_IO_Serialization_GH_Archive_AddMessage.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)