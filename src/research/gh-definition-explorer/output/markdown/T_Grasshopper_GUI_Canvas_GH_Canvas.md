# T_Grasshopper_GUI_Canvas_GH_Canvas

﻿ GH\_Canvas Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Canvas Class](../html/T_Grasshopper_GUI_Canvas_GH_Canvas.htm "GH_Canvas Class")

[GH\_Canvas Constructor](../html/M_Grasshopper_GUI_Canvas_GH_Canvas__ctor.htm "GH_Canvas Constructor ")

[GH\_Canvas Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_Canvas.htm "GH_Canvas Properties")

[GH\_Canvas Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Canvas.htm "GH_Canvas Methods")

[GH\_Canvas Events](../html/Events_T_Grasshopper_GUI_Canvas_GH_Canvas.htm "GH_Canvas Events")

[GH\_Canvas Fields](../html/Fields_T_Grasshopper_GUI_Canvas_GH_Canvas.htm "GH_Canvas Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Canvas Class |

The GH\_Canvas is the control that handles all mouse and paint events for a single loaded document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST6B8C5994\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST6B8C5994\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");MarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
    [System.ComponentModelAddLanguageSpecificTextSet("LST6B8C5994\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Component](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
      [System.Windows.FormsAddLanguageSpecificTextSet("LST6B8C5994\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Control](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
        Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST6B8C5994\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Canvas

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Canvas : Control
```

```
Public Class GH_Canvas
	Inherits Control
```

AddLanguageTabSet("ID1EBCA");

The GH\_Canvas type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_Canvas](M_Grasshopper_GUI_Canvas_GH_Canvas__ctor.htm) | Initializes a new instance of the GH\_Canvas class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ActiveInteraction](P_Grasshopper_GUI_Canvas_GH_Canvas_ActiveInteraction.htm) | Gets or sets the currently active interaction object. |
| Public property | [ActiveObject](P_Grasshopper_GUI_Canvas_GH_Canvas_ActiveObject.htm) | Gets or sets the currently active object. |
| Public property | [ActiveWidget](P_Grasshopper_GUI_Canvas_GH_Canvas_ActiveWidget.htm) | Gets or sets the currently active widget. |
| Public property | [CursorCanvasPosition](P_Grasshopper_GUI_Canvas_GH_Canvas_CursorCanvasPosition.htm) | Gets the location of the cursor in Canvas coordinates. |
| Public property | [CursorControlPosition](P_Grasshopper_GUI_Canvas_GH_Canvas_CursorControlPosition.htm) | Gets the location of the cursor in Control coordinates. |
| Public propertyStatic member | [DisplayVoronoiWarning](P_Grasshopper_GUI_Canvas_GH_Canvas_DisplayVoronoiWarning.htm) | Gets or sets whether the Voronoi Over-dose warning message is displayed. This property is set once at Grasshopper startup to True. |
| Public property | [Document](P_Grasshopper_GUI_Canvas_GH_Canvas_Document.htm) | Gets or sets the document currently loaded in this canvas. |
| Public property | [DrawingMode](P_Grasshopper_GUI_Canvas_GH_Canvas_DrawingMode.htm) | Gets the current drawing mode for this canvas. |
| Public property | [HasControlWithFocus](P_Grasshopper_GUI_Canvas_GH_Canvas_HasControlWithFocus.htm) | Gets whether or not this canvas has a child control on it with focus. |
| Public property | [IsActiveInteraction](P_Grasshopper_GUI_Canvas_GH_Canvas_IsActiveInteraction.htm) | Gets a value indicating whether or not there is an interaction object loaded in this canvas. |
| Public property | [IsActiveObject](P_Grasshopper_GUI_Canvas_GH_Canvas_IsActiveObject.htm) | Gets a value indicating whether or not an object is currently activated. |
| Public property | [IsActiveWidget](P_Grasshopper_GUI_Canvas_GH_Canvas_IsActiveWidget.htm) | Gets a value indicating whether or not a widget is currently activated. |
| Public property | [IsDocument](P_Grasshopper_GUI_Canvas_GH_Canvas_IsDocument.htm) | Gets a value indicating whether or not a document is currently loaded in this canvas. |
| Public property | [MarkovSuggestions](P_Grasshopper_GUI_Canvas_GH_Canvas_MarkovSuggestions.htm) |  |
| Public property | [ModifiersEnabled](P_Grasshopper_GUI_Canvas_GH_Canvas_ModifiersEnabled.htm) | Gets or sets the modifiers enabled flag. When modifiers are disabled, only zooming and panning is still allowed. |
| Public propertyStatic member | [NavigationPanDown](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationPanDown.htm) | Gets or sets the special key for panning down. |
| Public propertyStatic member | [NavigationPanLeft](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationPanLeft.htm) | Gets or sets the special key for panning left. |
| Public propertyStatic member | [NavigationPanPixels](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationPanPixels.htm) | Gets or sets the number of pixels for each pan operation. |
| Public propertyStatic member | [NavigationPanRight](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationPanRight.htm) | Gets or sets the special key for panning right. |
| Public propertyStatic member | [NavigationPanUp](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationPanUp.htm) | Gets or sets the special key for panning up. |
| Public propertyStatic member | [NavigationZoomFactor](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationZoomFactor.htm) | Gets or sets the zoom factor for navigation zoom operations. |
| Public propertyStatic member | [NavigationZoomIn](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationZoomIn.htm) | Gets or sets the special key for zooming in. |
| Public propertyStatic member | [NavigationZoomOut](P_Grasshopper_GUI_Canvas_GH_Canvas_NavigationZoomOut.htm) | Gets or sets the special key for zooming in. |
| Public property | [Painter](P_Grasshopper_GUI_Canvas_GH_Canvas_Painter.htm) | Gets the painter object that handles most of the drawing logic for this canvas. |
| Public property | [Painting](P_Grasshopper_GUI_Canvas_GH_Canvas_Painting.htm) | Gets whether this canvas is currently busy painting itself. |
| Public property | [RecordPreviewBoundary](P_Grasshopper_GUI_Canvas_GH_Canvas_RecordPreviewBoundary.htm) |  |
| Public property | [TagArtistIDs](P_Grasshopper_GUI_Canvas_GH_Canvas_TagArtistIDs.htm) | Gets all the TagArtist IDs in this Canvas. |
| Public propertyStatic member | [ThumbnailSize](P_Grasshopper_GUI_Canvas_GH_Canvas_ThumbnailSize.htm) | Gets the thumbnail size for documents. |
| Public property | [TooltipDelay](P_Grasshopper_GUI_Canvas_GH_Canvas_TooltipDelay.htm) | Gets the delay (in milliseconds) required for a tooltip popup. This delay is a user setting stored under the Canvas:TooltipDelay field of the core settings. |
| Public property | [Validator](P_Grasshopper_GUI_Canvas_GH_Canvas_Validator.htm) | Provides access to all the validators associated with this canvas. |
| Public property | [Viewport](P_Grasshopper_GUI_Canvas_GH_Canvas_Viewport.htm) | Gets the viewport that determines the panning and zooming for this canvas. |
| Public property | [Widgets](P_Grasshopper_GUI_Canvas_GH_Canvas_Widgets.htm) | Gets a list of all the widgets on this canvas. |
| Public propertyStatic member | [ZoomFadeHigh](P_Grasshopper_GUI_Canvas_GH_Canvas_ZoomFadeHigh.htm) | Gets the ZUI fade alpha value for the high zoom level threshold. This static field gets set on every Canvas paint start. The high threshold is typically used for ZUI elements that only appear when zoomed in. |
| Public propertyStatic member | [ZoomFadeLow](P_Grasshopper_GUI_Canvas_GH_Canvas_ZoomFadeLow.htm) | Gets the ZUI fade alpha value for the low zoom level threshold. This static field gets set on every Canvas paint start. The low threshold is typically used for fading of icons and object names. |
| Public propertyStatic member | [ZoomFadeMedium](P_Grasshopper_GUI_Canvas_GH_Canvas_ZoomFadeMedium.htm) | Gets the ZUI fade alpha value for the medium zoom level threshold. This static field gets set on every Canvas paint start. The medium threshold is typically used for non-informative UI elements such as highlights. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddTagArtist](M_Grasshopper_GUI_Canvas_GH_Canvas_AddTagArtist.htm) | Add a Tag Artist instance to this canvas. |
| Public method | [AddValidator](M_Grasshopper_GUI_Canvas_GH_Canvas_AddValidator.htm) | Add a new drop validator to the canvas. |
| Public method | [AutoSaveDocument](M_Grasshopper_GUI_Canvas_GH_Canvas_AutoSaveDocument.htm) |  |
| Public method | [CanvasOldSchoolMenu](M_Grasshopper_GUI_Canvas_GH_Canvas_CanvasOldSchoolMenu.htm) |  |
| Public method | [CreateMRUPanels](M_Grasshopper_GUI_Canvas_GH_Canvas_CreateMRUPanels.htm) | Create new MRU panels. This function only does something if there is no document loaded in the canvas. |
| Public method | [CreatePreview](M_Grasshopper_GUI_Canvas_GH_Canvas_CreatePreview.htm) | Render this canvas to a thumbnail preview. |
| Public method | [DestroyMRUPanels](M_Grasshopper_GUI_Canvas_GH_Canvas_DestroyMRUPanels.htm) | Destroy any MRU panels that might be in existence. |
| Protected method | [Dispose](M_Grasshopper_GUI_Canvas_GH_Canvas_Dispose.htm) | Releases the unmanaged resources used by the GH\_Canvas and optionally releases the managed resources (Overrides [ControlAddLanguageSpecificTextSet("LST6B8C5994\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Dispose(Boolean)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.dispose#system-windows-forms-control-dispose(system-boolean)).) |
| Public method | [GenerateHiResImage](M_Grasshopper_GUI_Canvas_GH_Canvas_GenerateHiResImage.htm) | Generate a collection of hi-res images of the document. |
| Public method | [GenerateHiResImageTile](M_Grasshopper_GUI_Canvas_GH_Canvas_GenerateHiResImageTile.htm) | Generate a single tile in a Hi-Res image export. |
| Public method | [GetCanvasScreenBuffer](M_Grasshopper_GUI_Canvas_GH_Canvas_GetCanvasScreenBuffer.htm) | Get a bitmap that resembles the current state of the canvas. |
| Public method | [GetGraphicsObject](M_Grasshopper_GUI_Canvas_GH_Canvas_GetGraphicsObject.htm) | Gets a graphics object for this control. You are not allowed to draw with this object, use it only for visibility testing and such. If you're inside a canvas update, use the Graphics() property instead. You must dispose of the Graphics object returned by this method or resources will be leaked. |
| Public method | [HideMRUPanels](M_Grasshopper_GUI_Canvas_GH_Canvas_HideMRUPanels.htm) | Hide all existing MRU panels by sliding them out of view. |
| Public method | [InstantiateNewObject(Guid, PointF, Boolean)](M_Grasshopper_GUI_Canvas_GH_Canvas_InstantiateNewObject.htm) |  |
| Public method | [InstantiateNewObject(Guid, String, PointF, Boolean)](M_Grasshopper_GUI_Canvas_GH_Canvas_InstantiateNewObject_1.htm) |  |
| Public method | [Navigate](M_Grasshopper_GUI_Canvas_GH_Canvas_Navigate.htm) | Perform a single navigation step. |
| Protected method | [OnPaint](M_Grasshopper_GUI_Canvas_GH_Canvas_OnPaint.htm) | (Overrides [ControlAddLanguageSpecificTextSet("LST6B8C5994\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaint(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaint#system-windows-forms-control-onpaint(system-windows-forms-painteventargs)).) |
| Protected method | [OnPaintBackground](M_Grasshopper_GUI_Canvas_GH_Canvas_OnPaintBackground.htm) | (Overrides [ControlAddLanguageSpecificTextSet("LST6B8C5994\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");OnPaintBackground(PaintEventArgs)](https://docs.microsoft.com/dotnet/api/system.windows.forms.control.onpaintbackground#system-windows-forms-control-onpaintbackground(system-windows-forms-painteventargs)).) |
| Public method | [OnViewportChanged](M_Grasshopper_GUI_Canvas_GH_Canvas_OnViewportChanged.htm) | Ensure the canvas and document viewport data are synchronised and raises the ViewportChanged event. |
| Public method | [ReevaluateMarkovSuggestions](M_Grasshopper_GUI_Canvas_GH_Canvas_ReevaluateMarkovSuggestions.htm) |  |
| Public method | [RemoveAllTagArtists](M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveAllTagArtists.htm) | Remove all IGH\_TagArtists from this canvas. Do not use this method unless you want to screw over everyone else. |
| Public method | [RemoveTagArtist(Guid)](M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveTagArtist_1.htm) | Remove all IGH\_TagArtists from this canvas that match a certain ID. |
| Public method | [RemoveTagArtist(IGH\_TagArtist)](M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveTagArtist.htm) | Remove a specific tag artist from this canvas. If the instance occurs multiple times in the TagArtist list, all instances will be removed. |
| Public method | [RemoveValidator](M_Grasshopper_GUI_Canvas_GH_Canvas_RemoveValidator.htm) | Remove a drop validator from the canvas. |
| Public method | [ScheduleRegen](M_Grasshopper_GUI_Canvas_GH_Canvas_ScheduleRegen.htm) | Schedule a regen to occur after the specified number of milliseconds have elapsed. If a Regen is called in this time frame, the schedule will be cleared. Only a single schedule can be active at any time, so any call to ScheduleRegen will clear existing schedules. |
| Public method | [SetSmartTextRenderingHint](M_Grasshopper_GUI_Canvas_GH_Canvas_SetSmartTextRenderingHint.htm) | When this method is called during a redraw, the TextRenderingHint of the associated graphics object will be set to either GH\_CrispText or GH\_SmoothText depending on zoom level. |
| Public method | [ShowComponentSearchBoxAddLanguageSpecificTextSet("LST6B8C5994\_8?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_Canvas_GH_Canvas_ShowComponentSearchBox.htm) | Display the component Search dialog at the current mouse location. The dialog cannot be shown if ModifiersEnabled=False. |
| Public method | [ShowComponentSearchBox(Point)](M_Grasshopper_GUI_Canvas_GH_Canvas_ShowComponentSearchBox_1.htm) | Display the component Search dialog at the given coordinate. The dialog cannot be shown if ModifiersEnabled=False. |
| Public method | [ShowMRUPanels](M_Grasshopper_GUI_Canvas_GH_Canvas_ShowMRUPanels.htm) | Show any hidden MRU panels by sliding them back into view. |
| Public method | [ShowNavigationPane](M_Grasshopper_GUI_Canvas_GH_Canvas_ShowNavigationPane.htm) | Displays the quick-navigation popup pane at the cursor. |
| Public method | [ShowSearchDialog](M_Grasshopper_GUI_Canvas_GH_Canvas_ShowSearchDialog.htm) | Display the Find dialog. If a Find dialog is already active for this canvas, nothing will happen. |
| Public method | [StartAutoPan](M_Grasshopper_GUI_Canvas_GH_Canvas_StartAutoPan.htm) | Start the auto-panning timer. |
| Public method | [StopAutoPan](M_Grasshopper_GUI_Canvas_GH_Canvas_StopAutoPan.htm) | Stop the auto-panning timer. |
| Public method | [UpdateDocumentPreview](M_Grasshopper_GUI_Canvas_GH_Canvas_UpdateDocumentPreview.htm) | Call this method to update the preview thumbnail for the currently loaded document. If no document is currently loaded, nothing will happen. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [CanvasPaintBackground](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPaintBackground.htm) | Raised after the background has been drawn. |
| Public event | [CanvasPaintBegin](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPaintBegin.htm) | Raised before a new paint operation starts. This event is always raised, even if the Canvas isn't visible. |
| Public event | [CanvasPaintEnd](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPaintEnd.htm) | Raised after a paint operation completes. This event is always raised, even if the Canvas isn't visible. |
| Public event | [CanvasPostPaintGroups](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPostPaintGroups.htm) | Raised after group drawing completes. |
| Public event | [CanvasPostPaintObjects](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPostPaintObjects.htm) | Raised after object drawing completes. |
| Public event | [CanvasPostPaintOverlay](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPostPaintOverlay.htm) | Raised after object overlay drawing completes. |
| Public event | [CanvasPostPaintWidgets](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPostPaintWidgets.htm) | Raised after widgets are drawn. This is the final event in the Drawing pipeline. |
| Public event | [CanvasPostPaintWires](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPostPaintWires.htm) | Raised after wire drawing completes. |
| Public event | [CanvasPrePaintGroups](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPrePaintGroups.htm) | Raised before group drawing starts. |
| Public event | [CanvasPrePaintObjects](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPrePaintObjects.htm) | Raised before object drawing starts. |
| Public event | [CanvasPrePaintOverlay](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPrePaintOverlay.htm) | Raised before object overlay drawing starts. |
| Public event | [CanvasPrePaintWidgets](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPrePaintWidgets.htm) | Raised before Widgets are drawn. |
| Public event | [CanvasPrePaintWires](E_Grasshopper_GUI_Canvas_GH_Canvas_CanvasPrePaintWires.htm) | Raised before wire drawing starts. |
| Public event | [Document\_ModifiedChanged](E_Grasshopper_GUI_Canvas_GH_Canvas_Document_ModifiedChanged.htm) |  |
| Public event | [Document\_ObjectsAdded](E_Grasshopper_GUI_Canvas_GH_Canvas_Document_ObjectsAdded.htm) |  |
| Public event | [Document\_ObjectsDeleted](E_Grasshopper_GUI_Canvas_GH_Canvas_Document_ObjectsDeleted.htm) |  |
| Public event | [Document\_SettingsChanged](E_Grasshopper_GUI_Canvas_GH_Canvas_Document_SettingsChanged.htm) |  |
| Public event | [DocumentChanged](E_Grasshopper_GUI_Canvas_GH_Canvas_DocumentChanged.htm) | This event is raised whenever a different document is loaded into this canvas. |
| Public event | [DocumentObjectMouseDown](E_Grasshopper_GUI_Canvas_GH_Canvas_DocumentObjectMouseDown.htm) | This event is raised whenever the left mouse button is pressed while over a Document object. |
| Public event | [ModifiersChanged](E_Grasshopper_GUI_Canvas_GH_Canvas_ModifiersChanged.htm) | This event is raised whenever the ModifiersEnabled property changes. |
| Public eventStatic member | [NavigationSettingsChanged](E_Grasshopper_GUI_Canvas_GH_Canvas_NavigationSettingsChanged.htm) | Raised whenever any of the shared navigation properties changed. |
| Public event | [ViewportChanged](E_Grasshopper_GUI_Canvas_GH_Canvas_ViewportChanged.htm) | This event is raised whenever the viewport properties are modified, for example when the pan or zoom values are affected. |
| Public eventStatic member | [WidgetListCreated](E_Grasshopper_GUI_Canvas_GH_Canvas_WidgetListCreated.htm) | This event is raised once for every GH\_Canvas object that is created anew. The event is Shared (static) because it is raised inside the constructor of a GH\_Canvas object and therefor cannot be registered on an instance. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public fieldStatic member | [ScheduleInactive](F_Grasshopper_GUI_Canvas_GH_Canvas_ScheduleInactive.htm) | Defines the delay used to indicate the absence of a schedule. |
| Public fieldStatic member | [ThumbnailHeight](F_Grasshopper_GUI_Canvas_GH_Canvas_ThumbnailHeight.htm) |  |
| Public fieldStatic member | [ThumbnailWidth](F_Grasshopper_GUI_Canvas_GH_Canvas_ThumbnailWidth.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Extension Methods

|  | Name | Description |
| --- | --- | --- |
| Public Extension Method | [ToEto](M_Grasshopper_EtoExtensions_ToEto_7.htm) | (Defined by [EtoExtensions](T_Grasshopper_EtoExtensions.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)