# T_Grasshopper_GUI_Canvas_GH_Skin

﻿ GH\_Skin Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Skin Class](../html/T_Grasshopper_GUI_Canvas_GH_Skin.htm "GH_Skin Class")

[GH\_Skin Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Skin.htm "GH_Skin Methods")

[GH\_Skin Fields](../html/Fields_T_Grasshopper_GUI_Canvas_GH_Skin.htm "GH_Skin Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Skin Class |

Provides static access to typical Palletes and other GUI colours.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST3192359C\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST3192359C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Skin

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_Skin
```

```
Public NotInheritable Class GH_Skin
```

AddLanguageTabSet("ID1EBCA");

The GH\_Skin type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [LoadSkin](M_Grasshopper_GUI_Canvas_GH_Skin_LoadSkin.htm) | Instantiate all palette and gui defaults. This function reads the colour values out of grasshopper\_gui.xml settings database if it exists. |
| Public methodStatic member | [SaveSkin](M_Grasshopper_GUI_Canvas_GH_Skin_SaveSkin.htm) | Store all palette and gui defaults. This function writes the colour values out to grasshopper\_gui.xml settings database. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public fieldStatic member | [canvas\_back](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_back.htm) | Specifies canvas background colour. |
| Public fieldStatic member | [canvas\_edge](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_edge.htm) | Specifies canvas edge colour. |
| Public fieldStatic member | [canvas\_grid](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_grid.htm) | Specifies canvas grid colour. |
| Public fieldStatic member | [canvas\_grid\_col](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_grid_col.htm) | Specifies the interval of the canvas grid columns. |
| Public fieldStatic member | [canvas\_grid\_row](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_grid_row.htm) | Specifies the interval of the canvas grid rows. |
| Public fieldStatic member | [canvas\_mono](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_mono.htm) | Canvas monochromatic flag. If True, the canvas background is a solid colour. |
| Public fieldStatic member | [canvas\_mono\_color](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_mono_color.htm) | If canvas\_mono is set to true, this colour specified the solid background fill for the canvas. |
| Public fieldStatic member | [canvas\_shade](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_shade.htm) | Specifies the colour of the canvas drop shadow. |
| Public fieldStatic member | [canvas\_shade\_size](F_Grasshopper_GUI_Canvas_GH_Skin_canvas_shade_size.htm) | Specifies the size of the canvas drop shadow. |
| Public fieldStatic member | [group\_back](F_Grasshopper_GUI_Canvas_GH_Skin_group_back.htm) | Specifies the default fill colour for Group objects. |
| Public fieldStatic member | [palette\_black\_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_black_selected.htm) | Black palette, selected. |
| Public fieldStatic member | [palette\_black\_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_black_standard.htm) | Black palette, unselected. |
| Public fieldStatic member | [palette\_blue\_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_blue_selected.htm) | Blue palette, selected. |
| Public fieldStatic member | [palette\_blue\_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_blue_standard.htm) | Blue palette, unselected. |
| Public fieldStatic member | [palette\_brown\_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_brown_selected.htm) | Brown palette, selected. |
| Public fieldStatic member | [palette\_brown\_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_brown_standard.htm) | Brown palette, unselected. |
| Public fieldStatic member | [palette\_error\_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_error_selected.htm) | Errors, selected palette. Default background for parameters and components that carry errors. |
| Public fieldStatic member | [palette\_error\_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_error_standard.htm) | Errors, unselected palette. Default background for parameters and components that carry errors. |
| Public fieldStatic member | [palette\_grey\_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_grey_selected.htm) | Grey palette, selected. |
| Public fieldStatic member | [palette\_grey\_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_grey_standard.htm) | Grey palette, unselected. |
| Public fieldStatic member | [palette\_hidden\_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_hidden_selected.htm) | Hidden, selected palette. Default background for PanelHidden (preview=off) parameters and components. |
| Public fieldStatic member | [palette\_hidden\_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_hidden_standard.htm) | Hidden, unselected palette. Default background for PanelHidden (preview=off) parameters and components. |
| Public fieldStatic member | [palette\_locked\_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_locked_selected.htm) | Locked, selected palette. Default background for locked parameters and components. |
| Public fieldStatic member | [palette\_locked\_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_locked_standard.htm) | Locked, unselected palette. Default background for locked parameters and components. |
| Public fieldStatic member | [palette\_normal\_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_normal_selected.htm) | Normal, selected palette. Default background for parameters and components. |
| Public fieldStatic member | [palette\_normal\_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_normal_standard.htm) | Normal, unselected palette. Default background for parameters and components. |
| Public fieldStatic member | [palette\_pink\_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_pink_selected.htm) | Pink palette, selected. |
| Public fieldStatic member | [palette\_pink\_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_pink_standard.htm) | Pink palette, unselected. |
| Public fieldStatic member | [palette\_trans\_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_trans_selected.htm) | Transparent palette, selected. |
| Public fieldStatic member | [palette\_trans\_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_trans_standard.htm) | Transparent palette, unselected. |
| Public fieldStatic member | [palette\_warning\_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_warning_selected.htm) | Warnings, selected palette. Default background for parameters and components that carry warnings. |
| Public fieldStatic member | [palette\_warning\_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_warning_standard.htm) | Warnings, unselected palette. Default background for parameters and components that carry warnings. |
| Public fieldStatic member | [palette\_white\_selected](F_Grasshopper_GUI_Canvas_GH_Skin_palette_white_selected.htm) | White palette, selected. |
| Public fieldStatic member | [palette\_white\_standard](F_Grasshopper_GUI_Canvas_GH_Skin_palette_white_standard.htm) | White palette, unselected. |
| Public fieldStatic member | [panel\_back](F_Grasshopper_GUI_Canvas_GH_Skin_panel_back.htm) | Specifies the default fill colour for Panel objects. |
| Public fieldStatic member | [wire\_default](F_Grasshopper_GUI_Canvas_GH_Skin_wire_default.htm) | Specifies the default wire colour. |
| Public fieldStatic member | [wire\_empty](F_Grasshopper_GUI_Canvas_GH_Skin_wire_empty.htm) | Specifies the colour for empty (null) wires. |
| Public fieldStatic member | [wire\_selected\_a](F_Grasshopper_GUI_Canvas_GH_Skin_wire_selected_a.htm) | Specifies the colour for wires at the selected end. |
| Public fieldStatic member | [wire\_selected\_b](F_Grasshopper_GUI_Canvas_GH_Skin_wire_selected_b.htm) | Specifies the colour for wires at the unselected end. |
| Public fieldStatic member | [zui\_edge](F_Grasshopper_GUI_Canvas_GH_Skin_zui_edge.htm) | Specifies the default edge colour for ZUI elements. |
| Public fieldStatic member | [zui\_edge\_highlight](F_Grasshopper_GUI_Canvas_GH_Skin_zui_edge_highlight.htm) | Specifies the default edge colour for highlighted ZUI elements. |
| Public fieldStatic member | [zui\_fill](F_Grasshopper_GUI_Canvas_GH_Skin_zui_fill.htm) | Specifies the default fill colour for ZUI elements. |
| Public fieldStatic member | [zui\_fill\_highlight](F_Grasshopper_GUI_Canvas_GH_Skin_zui_fill_highlight.htm) | Specifies the default fill colour for highlighted ZUI elements. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)