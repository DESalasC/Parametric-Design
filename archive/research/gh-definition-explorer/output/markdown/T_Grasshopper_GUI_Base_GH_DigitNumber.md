# T_Grasshopper_GUI_Base_GH_DigitNumber

﻿ GH\_DigitNumber Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_DigitNumber Class](../html/T_Grasshopper_GUI_Base_GH_DigitNumber.htm "GH_DigitNumber Class")

[GH\_DigitNumber Constructor](../html/Overload_Grasshopper_GUI_Base_GH_DigitNumber__ctor.htm "GH_DigitNumber Constructor ")

[GH\_DigitNumber Properties](../html/Properties_T_Grasshopper_GUI_Base_GH_DigitNumber.htm "GH_DigitNumber Properties")

[GH\_DigitNumber Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_DigitNumber.htm "GH_DigitNumber Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DigitNumber Class |

Maintains and provides functionality for evaluating and modifying numbers as used in the GH\_DigitScrollerBase control.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTAB8894D6\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.BaseAddLanguageSpecificTextSet("LSTAB8894D6\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DigitNumber

**Namespace:**
 [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DigitNumber
```

```
Public Class GH_DigitNumber
```

AddLanguageTabSet("ID1EBCA");

The GH\_DigitNumber type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DigitNumber(GH\_DigitNumber)](M_Grasshopper_GUI_Base_GH_DigitNumber__ctor.htm) | Create an exact duplicate of another GH\_DigitNumber instance. |
| Public method | [GH\_DigitNumber(Int32)](M_Grasshopper_GUI_Base_GH_DigitNumber__ctor_1.htm) | Create a new GH\_DigitNumber instance with the specified number of decimal places. |
| Public method | [GH\_DigitNumber(Int32, Int32)](M_Grasshopper_GUI_Base_GH_DigitNumber__ctor_2.htm) | Create a new GH\_DigitNumber instance with the specified number of decimal places and a given radix position. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [DigitCount](P_Grasshopper_GUI_Base_GH_DigitNumber_DigitCount.htm) | Gets or sets the amount of digits in this number. |
| Public property | [Epsilon](P_Grasshopper_GUI_Base_GH_DigitNumber_Epsilon.htm) | Gets the smallest possible change. |
| Public property | [IsPrimaryDigitSignificant](P_Grasshopper_GUI_Base_GH_DigitNumber_IsPrimaryDigitSignificant.htm) | Gets whether the primary digit at the given index is significant. |
| Public property | [IsSecondaryDigitSignificant](P_Grasshopper_GUI_Base_GH_DigitNumber_IsSecondaryDigitSignificant.htm) | Gets whether the secondary digit at the given index is significant. |
| Public property | [Maximum](P_Grasshopper_GUI_Base_GH_DigitNumber_Maximum.htm) | Gets the maximum value allowed in this number. |
| Public property | [Minimum](P_Grasshopper_GUI_Base_GH_DigitNumber_Minimum.htm) | Gets the minimum value allowed in this number. |
| Public property | [Offset](P_Grasshopper_GUI_Base_GH_DigitNumber_Offset.htm) | Gets the offset between the primary and secondary digits. |
| Public property | [PrimaryDigits](P_Grasshopper_GUI_Base_GH_DigitNumber_PrimaryDigits.htm) | Gets the internal list of primary digits. Do not modify this list. |
| Public property | [PrimaryPositive](P_Grasshopper_GUI_Base_GH_DigitNumber_PrimaryPositive.htm) | Gets or sets a value indicating whether the number is positive. |
| Public property | [Radix](P_Grasshopper_GUI_Base_GH_DigitNumber_Radix.htm) | Gets or sets the radix point index. A negative radix index disables the radix point, zero is not a valid index. |
| Public property | [RadixIndex](P_Grasshopper_GUI_Base_GH_DigitNumber_RadixIndex.htm) | Gets the mapped radix. |
| Public property | [SecondaryDigits](P_Grasshopper_GUI_Base_GH_DigitNumber_SecondaryDigits.htm) | Gets the internal list of secondary digits. Do not modify this list. |
| Public property | [SecondaryPositive](P_Grasshopper_GUI_Base_GH_DigitNumber_SecondaryPositive.htm) | Gets a value indicating whether the secondary number is positive. |
| Public property | [Value](P_Grasshopper_GUI_Base_GH_DigitNumber_Value.htm) | Gets or sets the value of this number. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AssignOffset](M_Grasshopper_GUI_Base_GH_DigitNumber_AssignOffset.htm) | Assign an offset to a given digit and recursively adjust all leftwards offsets if needed. |
| Public method | [LimitValue](M_Grasshopper_GUI_Base_GH_DigitNumber_LimitValue.htm) | Limits the value to the minimum and maximum domain. |
| Public method | [Reset](M_Grasshopper_GUI_Base_GH_DigitNumber_Reset.htm) | Reset all parts to zero. |
| Public method | [Round](M_Grasshopper_GUI_Base_GH_DigitNumber_Round.htm) | Round the number by cancelling the offset in the proper direction. |
| Public method | [ToString](M_Grasshopper_GUI_Base_GH_DigitNumber_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LSTAB8894D6\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTAB8894D6\_3?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)