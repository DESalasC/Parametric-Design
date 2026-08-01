# M_Grasshopper_GUI_Base_GH_DigitNumber_AssignOffset

﻿ GH\_DigitNumber.AssignOffset Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_DigitNumber Class](../html/T_Grasshopper_GUI_Base_GH_DigitNumber.htm "GH_DigitNumber Class")

[GH\_DigitNumber Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_DigitNumber.htm "GH_DigitNumber Methods")

[AssignOffset Method](../html/M_Grasshopper_GUI_Base_GH_DigitNumber_AssignOffset.htm "AssignOffset Method ")

[LimitValue Method](../html/M_Grasshopper_GUI_Base_GH_DigitNumber_LimitValue.htm "LimitValue Method ")

[Reset Method](../html/M_Grasshopper_GUI_Base_GH_DigitNumber_Reset.htm "Reset Method ")

[Round Method](../html/M_Grasshopper_GUI_Base_GH_DigitNumber_Round.htm "Round Method ")

[ToString Method](../html/M_Grasshopper_GUI_Base_GH_DigitNumber_ToString.htm "ToString Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DigitNumberAddLanguageSpecificTextSet("LST1E44DAC8\_0?cpp=::|nu=.");AssignOffset Method |

Assign an offset to a given digit and recursively adjust all leftwards offsets if needed.

**Namespace:**
 [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool AssignOffset(
	int index,
	decimal offset
)
```

```
Public Function AssignOffset ( 
	index As Integer,
	offset As Decimal
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

index
:   Type: [SystemAddLanguageSpecificTextSet("LST1E44DAC8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of digit to offset.

offset
:   Type: [SystemAddLanguageSpecificTextSet("LST1E44DAC8\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Decimal](https://docs.microsoft.com/dotnet/api/system.decimal)  
    New offset for digit.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DigitNumber Class](T_Grasshopper_GUI_Base_GH_DigitNumber.htm)

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)