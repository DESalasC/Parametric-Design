# M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion_1

﻿ GH\_Attributes(T).IsPickRegion Method (RectangleF, GH\_PickBox)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Attributes(T) Class](../html/T_Grasshopper_Kernel_GH_Attributes_1.htm "GH_Attributes(T) Class")

[GH\_Attributes(T) Methods](../html/Methods_T_Grasshopper_Kernel_GH_Attributes_1.htm "GH_Attributes(T) Methods")

[IsPickRegion Method](../html/Overload_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm "IsPickRegion Method ")

[IsPickRegion Method (PointF)](../html/M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm "IsPickRegion Method (PointF)")

[IsPickRegion Method (RectangleF, GH\_PickBox)](../html/M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion_1.htm "IsPickRegion Method (RectangleF, GH_PickBox)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AttributesAddLanguageSpecificTextSet("LSTDEB8AA3C\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTDEB8AA3C\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTDEB8AA3C\_2?cpp=::|nu=.");IsPickRegion Method (RectangleF, GH\_PickBox) |

Determines whether a rectangle is a valid pick region for this object.
By default, the picking rectangle is intersected with the Bounds rectangle.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual bool IsPickRegion(
	RectangleF box,
	GH_PickBox method
)
```

```
Public Overridable Function IsPickRegion ( 
	box As RectangleF,
	method As GH_PickBox
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTDEB8AA3C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Selection box.

method
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTDEB8AA3C\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PickBox](T_Grasshopper_Kernel_GH_PickBox.htm)  
    Selection method.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

#### Implements

[IGH\_AttributesAddLanguageSpecificTextSet("LSTDEB8AA3C\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");IsPickRegion(RectangleF, GH\_PickBox)](M_Grasshopper_Kernel_IGH_Attributes_IsPickRegion_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_AttributesAddLanguageSpecificTextSet("LSTDEB8AA3C\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTDEB8AA3C\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_Attributes_1.htm)

[IsPickRegion Overload](Overload_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)