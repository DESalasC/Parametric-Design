# M_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion

﻿ GH\_Attributes(T).IsPickRegion Method (PointF)

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
| GH\_AttributesAddLanguageSpecificTextSet("LST180D7476\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST180D7476\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST180D7476\_2?cpp=::|nu=.");IsPickRegion Method (PointF) |

Determines whether a point is within the pickable region for this object.
By default, any point inside the Bounds is treated as pickable.

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
	PointF point
)
```

```
Public Overridable Function IsPickRegion ( 
	point As PointF
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

point
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST180D7476\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Point location to test.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

#### Implements

[IGH\_AttributesAddLanguageSpecificTextSet("LST180D7476\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");IsPickRegion(PointF)](M_Grasshopper_Kernel_IGH_Attributes_IsPickRegion.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_AttributesAddLanguageSpecificTextSet("LST180D7476\_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST180D7476\_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_Attributes_1.htm)

[IsPickRegion Overload](Overload_Grasshopper_Kernel_GH_Attributes_1_IsPickRegion.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)