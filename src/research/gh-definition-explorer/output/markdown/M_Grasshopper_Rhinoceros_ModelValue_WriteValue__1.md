# M_Grasshopper_Rhinoceros_ModelValue_WriteValue__1

﻿ ModelValue.WriteValue(T) Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm "Grasshopper.Rhinoceros")

[ModelValue Class](../html/T_Grasshopper_Rhinoceros_ModelValue.htm "ModelValue Class")

[ModelValue Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelValue.htm "ModelValue Methods")

[CastTo(T) Method](../html/M_Grasshopper_Rhinoceros_ModelValue_CastTo__1.htm "CastTo(T) Method ")

[Clone Method](../html/M_Grasshopper_Rhinoceros_ModelValue_Clone.htm "Clone Method ")

[Read Method](../html/M_Grasshopper_Rhinoceros_ModelValue_Read.htm "Read Method ")

[ReadValue(T) Method](../html/M_Grasshopper_Rhinoceros_ModelValue_ReadValue__1.htm "ReadValue(T) Method ")

[ScriptVariable Method](../html/M_Grasshopper_Rhinoceros_ModelValue_ScriptVariable.htm "ScriptVariable Method ")

[TooltipString Method](../html/M_Grasshopper_Rhinoceros_ModelValue_TooltipString.htm "TooltipString Method ")

[ToString Method](../html/M_Grasshopper_Rhinoceros_ModelValue_ToString.htm "ToString Method ")

[Write Method](../html/M_Grasshopper_Rhinoceros_ModelValue_Write.htm "Write Method ")

[WriteValue(T) Method](../html/M_Grasshopper_Rhinoceros_ModelValue_WriteValue__1.htm "WriteValue(T) Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelValueAddLanguageSpecificTextSet("LSTB0C9821D\_0?cpp=::|nu=.");WriteValueAddLanguageSpecificTextSet("LSTB0C9821D\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTB0C9821D\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Method |

**Namespace:**
 [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected internal static bool WriteValue<T>(
	GH_IWriter writer,
	in T serializable
)
where T : struct, new(), GH_ISerializable
```

```
Protected Friend Shared Function WriteValue(Of T As {Structure, New, GH_ISerializable}) ( 
	writer As GH_IWriter,
	ByRef serializable As T
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

writer
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LSTB0C9821D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IWriter](T_GH_IO_Serialization_GH_IWriter.htm)

serializable
:   Type: TAddLanguageSpecificTextSet("LSTB0C9821D\_4?cpp=%");

#### Type Parameters

T

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[ModelValue Class](T_Grasshopper_Rhinoceros_ModelValue.htm)

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)