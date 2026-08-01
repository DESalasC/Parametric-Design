# T_Grasshopper_GUI_GH_RotationalTuningData_1

﻿ GH\_RotationalTuningData(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_RotationalTuningData(T) Class](../html/T_Grasshopper_GUI_GH_RotationalTuningData_1.htm "GH_RotationalTuningData(T) Class")

[GH\_RotationalTuningData(T) Constructor](../html/Overload_Grasshopper_GUI_GH_RotationalTuningData_1__ctor.htm "GH_RotationalTuningData(T) Constructor ")

[GH\_RotationalTuningData(T) Properties](../html/Properties_T_Grasshopper_GUI_GH_RotationalTuningData_1.htm "GH_RotationalTuningData(T) Properties")

[GH\_RotationalTuningData(T) Methods](../html/Methods_T_Grasshopper_GUI_GH_RotationalTuningData_1.htm "GH_RotationalTuningData(T) Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_RotationalTuningDataAddLanguageSpecificTextSet("LST7722F6FC\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST7722F6FC\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

Utility class for keeping track of rotational mouse events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST7722F6FC\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LST7722F6FC\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RotationalTuningDataAddLanguageSpecificTextSet("LST7722F6FC\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7722F6FC\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_RotationalTuningData<T>
```

```
Public Class GH_RotationalTuningData(Of T)
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T
:   Basic type for initial conditions.

The GH\_RotationalTuningDataAddLanguageSpecificTextSet("LST7722F6FC\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7722F6FC\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_RotationalTuningDataAddLanguageSpecificTextSet("LST7722F6FC\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7722F6FC\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(T, PointF)](M_Grasshopper_GUI_GH_RotationalTuningData_1__ctor.htm) | Create a new instance of the rotational tuning data. |
| Public method | [GH\_RotationalTuningDataAddLanguageSpecificTextSet("LST7722F6FC\_10?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7722F6FC\_11?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(T, PointF, PointF)](M_Grasshopper_GUI_GH_RotationalTuningData_1__ctor_1.htm) | Create a new instance of the rotational tuning data. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Frame](P_Grasshopper_GUI_GH_RotationalTuningData_1_Frame.htm) | Gets the frame at the given index. |
| Public property | [FrameCount](P_Grasshopper_GUI_GH_RotationalTuningData_1_FrameCount.htm) | Gets the total number of recorded frames. |
| Public property | [InitialValue](P_Grasshopper_GUI_GH_RotationalTuningData_1_InitialValue.htm) | Gets the initial value. |
| Public property | [Pivot](P_Grasshopper_GUI_GH_RotationalTuningData_1_Pivot.htm) | Gets or sets the rotational pivot. You only need to set this if the pivot changes. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddFrame](M_Grasshopper_GUI_GH_RotationalTuningData_1_AddFrame.htm) | Grow the tuning track by one point and compute the angle. |
| Public method | [TotalAngle](M_Grasshopper_GUI_GH_RotationalTuningData_1_TotalAngle.htm) | Compute the total angle from the first to the last frame. |
| Public method | [TotalTurns](M_Grasshopper_GUI_GH_RotationalTuningData_1_TotalTurns.htm) | Compute the total number of full turns from the first to the last frame. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)