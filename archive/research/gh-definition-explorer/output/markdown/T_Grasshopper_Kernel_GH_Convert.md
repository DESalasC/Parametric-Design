# T_Grasshopper_Kernel_GH_Convert

﻿ GH\_Convert Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Convert Class](../html/T_Grasshopper_Kernel_GH_Convert.htm "GH_Convert Class")

[GH\_Convert Properties](../html/Properties_T_Grasshopper_Kernel_GH_Convert.htm "GH_Convert Properties")

[GH\_Convert Methods](../html/Methods_T_Grasshopper_Kernel_GH_Convert.htm "GH_Convert Methods")

[GH\_Convert Fields](../html/Fields_T_Grasshopper_Kernel_GH_Convert.htm "GH_Convert Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Convert Class |

Provides static converters for different data types inside Grasshopper.
This class both has specific and generic converters.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST2CE4F34A\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST2CE4F34A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Convert

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_Convert
```

```
Public NotInheritable Class GH_Convert
```

AddLanguageTabSet("ID1EBCA");

The GH\_Convert type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public propertyStatic member | [CultureTable](P_Grasshopper_Kernel_GH_Convert_CultureTable.htm) | Gets the cached culture table. Do not modify this dictionary unless you know what you are doing. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [BackSolveExpression](M_Grasshopper_Kernel_GH_Convert_BackSolveExpression.htm) | Try and backsolve an expression |
| Public methodStatic member | [ByteArrayToCommonObjectAddLanguageSpecificTextSet("LST2CE4F34A\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST2CE4F34A\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_GH_Convert_ByteArrayToCommonObject__1.htm) | Convert an OpenNurbs compliant compressed byte array into a RhinoCommon object. |
| Public methodStatic member | [CombineDateAndTime](M_Grasshopper_Kernel_GH_Convert_CombineDateAndTime.htm) | Combine a pure date and a pure time. |
| Public methodStatic member | [CommonObjectToByteArray](M_Grasshopper_Kernel_GH_Convert_CommonObjectToByteArray.htm) | Convert a RhinoCommon object into a compressed byte-array using OpenNurbs serialization. |
| Public methodStatic member | [CreateDateAndTime](M_Grasshopper_Kernel_GH_Convert_CreateDateAndTime.htm) |  |
| Public methodStatic member | [CreatePureDate](M_Grasshopper_Kernel_GH_Convert_CreatePureDate.htm) | Convert a datetime structure into a pure date, i.e. remove the time portion. As per convention, this leaves 1 tick into the day in question intact. |
| Public methodStatic member | [CreatePureTime(DateTime)](M_Grasshopper_Kernel_GH_Convert_CreatePureTime.htm) | Convert a datetime structure into a pure time, i.e. remove the date portion. As per convention, this means setting the year, month and day to 1. |
| Public methodStatic member | [CreatePureTime(Int32, Int32, Int32)](M_Grasshopper_Kernel_GH_Convert_CreatePureTime_1.htm) | Create a pure time instance. If the total number of hours, minutes and seconds exceeds a full year then it is not possible to create a pure time and the largest possible pure time will be returned instead. |
| Public methodStatic member | [FileToHash](M_Grasshopper_Kernel_GH_Convert_FileToHash.htm) | Create a hash of a file. |
| Public methodStatic member | [FindRhinoObjectByNameAndType](M_Grasshopper_Kernel_GH_Convert_FindRhinoObjectByNameAndType.htm) | Search the current Rhino document for an object with a given name of a given type. |
| Public methodStatic member | [GeometryToObjRef](M_Grasshopper_Kernel_GH_Convert_GeometryToObjRef.htm) | Create an ObjRef for a referenced IGH\_GeometricGoo. Unreferenced IGH\_GeometryGoo will return null. |
| Public methodStatic member | [GetBrepFromDocument](M_Grasshopper_Kernel_GH_Convert_GetBrepFromDocument.htm) | Harvest a brep object from a Rhino document. |
| Public methodStatic member | [GetClippingPlaneFromDocument](M_Grasshopper_Kernel_GH_Convert_GetClippingPlaneFromDocument.htm) | Harvest a clipping plane surface from a Rhino document. |
| Public methodStatic member | [GetCurveFromDocument](M_Grasshopper_Kernel_GH_Convert_GetCurveFromDocument.htm) | Harvest a curve object from a Rhino document. |
| Public methodStatic member | [GetExtrusionFromDocument](M_Grasshopper_Kernel_GH_Convert_GetExtrusionFromDocument.htm) | Harvest an extrusion object from a Rhino document. |
| Public methodStatic member | [GetMeshFromDocument](M_Grasshopper_Kernel_GH_Convert_GetMeshFromDocument.htm) | Harvest a mesh object from a Rhino document. |
| Public methodStatic member | [GetPlaneFromDocument](M_Grasshopper_Kernel_GH_Convert_GetPlaneFromDocument.htm) | Harvest the object frame plane from a Rhino document. |
| Public methodStatic member | [GetPointFromDocument](M_Grasshopper_Kernel_GH_Convert_GetPointFromDocument.htm) | Harvest a point object from a Rhino document. |
| Public methodStatic member | [GetSubDFromDocument](M_Grasshopper_Kernel_GH_Convert_GetSubDFromDocument.htm) | Harvest a sub-d object from a Rhino document. |
| Public methodStatic member | [GetSurfaceFromDocument](M_Grasshopper_Kernel_GH_Convert_GetSurfaceFromDocument.htm) | Harvest a surface object from a Rhino document. |
| Public methodStatic member | [GetTimeKind(DateTime)](M_Grasshopper_Kernel_GH_Convert_GetTimeKind.htm) | Gets the kind of time implied by a System.DateTime value. |
| Public methodStatic member | [GetTimeKind(DateTime, DateTime)](M_Grasshopper_Kernel_GH_Convert_GetTimeKind_1.htm) | Gets the kind of time implied by two System.DateTime values. |
| Public methodStatic member | [IsPureDate](M_Grasshopper_Kernel_GH_Convert_IsPureDate.htm) | Tests whether a DateTime instance represents a pure date (i.e. that the time portion is undefined). Pure dates are a Grasshopper convention, basically a pure date is 1 tick past midnight. |
| Public methodStatic member | [IsPureTime](M_Grasshopper_Kernel_GH_Convert_IsPureTime.htm) | Tests whether a DateTime instance represents a pure time (i.e. that the date portion is undefined). Pure times are a Grasshopper convention, basically a pure time is 2 ticks past any second. |
| Public methodStatic member | [ObjRefToGeometry](M_Grasshopper_Kernel_GH_Convert_ObjRefToGeometry.htm) | Convert a Rhino Object Reference into Grasshopper IGH\_GeometricGoo. |
| Public methodStatic member | [ParseExpression](M_Grasshopper_Kernel_GH_Convert_ParseExpression.htm) | Attempts to parse an expression. |
| Public methodStatic member | [StringToDate](M_Grasshopper_Kernel_GH_Convert_StringToDate.htm) | Convert a string representing a date into an actual date. If a pure date is possible it will be returned. If the input is a pure time this method will fail, you need to use StringToTime instead. |
| Public methodStatic member | [StringToGuid](M_Grasshopper_Kernel_GH_Convert_StringToGuid.htm) | Create a Guid based on SHA256 hashing of a string. |
| Public methodStatic member | [StringToTime](M_Grasshopper_Kernel_GH_Convert_StringToTime.htm) | Convert a string representing a time into an pure time. Allowed separators of hour, minute and second portions are colons, semi-colons, points and commas. Grasshopper itself uses colons when formatting times. A PM or AM symbol is allowed provided it does not border on any alphabetical characters. A time can be prefixed by a "X day[s] + " string which defines the total number of 24-hour periods to include. |
| Public methodStatic member | [ToAnnotationBase](M_Grasshopper_Kernel_GH_Convert_ToAnnotationBase.htm) | Convert data into Rhino.Geometry.AnnotationBase. |
| Public methodStatic member | [ToAnnotationBase\_Primary](M_Grasshopper_Kernel_GH_Convert_ToAnnotationBase_Primary.htm) | Performs a direct cast from Rhino.Geometry.AnnotationBase or GH\_AnnotationBase. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToAnnotationBase\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToAnnotationBase_Secondary.htm) | Attempts to convert other data types into an Rhino.Geometry.AnnotationBase. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToArc](M_Grasshopper_Kernel_GH_Convert_ToArc.htm) | Convert data into Rhino.Geometry.Arc. |
| Public methodStatic member | [ToArc\_Primary](M_Grasshopper_Kernel_GH_Convert_ToArc_Primary.htm) | Performs a direct cast from OnArc or GH\_Arc. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToArc\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToArc_Secondary.htm) | Attempts to convert other data types into an OnArc. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToBoolean](M_Grasshopper_Kernel_GH_Convert_ToBoolean.htm) | Convert data into Booleans. |
| Public methodStatic member | [ToBoolean\_Primary](M_Grasshopper_Kernel_GH_Convert_ToBoolean_Primary.htm) | Performs a direct cast from boolean or GH\_Boolean. |
| Public methodStatic member | [ToBoolean\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToBoolean_Secondary.htm) | Performs indirect casts from other data types into booleans. |
| Public methodStatic member | [ToBoundingBox\_Primary](M_Grasshopper_Kernel_GH_Convert_ToBoundingBox_Primary.htm) | Performs a direct cast from OnBoundingBox. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToBox\_Primary](M_Grasshopper_Kernel_GH_Convert_ToBox_Primary.htm) | Performs a direct cast from Box. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToBrep](M_Grasshopper_Kernel_GH_Convert_ToBrep.htm) | Convert data into Rhino.Geometry.Brep. |
| Public methodStatic member | [ToBrep\_Primary](M_Grasshopper_Kernel_GH_Convert_ToBrep_Primary.htm) | Performs a direct cast from OnBrep or GH\_Brep. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToBrep\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToBrep_Secondary.htm) | Attempts to convert other data types into an OnBrep. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToCircle](M_Grasshopper_Kernel_GH_Convert_ToCircle.htm) | Convert data into Rhino.Geometry.Circle. |
| Public methodStatic member | [ToCircle\_Primary](M_Grasshopper_Kernel_GH_Convert_ToCircle_Primary.htm) | Performs a direct cast from OnCircle or GH\_Circle. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToCircle\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToCircle_Secondary.htm) | Attempts to convert other data types into an OnCircle. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToColor](M_Grasshopper_Kernel_GH_Convert_ToColor.htm) | Convert data into Colors. |
| Public methodStatic member | [ToColor\_Primary](M_Grasshopper_Kernel_GH_Convert_ToColor_Primary.htm) | Performs a direct cast from Drawing.Color, GH\_Color and OnColor. |
| Public methodStatic member | [ToColor\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToColor_Secondary.htm) | Performs indirect casts from other data types into Colors. |
| Public methodStatic member | [ToComplex](M_Grasshopper_Kernel_GH_Convert_ToComplex.htm) | Convert data into Complex. |
| Public methodStatic member | [ToComplex\_Primary](M_Grasshopper_Kernel_GH_Convert_ToComplex_Primary.htm) | Performs a direct cast from Complex or GH\_ComplexNumber |
| Public methodStatic member | [ToComplex\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToComplex_Secondary.htm) | Performs indirect casts from other data types into Complex. |
| Public methodStatic member | [ToCoordinates](M_Grasshopper_Kernel_GH_Convert_ToCoordinates.htm) |  |
| Public methodStatic member | [ToCulture](M_Grasshopper_Kernel_GH_Convert_ToCulture.htm) | Convert data into Colors. |
| Public methodStatic member | [ToCulture\_Primary](M_Grasshopper_Kernel_GH_Convert_ToCulture_Primary.htm) | Performs a direct cast from System.Globalization.CultureInfo and GH\_Culture. |
| Public methodStatic member | [ToCulture\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToCulture_Secondary.htm) | Performs indirect casts from other data types into CultureInfo. |
| Public methodStatic member | [ToCurve](M_Grasshopper_Kernel_GH_Convert_ToCurve.htm) | Convert data into Rhino.Geometry.Curve. |
| Public methodStatic member | [ToCurve\_Primary](M_Grasshopper_Kernel_GH_Convert_ToCurve_Primary.htm) | Performs a direct cast from OnCurve or GH\_Curve. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToCurve\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToCurve_Secondary.htm) | Attempts to convert other data types into an IOnCurve. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToDate](M_Grasshopper_Kernel_GH_Convert_ToDate.htm) | Convert data into Dates. |
| Public methodStatic member | [ToDate\_Primary](M_Grasshopper_Kernel_GH_Convert_ToDate_Primary.htm) | Performs a direct cast from DateTime or GH\_DateTime. |
| Public methodStatic member | [ToDate\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToDate_Secondary.htm) | Performs indirect casts from other data types into DateTime constructs. |
| Public methodStatic member | [ToDimension](M_Grasshopper_Kernel_GH_Convert_ToDimension.htm) | Convert data into Rhino.Geometry.Dimension. |
| Public methodStatic member | [ToDimension\_Primary](M_Grasshopper_Kernel_GH_Convert_ToDimension_Primary.htm) | Performs a direct cast from Rhino.Geometry.Dimension or GH\_Dimension. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToDimension\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToDimension_Secondary.htm) | Attempts to convert other data types into an Rhino.Geometry.Dimension. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToDouble](M_Grasshopper_Kernel_GH_Convert_ToDouble.htm) | Convert data into Doubles. |
| Public methodStatic member | [ToDouble\_Primary](M_Grasshopper_Kernel_GH_Convert_ToDouble_Primary.htm) | Performs a direct cast from Double or GH\_Number. |
| Public methodStatic member | [ToDouble\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToDouble_Secondary.htm) | Performs indirect casts from other data types into Doubles. |
| Public methodStatic member | [ToExtrusion](M_Grasshopper_Kernel_GH_Convert_ToExtrusion.htm) | Convert data into Rhino.Geometry.Brep. |
| Public methodStatic member | [ToExtrusion\_Primary](M_Grasshopper_Kernel_GH_Convert_ToExtrusion_Primary.htm) | Performs a direct cast from Rhino.Geometry.Extrusion or GH\_Extrusion. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToExtrusion\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToExtrusion_Secondary.htm) | Attempts to convert other data types into a Extrusion. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGeometricGoo](M_Grasshopper_Kernel_GH_Convert_ToGeometricGoo.htm) | Converts an object into GeometricGoo. Does not duplicate the data if a lossless conversion is possible. |
| Public methodStatic member | [ToGeometryBase](M_Grasshopper_Kernel_GH_Convert_ToGeometryBase.htm) | Attempt to convert an object into a Rhino.Geometry.GeometryBase instance. |
| Public methodStatic member | [ToGHAngularDimension](M_Grasshopper_Kernel_GH_Convert_ToGHAngularDimension.htm) | Convert data into GH\_AngularDimension. |
| Public methodStatic member | [ToGHAngularDimension\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHAngularDimension_Primary.htm) | Converts similar data into a GH\_AngularDimension instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHAngularDimension\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHAngularDimension_Secondary.htm) | Converts similar data into a GH\_AngularDimension instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHAnnotationBase](M_Grasshopper_Kernel_GH_Convert_ToGHAnnotationBase.htm) | Convert data into GH\_AnnotationBase. |
| Public methodStatic member | [ToGHArc](M_Grasshopper_Kernel_GH_Convert_ToGHArc.htm) | Convert data into GH\_Arcs. |
| Public methodStatic member | [ToGHArc\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHArc_Primary.htm) | Converts similar data into a GH\_Arc instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHArc\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHArc_Secondary.htm) | Converts similar data into a GH\_Arc instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHBoolean](M_Grasshopper_Kernel_GH_Convert_ToGHBoolean.htm) | Convert data into GH\_Boolean. |
| Public methodStatic member | [ToGHBoolean\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHBoolean_Primary.htm) | Converts similar data into a GH\_Boolean instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHBoolean\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHBoolean_Secondary.htm) | Converts similar data into a GH\_Boolean instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHBox](M_Grasshopper_Kernel_GH_Convert_ToGHBox.htm) | Convert data into GH\_Boxes. |
| Public methodStatic member | [ToGHBox\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHBox_Primary.htm) | Converts similar data into a GH\_Box instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHBox\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHBox_Secondary.htm) | Converts similar data into a GH\_Box instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHBrep](M_Grasshopper_Kernel_GH_Convert_ToGHBrep.htm) | Convert data into GH\_Breps. |
| Public methodStatic member | [ToGHBrep\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHBrep_Primary.htm) | Converts similar data into a GH\_Brep instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHBrep\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHBrep_Secondary.htm) | Converts similar data into a GH\_Brep instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHCentermark](M_Grasshopper_Kernel_GH_Convert_ToGHCentermark.htm) | Convert data into GH\_Centermark. |
| Public methodStatic member | [ToGHCentermark\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHCentermark_Primary.htm) | Converts similar data into a GH\_Centermark instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHCentermark\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHCentermark_Secondary.htm) | Converts similar data into a GH\_Centermark instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHCircle](M_Grasshopper_Kernel_GH_Convert_ToGHCircle.htm) | Convert data into GH\_Circles. |
| Public methodStatic member | [ToGHCircle\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHCircle_Primary.htm) | Converts similar data into a GH\_Circle instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHCircle\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHCircle_Secondary.htm) | Converts similar data into a GH\_Circle instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHColour](M_Grasshopper_Kernel_GH_Convert_ToGHColour.htm) | Convert data into GH\_Colour. |
| Public methodStatic member | [ToGHColour\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHColour_Primary.htm) | Converts similar data into a GH\_Colour instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHColour\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHColour_Secondary.htm) | Converts similar data into a GH\_Colour instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHComplexNumber](M_Grasshopper_Kernel_GH_Convert_ToGHComplexNumber.htm) | Convert data into GH\_ComplexNumber. |
| Public methodStatic member | [ToGHComplexNumber\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHComplexNumber_Primary.htm) | Converts similar data into a GH\_ComplexNumber instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHComplexNumber\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHComplexNumber_Secondary.htm) | Converts similar data into a GH\_ComplexNumber instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHCurve](M_Grasshopper_Kernel_GH_Convert_ToGHCurve.htm) | Convert data into GH\_Curves. |
| Public methodStatic member | [ToGHCurve\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHCurve_Primary.htm) | Converts similar data into a GH\_Curve instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHCurve\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHCurve_Secondary.htm) | Converts similar data into a GH\_Curve instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHDimension](M_Grasshopper_Kernel_GH_Convert_ToGHDimension.htm) | Convert data into GH\_Dimension. |
| Public methodStatic member | [ToGHExtrusion](M_Grasshopper_Kernel_GH_Convert_ToGHExtrusion.htm) | Convert data into GH\_Extrusion. |
| Public methodStatic member | [ToGHExtrusion\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHExtrusion_Primary.htm) | Converts similar data into a GH\_Extrusion instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHExtrusion\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHExtrusion_Secondary.htm) | Converts similar data into a GH\_Brep instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHGuid](M_Grasshopper_Kernel_GH_Convert_ToGHGuid.htm) | Convert data into GH\_Guid. |
| Public methodStatic member | [ToGHGuid\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHGuid_Primary.htm) | Converts similar data into a GH\_Guid instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHGuid\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHGuid_Secondary.htm) | Converts similar data into a GH\_Guid instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHHatch](M_Grasshopper_Kernel_GH_Convert_ToGHHatch.htm) | Convert data into GH\_Hatch. |
| Public methodStatic member | [ToGHHatch\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHHatch_Primary.htm) | Converts similar data into a GH\_Hatch instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHHatch\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHHatch_Secondary.htm) | Converts similar data into a GH\_Hatch instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHInstanceReference](M_Grasshopper_Kernel_GH_Convert_ToGHInstanceReference.htm) | Convert data into GH\_InstanceReference. |
| Public methodStatic member | [ToGHInstanceReference\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHInstanceReference_Primary.htm) | Converts similar data into a GH\_InstanceReference instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHInstanceReference\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHInstanceReference_Secondary.htm) | Converts similar data into a GH\_InstanceReference instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHInteger](M_Grasshopper_Kernel_GH_Convert_ToGHInteger.htm) | Convert data into GH\_Integer. |
| Public methodStatic member | [ToGHInteger\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHInteger_Primary.htm) | Converts similar data into a GH\_Integer instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHInteger\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHInteger_Secondary.htm) | Converts similar data into a GH\_Integer instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHInterval](M_Grasshopper_Kernel_GH_Convert_ToGHInterval.htm) | Convert data into GH\_Intervals. |
| Public methodStatic member | [ToGHInterval\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHInterval_Primary.htm) | Converts similar data into a GH\_Interval instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHInterval\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHInterval_Secondary.htm) | Converts similar data into a GH\_Interval instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHInterval2D](M_Grasshopper_Kernel_GH_Convert_ToGHInterval2D.htm) | Convert data into GH\_Interval2Ds. |
| Public methodStatic member | [ToGHInterval2D\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHInterval2D_Primary.htm) | Converts similar data into a GH\_Interval2D instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHInterval2D\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHInterval2D_Secondary.htm) | Converts similar data into a GH\_Interval2D instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHLeader](M_Grasshopper_Kernel_GH_Convert_ToGHLeader.htm) | Convert data into GH\_Leader. |
| Public methodStatic member | [ToGHLeader\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHLeader_Primary.htm) | Converts similar data into a GH\_Leader instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHLeader\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHLeader_Secondary.htm) | Converts similar data into a GH\_Leader instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHLight](M_Grasshopper_Kernel_GH_Convert_ToGHLight.htm) | Convert data into GH\_Light. |
| Public methodStatic member | [ToGHLight\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHLight_Primary.htm) | Converts similar data into a GH\_Light instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHLight\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHLight_Secondary.htm) | Converts similar data into a GH\_Light instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHLine](M_Grasshopper_Kernel_GH_Convert_ToGHLine.htm) | Convert data into GH\_Lines. |
| Public methodStatic member | [ToGHLine\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHLine_Primary.htm) | Converts similar data into a GH\_Line instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHLine\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHLine_Secondary.htm) | Converts similar data into a GH\_Line instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHLinearDimension](M_Grasshopper_Kernel_GH_Convert_ToGHLinearDimension.htm) | Convert data into GH\_LinearDimension. |
| Public methodStatic member | [ToGHLinearDimension\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHLinearDimension_Primary.htm) | Converts similar data into a GH\_LinearDimension instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHLinearDimension\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHLinearDimension_Secondary.htm) | Converts similar data into a GH\_LinearDimension instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHMatrix](M_Grasshopper_Kernel_GH_Convert_ToGHMatrix.htm) | Convert data into ToGHMatrix. |
| Public methodStatic member | [ToGHMatrix\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHMatrix_Primary.htm) | Converts similar data into a GH\_Matrix instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHMatrix\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHMatrix_Secondary.htm) | Converts similar data into a GH\_Matrix instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHMesh](M_Grasshopper_Kernel_GH_Convert_ToGHMesh.htm) | Convert data into GH\_Meshs. |
| Public methodStatic member | [ToGHMesh\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHMesh_Primary.htm) | Converts similar data into a GH\_Mesh instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHMesh\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHMesh_Secondary.htm) | Converts similar data into a GH\_Mesh instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHMeshFace](M_Grasshopper_Kernel_GH_Convert_ToGHMeshFace.htm) | Convert data into GH\_MeshFaces. |
| Public methodStatic member | [ToGHMeshFace\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHMeshFace_Primary.htm) | Converts similar data into a GH\_MeshFace instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHMeshFace\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHMeshFace_Secondary.htm) | Converts similar data into a GH\_MeshFace instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHNumber](M_Grasshopper_Kernel_GH_Convert_ToGHNumber.htm) | Convert data into GH\_Number. |
| Public methodStatic member | [ToGHNumber\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHNumber_Primary.htm) | Converts similar data into a GH\_Number instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHNumber\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHNumber_Secondary.htm) | Converts similar data into a GH\_Number instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHOrdinateDimension](M_Grasshopper_Kernel_GH_Convert_ToGHOrdinateDimension.htm) | Convert data into GH\_OrdinateDimension. |
| Public methodStatic member | [ToGHOrdinateDimension\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHOrdinateDimension_Primary.htm) | Converts similar data into a GH\_OrdinateDimension instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHOrdinateDimension\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHOrdinateDimension_Secondary.htm) | Converts similar data into a GH\_OrdinateDimension instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHPlane](M_Grasshopper_Kernel_GH_Convert_ToGHPlane.htm) | Convert data into GH\_Planes. |
| Public methodStatic member | [ToGHPlane\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHPlane_Primary.htm) | Converts similar data into a GH\_Plane instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHPlane\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHPlane_Secondary.htm) | Converts similar data into a GH\_Plane instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHPoint](M_Grasshopper_Kernel_GH_Convert_ToGHPoint.htm) | Convert data into GH\_Points. |
| Public methodStatic member | [ToGHPoint\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHPoint_Primary.htm) | Converts similar data into a GH\_Point instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHPoint\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHPoint_Secondary.htm) | Converts similar data into a GH\_Point instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHPointCloud](M_Grasshopper_Kernel_GH_Convert_ToGHPointCloud.htm) | Convert data into GH\_PointCloud. |
| Public methodStatic member | [ToGHPointCloud\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHPointCloud_Primary.htm) | Converts similar data into a GH\_PointCloud instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHPointCloud\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHPointCloud_Secondary.htm) | Converts similar data into a GH\_PointCloud instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHRadialDimension](M_Grasshopper_Kernel_GH_Convert_ToGHRadialDimension.htm) | Convert data into GH\_RadialDimension. |
| Public methodStatic member | [ToGHRadialDimension\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHRadialDimension_Primary.htm) | Converts similar data into a GH\_RadialDimension instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHRadialDimension\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHRadialDimension_Secondary.htm) | Converts similar data into a GH\_RadialDimension instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHRectangle](M_Grasshopper_Kernel_GH_Convert_ToGHRectangle.htm) | Convert data into GH\_Rectangles. |
| Public methodStatic member | [ToGHRectangle\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHRectangle_Primary.htm) | Converts similar data into a GH\_Rectangle instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHRectangle\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHRectangle_Secondary.htm) | Converts similar data into a GH\_Rectangle instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHString](M_Grasshopper_Kernel_GH_Convert_ToGHString.htm) | Convert data into GH\_String. |
| Public methodStatic member | [ToGHString\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHString_Primary.htm) | Converts similar data into a GH\_String instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHString\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHString_Secondary.htm) | Converts similar data into a GH\_String instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHSubD](M_Grasshopper_Kernel_GH_Convert_ToGHSubD.htm) | Convert data into GH\_SubDs. |
| Public methodStatic member | [ToGHSubD\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHSubD_Primary.htm) | Converts similar data into a GH\_SubD instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHSubD\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHSubD_Secondary.htm) | Converts similar data into a GH\_SubD instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHSurface](M_Grasshopper_Kernel_GH_Convert_ToGHSurface.htm) | Convert data into GH\_Surfaces. |
| Public methodStatic member | [ToGHSurface\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHSurface_Primary.htm) | Converts similar data into a GH\_Surface instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHSurface\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHSurface_Secondary.htm) | Converts similar data into a GH\_Surface instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHTextDot](M_Grasshopper_Kernel_GH_Convert_ToGHTextDot.htm) | Convert data into GH\_TextDot. |
| Public methodStatic member | [ToGHTextDot\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHTextDot_Primary.htm) | Converts similar data into a GH\_TextDot instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHTextDot\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHTextDot_Secondary.htm) | Converts similar data into a GH\_TextDot instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHTextEntity](M_Grasshopper_Kernel_GH_Convert_ToGHTextEntity.htm) | Convert data into GH\_TextEntity. |
| Public methodStatic member | [ToGHTextEntity\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHTextEntity_Primary.htm) | Converts similar data into a GH\_TextEntity instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHTextEntity\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHTextEntity_Secondary.htm) | Converts similar data into a GH\_TextEntity instance. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToGHTime](M_Grasshopper_Kernel_GH_Convert_ToGHTime.htm) | Convert data into GH\_Time. |
| Public methodStatic member | [ToGHTime\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHTime_Primary.htm) | Converts similar data into a GH\_Time instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHTime\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHTime_Secondary.htm) | Converts similar data into a GH\_Time instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHVector](M_Grasshopper_Kernel_GH_Convert_ToGHVector.htm) | Convert data into GH\_Vectors. |
| Public methodStatic member | [ToGHVector\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGHVector_Primary.htm) | Converts similar data into a GH\_Vector instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGHVector\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGHVector_Secondary.htm) | Converts similar data into a GH\_Vector instance. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToGoo](M_Grasshopper_Kernel_GH_Convert_ToGoo.htm) | Converts an object into Goo. Does not duplicate the data if a lossless conversion is possible. |
| Public methodStatic member | [ToGUID](M_Grasshopper_Kernel_GH_Convert_ToGUID.htm) | Convert data into Guids. |
| Public methodStatic member | [ToGUID\_Primary](M_Grasshopper_Kernel_GH_Convert_ToGUID_Primary.htm) | Performs a direct cast from Guid, GH\_Guid, String and GH\_String. |
| Public methodStatic member | [ToGUID\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToGUID_Secondary.htm) | Performs indirect casts from other data types into Guids. |
| Public methodStatic member | [ToHatch](M_Grasshopper_Kernel_GH_Convert_ToHatch.htm) | Convert data into Rhino.Geometry.Hatch. |
| Public methodStatic member | [ToHatch\_Primary](M_Grasshopper_Kernel_GH_Convert_ToHatch_Primary.htm) | Performs a direct cast from Rhino.Geometry.Hatch or GH\_Hatch. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToHatch\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToHatch_Secondary.htm) | Attempts to convert other data types into an Rhino.Geometry.Hatch. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToInt32](M_Grasshopper_Kernel_GH_Convert_ToInt32.htm) | Convert data into Int32s. |
| Public methodStatic member | [ToInt32\_Primary](M_Grasshopper_Kernel_GH_Convert_ToInt32_Primary.htm) | Performs a direct cast from Int32 or GH\_Integer. |
| Public methodStatic member | [ToInt32\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToInt32_Secondary.htm) | Performs indirect casts from other data types into Integers. |
| Public methodStatic member | [ToInterval](M_Grasshopper_Kernel_GH_Convert_ToInterval.htm) | Convert data into Rhino.Geometry.Interval. |
| Public methodStatic member | [ToInterval\_Primary](M_Grasshopper_Kernel_GH_Convert_ToInterval_Primary.htm) | Performs a direct cast from OnInterval or GH\_Interval. |
| Public methodStatic member | [ToInterval\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToInterval_Secondary.htm) | Attempts to convert other data types into an Interval. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToLeader](M_Grasshopper_Kernel_GH_Convert_ToLeader.htm) | Convert data into Rhino.Geometry.Leader. |
| Public methodStatic member | [ToLeader\_Primary](M_Grasshopper_Kernel_GH_Convert_ToLeader_Primary.htm) | Performs a direct cast from Rhino.Geometry.Leader or GH\_Leader. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToLeader\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToLeader_Secondary.htm) | Attempts to convert other data types into an Rhino.Geometry.Leader. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToLight\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToLight_Secondary.htm) | Attempts to convert other data types into an Rhino.Geometry.Light. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToLine](M_Grasshopper_Kernel_GH_Convert_ToLine.htm) | Convert data into Rhino.Geometry.Line. |
| Public methodStatic member | [ToLine\_Primary](M_Grasshopper_Kernel_GH_Convert_ToLine_Primary.htm) | Performs a direct cast from OnLine or GH\_Line. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToLine\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToLine_Secondary.htm) | Attempts to convert other data types into an OnLine. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToMatrix](M_Grasshopper_Kernel_GH_Convert_ToMatrix.htm) | Convert data into Rhino.Geometry.Matrix. |
| Public methodStatic member | [ToMatrix\_Primary](M_Grasshopper_Kernel_GH_Convert_ToMatrix_Primary.htm) | Performs a direct cast from Matrix or GH\_Matrix. |
| Public methodStatic member | [ToMatrix\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToMatrix_Secondary.htm) | Attempts to convert other data types into a Matrix. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToMesh](M_Grasshopper_Kernel_GH_Convert_ToMesh.htm) | Convert data into Rhino.Geometry.Mesh. |
| Public methodStatic member | [ToMesh\_Primary](M_Grasshopper_Kernel_GH_Convert_ToMesh_Primary.htm) | Performs a direct cast from Rhino.Geometry.Mesh or GH\_Mesh. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToMesh\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToMesh_Secondary.htm) | Attempts to convert other data types into an OnMesh. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToNextPowerOfTen](M_Grasshopper_Kernel_GH_Convert_ToNextPowerOfTen.htm) | Round a number upwards to the nearest power of ten. |
| Public methodStatic member | [ToPlane](M_Grasshopper_Kernel_GH_Convert_ToPlane.htm) | Convert data into Rhino.Geometry.Plane. |
| Public methodStatic member | [ToPlane\_Primary](M_Grasshopper_Kernel_GH_Convert_ToPlane_Primary.htm) | Performs a direct cast from OnPlane or GH\_Plane. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToPlane\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToPlane_Secondary.htm) | Attempts to convert other data types into an OnPlane. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToPlural](M_Grasshopper_Kernel_GH_Convert_ToPlural.htm) | Apply english rules to convert a noun into its plural form. This algorithm is not water-tight as it will not handle any irregular cases. |
| Public methodStatic member | [ToPoint](M_Grasshopper_Kernel_GH_Convert_ToPoint.htm) | Convert a floating point GDI point structure to an integer rounded point. |
| Public methodStatic member | [ToPoint3d](M_Grasshopper_Kernel_GH_Convert_ToPoint3d.htm) | Convert data into Rhino.Geometry.Point3d. |
| Public methodStatic member | [ToPoint3d\_Primary](M_Grasshopper_Kernel_GH_Convert_ToPoint3d_Primary.htm) | Performs a direct cast from On3dPoint or GH\_Point. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToPoint3d\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToPoint3d_Secondary.htm) | Attempts to convert other data types into an Point. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToPointCloud](M_Grasshopper_Kernel_GH_Convert_ToPointCloud.htm) | Convert data into Rhino.Geometry.PointCloud. |
| Public methodStatic member | [ToPointCloud\_Primary](M_Grasshopper_Kernel_GH_Convert_ToPointCloud_Primary.htm) | Performs a direct cast from Rhino.Geometry.PointCloud or GH\_PointCloud. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToPointCloud\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToPointCloud_Secondary.htm) | Attempts to convert other data types into an Rhino.Geometry.PointCloud. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToPointF](M_Grasshopper_Kernel_GH_Convert_ToPointF.htm) | Convert a Rhino SDK point structure to a GDI point structure. |
| Public methodStatic member | [ToPrevPowerOfTen](M_Grasshopper_Kernel_GH_Convert_ToPrevPowerOfTen.htm) | Round a number downwards to the nearest power of ten. |
| Public methodStatic member | [ToRectangle](M_Grasshopper_Kernel_GH_Convert_ToRectangle.htm) | Convert a floating point GDI rectangle structure to an integer rounded rectangle. Use this method for any and all GUI conversions as the specific rounding scheme used here avoids pixel jitter. |
| Public methodStatic member | [ToRectangle3d](M_Grasshopper_Kernel_GH_Convert_ToRectangle3d.htm) | Convert data into Rhino.Geometry.Line. |
| Public methodStatic member | [ToRectangle3d\_Primary](M_Grasshopper_Kernel_GH_Convert_ToRectangle3d_Primary.htm) | Performs a direct cast from Rectangle3d or GH\_Rectangle. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToRectangle3d\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToRectangle3d_Secondary.htm) | Attempts to convert other data types into a Rectangle3d. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToRelativePath](M_Grasshopper_Kernel_GH_Convert_ToRelativePath.htm) | **Obsolete.**  Create a relative path from two absolute paths. |
| Public methodStatic member | [ToSafeRhinoCommonObject](M_Grasshopper_Kernel_GH_Convert_ToSafeRhinoCommonObject.htm) | Convert RhinoCommon types that are dangerous to use out of context (BrepFace, BrepEdge, etc.) into safe types (Brep, Curve, etc.). |
| Public methodStatic member | [ToSHA\_Hash(AddLanguageSpecificTextSet("LST2CE4F34A\_4?cpp=array&lt;");ByteAddLanguageSpecificTextSet("LST2CE4F34A\_5?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_Convert_ToSHA_Hash.htm) | Create a SHA hash. The hash algorithm is only guaranteed to yield the same results from within a unique application domain. |
| Public methodStatic member | [ToSHA\_Hash(Stream)](M_Grasshopper_Kernel_GH_Convert_ToSHA_Hash_1.htm) | Create a SHA hash. The hash algorithm is only guaranteed to yield the same results from within a unique application domain. |
| Public methodStatic member | [ToSize](M_Grasshopper_Kernel_GH_Convert_ToSize.htm) | Convert a floating point GDI size structure to an integer rounded size. |
| Public methodStatic member | [ToString](M_Grasshopper_Kernel_GH_Convert_ToString.htm) | Convert data into Colors. |
| Public methodStatic member | [ToString\_Primary](M_Grasshopper_Kernel_GH_Convert_ToString_Primary.htm) | Performs a direct cast from String and GH\_String. |
| Public methodStatic member | [ToString\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToString_Secondary.htm) | Creates a String representation of an object by calling the ToString() function. |
| Public methodStatic member | [ToSubD](M_Grasshopper_Kernel_GH_Convert_ToSubD.htm) | Convert data into Rhino.Geometry.SubD. |
| Public methodStatic member | [ToSubD\_Primary](M_Grasshopper_Kernel_GH_Convert_ToSubD_Primary.htm) | Performs a direct cast from OnSubD or GH\_SubD. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToSubD\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToSubD_Secondary.htm) | Attempts to convert other data types into a Sub-D. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToSurface](M_Grasshopper_Kernel_GH_Convert_ToSurface.htm) | Convert data into Rhino.Geometry.Surface. |
| Public methodStatic member | [ToSurface\_Primary](M_Grasshopper_Kernel_GH_Convert_ToSurface_Primary.htm) | Performs a direct cast from OnSurface or GH\_Surface. Data is not quaranteed to be duplicated. If data is of type GH\_Surface, then trim curves are ignored. |
| Public methodStatic member | [ToSurface\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToSurface_Secondary.htm) | Attempts to convert other data types into an IOnSurface. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToTextDot](M_Grasshopper_Kernel_GH_Convert_ToTextDot.htm) | Convert data into Rhino.Geometry.TextDot. |
| Public methodStatic member | [ToTextDot\_Primary](M_Grasshopper_Kernel_GH_Convert_ToTextDot_Primary.htm) | Performs a direct cast from Rhino.Geometry.TextDot or GH\_TextDot. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToTextDot\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToTextDot_Secondary.htm) | Attempts to convert other data types into an Rhino.Geometry.TextDot. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToTextEntity](M_Grasshopper_Kernel_GH_Convert_ToTextEntity.htm) | Convert data into Rhino.Geometry.TextEntity. |
| Public methodStatic member | [ToTextEntity\_Primary](M_Grasshopper_Kernel_GH_Convert_ToTextEntity_Primary.htm) | Performs a direct cast from Rhino.Geometry.TextEntity or GH\_TextEntity. Data is not guaranteed to be duplicated. |
| Public methodStatic member | [ToTextEntity\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToTextEntity_Secondary.htm) | Attempts to convert other data types into an Rhino.Geometry.TextEntity. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToUVInterval](M_Grasshopper_Kernel_GH_Convert_ToUVInterval.htm) | Convert data into Grasshopper.Kernel.Types.UVInterval. |
| Public methodStatic member | [ToUVInterval\_Primary](M_Grasshopper_Kernel_GH_Convert_ToUVInterval_Primary.htm) | Performs a direct cast from UVInterval or GH\_Interval2D. |
| Public methodStatic member | [ToUVInterval\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToUVInterval_Secondary.htm) | Attempts to convert other data types into a UVInterval. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToVariableName](M_Grasshopper_Kernel_GH_Convert_ToVariableName.htm) | Extract the implied variable name from a compound string. A string is considered compound if it contains a parenthesis pair with at least one character within the brackets. |
| Public methodStatic member | [ToVariant](M_Grasshopper_Kernel_GH_Convert_ToVariant.htm) | Convert an object to a Grasshopper Expression Variant if possible. |
| Public methodStatic member | [ToVector3d](M_Grasshopper_Kernel_GH_Convert_ToVector3d.htm) | Convert data into Rhino.Geometry.Vector3d. |
| Public methodStatic member | [ToVector3d\_Primary](M_Grasshopper_Kernel_GH_Convert_ToVector3d_Primary.htm) | Performs a direct cast from On3dVector or GH\_Vector. Data is not quaranteed to be duplicated. |
| Public methodStatic member | [ToVector3d\_Secondary](M_Grasshopper_Kernel_GH_Convert_ToVector3d_Secondary.htm) | Attempts to convert other data types into a Vector. Data is not quaranteed to be duplicated. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public fieldStatic member | [PureDateTicks](F_Grasshopper_Kernel_GH_Convert_PureDateTicks.htm) | Represents the total number of ticks past midnight that (by Grasshopper convention) identifies a pure date. |
| Public fieldStatic member | [PureTimeTicks](F_Grasshopper_Kernel_GH_Convert_PureTimeTicks.htm) | Represents the total number of ticks past a whole second that (by Grasshopper convention) identifies a pure time. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)