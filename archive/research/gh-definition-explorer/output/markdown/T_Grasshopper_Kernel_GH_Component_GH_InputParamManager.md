# T_Grasshopper_Kernel_GH_Component_GH_InputParamManager

﻿ GH\_Component.GH\_InputParamManager Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component.GH\_InputParamManager Class](../html/T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_Component.GH_InputParamManager Class")

[GH\_InputParamManager Properties](../html/Properties_T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_InputParamManager Properties")

[GH\_InputParamManager Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_InputParamManager.htm "GH_InputParamManager Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAddLanguageSpecificTextSet("LST7C150B30\_0?cpp=::|nu=.");GH\_InputParamManager Class |

This class is used during Component construction to add input parameters.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST7C150B30\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  GH\_ParamManager  
    Grasshopper.KernelAddLanguageSpecificTextSet("LST7C150B30\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ComponentAddLanguageSpecificTextSet("LST7C150B30\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InputParamManager

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected class GH_InputParamManager : GH_ParamManager
```

```
Protected Class GH_InputParamManager
	Inherits GH_ParamManager
```

AddLanguageTabSet("ID1EBCA");

The GH\_ComponentAddLanguageSpecificTextSet("LST7C150B30\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InputParamManager type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Param](P_Grasshopper_Kernel_GH_Component_GH_InputParamManager_Param.htm) | Gets the input parameter at the given index. (Overrides GH\_ParamManager.Param.) |
| Public property | [ParamCount](P_Grasshopper_Kernel_GH_Component_GH_InputParamManager_ParamCount.htm) | Returns the number of input parameters already part of this component. (Overrides GH\_ParamManager.ParamCount.) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddAngleParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddAngleParameter.htm) | Add a floating point Number parameter to the input list of this component. The parameter will be aware that it is representing angles. |
| Public method | [AddAngleParameter(String, String, String, GH\_ParamAccess, IEnumerableAddLanguageSpecificTextSet("LST7C150B30\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");DoubleAddLanguageSpecificTextSet("LST7C150B30\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddAngleParameter_1.htm) | Add a floating point Number parameter to the input list of this component. The parameter will be aware that it is representing angles. |
| Public method | [AddAngleParameter(String, String, String, GH\_ParamAccess, Double)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddAngleParameter_2.htm) | Add a floating point Number parameter to the input list of this component. The parameter will be aware that it is representing angles. |
| Public method | [AddArcParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddArcParameter.htm) | Add a 3D Arc parameter to the input list of this component. |
| Public method | [AddArcParameter(String, String, String, GH\_ParamAccess, Arc)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddArcParameter_1.htm) | Add a 3D Arc parameter to the input list of this component. |
| Public method | [AddBooleanParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBooleanParameter.htm) | Add a Boolean parameter to the input list of this component. |
| Public method | [AddBooleanParameter(String, String, String, GH\_ParamAccess, Boolean)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBooleanParameter_1.htm) | Add a Boolean parameter to the input list of this component. |
| Public method | [AddBooleanParameter(String, String, String, GH\_ParamAccess, IEnumerableAddLanguageSpecificTextSet("LST7C150B30\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");BooleanAddLanguageSpecificTextSet("LST7C150B30\_8?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBooleanParameter_2.htm) | Add a Boolean parameter to the input list of this component. |
| Public method | [AddBoxParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBoxParameter.htm) | Add a 3D Box parameter to the input list of this component. |
| Public method | [AddBoxParameter(String, String, String, GH\_ParamAccess, Box)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBoxParameter_1.htm) | Add a 3D Box parameter to the input list of this component. |
| Public method | [AddBrepParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddBrepParameter.htm) | Add a 3D Brep parameter to the input list of this component. Brep parameters can handle both trimmed and untrimmed single or multi-faced Breps. |
| Public method | [AddCircleParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddCircleParameter.htm) | Add a 3D Circle parameter to the input list of this component. |
| Public method | [AddCircleParameter(String, String, String, GH\_ParamAccess, Circle)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddCircleParameter_1.htm) | Add a 3D Circle parameter to the input list of this component. |
| Public method | [AddColourParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddColourParameter.htm) | Add an ARGB Colour parameter to the input list of this component. |
| Public method | [AddColourParameter(String, String, String, GH\_ParamAccess, IEnumerableAddLanguageSpecificTextSet("LST7C150B30\_9?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");ColorAddLanguageSpecificTextSet("LST7C150B30\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddColourParameter_1.htm) | Add an ARGB Colour parameter to the input list of this component. |
| Public method | [AddColourParameter(String, String, String, GH\_ParamAccess, Color)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddColourParameter_2.htm) | Add an ARGB Colour parameter to the input list of this component. |
| Public method | [AddComplexNumberParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddComplexNumberParameter.htm) | Add a Complex Number parameter to the input list of this component. |
| Public method | [AddComplexNumberParameter(String, String, String, GH\_ParamAccess, GH\_ComplexNumber)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddComplexNumberParameter_1.htm) | Add a Complex Number parameter to the input list of this component. |
| Public method | [AddCultureParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddCultureParameter.htm) | Add a Cultue parameter to the input list of this component. |
| Public method | [AddCultureParameter(String, String, String, GH\_ParamAccess, CultureInfo)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddCultureParameter_1.htm) | Add a Culture parameter to the input list of this component. |
| Public method | [AddCurveParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddCurveParameter.htm) | Add a 3D Curve parameter to the input list of this component. Curve parameters can handle all curve types (Lines, Polylines, Circles, Arcs, NurbsCurves etc.) |
| Public method | [AddFieldParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddFieldParameter.htm) | Add a Field parameter to the input list of this component. |
| Public method | [AddGenericParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddGenericParameter.htm) | Add a Generic parameter to the input list of this component. Generic parameters can handle all types of data. |
| Public method | [AddGeometryParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddGeometryParameter.htm) | Add a generic 3D Geometry parameter to the input list of this component. Geometry parameters can handle all types that represent actual shapes. |
| Public method | [AddGroupParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddGroupParameter.htm) | Add a Transform Group parameter to the input list of this component. Groups are collections of geometry that are transformed as one, they are not the same as Rhino groups. |
| Public method | [AddIntegerParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntegerParameter.htm) | Add a Integer parameter to the input list of this component. |
| Public method | [AddIntegerParameter(String, String, String, GH\_ParamAccess, IEnumerableAddLanguageSpecificTextSet("LST7C150B30\_11?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");Int32AddLanguageSpecificTextSet("LST7C150B30\_12?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntegerParameter_1.htm) | Add a Integer parameter to the input list of this component. |
| Public method | [AddIntegerParameter(String, String, String, GH\_ParamAccess, Int32)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntegerParameter_2.htm) | Add a Integer parameter to the input list of this component. |
| Public method | [AddInterval2DParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddInterval2DParameter.htm) | Add an Interval2D (i.e. uv domain) parameter to the input list of this component. |
| Public method | [AddIntervalParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntervalParameter.htm) | Add an Interval (i.e. numeric domain) parameter to the input list of this component. |
| Public method | [AddIntervalParameter(String, String, String, GH\_ParamAccess, Interval)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntervalParameter_1.htm) | Add an Interval (i.e. numeric domain) parameter to the input list of this component. |
| Public method | [AddIntervalParameter(String, String, String, GH\_ParamAccess, IEnumerableAddLanguageSpecificTextSet("LST7C150B30\_13?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IntervalAddLanguageSpecificTextSet("LST7C150B30\_14?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddIntervalParameter_2.htm) | Add an Interval (i.e. numeric domain) parameter to the input list of this component. |
| Public method | [AddLineParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddLineParameter.htm) | Add a 3D Line parameter to the input list of this component. |
| Public method | [AddLineParameter(String, String, String, GH\_ParamAccess, Line)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddLineParameter_1.htm) | Add a 3D Line parameter to the input list of this component. |
| Public method | [AddMatrixParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddMatrixParameter.htm) | Add a Matrix parameter to the input list of this component. |
| Public method | [AddMeshFaceParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddMeshFaceParameter.htm) | Add a topological MeshFace parameter to the input list of this component. |
| Public method | [AddMeshParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddMeshParameter.htm) | Add a 3D Mesh parameter to the input list of this component. |
| Public method | [AddNumberParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddNumberParameter.htm) | Add a floating point Number parameter to the input list of this component. |
| Public method | [AddNumberParameter(String, String, String, GH\_ParamAccess, IEnumerableAddLanguageSpecificTextSet("LST7C150B30\_15?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");DoubleAddLanguageSpecificTextSet("LST7C150B30\_16?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddNumberParameter_1.htm) | Add a floating point Number parameter to the input list of this component. |
| Public method | [AddNumberParameter(String, String, String, GH\_ParamAccess, Double)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddNumberParameter_2.htm) | Add a floating point Number parameter to the input list of this component. |
| Public method | [AddParameter(IGH\_Param)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddParameter.htm) | Generic parameter addition. If you cannot use one of the utility methods provided by this class, you can register a customized parameter using this method. |
| Public method | [AddParameter(IGH\_Param, String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddParameter_1.htm) | Generic parameter addition. If you cannot use one of the utility methods provided by this class, you can register a customized parameter using this method. |
| Public method | [AddPathParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPathParameter.htm) | Add a Data Path parameter to the input list of this component. |
| Public method | [AddPlaneParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPlaneParameter.htm) | Add a 3D Plane parameter to the input list of this component. |
| Public method | [AddPlaneParameter(String, String, String, GH\_ParamAccess, Plane)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPlaneParameter_1.htm) | Add a 3D Plane parameter to the input list of this component. |
| Public method | [AddPointParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPointParameter.htm) | Add a 3D Point parameter to the input list of this component. |
| Public method | [AddPointParameter(String, String, String, GH\_ParamAccess, Point3d)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPointParameter_1.htm) | Register a new 3D point param with a single default coordinate. |
| Public method | [AddPointParameter(String, String, String, GH\_ParamAccess, IEnumerableAddLanguageSpecificTextSet("LST7C150B30\_17?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");Point3dAddLanguageSpecificTextSet("LST7C150B30\_18?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddPointParameter_2.htm) | Register a new 3D point param with multiple default coordinates. |
| Public method | [AddRectangleParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddRectangleParameter.htm) | Add a 3D Rectangle parameter to the input list of this component. |
| Public method | [AddRectangleParameter(String, String, String, GH\_ParamAccess, Rectangle3d)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddRectangleParameter_1.htm) | Add a 3D Rectangle parameter to the input list of this component. |
| Public method | [AddScriptVariableParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddScriptVariableParameter.htm) | Add a Script Variable parameter to the input list of this component. Script variable parameters are used almost exclusively in VB/C#/Python components so you probably don't want this one. |
| Public method | [AddSubDParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddSubDParameter.htm) | Add a 3D Sub-D parameter to the input list of this component. |
| Public method | [AddSurfaceParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddSurfaceParameter.htm) | Add a 3D Surface parameter to the input list of this component. Surface parameters can handle both trimmed and untrimmed single-faced Breps. |
| Public method | [AddTextParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddTextParameter.htm) | Add a Text parameter to the input list of this component. |
| Public method | [AddTextParameter(String, String, String, GH\_ParamAccess, IEnumerableAddLanguageSpecificTextSet("LST7C150B30\_19?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LST7C150B30\_20?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddTextParameter_1.htm) | Add a Text parameter to the input list of this component. |
| Public method | [AddTextParameter(String, String, String, GH\_ParamAccess, String)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddTextParameter_2.htm) | Add a Text parameter to the input list of this component. |
| Public method | [AddTimeParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddTimeParameter.htm) | Add a Time parameter to the input list of this component. |
| Public method | [AddTimeParameter(String, String, String, GH\_ParamAccess, DateTime)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddTimeParameter_1.htm) | Add a Time parameter to the input list of this component. |
| Public method | [AddTransformParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddTransformParameter.htm) | Add a Transformation parameter to the input list of this component. |
| Public method | [AddVectorParameter(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddVectorParameter.htm) | Add a 3D Vector parameter to the input list of this component. |
| Public method | [AddVectorParameter(String, String, String, GH\_ParamAccess, Vector3d)](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_AddVectorParameter_1.htm) | Add a 3D Vector parameter to the input list of this component. |
| Public method | [HideParameter](M_Grasshopper_Kernel_GH_Component_GH_InputParamManager_HideParameter.htm) | Hide a specific input parameter. If the parameter at the given index implements IGH\_PreviewObject then the Hidden flag will be set to True. Otherwise, nothing will happen. (Overrides GH\_ParamManager.HideParameter(Int32).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)