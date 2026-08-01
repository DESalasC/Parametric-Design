# T_Grasshopper_Kernel_GH_RelevantObjectData

﻿ GH\_RelevantObjectData Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_RelevantObjectData Class](../html/T_Grasshopper_Kernel_GH_RelevantObjectData.htm "GH_RelevantObjectData Class")

[GH\_RelevantObjectData Constructor](../html/M_Grasshopper_Kernel_GH_RelevantObjectData__ctor.htm "GH_RelevantObjectData Constructor ")

[GH\_RelevantObjectData Properties](../html/Properties_T_Grasshopper_Kernel_GH_RelevantObjectData.htm "GH_RelevantObjectData Properties")

[GH\_RelevantObjectData Methods](../html/Methods_T_Grasshopper_Kernel_GH_RelevantObjectData.htm "GH_RelevantObjectData Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_RelevantObjectData Class |

Contains information about relevant objects at a specific canvas location.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST38F3C859\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST38F3C859\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RelevantObjectData

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_RelevantObjectData
```

```
Public Class GH_RelevantObjectData
```

AddLanguageTabSet("ID1EBCA");

The GH\_RelevantObjectData type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_RelevantObjectData](M_Grasshopper_Kernel_GH_RelevantObjectData__ctor.htm) | Construct a new instance. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Attributes](P_Grasshopper_Kernel_GH_RelevantObjectData_Attributes.htm) | Gets the attributes that belong to the object. |
| Public property | [Group](P_Grasshopper_Kernel_GH_RelevantObjectData_Group.htm) | Gets the cast of the DocObject to GH\_Group. |
| Public property | [IsTopLevelObject](P_Grasshopper_Kernel_GH_RelevantObjectData_IsTopLevelObject.htm) | Gets a value indicating whether or not the Object is a top-level object. |
| Public property | [Object](P_Grasshopper_Kernel_GH_RelevantObjectData_Object.htm) | Gets the raw object cached in this data instance. |
| Public property | [ObjectType](P_Grasshopper_Kernel_GH_RelevantObjectData_ObjectType.htm) | Gets the type of object indicated by this data. |
| Public property | [Parameter](P_Grasshopper_Kernel_GH_RelevantObjectData_Parameter.htm) | Gets the cast of the DocObject to IGH\_Param. If the DocObject is not of type IGH\_Param, the attributes of the object will be perused to find a nested IGH\_Param at the point. |
| Public property | [Point](P_Grasshopper_Kernel_GH_RelevantObjectData_Point.htm) | Gets the point for which this GH\_RelevantObjectData has been made. |
| Public property | [TopLevelObject](P_Grasshopper_Kernel_GH_RelevantObjectData_TopLevelObject.htm) | Gets the top-level object. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CreateBalloonData](M_Grasshopper_Kernel_GH_RelevantObjectData_CreateBalloonData.htm) |  |
| Public method | [CreateGripData](M_Grasshopper_Kernel_GH_RelevantObjectData_CreateGripData.htm) |  |
| Public method | [CreateGroupData](M_Grasshopper_Kernel_GH_RelevantObjectData_CreateGroupData.htm) |  |
| Public method | [CreateObjectData](M_Grasshopper_Kernel_GH_RelevantObjectData_CreateObjectData.htm) |  |
| Public method | [CreateWireData](M_Grasshopper_Kernel_GH_RelevantObjectData_CreateWireData.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)