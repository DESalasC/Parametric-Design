# T_Grasshopper_Kernel_GH_DebugDescriptionWriter

﻿ GH\_DebugDescriptionWriter Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DebugDescriptionWriter Class](../html/T_Grasshopper_Kernel_GH_DebugDescriptionWriter.htm "GH_DebugDescriptionWriter Class")

[GH\_DebugDescriptionWriter Constructor](../html/M_Grasshopper_Kernel_GH_DebugDescriptionWriter__ctor.htm "GH_DebugDescriptionWriter Constructor ")

[GH\_DebugDescriptionWriter Properties](../html/Properties_T_Grasshopper_Kernel_GH_DebugDescriptionWriter.htm "GH_DebugDescriptionWriter Properties")

[GH\_DebugDescriptionWriter Methods](../html/Methods_T_Grasshopper_Kernel_GH_DebugDescriptionWriter.htm "GH_DebugDescriptionWriter Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DebugDescriptionWriter Class |

Writer object used to create debug logs.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST7CA5EE05\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST7CA5EE05\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DebugDescriptionWriter

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DebugDescriptionWriter
```

```
Public Class GH_DebugDescriptionWriter
```

AddLanguageTabSet("ID1EBCA");

The GH\_DebugDescriptionWriter type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DebugDescriptionWriter](M_Grasshopper_Kernel_GH_DebugDescriptionWriter__ctor.htm) | Initializes a new instance of the GH\_DebugDescriptionWriter class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Depth](P_Grasshopper_Kernel_GH_DebugDescriptionWriter_Depth.htm) | Gets the depth of the current writer. Depth is represented by whitespace in front of each line. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CloseBlock](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CloseBlock.htm) | Close the current block and decrease the depth by 1. |
| Public method | [CreateBlock](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CreateBlock.htm) | Begin a new block. This will increase the depth by 1. You *must* call CloseBlock() if you call this function. |
| Public method | [CreateLog](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_CreateLog.htm) | Get a single string that represents the entire log so far. |
| Public method | [WriteLineAddLanguageSpecificTextSet("LST7CA5EE05\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLine.htm) | Write a new blank line to the log. |
| Public method | [WriteLine(String)](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLine_1.htm) | Write a new line to the log. |
| Public method | [WriteLine(String, AddLanguageSpecificTextSet("LST7CA5EE05\_3?cpp=array&lt;");ObjectAddLanguageSpecificTextSet("LST7CA5EE05\_4?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLine_2.htm) | Write a new formatted line to the log. |
| Public method | [WriteLogToFile](M_Grasshopper_Kernel_GH_DebugDescriptionWriter_WriteLogToFile.htm) | Write the log to a text file. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)