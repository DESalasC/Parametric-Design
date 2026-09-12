# T_Grasshopper_Kernel_Geometry_SpatialTrees_Validation3d_1

﻿ Validation3d(T) Delegate

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Geometry.SpatialTrees](../html/N_Grasshopper_Kernel_Geometry_SpatialTrees.htm "Grasshopper.Kernel.Geometry.SpatialTrees")

[Coordinates3d(T) Delegate](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Coordinates3d_1.htm "Coordinates3d(T) Delegate")

[Index3d(T) Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1.htm "Index3d(T) Class")

[Node3d(T) Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Class")

[TreeDelegates Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_TreeDelegates.htm "TreeDelegates Class")

[Validation3d(T) Delegate](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Validation3d_1.htm "Validation3d(T) Delegate")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Validation3dAddLanguageSpecificTextSet("LST10B581D3\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST10B581D3\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Delegate |

Delegate to be used during advanced customized searches.

**Namespace:**
 [Grasshopper.Kernel.Geometry.SpatialTrees](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public delegate bool Validation3d<T>(
	T element,
	int globalIndex,
	Node3d<T> node
)
```

```
Public Delegate Function Validation3d(Of T) ( 
	element As T,
	globalIndex As Integer,
	node As Node3d(Of T)
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

element
:   Type: T  
    Potential hit.

globalIndex
:   Type: [SystemAddLanguageSpecificTextSet("LST10B581D3\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item in global list.

node
:   Type: [Grasshopper.Kernel.Geometry.SpatialTreesAddLanguageSpecificTextSet("LST10B581D3\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Node3d](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)AddLanguageSpecificTextSet("LST10B581D3\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST10B581D3\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Node containing the element.

#### Type Parameters

T
:   Element type.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if item can be included in the search, false if not.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Geometry.SpatialTrees Namespace](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)