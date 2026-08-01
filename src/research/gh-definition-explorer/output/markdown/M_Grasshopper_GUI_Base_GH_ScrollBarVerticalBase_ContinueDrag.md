# M_Grasshopper_GUI_Base_GH_ScrollBarVerticalBase_ContinueDrag

﻿ GH\_ScrollBarVerticalBase.ContinueDrag Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_ScrollBarVerticalBase Class](../html/T_Grasshopper_GUI_Base_GH_ScrollBarVerticalBase.htm "GH_ScrollBarVerticalBase Class")

[GH\_ScrollBarVerticalBase Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_ScrollBarVerticalBase.htm "GH_ScrollBarVerticalBase Methods")

[BeginDrag Method](../html/M_Grasshopper_GUI_Base_GH_ScrollBarVerticalBase_BeginDrag.htm "BeginDrag Method ")

[ContinueDrag Method](../html/M_Grasshopper_GUI_Base_GH_ScrollBarVerticalBase_ContinueDrag.htm "ContinueDrag Method ")

[ScrollBar Method](../html/Overload_Grasshopper_GUI_Base_GH_ScrollBarVerticalBase_ScrollBar.htm "ScrollBar Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ScrollBarVerticalBaseAddLanguageSpecificTextSet("LSTA1B9C69B\_0?cpp=::|nu=.");ContinueDrag Method |

Continue a drag operation.

**Namespace:**
 [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool ContinueDrag(
	double position
)
```

```
Public Function ContinueDrag ( 
	position As Double
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

position
:   Type: [SystemAddLanguageSpecificTextSet("LSTA1B9C69B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    New offset hint.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the drag resulted in an offset change, false if not.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ScrollBarVerticalBase Class](T_Grasshopper_GUI_Base_GH_ScrollBarVerticalBase.htm)

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)