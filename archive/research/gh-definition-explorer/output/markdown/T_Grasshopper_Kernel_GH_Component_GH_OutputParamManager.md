# T_Grasshopper_Kernel_GH_Component_GH_OutputParamManager

﻿ GH\_Component.GH\_OutputParamManager Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component.GH\_OutputParamManager Class](../html/T_Grasshopper_Kernel_GH_Component_GH_OutputParamManager.htm "GH_Component.GH_OutputParamManager Class")

[GH\_OutputParamManager Properties](../html/Properties_T_Grasshopper_Kernel_GH_Component_GH_OutputParamManager.htm "GH_OutputParamManager Properties")

[GH\_OutputParamManager Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component_GH_OutputParamManager.htm "GH_OutputParamManager Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAddLanguageSpecificTextSet("LST9DD92BA6\_0?cpp=::|nu=.");GH\_OutputParamManager Class |

This class is used during Component construction to add output parameters.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST9DD92BA6\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  GH\_ParamManager  
    Grasshopper.KernelAddLanguageSpecificTextSet("LST9DD92BA6\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ComponentAddLanguageSpecificTextSet("LST9DD92BA6\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_OutputParamManager

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected class GH_OutputParamManager : GH_ParamManager
```

```
Protected Class GH_OutputParamManager
	Inherits GH_ParamManager
```

AddLanguageTabSet("ID1EBCA");

The GH\_ComponentAddLanguageSpecificTextSet("LST9DD92BA6\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_OutputParamManager type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Param](P_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Param.htm) | Gets the output parameter at the given index. (Overrides GH\_ParamManager.Param.) |
| Public property | [ParamCount](P_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_ParamCount.htm) | Returns the number of output parameters already part of this component. (Overrides GH\_ParamManager.ParamCount.) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddArcParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddArcParameter.htm) | Add a 3D Arc parameter to the output list of this component. |
| Public method | [AddBooleanParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddBooleanParameter.htm) | Add a Boolean parameter to the output list of this component. |
| Public method | [AddBoxParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddBoxParameter.htm) | Add a 3D Box parameter to the output list of this component. |
| Public method | [AddBrepParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddBrepParameter.htm) | Add a Brep parameter to the output list of this component. Brep parameters can handle both trimmed and untrimmed single or multi-faced Breps. |
| Public method | [AddCircleParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddCircleParameter.htm) | Add a 3D Circle parameter to the output list of this component. |
| Public method | [AddColourParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddColourParameter.htm) | Add a ARGB Colour parameter to the output list of this component. |
| Public method | [AddComplexNumberParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddComplexNumberParameter.htm) | Add a Complex Number parameter to the output list of this component. |
| Public method | [AddCultureParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddCultureParameter.htm) | Add a Culture parameter to the output list of this component. |
| Public method | [AddCurveParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddCurveParameter.htm) | Add a Curve parameter to the output list of this component. Curve parameters can handle all curve types (Lines, Polylines, Circles, Arcs, NurbsCurves etc.) |
| Public method | [AddFieldParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddFieldParameter.htm) | Add a Field parameter to the output list of this component. |
| Public method | [AddGenericParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddGenericParameter.htm) | Add a Generic parameter to the output list of this component. Generic parameters can handle all types of data. |
| Public method | [AddGeometryParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddGeometryParameter.htm) | Add a Geometry parameter to the output list of this component. Geometry parameters can handle all types that represent actual shapes. |
| Public method | [AddGroupParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddGroupParameter.htm) | Add a Transform Group parameter to the output list of this component. Groups are collections of geometry that are transformed as one, they are not the same as Rhino groups. |
| Public method | [AddIntegerParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddIntegerParameter.htm) | Add a Integer parameter to the output list of this component. |
| Public method | [AddInterval2DParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddInterval2DParameter.htm) | Add a Interval2D (i.e. uv domain) parameter to the output list of this component. |
| Public method | [AddIntervalParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddIntervalParameter.htm) | Add a Interval (i.e. numeric domain) parameter to the output list of this component. |
| Public method | [AddLineParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddLineParameter.htm) | Add a 3D Line parameter to the output list of this component. |
| Public method | [AddMatrixParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddMatrixParameter.htm) | Add a Matrix parameter to the output list of this component. |
| Public method | [AddMeshFaceParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddMeshFaceParameter.htm) | Add a topological MeshFace parameter to the output list of this component. |
| Public method | [AddMeshParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddMeshParameter.htm) | Add a Mesh parameter to the output list of this component. |
| Public method | [AddNumberParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddNumberParameter.htm) | Add a floating point Number parameter to the output list of this component. |
| Public method | [AddParameter(IGH\_Param)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddParameter.htm) | Generic parameter addition. If you cannot use one of the utility methods provided by this class, you can register a customized parameter using this method. |
| Public method | [AddParameter(IGH\_Param, String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddParameter_1.htm) | Generic parameter addition. If you cannot use one of the utility methods provided by this class, you can register a customized parameter using this method. |
| Public method | [AddPathParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddPathParameter.htm) | Add a Data Path parameter to the output list of this component. |
| Public method | [AddPlaneParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddPlaneParameter.htm) | Add a 3D Plane parameter to the output list of this component. |
| Public method | [AddPointParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddPointParameter.htm) | Add a 3D Point parameter to the output list of this component. |
| Public method | [AddRectangleParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddRectangleParameter.htm) | Add a 3D Rectangle parameter to the output list of this component. |
| Public method | [AddSubDParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddSubDParameter.htm) | Add a Sub-D parameter to the output list of this component. |
| Public method | [AddSurfaceParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddSurfaceParameter.htm) | Add a Surface parameter to the output list of this component. Surface parameters can handle both trimmed and untrimmed single-faced Breps. |
| Public method | [AddTextParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddTextParameter.htm) | Add a Text parameter to the output list of this component. |
| Public method | [AddTimeParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddTimeParameter.htm) | Add a Time parameter to the output list of this component. |
| Public method | [AddTransformParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddTransformParameter.htm) | Add a Transformation parameter to the output list of this component. |
| Public method | [AddVectorParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_AddVectorParameter.htm) | Add a 3D Vector parameter to the output list of this component. |
| Public method | [HideParameter](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_HideParameter.htm) | Hide a specific output parameter. If the parameter at the given index implement IGH\_PreviewObject then the Hidden flag will be set to True. Otherwise, nothing will happen. (Overrides GH\_ParamManager.HideParameter(Int32).) |
| Public method | [Register\_2DIntervalParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_2DIntervalParam.htm) | Register a new two-dimensional OnInterval parameter |
| Public method | [Register\_2DIntervalParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_2DIntervalParam_1.htm) | Register a new two-dimensional OnInterval parameter |
| Public method | [Register\_ArcParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_ArcParam.htm) | Register a new 3D arc parameter |
| Public method | [Register\_ArcParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_ArcParam_1.htm) | Register a new 3D arc parameter |
| Public method | [Register\_BooleanParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_BooleanParam.htm) | Register a new Boolean primitive parameter |
| Public method | [Register\_BooleanParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_BooleanParam_1.htm) | Register a new Boolean primitive parameter |
| Public method | [Register\_BoxParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_BoxParam.htm) | Register a new 3D box parameter |
| Public method | [Register\_BoxParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_BoxParam_1.htm) | Register a new 3D box parameter |
| Public method | [Register\_BRepParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_BRepParam.htm) | Register a new 3D Brep parameter |
| Public method | [Register\_BRepParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_BRepParam_1.htm) | Register a new 3D Brep parameter |
| Public method | [Register\_CircleParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_CircleParam.htm) | Register a new 3D circle parameter |
| Public method | [Register\_CircleParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_CircleParam_1.htm) | Register a new 3D circle parameter |
| Public method | [Register\_ColourParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_ColourParam.htm) | Register a new Colour primitive parameter |
| Public method | [Register\_ColourParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_ColourParam_1.htm) | Register a new Colour primitive parameter |
| Public method | [Register\_ComplexParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_ComplexParam.htm) | Register a new Complex primitive parameter |
| Public method | [Register\_ComplexParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_ComplexParam_1.htm) | Register a new Complex primitive parameter |
| Public method | [Register\_CurveParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_CurveParam.htm) | Register a new 3D curve parameter |
| Public method | [Register\_CurveParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_CurveParam_1.htm) | Register a new 3D curve parameter |
| Public method | [Register\_DoubleParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_DoubleParam.htm) | Register a new Double primitive parameter |
| Public method | [Register\_DoubleParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_DoubleParam_1.htm) | Register a new Double primitive parameter |
| Public method | [Register\_FieldParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_FieldParam.htm) | Register a new field parameter |
| Public method | [Register\_FieldParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_FieldParam_1.htm) | Register a new field parameter |
| Public method | [Register\_GenericParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_GenericParam.htm) | Register a new Generic (Object) parameter |
| Public method | [Register\_GenericParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_GenericParam_1.htm) | Register a new Generic (Object) parameter |
| Public method | [Register\_GeometryParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_GeometryParam.htm) | Register a new 3D geometry parameter |
| Public method | [Register\_GeometryParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_GeometryParam_1.htm) | Register a new 3D geometry parameter |
| Public method | [Register\_GroupParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_GroupParam.htm) | Register a new geometric group parameter |
| Public method | [Register\_GroupParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_GroupParam_1.htm) | Register a new geometric group parameter |
| Public method | [Register\_IntegerParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_IntegerParam.htm) | Register a new Integer primitive parameter |
| Public method | [Register\_IntegerParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_IntegerParam_1.htm) | Register a new Integer primitive parameter |
| Public method | [Register\_IntervalParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_IntervalParam.htm) | Register a new Interval parameter |
| Public method | [Register\_IntervalParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_IntervalParam_1.htm) | Register a new Interval parameter |
| Public method | [Register\_LineParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_LineParam.htm) | Register a new 3D line parameter |
| Public method | [Register\_LineParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_LineParam_1.htm) | Register a new 3D line parameter |
| Public method | [Register\_MatrixParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_MatrixParam.htm) | Register a new matrix parameter |
| Public method | [Register\_MatrixParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_MatrixParam_1.htm) | Register a new matrix parameter |
| Public method | [Register\_MeshFaceParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_MeshFaceParam.htm) | Register a new 3D Mesh face parameter |
| Public method | [Register\_MeshFaceParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_MeshFaceParam_1.htm) | Register a new 3D Mesh face parameter |
| Public method | [Register\_MeshParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_MeshParam.htm) | Register a new 3D Mesh parameter |
| Public method | [Register\_MeshParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_MeshParam_1.htm) | Register a new 3D Mesh parameter |
| Public method | [Register\_PathParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_PathParam.htm) | Register a new Data Structure path parameter |
| Public method | [Register\_PathParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_PathParam_1.htm) | Register a new Data Structure path parameter |
| Public method | [Register\_PlaneParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_PlaneParam.htm) | Register a new 3D plane parameter |
| Public method | [Register\_PlaneParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_PlaneParam_1.htm) | Register a new 3D plane parameter |
| Public method | [Register\_PointParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_PointParam.htm) | Register a new 3D point parameter |
| Public method | [Register\_PointParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_PointParam_1.htm) | Register a new 3D point parameter |
| Public method | [Register\_RectangleParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_RectangleParam.htm) | Register a new 3D rectangle parameter |
| Public method | [Register\_RectangleParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_RectangleParam_1.htm) | Register a new 3D rectangle parameter |
| Public method | [Register\_StringParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_StringParam.htm) | Register a new String primitive parameter |
| Public method | [Register\_StringParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_StringParam_1.htm) | Register a new String primitive parameter |
| Public method | [Register\_SurfaceParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_SurfaceParam.htm) | Register a new 3D surface parameter |
| Public method | [Register\_SurfaceParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_SurfaceParam_1.htm) | Register a new 3D surface parameter |
| Public method | [Register\_TransformParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_TransformParam.htm) | Register a new Transform parameter |
| Public method | [Register\_TransformParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_TransformParam_1.htm) | Register a new Transform parameter |
| Public method | [Register\_VectorParam(String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_VectorParam.htm) | Register a new 3D vector parameter |
| Public method | [Register\_VectorParam(String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_Register_VectorParam_1.htm) | Register a new 3D vector parameter |
| Public method | [RegisterParam(IGH\_Param)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_RegisterParam.htm) | Generic parameter registration. This class provides methods to register standard parameters, but if you have a special type you're in charge of setting it all up yourself. |
| Public method | [RegisterParam(IGH\_Param, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_RegisterParam_1.htm) | Generic parameter registration. This class provides methods to register standard parameters, but if you have a special type you're in charge of setting it all up yourself. |
| Public method | [RegisterParam(IGH\_Param, String, String, String)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_RegisterParam_2.htm) | Generic parameter registration. This class provides methods to register standard parameters, but if you have a special type you're in charge of setting it all up yourself. |
| Public method | [RegisterParam(IGH\_Param, String, String, String, GH\_ParamAccess)](M_Grasshopper_Kernel_GH_Component_GH_OutputParamManager_RegisterParam_3.htm) | Generic parameter registration. This class provides methods to register standard parameters, but if you have a special type you're in charge of setting it all up yourself. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)