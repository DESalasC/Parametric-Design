# M_Grasshopper_Kernel_IGH_VariableParameterComponent_CanRemoveParameter

﻿ IGH\_VariableParameterComponent.CanRemoveParameter Method 

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
| IGH\_VariableParameterComponentAddLanguageSpecificTextSet("LSTC03DF31\_0?cpp=::|nu=.");CanRemoveParameter Method |

This function will get called before an attempt is made to remove a parameter.
Since this method is potentially called on Canvas redraws, it must be *fast*.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool CanRemoveParameter(
	GH_ParameterSide side,
	int index
)
```

```
Function CanRemoveParameter ( 
	side As GH_ParameterSide,
	index As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

side
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTC03DF31\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParameterSide](T_Grasshopper_Kernel_GH_ParameterSide.htm)  
    Parameter side.

index
:   Type: [SystemAddLanguageSpecificTextSet("LSTC03DF31\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Removal index of parameter.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
Return True if your component supports removing a parameter at the given location.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_VariableParameterComponent Interface](T_Grasshopper_Kernel_IGH_VariableParameterComponent.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)