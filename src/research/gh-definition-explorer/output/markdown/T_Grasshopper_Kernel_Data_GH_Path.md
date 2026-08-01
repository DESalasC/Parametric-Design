# T_Grasshopper_Kernel_Data_GH_Path

﻿ GH\_Path Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Path Class](../html/T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Class")

[GH\_Path Constructor](../html/Overload_Grasshopper_Kernel_Data_GH_Path__ctor.htm "GH_Path Constructor ")

[GH\_Path Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Properties")

[GH\_Path Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Methods")

[GH\_Path Operators](../html/Operators_T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Operators")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Path Class |

Describes the path in structure space of a data item or a list of items.
A path consists of a series of integers, each one of which represents an index in a branch structure.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST20B9421\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST20B9421\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Path : IComparable<GH_Path>, 
	IComparer<GH_Path>, GH_ISerializable
```

```
Public Class GH_Path
	Implements IComparable(Of GH_Path), IComparer(Of GH_Path), 
	GH_ISerializable
```

AddLanguageTabSet("ID1EBCA");

The GH\_Path type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_PathAddLanguageSpecificTextSet("LST20B9421\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Data_GH_Path__ctor.htm) | Default constructor, creates a path with zero elements. |
| Public method | [GH\_Path(GH\_Path)](M_Grasshopper_Kernel_Data_GH_Path__ctor_1.htm) | Creates an exact copy of another path. |
| Public method | [GH\_Path(Int32)](M_Grasshopper_Kernel_Data_GH_Path__ctor_2.htm) | Creates a new path with a single element. |
| Public method | [GH\_Path(AddLanguageSpecificTextSet("LST20B9421\_3?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST20B9421\_4?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_Data_GH_Path__ctor_3.htm) | Creates a new path from a series of elements. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Indices](P_Grasshopper_Kernel_Data_GH_Path_Indices.htm) | Gets or sets the entire index space; the path that identifies an element in structure space. You should not change the index space when the path is used inside a structure since it will invalidate the sort order. If you don't know what you're doing, for Pete's sake don't touch this. |
| Public property | [Length](P_Grasshopper_Kernel_Data_GH_Path_Length.htm) | Returns the number of dimensions in the path. |
| Public property | [Valid](P_Grasshopper_Kernel_Data_GH_Path_Valid.htm) | Gets whether this path is valid. Invalid paths either have no elements or negative elements. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendElement](M_Grasshopper_Kernel_Data_GH_Path_AppendElement.htm) | Create a new path by appending a new index value to this path. |
| Public method | [Compare](M_Grasshopper_Kernel_Data_GH_Path_Compare.htm) | Compare two paths. This function determines the Sorting behaviour of paths. |
| Public method | [CompareTo](M_Grasshopper_Kernel_Data_GH_Path_CompareTo.htm) | Compare this path to another path. This function determines the Sorting behaviour of paths. |
| Public method | [CullElement](M_Grasshopper_Kernel_Data_GH_Path_CullElement.htm) | Removes the last index value from the path. If the path is already empty, nothing will happen. |
| Public method | [CullFirstElement](M_Grasshopper_Kernel_Data_GH_Path_CullFirstElement.htm) | Removes the first index value from the path. If the path is already empty, nothing will happen. |
| Public method | [Format](M_Grasshopper_Kernel_Data_GH_Path_Format.htm) | Format a path. |
| Public method | [FromString](M_Grasshopper_Kernel_Data_GH_Path_FromString.htm) | Try to deserialize a GH\_Path from a String. |
| Public method | [GetHashCode](M_Grasshopper_Kernel_Data_GH_Path_GetHashCode.htm) | Specialized Hash code pattern. (Overrides [ObjectAddLanguageSpecificTextSet("LST20B9421\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GetHashCodeAddLanguageSpecificTextSet("LST20B9421\_6?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-object-gethashcode).) |
| Public method | [Increment(Int32)](M_Grasshopper_Kernel_Data_GH_Path_Increment.htm) | Increment a specific index in this path by one. |
| Public method | [Increment(Int32, Int32)](M_Grasshopper_Kernel_Data_GH_Path_Increment_1.htm) | Increment a specific index in this path by one. |
| Public method | [IsAncestor](M_Grasshopper_Kernel_Data_GH_Path_IsAncestor.htm) | Test another path to see if it is an ancestor of this path. For a path to be considered an ancestor, it must share the initial dimensions. |
| Public method | [IsCoincident(GH\_Path)](M_Grasshopper_Kernel_Data_GH_Path_IsCoincident.htm) | Test to see if this path is coincident with another path. |
| Public method | [IsCoincident(AddLanguageSpecificTextSet("LST20B9421\_7?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST20B9421\_8?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_Data_GH_Path_IsCoincident_1.htm) | Test to see if this path is coincident with set of integers. |
| Public method | [PrependElement](M_Grasshopper_Kernel_Data_GH_Path_PrependElement.htm) | Create a new path by prepending a new index value to this path. |
| Public method | [Read](M_Grasshopper_Kernel_Data_GH_Path_Read.htm) | Read this path from an archive. |
| Public methodStatic member | [SplitPathLikeString](M_Grasshopper_Kernel_Data_GH_Path_SplitPathLikeString.htm) | Try to split up a path-like formatted string "{A;B;C}(i)" into component parts. |
| Public method | [ToStringAddLanguageSpecificTextSet("LST20B9421\_9?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Data_GH_Path_ToString.htm) | Concatenates the indices in the path. (Overrides [ObjectAddLanguageSpecificTextSet("LST20B9421\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST20B9421\_11?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |
| Public method | [ToString(Boolean)](M_Grasshopper_Kernel_Data_GH_Path_ToString_1.htm) | Concatenates the indices in the path. |
| Public method | [Write](M_Grasshopper_Kernel_Data_GH_Path_Write.htm) | Write this path to an archive. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [Equality](M_Grasshopper_Kernel_Data_GH_Path_op_Equality.htm) |  |
| Public operatorStatic member | [GreaterThan](M_Grasshopper_Kernel_Data_GH_Path_op_GreaterThan.htm) |  |
| Public operatorStatic member | [Inequality](M_Grasshopper_Kernel_Data_GH_Path_op_Inequality.htm) |  |
| Public operatorStatic member | [LessThan](M_Grasshopper_Kernel_Data_GH_Path_op_LessThan.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)