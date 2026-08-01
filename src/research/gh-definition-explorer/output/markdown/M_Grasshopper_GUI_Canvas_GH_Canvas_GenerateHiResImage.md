# M_Grasshopper_GUI_Canvas_GH_Canvas_GenerateHiResImage

﻿ GH\_Canvas.GenerateHiResImage Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Canvas Class](../html/T_Grasshopper_GUI_Canvas_GH_Canvas.htm "GH_Canvas Class")

[GH\_Canvas Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Canvas.htm "GH_Canvas Methods")

[AddTagArtist Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_AddTagArtist.htm "AddTagArtist Method ")

[AddValidator Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_AddValidator.htm "AddValidator Method ")

[AutoSaveDocument Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_AutoSaveDocument.htm "AutoSaveDocument Method ")

[CanvasOldSchoolMenu Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_CanvasOldSchoolMenu.htm "CanvasOldSchoolMenu Method ")

[CreateMRUPanels Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_CreateMRUPanels.htm "CreateMRUPanels Method ")

[CreatePreview Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_CreatePreview.htm "CreatePreview Method ")

[DestroyMRUPanels Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_DestroyMRUPanels.htm "DestroyMRUPanels Method ")

[Dispose Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_Dispose.htm "Dispose Method ")

[GenerateHiResImage Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_GenerateHiResImage.htm "GenerateHiResImage Method ")

[GenerateHiResImageTile Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_GenerateHiResImageTile.htm "GenerateHiResImageTile Method ")

[GetCanvasScreenBuffer Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_GetCanvasScreenBuffer.htm "GetCanvasScreenBuffer Method ")

[GetGraphicsObject Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_GetGraphicsObject.htm "GetGraphicsObject Method ")

[HideMRUPanels Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_HideMRUPanels.htm "HideMRUPanels Method ")

[InstantiateNewObject Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Canvas_InstantiateNewObject.htm "InstantiateNewObject Method ")

[Navigate Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_Navigate.htm "Navigate Method ")

[OnPaint Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_OnPaint.htm "OnPaint Method ")

[OnPaintBackground Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_OnPaintBackground.htm "OnPaintBackground Method ")

[OnViewportChanged Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_OnViewportChanged.htm "OnViewportChanged Method ")

[ReevaluateMarkovSuggestions Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_ReevaluateMarkovSuggestions.htm "ReevaluateMarkovSuggestions Method ")

[RemoveAllTagArtists Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveAllTagArtists.htm "RemoveAllTagArtists Method ")

[RemoveTagArtist Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Canvas_RemoveTagArtist.htm "RemoveTagArtist Method ")

[RemoveValidator Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveValidator.htm "RemoveValidator Method ")

[ScheduleRegen Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_ScheduleRegen.htm "ScheduleRegen Method ")

[SetSmartTextRenderingHint Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_SetSmartTextRenderingHint.htm "SetSmartTextRenderingHint Method ")

[ShowComponentSearchBox Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Canvas_ShowComponentSearchBox.htm "ShowComponentSearchBox Method ")

[ShowMRUPanels Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_ShowMRUPanels.htm "ShowMRUPanels Method ")

[ShowNavigationPane Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_ShowNavigationPane.htm "ShowNavigationPane Method ")

[ShowSearchDialog Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_ShowSearchDialog.htm "ShowSearchDialog Method ")

[StartAutoPan Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_StartAutoPan.htm "StartAutoPan Method ")

[StopAutoPan Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_StopAutoPan.htm "StopAutoPan Method ")

[UpdateDocumentPreview Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_UpdateDocumentPreview.htm "UpdateDocumentPreview Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CanvasAddLanguageSpecificTextSet("LST68B69161\_0?cpp=::|nu=.");GenerateHiResImage Method |

Generate a collection of hi-res images of the document.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public List<string> GenerateHiResImage(
	Rectangle rec,
	GH_CanvasAddLanguageSpecificTextSet("LST68B69161_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH_ImageSettings settings,
	out Size totalSize
)
```

```
Public Function GenerateHiResImage ( 
	rec As Rectangle,
	settings As GH_CanvasAddLanguageSpecificTextSet("LST68B69161_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH_ImageSettings,
	<OutAttribute> ByRef totalSize As Size
) As List(Of String)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

rec
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST68B69161\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    BoundingBox rectangle of export.

settings
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST68B69161\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CanvasAddLanguageSpecificTextSet("LST68B69161\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ImageSettings](T_Grasshopper_GUI_Canvas_GH_Canvas_GH_ImageSettings.htm)  
    Hi-res settings.

totalSize
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST68B69161\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Size](https://docs.microsoft.com/dotnet/api/system.drawing.size)AddLanguageSpecificTextSet("LST68B69161\_7?cpp=%");

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST68B69161\_8?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LST68B69161\_9?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
List of file paths that indicate the individual images.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Canvas Class](T_Grasshopper_GUI_Canvas_GH_Canvas.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)