# T_Grasshopper_Kernel_IGH_TaskCapableComponent

﻿ IGH\_TaskCapableComponent Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_TaskCapableComponent Interface](../html/T_Grasshopper_Kernel_IGH_TaskCapableComponent.htm "IGH_TaskCapableComponent Interface")

[IGH\_TaskCapableComponent Properties](../html/Properties_T_Grasshopper_Kernel_IGH_TaskCapableComponent.htm "IGH_TaskCapableComponent Properties")

[IGH\_TaskCapableComponent Methods](../html/Methods_T_Grasshopper_Kernel_IGH_TaskCapableComponent.htm "IGH_TaskCapableComponent Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_TaskCapableComponent Interface |

GH\_Component that can choose to support the use of Tasks to compute solutions
When UseTasks returns true, the component has it's SolveInstance enumeration called
twice. The first pass (InPreSolve=True) is intended solely for collecting data and
starting calculation tasks. The second pass (InPreSolve=False) takes results or the
tasks and sets the output.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_TaskCapableComponent : IGH_Component
```

```
Public Interface IGH_TaskCapableComponent
	Inherits IGH_Component
```

AddLanguageTabSet("ID0EBCA");

The IGH\_TaskCapableComponent type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [InConstructor](P_Grasshopper_Kernel_IGH_Component_InConstructor.htm) | Gets the constructor flag for this instance. If InConstructor = True, it means the component is still registering parameters and the layout is not yet complete. (Inherited from [IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm).) |
| Public property | [InPreSolve](P_Grasshopper_Kernel_IGH_TaskCapableComponent_InPreSolve.htm) | Is set to True by the framework right before a "use tasks" pass is made on SolveIntance calls. When True, SolveInstance should be using Tasks to start calculations on input data. When False, SolveInstance should be setting the output data by either using the result of a task or directly computing the results. |
| Public property | [IsValidMasterParameterIndex](P_Grasshopper_Kernel_IGH_Component_IsValidMasterParameterIndex.htm) | Gets whether the MasterParameterIndex property identifies a valid parameter. (Inherited from [IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm).) |
| Public property | [MasterParameterIndex](P_Grasshopper_Kernel_IGH_Component_MasterParameterIndex.htm) | Gets or sets the master parameter index override. Negative indices or indices larger than or equal to the input parameter count will be ignored and regular master parameter detection will kick in. (Inherited from [IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm).) |
| Public property | [Message](P_Grasshopper_Kernel_IGH_Component_Message.htm) | Gets or sets a custom message to be displayed underneath the component. (Inherited from [IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm).) |
| Public property | [Params](P_Grasshopper_Kernel_IGH_Component_Params.htm) | Gets the Params object that managed input and output parameters. (Inherited from [IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm).) |
| Public property | [RunCount](P_Grasshopper_Kernel_IGH_Component_RunCount.htm) | Gets a value indicating how many times the SolveInstance method was called on this component during the last solution. This property will return -1 if no valid runcount is available. (Inherited from [IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm).) |
| Public property | [UseTasks](P_Grasshopper_Kernel_IGH_TaskCapableComponent_UseTasks.htm) | Returns True if the component is set to support tasks. Components can have this feature turned on/off. Note that even if UseTasks returns True, there is a chance that a multipass task based solution may not be invoked depending on if multiple calls need to be made during enumeration. You must pay attention to the value of InPreSolve during SolveInstance. The set version of this property can be called by the framework if we want to provide a technique to globally turn on/off task support for all components in a definition. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [RequestTaskCancellation](M_Grasshopper_Kernel_IGH_TaskCapableComponent_RequestTaskCancellation.htm) | Called by the framework when solving has been interrupted and tasks do not need to complete. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)