# M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires

﻿ GH\_Attributes(T).RenderIncomingWires Method (GH\_Painter, IEnumerable(IGH\_Param), GH\_ParamWireDisplay)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Attributes(T) Class](../html/T_Grasshopper_Kernel_GH_Attributes_1.htm "GH_Attributes(T) Class")

[GH\_Attributes(T) Methods](../html/Methods_T_Grasshopper_Kernel_GH_Attributes_1.htm "GH_Attributes(T) Methods")

[RenderIncomingWires Method](../html/Overload_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires.htm "RenderIncomingWires Method ")

[RenderIncomingWires Method (GH\_Painter, IEnumerable(IGH\_Param), GH\_ParamWireDisplay)](../html/M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires.htm "RenderIncomingWires Method (GH_Painter, IEnumerable(IGH_Param), GH_ParamWireDisplay)")

[RenderIncomingWires Method (GH\_Painter, IEnumerable(IGH\_Param), IEnumerable(Pen))](../html/M_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires_1.htm "RenderIncomingWires Method (GH_Painter, IEnumerable(IGH_Param), IEnumerable(Pen))")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AttributesAddLanguageSpecificTextSet("LSTAFCFA9DC\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTAFCFA9DC\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTAFCFA9DC\_2?cpp=::|nu=.");RenderIncomingWires Method (GH\_Painter, IEnumerableAddLanguageSpecificTextSet("LSTAFCFA9DC\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LSTAFCFA9DC\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_ParamWireDisplay) |

Utility function for derived classes. This method draws all the wires going into the
left side of the attributes.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected void RenderIncomingWires(
	GH_Painter painter,
	IEnumerable<IGH_Param> sources,
	GH_ParamWireDisplay style
)
```

```
Protected Sub RenderIncomingWires ( 
	painter As GH_Painter,
	sources As IEnumerable(Of IGH_Param),
	style As GH_ParamWireDisplay
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

painter
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LSTAFCFA9DC\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Painter](T_Grasshopper_GUI_Canvas_GH_Painter.htm)  
    The graphics object to paint with

sources
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LSTAFCFA9DC\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LSTAFCFA9DC\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_Param](T_Grasshopper_Kernel_IGH_Param.htm)AddLanguageSpecificTextSet("LSTAFCFA9DC\_8?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    A list of sources that will be connected with the input grip of this attribute

style
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTAFCFA9DC\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParamWireDisplay](T_Grasshopper_Kernel_GH_ParamWireDisplay.htm)  
    Style for wire display.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_AttributesAddLanguageSpecificTextSet("LSTAFCFA9DC\_10?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTAFCFA9DC\_11?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_Attributes_1.htm)

[RenderIncomingWires Overload](Overload_Grasshopper_Kernel_GH_Attributes_1_RenderIncomingWires.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)