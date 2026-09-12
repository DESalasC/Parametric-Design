# M_Grasshopper_Kernel_Types_GH_Field_SolveStep

﻿ GH\_Field.SolveStep Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Field Class](../html/T_Grasshopper_Kernel_Types_GH_Field.htm "GH_Field Class")

[GH\_Field Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Field.htm "GH_Field Methods")

[CastFrom Method](../html/M_Grasshopper_Kernel_Types_GH_Field_CastFrom.htm "CastFrom Method ")

[CastTo(T) Method](../html/M_Grasshopper_Kernel_Types_GH_Field_CastTo__1.htm "CastTo(T) Method ")

[CurvatureAt Method](../html/M_Grasshopper_Kernel_Types_GH_Field_CurvatureAt.htm "CurvatureAt Method ")

[DrawViewportMeshes Method](../html/M_Grasshopper_Kernel_Types_GH_Field_DrawViewportMeshes.htm "DrawViewportMeshes Method ")

[DrawViewportWires Method](../html/M_Grasshopper_Kernel_Types_GH_Field_DrawViewportWires.htm "DrawViewportWires Method ")

[Duplicate Method](../html/M_Grasshopper_Kernel_Types_GH_Field_Duplicate.htm "Duplicate Method ")

[EmitProxy Method](../html/M_Grasshopper_Kernel_Types_GH_Field_EmitProxy.htm "EmitProxy Method ")

[Read Method](../html/M_Grasshopper_Kernel_Types_GH_Field_Read.htm "Read Method ")

[ScriptVariable Method](../html/M_Grasshopper_Kernel_Types_GH_Field_ScriptVariable.htm "ScriptVariable Method ")

[SolveStep Method](../html/M_Grasshopper_Kernel_Types_GH_Field_SolveStep.htm "SolveStep Method ")

[SolveSteps Method](../html/M_Grasshopper_Kernel_Types_GH_Field_SolveSteps.htm "SolveSteps Method ")

[TensorAt Method](../html/M_Grasshopper_Kernel_Types_GH_Field_TensorAt.htm "TensorAt Method ")

[ToString Method](../html/M_Grasshopper_Kernel_Types_GH_Field_ToString.htm "ToString Method ")

[Write Method](../html/M_Grasshopper_Kernel_Types_GH_Field_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FieldAddLanguageSpecificTextSet("LST1B64ECB2\_0?cpp=::|nu=.");SolveStep Method |

Move a point through the field.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Vector3d SolveStep(
	Point3d location,
	double factor,
	GH_DifferentialSolver method
)
```

```
Public Function SolveStep ( 
	location As Point3d,
	factor As Double,
	method As GH_DifferentialSolver
) As Vector3d
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

location
:   Type: Point3d  
    Point to move from.

factor
:   Type: [SystemAddLanguageSpecificTextSet("LST1B64ECB2\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Multiplication factor to apply to sampling. A low factor results in more accurate sampling, but smaller steps.

method
:   Type: [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST1B64ECB2\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DifferentialSolver](T_Grasshopper_Kernel_Types_GH_DifferentialSolver.htm)  
    Estimator to use.

#### Return Value

Type: Vector3d  
New point location.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Field Class](T_Grasshopper_Kernel_Types_GH_Field.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)