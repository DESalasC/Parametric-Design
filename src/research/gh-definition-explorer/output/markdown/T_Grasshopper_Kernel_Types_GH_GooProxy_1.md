# T_Grasshopper_Kernel_Types_GH_GooProxy_1

﻿ GH\_GooProxy(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_GooProxy(T) Class](../html/T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm "GH_GooProxy(T) Class")

[GH\_GooProxy(T) Constructor](../html/M_Grasshopper_Kernel_Types_GH_GooProxy_1__ctor.htm "GH_GooProxy(T) Constructor ")

[GH\_GooProxy(T) Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm "GH_GooProxy(T) Properties")

[GH\_GooProxy(T) Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_GooProxy_1.htm "GH_GooProxy(T) Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GooProxyAddLanguageSpecificTextSet("LST50959B2F\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST50959B2F\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

Abstract base implementation of IGH\_GooProxy

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST50959B2F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GooProxyAddLanguageSpecificTextSet("LST50959B2F\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST50959B2F\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");  
    [More...](#fullInheritance)

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_GooProxy<T> : IGH_GooProxy
where T : IGH_Goo
```

```
Public MustInherit Class GH_GooProxy(Of T As IGH_Goo)
	Implements IGH_GooProxy
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T

The GH\_GooProxyAddLanguageSpecificTextSet("LST50959B2F\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST50959B2F\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_GooProxyAddLanguageSpecificTextSet("LST50959B2F\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST50959B2F\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](M_Grasshopper_Kernel_Types_GH_GooProxy_1__ctor.htm) | Initializes a new instance of the GH\_GooProxyAddLanguageSpecificTextSet("LST50959B2F\_10?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST50959B2F\_11?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_GH_GooProxy_1_TypeDescription.htm) |  |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_GH_GooProxy_1_TypeName.htm) |  |
| Public property | [Valid](P_Grasshopper_Kernel_Types_GH_GooProxy_1_Valid.htm) | Gets a value indicating whether this proxy represents valid data. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Construct](M_Grasshopper_Kernel_Types_GH_GooProxy_1_Construct.htm) | Override this method to supply a custom UI during proxy construction. |
| Public method | [FormatInstance](M_Grasshopper_Kernel_Types_GH_GooProxy_1_FormatInstance.htm) | Returns a String description of the current value. |
| Public method | [FromString](M_Grasshopper_Kernel_Types_GH_GooProxy_1_FromString.htm) | If IsParsable(), then attempts to convert the string to a generic type value |
| Public method | [MutateString](M_Grasshopper_Kernel_Types_GH_GooProxy_1_MutateString.htm) | Munge a string to remove obvious errors on account of the user. |
| Protected method | [NumberToString](M_Grasshopper_Kernel_Types_GH_GooProxy_1_NumberToString.htm) |  |
| Protected method | [StringToNumber](M_Grasshopper_Kernel_Types_GH_GooProxy_1_StringToNumber.htm) |  |
| Public method | [ToString](M_Grasshopper_Kernel_Types_GH_GooProxy_1_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST50959B2F\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST50959B2F\_13?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST50959B2F\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GooProxyAddLanguageSpecificTextSet("LST50959B2F\_16?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST50959B2F\_17?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AnnotationBaseAddLanguageSpecificTextSet("LST50959B2F\_19?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AnnotationBaseProxyAddLanguageSpecificTextSet("LST50959B2F\_20?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST50959B2F\_21?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Types_GH_AnnotationBase_GH_AnnotationBaseProxy_1.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_BoxAddLanguageSpecificTextSet("LST50959B2F\_23?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_BoxProxy](T_Grasshopper_Kernel_Types_GH_Box_GH_BoxProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_24?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_BrepAddLanguageSpecificTextSet("LST50959B2F\_25?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_BrepProxy](T_Grasshopper_Kernel_Types_GH_Brep_GH_BrepProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_26?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CircleAddLanguageSpecificTextSet("LST50959B2F\_27?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CircleProxy](T_Grasshopper_Kernel_Types_GH_Circle_GH_CircleProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_28?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CurveAddLanguageSpecificTextSet("LST50959B2F\_29?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CurveProxy](T_Grasshopper_Kernel_Types_GH_Curve_GH_CurveProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_30?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ExtrusionAddLanguageSpecificTextSet("LST50959B2F\_31?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ExtrusionProxy](T_Grasshopper_Kernel_Types_GH_Extrusion_GH_ExtrusionProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_32?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometryGroupAddLanguageSpecificTextSet("LST50959B2F\_33?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GeometryGroupProxy](T_Grasshopper_Kernel_Types_GH_GeometryGroup_GH_GeometryGroupProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_34?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_HatchAddLanguageSpecificTextSet("LST50959B2F\_35?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_HatchProxy](T_Grasshopper_Kernel_Types_GH_Hatch_GH_HatchProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_36?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InstanceReferenceAddLanguageSpecificTextSet("LST50959B2F\_37?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InstanceReferenceProxy](T_Grasshopper_Kernel_Types_GH_InstanceReference_GH_InstanceReferenceProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_38?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Interval2DAddLanguageSpecificTextSet("LST50959B2F\_39?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Interval2DProxy](T_Grasshopper_Kernel_Types_GH_Interval2D_GH_Interval2DProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_40?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_LineAddLanguageSpecificTextSet("LST50959B2F\_41?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_LineProxy](T_Grasshopper_Kernel_Types_GH_Line_GH_LineProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_42?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MaterialAddLanguageSpecificTextSet("LST50959B2F\_43?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Material\_Proxy](T_Grasshopper_Kernel_Types_GH_Material_GH_Material_Proxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_44?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MeshAddLanguageSpecificTextSet("LST50959B2F\_45?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MeshProxy](T_Grasshopper_Kernel_Types_GH_Mesh_GH_MeshProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_46?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MeshFaceAddLanguageSpecificTextSet("LST50959B2F\_47?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MeshFaceProxy](T_Grasshopper_Kernel_Types_GH_MeshFace_GH_MeshFaceProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_48?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MeshingParametersAddLanguageSpecificTextSet("LST50959B2F\_49?cs=.|vb=.|cpp=::|nu=.|fs=.");RhMesherSettings\_Proxy](T_Grasshopper_Kernel_Types_GH_MeshingParameters_RhMesherSettings_Proxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_50?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PlaneAddLanguageSpecificTextSet("LST50959B2F\_51?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PlaneProxy](T_Grasshopper_Kernel_Types_GH_Plane_GH_PlaneProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_52?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PointAddLanguageSpecificTextSet("LST50959B2F\_53?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PointProxy](T_Grasshopper_Kernel_Types_GH_Point_GH_PointProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_54?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PointCloudAddLanguageSpecificTextSet("LST50959B2F\_55?cs=.|vb=.|cpp=::|nu=.|fs=.");PointCloudProxy](T_Grasshopper_Kernel_Types_GH_PointCloud_PointCloudProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_56?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RectangleAddLanguageSpecificTextSet("LST50959B2F\_57?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RectangleProxy](T_Grasshopper_Kernel_Types_GH_Rectangle_GH_RectangleProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_58?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SubDAddLanguageSpecificTextSet("LST50959B2F\_59?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SubDProxy](T_Grasshopper_Kernel_Types_GH_SubD_GH_SubDProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_60?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SurfaceAddLanguageSpecificTextSet("LST50959B2F\_61?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SurfaceProxy](T_Grasshopper_Kernel_Types_GH_Surface_GH_SurfaceProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_62?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_TextDotAddLanguageSpecificTextSet("LST50959B2F\_63?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_TextDotProxy](T_Grasshopper_Kernel_Types_GH_TextDot_GH_TextDotProxy.htm)  
    [Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LST50959B2F\_64?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_VectorAddLanguageSpecificTextSet("LST50959B2F\_65?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_VectorProxy](T_Grasshopper_Kernel_Types_GH_Vector_GH_VectorProxy.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)