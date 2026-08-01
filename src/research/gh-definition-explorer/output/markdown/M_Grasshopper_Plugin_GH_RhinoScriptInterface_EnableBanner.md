# M_Grasshopper_Plugin_GH_RhinoScriptInterface_EnableBanner

﻿ GH\_RhinoScriptInterface.EnableBanner Method  

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Plugin](../html/N_Grasshopper_Plugin.htm "Grasshopper.Plugin")

[GH\_RhinoScriptInterface Class](../html/T_Grasshopper_Plugin_GH_RhinoScriptInterface.htm "GH_RhinoScriptInterface Class")

[GH\_RhinoScriptInterface Methods](../html/Methods_T_Grasshopper_Plugin_GH_RhinoScriptInterface.htm "GH_RhinoScriptInterface Methods")

[AssignDataToParameter Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_AssignDataToParameter.htm "AssignDataToParameter Method ")

[BakeDataInObject Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_BakeDataInObject.htm "BakeDataInObject Method ")

[CloseAllDocuments Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_CloseAllDocuments.htm "CloseAllDocuments Method ")

[CloseDocument Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_CloseDocument.htm "CloseDocument Method ")

[DisableBanner Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_DisableBanner.htm "DisableBanner Method ")

[DisableSolver Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_DisableSolver.htm "DisableSolver Method ")

[EnableBanner Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_EnableBanner.htm "EnableBanner Method ")

[EnableSolver Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_EnableSolver.htm "EnableSolver Method ")

[HideEditor Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_HideEditor.htm "HideEditor Method ")

[IsEditorLoaded Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_IsEditorLoaded.htm "IsEditorLoaded Method ")

[IsEditorVisible Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_IsEditorVisible.htm "IsEditorVisible Method ")

[IsSolverEnabled Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_IsSolverEnabled.htm "IsSolverEnabled Method ")

[LoadEditor Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_LoadEditor.htm "LoadEditor Method ")

[LoadedPluginGuids Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_LoadedPluginGuids.htm "LoadedPluginGuids Method ")

[LoadedPluginNames Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_LoadedPluginNames.htm "LoadedPluginNames Method ")

[OpenDocument Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_OpenDocument.htm "OpenDocument Method ")

[RunAsCommand Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_RunAsCommand.htm "RunAsCommand Method ")

[RunHeadless Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_RunHeadless.htm "RunHeadless Method ")

[RunInCommandContext Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_RunInCommandContext.htm "RunInCommandContext Method ")

[RunSolver Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_RunSolver.htm "RunSolver Method ")

[SaveDocument Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_SaveDocument.htm "SaveDocument Method ")

[SaveDocumentAs Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_SaveDocumentAs.htm "SaveDocumentAs Method ")

[SetSliderRangeAndValue Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_SetSliderRangeAndValue.htm "SetSliderRangeAndValue Method ")

[SetSliderValue Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_SetSliderValue.htm "SetSliderValue Method ")

[ShowEditor Method](../html/M_Grasshopper_Plugin_GH_RhinoScriptInterface_ShowEditor.htm "ShowEditor Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_RhinoScriptInterfaceAddLanguageSpecificTextSet("LST93A3C4B9\_0?cpp=::|nu=.");EnableBanner Method |

Enables the display of the Grasshopper banner during Component loading.
The banner is typically only shown once during a Grasshopper session,
namely when the Editor is first loaded.

**Namespace:**
 [Grasshopper.Plugin](N_Grasshopper_Plugin.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void EnableBanner()
```

```
Public Sub EnableBanner
```

AddLanguageTabSet("ID0EBCA");

![](../icons/SectionExpanded.png)Examples

VBScript

[Copy](# "Copy")

```
Call GrasshopperExampleScript()
Sub GrasshopperExampleScript()
  Dim GH 
  Set GH = Rhino.GetPlugInObject("Grasshopper")
  Call GH.EnableBanner()
  Call GH.ShowEditor()
  Set GH = Nothing
End Sub
```

AddLanguageTabSet("ID0EAAABA");

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_RhinoScriptInterface Class](T_Grasshopper_Plugin_GH_RhinoScriptInterface.htm)

[Grasshopper.Plugin Namespace](N_Grasshopper_Plugin.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)