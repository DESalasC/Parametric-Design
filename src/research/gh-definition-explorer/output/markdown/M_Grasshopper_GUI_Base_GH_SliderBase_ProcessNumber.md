# M_Grasshopper_GUI_Base_GH_SliderBase_ProcessNumber

﻿ GH\_SliderBase.ProcessNumber Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_SliderBase Class](../html/T_Grasshopper_GUI_Base_GH_SliderBase.htm "GH_SliderBase Class")

[GH\_SliderBase Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_SliderBase.htm "GH_SliderBase Methods")

[FixDomain Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_FixDomain.htm "FixDomain Method ")

[FixValue Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_FixValue.htm "FixValue Method ")

[HandleTextInputAccepted Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_HandleTextInputAccepted.htm "HandleTextInputAccepted Method ")

[KeyDown Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_KeyDown.htm "KeyDown Method ")

[MouseDown Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_MouseDown.htm "MouseDown Method ")

[MouseMove Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_MouseMove.htm "MouseMove Method ")

[MouseUp Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_MouseUp.htm "MouseUp Method ")

[OnValueChanged Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_OnValueChanged.htm "OnValueChanged Method ")

[ProcessNumber Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_ProcessNumber.htm "ProcessNumber Method ")

[Render Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_Render.htm "Render Method ")

[SetSnapRanges Method](../html/M_Grasshopper_GUI_Base_GH_SliderBase_SetSnapRanges.htm "SetSnapRanges Method ")

[ShowTextInputBox Method](../html/Overload_Grasshopper_GUI_Base_GH_SliderBase_ShowTextInputBox.htm "ShowTextInputBox Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SliderBaseAddLanguageSpecificTextSet("LST7D58D9B5\_0?cpp=::|nu=.");ProcessNumber Method |

Process a number using the given slider characteristics.

**Namespace:**
 [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static decimal ProcessNumber(
	decimal val,
	GH_SliderAccuracy accuracy,
	int digits
)
```

```
Public Shared Function ProcessNumber ( 
	val As Decimal,
	accuracy As GH_SliderAccuracy,
	digits As Integer
) As Decimal
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

val
:   Type: [SystemAddLanguageSpecificTextSet("LST7D58D9B5\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Decimal](https://docs.microsoft.com/dotnet/api/system.decimal)  
    Number to process.

accuracy
:   Type: [Grasshopper.GUI.BaseAddLanguageSpecificTextSet("LST7D58D9B5\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SliderAccuracy](T_Grasshopper_GUI_Base_GH_SliderAccuracy.htm)  
    Slider rounding accuracy.

digits
:   Type: [SystemAddLanguageSpecificTextSet("LST7D58D9B5\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Number of digits to use for floating point rounding.

#### Return Value

Type: [Decimal](https://docs.microsoft.com/dotnet/api/system.decimal)  
Processed number.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_SliderBase Class](T_Grasshopper_GUI_Base_GH_SliderBase.htm)

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)