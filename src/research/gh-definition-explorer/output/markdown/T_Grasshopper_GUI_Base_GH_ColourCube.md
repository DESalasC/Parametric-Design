# T_Grasshopper_GUI_Base_GH_ColourCube

﻿ GH\_ColourCube Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Base](../html/N_Grasshopper_GUI_Base.htm "Grasshopper.GUI.Base")

[GH\_ColourCube Class](../html/T_Grasshopper_GUI_Base_GH_ColourCube.htm "GH_ColourCube Class")

[GH\_ColourCube Constructor](../html/M_Grasshopper_GUI_Base_GH_ColourCube__ctor.htm "GH_ColourCube Constructor ")

[GH\_ColourCube Properties](../html/Properties_T_Grasshopper_GUI_Base_GH_ColourCube.htm "GH_ColourCube Properties")

[GH\_ColourCube Methods](../html/Methods_T_Grasshopper_GUI_Base_GH_ColourCube.htm "GH_ColourCube Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ColourCube Class |

Maintains a collection of graphical shapes and coordinates that specify
important features of the Colour Space Cube graphics.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST6D52100A\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.BaseAddLanguageSpecificTextSet("LST6D52100A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ColourCube

**Namespace:**
 [Grasshopper.GUI.Base](N_Grasshopper_GUI_Base.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ColourCube
```

```
Public Class GH_ColourCube
```

AddLanguageTabSet("ID1EBCA");

The GH\_ColourCube type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ColourCube](M_Grasshopper_GUI_Base_GH_ColourCube__ctor.htm) | Create a new instance of this class. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BackFace](P_Grasshopper_GUI_Base_GH_ColourCube_BackFace.htm) | Gets a graphics path describing the back face of the cube. Caller is responsible for disposing of this path instance. |
| Public property | [BottomFace](P_Grasshopper_GUI_Base_GH_ColourCube_BottomFace.htm) | Gets a graphics path describing the bottom face of the cube. Caller is responsible for disposing of this path instance. |
| Public property | [C0](P_Grasshopper_GUI_Base_GH_ColourCube_C0.htm) | Gets the first point in the corner point list. |
| Public property | [C1](P_Grasshopper_GUI_Base_GH_ColourCube_C1.htm) | Gets the second point in the corner point list. |
| Public property | [C2](P_Grasshopper_GUI_Base_GH_ColourCube_C2.htm) | Gets the third point in the corner point list. |
| Public property | [C3](P_Grasshopper_GUI_Base_GH_ColourCube_C3.htm) | Gets the fourth point in the corner point list. |
| Public property | [C4](P_Grasshopper_GUI_Base_GH_ColourCube_C4.htm) | Gets the fifth point in the corner point list. |
| Public property | [C5](P_Grasshopper_GUI_Base_GH_ColourCube_C5.htm) | Gets the sixth point in the corner point list. |
| Public property | [C6](P_Grasshopper_GUI_Base_GH_ColourCube_C6.htm) | Gets the seventh point in the corner point list. |
| Public property | [C7](P_Grasshopper_GUI_Base_GH_ColourCube_C7.htm) | Gets the eighth point in the corner point list. |
| Public property | [Grip](P_Grasshopper_GUI_Base_GH_ColourCube_Grip.htm) | Gets the rectangle that describes the slice grip. |
| Public property | [LeftFace](P_Grasshopper_GUI_Base_GH_ColourCube_LeftFace.htm) | Gets a graphics path describing the left face of the cube. Caller is responsible for disposing of this path instance. |
| Public property | [Pivot](P_Grasshopper_GUI_Base_GH_ColourCube_Pivot.htm) | Gets the point that describes the center of the pivot on the slice. |
| Public property | [S0](P_Grasshopper_GUI_Base_GH_ColourCube_S0.htm) | Gets the first point in the shadow point list. This point is coincident with C0. |
| Public property | [S1](P_Grasshopper_GUI_Base_GH_ColourCube_S1.htm) | Gets the second point in the shadow point list. This is the corner of the drop-shadow on the bottom face. |
| Public property | [S2](P_Grasshopper_GUI_Base_GH_ColourCube_S2.htm) | Gets the third point in the shadow point list. This point is the kink of the drop-shadow on the edge connecting C2 and C3. |
| Public property | [S3](P_Grasshopper_GUI_Base_GH_ColourCube_S3.htm) | Gets the fourth point in the shadow point list. This point is coincident with C7. |
| Public property | [S4](P_Grasshopper_GUI_Base_GH_ColourCube_S4.htm) | Gets the fifth point in the shadow point list. This point is coincident with C4. |
| Public property | [Shadow](P_Grasshopper_GUI_Base_GH_ColourCube_Shadow.htm) | Gets a graphics path describing the outline of the drop shadow. Caller is responsible for disposing of this path instance. |
| Public property | [Silhouette](P_Grasshopper_GUI_Base_GH_ColourCube_Silhouette.htm) | Gets a graphics path describing the silhouette of the cube. Caller is responsible for disposing of this path instance. |
| Public property | [Slice](P_Grasshopper_GUI_Base_GH_ColourCube_Slice.htm) | Gets the rectangle that describes the cutting slide through the current colour space. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Average(Color, Color)](M_Grasshopper_GUI_Base_GH_ColourCube_Average.htm) | Compute the average of two colours. |
| Public method | [Average(Color, Color, Color, Color)](M_Grasshopper_GUI_Base_GH_ColourCube_Average_1.htm) | Compute the average of four colours. |
| Public method | [Blend](M_Grasshopper_GUI_Base_GH_ColourCube_Blend.htm) | Inteprolate between two colours. |
| Public method | [ColorAtRail](M_Grasshopper_GUI_Base_GH_ColourCube_ColorAtRail.htm) | Get the color at a position along the depth rail. |
| Public method | [ColorAtSlice](M_Grasshopper_GUI_Base_GH_ColourCube_ColorAtSlice.htm) | Get the color at a position on the slice. |
| Public method | [RenderAll](M_Grasshopper_GUI_Base_GH_ColourCube_RenderAll.htm) | Call all render methods in the correct order. |
| Public method | [RenderBackEdges](M_Grasshopper_GUI_Base_GH_ColourCube_RenderBackEdges.htm) | Render the edges of the back face creases. |
| Public method | [RenderBackFaces](M_Grasshopper_GUI_Base_GH_ColourCube_RenderBackFaces.htm) | Render the fills of the backfaces. |
| Public method | [RenderDropShadow](M_Grasshopper_GUI_Base_GH_ColourCube_RenderDropShadow.htm) | Render the drop shadow of the cube. |
| Public method | [RenderEdgeShadows](M_Grasshopper_GUI_Base_GH_ColourCube_RenderEdgeShadows.htm) | Render the edge shadows of the cube due to GI. |
| Public method | [RenderForeEdges](M_Grasshopper_GUI_Base_GH_ColourCube_RenderForeEdges.htm) | Render the edges of the fore face creases. |
| Public method | [RenderGrip](M_Grasshopper_GUI_Base_GH_ColourCube_RenderGrip.htm) | Render the slice grip. |
| Public method | [RenderPivot](M_Grasshopper_GUI_Base_GH_ColourCube_RenderPivot.htm) | Render the colour pivot on the current slice. |
| Public method | [RenderSilhouetteEdges](M_Grasshopper_GUI_Base_GH_ColourCube_RenderSilhouetteEdges.htm) | Render the edges of the cube silhouettes. |
| Public method | [RenderSlice](M_Grasshopper_GUI_Base_GH_ColourCube_RenderSlice.htm) | Render the square slice with colour gradients. |
| Public method | [RenderSliceDropShadow](M_Grasshopper_GUI_Base_GH_ColourCube_RenderSliceDropShadow.htm) | Render the drop shadow onto the slice. |
| Public method | [RenderSliceEdgeShadows](M_Grasshopper_GUI_Base_GH_ColourCube_RenderSliceEdgeShadows.htm) | Render the edge shadows of the slice due to GI. |
| Public method | [RenderSliceSilhouetteEdges](M_Grasshopper_GUI_Base_GH_ColourCube_RenderSliceSilhouetteEdges.htm) | Render the silhouette edges of the slice. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Base Namespace](N_Grasshopper_GUI_Base.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)