# T_Grasshopper_GUI_Gradient_GH_Grip

﻿ GH\_Grip Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Gradient](../html/N_Grasshopper_GUI_Gradient.htm "Grasshopper.GUI.Gradient")

[GH\_Grip Class](../html/T_Grasshopper_GUI_Gradient_GH_Grip.htm "GH_Grip Class")

[GH\_Grip Constructor](../html/Overload_Grasshopper_GUI_Gradient_GH_Grip__ctor.htm "GH_Grip Constructor ")

[GH\_Grip Properties](../html/Properties_T_Grasshopper_GUI_Gradient_GH_Grip.htm "GH_Grip Properties")

[GH\_Grip Methods](../html/Methods_T_Grasshopper_GUI_Gradient_GH_Grip.htm "GH_Grip Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Grip Class |

Represents a grip in a gradient.
A grip defines both where and how the colour of a gradient changes.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTEB05ED76\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.GradientAddLanguageSpecificTextSet("LSTEB05ED76\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Grip

**Namespace:**
 [Grasshopper.GUI.Gradient](N_Grasshopper_GUI_Gradient.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Grip : IComparable<GH_Grip>, 
	GH_ISerializable
```

```
Public Class GH_Grip
	Implements IComparable(Of GH_Grip), GH_ISerializable
```

AddLanguageTabSet("ID1EBCA");

The GH\_Grip type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_GripAddLanguageSpecificTextSet("LSTEB05ED76\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_Gradient_GH_Grip__ctor.htm) | Initializes a new instance of the GH\_Grip class |
| Public method | [GH\_Grip(GH\_Grip)](M_Grasshopper_GUI_Gradient_GH_Grip__ctor_1.htm) | Initializes a new instance of the GH\_Grip class |
| Public method | [GH\_Grip(Double, Color)](M_Grasshopper_GUI_Gradient_GH_Grip__ctor_2.htm) | Initializes a new instance of the GH\_Grip class |
| Public method | [GH\_Grip(Double, Color, Color)](M_Grasshopper_GUI_Gradient_GH_Grip__ctor_3.htm) | Initializes a new instance of the GH\_Grip class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ColourLeft](P_Grasshopper_GUI_Gradient_GH_Grip_ColourLeft.htm) | Gets the colour to the left of this grip. |
| Public property | [ColourRight](P_Grasshopper_GUI_Gradient_GH_Grip_ColourRight.htm) | Gets the colour to the right of this grip. |
| Public property | [GripId](P_Grasshopper_GUI_Gradient_GH_Grip_GripId.htm) | Gets the Grip ID. |
| Public property | [IsValid](P_Grasshopper_GUI_Gradient_GH_Grip_IsValid.htm) | Gets whether this grip is valid. A valid grip must have a non-empty Id and a non-NaN parameter. |
| Public property | [Parameter](P_Grasshopper_GUI_Gradient_GH_Grip_Parameter.htm) | Gets or sets the numeric parameter of the grip. |
| Public property | [Selected](P_Grasshopper_GUI_Gradient_GH_Grip_Selected.htm) | Gets or sets whether this grip is selected. Selection state is not (de)serialized. |
| Public property | [Type](P_Grasshopper_GUI_Gradient_GH_Grip_Type.htm) | Gets whether the colour across this grip is smooth. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Blend](M_Grasshopper_GUI_Gradient_GH_Grip_Blend.htm) |  |
| Public method | [CompareTo](M_Grasshopper_GUI_Gradient_GH_Grip_CompareTo.htm) |  |
| Public method | [MutateId](M_Grasshopper_GUI_Gradient_GH_Grip_MutateId.htm) | Create a new grip ID. |
| Public method | [Read](M_Grasshopper_GUI_Gradient_GH_Grip_Read.htm) |  |
| Public method | [Write](M_Grasshopper_GUI_Gradient_GH_Grip_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Gradient Namespace](N_Grasshopper_GUI_Gradient.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)