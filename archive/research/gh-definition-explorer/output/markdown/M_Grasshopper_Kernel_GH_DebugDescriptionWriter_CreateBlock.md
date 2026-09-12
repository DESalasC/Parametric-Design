# M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CreateBlock

﻿ GH\_DebugDescriptionWriter.CreateBlock Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DebugDescriptionWriter Class](../html/T_Grasshopper_Kernel_GH_DebugDescriptionWriter.htm "GH_DebugDescriptionWriter Class")

[GH\_DebugDescriptionWriter Methods](../html/Methods_T_Grasshopper_Kernel_GH_DebugDescriptionWriter.htm "GH_DebugDescriptionWriter Methods")

[CloseBlock Method](../html/M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CloseBlock.htm "CloseBlock Method ")

[CreateBlock Method](../html/M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CreateBlock.htm "CreateBlock Method ")

[CreateLog Method](../html/M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CreateLog.htm "CreateLog Method ")

[WriteLine Method](../html/Overload_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLine.htm "WriteLine Method ")

[WriteLogToFile Method](../html/M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLogToFile.htm "WriteLogToFile Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DebugDescriptionWriterAddLanguageSpecificTextSet("LST52934EB8\_0?cpp=::|nu=.");CreateBlock Method |

Begin a new block. This will increase the depth by 1.
You *must* call CloseBlock() if you call this function.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void CreateBlock(
	string name
)
```

```
Public Sub CreateBlock ( 
	name As String
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST52934EB8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DebugDescriptionWriter Class](T_Grasshopper_Kernel_GH_DebugDescriptionWriter.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)