# Methods_T_Grasshopper_Kernel_IGH_VariableParameterComponent

﻿ IGH\_VariableParameterComponent Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_VariableParameterComponent Interface](../html/T_Grasshopper_Kernel_IGH_VariableParameterComponent.htm "IGH_VariableParameterComponent Interface")

[IGH\_VariableParameterComponent Methods](../html/Methods_T_Grasshopper_Kernel_IGH_VariableParameterComponent.htm "IGH_VariableParameterComponent Methods")

[CanInsertParameter Method](../html/M_Grasshopper_Kernel_IGH_VariableParameterComponent_CanInsertParameter.htm "CanInsertParameter Method ")

[CanRemoveParameter Method](../html/M_Grasshopper_Kernel_IGH_VariableParameterComponent_CanRemoveParameter.htm "CanRemoveParameter Method ")

[CreateParameter Method](../html/M_Grasshopper_Kernel_IGH_VariableParameterComponent_CreateParameter.htm "CreateParameter Method ")

[DestroyParameter Method](../html/M_Grasshopper_Kernel_IGH_VariableParameterComponent_DestroyParameter.htm "DestroyParameter Method ")

[VariableParameterMaintenance Method](../html/M_Grasshopper_Kernel_IGH_VariableParameterComponent_VariableParameterMaintenance.htm "VariableParameterMaintenance Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_VariableParameterComponent Methods |

The [IGH\_VariableParameterComponent](T_Grasshopper_Kernel_IGH_VariableParameterComponent.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CanInsertParameter](M_Grasshopper_Kernel_IGH_VariableParameterComponent_CanInsertParameter.htm) | This function will get called before an attempt is made to insert a parameter. Since this method is potentially called on Canvas redraws, it must be *fast*. |
| Public method | [CanRemoveParameter](M_Grasshopper_Kernel_IGH_VariableParameterComponent_CanRemoveParameter.htm) | This function will get called before an attempt is made to remove a parameter. Since this method is potentially called on Canvas redraws, it must be *fast*. |
| Public method | [CreateParameter](M_Grasshopper_Kernel_IGH_VariableParameterComponent_CreateParameter.htm) | This function will be called when a new parameter is about to be inserted. You *must* provide a valid parameter or insertion will be skipped. You do not, repeat *not*, need to insert the parameter yourself. |
| Public method | [DestroyParameter](M_Grasshopper_Kernel_IGH_VariableParameterComponent_DestroyParameter.htm) | This function will be called when a parameter is about to be removed. You do not need to do anything, but this would be a good time to remove any event handlers that might be attached to the parameter in question. |
| Public method | [VariableParameterMaintenance](M_Grasshopper_Kernel_IGH_VariableParameterComponent_VariableParameterMaintenance.htm) | This method will be called when a closely related set of variable parameter operations completes. This would be a good time to ensure all Nicknames and parameter properties are correct. This method will also be called upon IO operations such as Open, Paste, Undo and Redo. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_VariableParameterComponent Interface](T_Grasshopper_Kernel_IGH_VariableParameterComponent.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)