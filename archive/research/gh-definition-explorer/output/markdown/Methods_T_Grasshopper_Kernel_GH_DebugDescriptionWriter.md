# Methods_T_Grasshopper_Kernel_GH_DebugDescriptionWriter

﻿ GH\_DebugDescriptionWriter Methods

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
| GH\_DebugDescriptionWriter Methods |

The [GH\_DebugDescriptionWriter](T_Grasshopper_Kernel_GH_DebugDescriptionWriter.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CloseBlock](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CloseBlock.htm) | Close the current block and decrease the depth by 1. |
| Public method | [CreateBlock](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CreateBlock.htm) | Begin a new block. This will increase the depth by 1. You *must* call CloseBlock() if you call this function. |
| Public method | [CreateLog](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CreateLog.htm) | Get a single string that represents the entire log so far. |
| Public method | [WriteLineAddLanguageSpecificTextSet("LST4C22E6E0\_0?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLine.htm) | Write a new blank line to the log. |
| Public method | [WriteLine(String)](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLine_1.htm) | Write a new line to the log. |
| Public method | [WriteLine(String, AddLanguageSpecificTextSet("LST4C22E6E0\_1?cpp=array&lt;");ObjectAddLanguageSpecificTextSet("LST4C22E6E0\_2?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLine_2.htm) | Write a new formatted line to the log. |
| Public method | [WriteLogToFile](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLogToFile.htm) | Write the log to a text file. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DebugDescriptionWriter Class](T_Grasshopper_Kernel_GH_DebugDescriptionWriter.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)