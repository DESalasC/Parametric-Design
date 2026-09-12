# T_Grasshopper_Instances

﻿ Instances Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Instances Class](../html/T_Grasshopper_Instances.htm "Instances Class")

[Instances Properties](../html/Properties_T_Grasshopper_Instances.htm "Instances Properties")

[Instances Methods](../html/Methods_T_Grasshopper_Instances.htm "Instances Methods")

[Instances Events](../html/Events_T_Grasshopper_Instances.htm "Instances Events")

[Instances Fields](../html/Fields_T_Grasshopper_Instances.htm "Instances Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Instances Class |

Provides access to a bunch of global instances and variables.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST73D5BAF\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  GrasshopperAddLanguageSpecificTextSet("LST73D5BAF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Instances

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class Instances
```

```
Public NotInheritable Class Instances
```

AddLanguageTabSet("ID1EBCA");

The Instances type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public propertyStatic member | [ActiveCanvas](P_Grasshopper_Instances_ActiveCanvas.htm) | Gets the currently active Grasshopper canvas (if any) |
| Public propertyStatic member | [ActiveDocument](P_Grasshopper_Instances_ActiveDocument.htm) |  |
| Public propertyStatic member | [ActiveRhinoDoc](P_Grasshopper_Instances_ActiveRhinoDoc.htm) |  |
| Public propertyStatic member | [AutoHideBanner](P_Grasshopper_Instances_AutoHideBanner.htm) | Gets or sets a value indicating whether the banner ought to be hidden automatically when loading completes. |
| Public propertyStatic member | [AutoShowBanner](P_Grasshopper_Instances_AutoShowBanner.htm) | Gets or sets a value indicating whether or not the banner will be displayed during the ComponentServer Loading process. |
| Public propertyStatic member | [ComponentServer](P_Grasshopper_Instances_ComponentServer.htm) | Gets the ComponentServer instance cached by the Instance Server. The ComponentServer will be instantiated the first time this property accessed. This is a rather involved process during which the Grasshopper Banner will be displayed. |
| Public propertyStatic member | [CursorServer](P_Grasshopper_Instances_CursorServer.htm) | Gets the CursorServer instance cached by the Instance Server. The CursorServer will be instantiated the first time this property is accessed. |
| Public propertyStatic member | [DocumentAssociationServer](P_Grasshopper_Instances_DocumentAssociationServer.htm) | Gets the Document Association Server instance cached by the Instance Server. The Document Association Server will be instantiated the first time this property accessed. |
| Public propertyStatic member | [DocumentEditor](P_Grasshopper_Instances_DocumentEditor.htm) | Gets the DocumentEditor of Grasshopper. |
| Public propertyStatic member | [DocumentServer](P_Grasshopper_Instances_DocumentServer.htm) | Gets the DocumentServer instance cached by the Instance Server. The DocumentServer will be instantiated the first time this property accessed. |
| Public propertyStatic member | [EtoDocumentEditor](P_Grasshopper_Instances_EtoDocumentEditor.htm) |  |
| Public propertyStatic member | [GrasshopperPluginId](P_Grasshopper_Instances_GrasshopperPluginId.htm) | Gets the ID of the Grasshopper Plugin. |
| Public propertyStatic member | [IsComponentServer](P_Grasshopper_Instances_IsComponentServer.htm) | Gets whether the Component server has been set. |
| Public propertyStatic member | [IsCursorServer](P_Grasshopper_Instances_IsCursorServer.htm) | Gets whether the Cursor server has been set. |
| Public propertyStatic member | [IsDocumentAssociationServer](P_Grasshopper_Instances_IsDocumentAssociationServer.htm) | Gets whether the Document Association server has been set. |
| Public propertyStatic member | [IsDocumentEditor](P_Grasshopper_Instances_IsDocumentEditor.htm) | Gets whether the Document Editor has been set. |
| Public propertyStatic member | [IsDocumentEditorOnTopOfViewports](P_Grasshopper_Instances_IsDocumentEditorOnTopOfViewports.htm) | Gets whether the Grasshopper document editor (or any of its child forms) is obscuring a significant part of the Rhino viewports. |
| Public propertyStatic member | [IsDocumentServer](P_Grasshopper_Instances_IsDocumentServer.htm) | Gets whether the Document server has been set. |
| Public propertyStatic member | [IsMarkovChain](P_Grasshopper_Instances_IsMarkovChain.htm) | Gets a value indicating whether or not the MarkovChain has already been initialized. |
| Public propertyStatic member | [IsMruServer](P_Grasshopper_Instances_IsMruServer.htm) | Gets a value indicating whether or not the MRU server has been initialized. |
| Public propertyStatic member | [IsRemotePanelVisible](P_Grasshopper_Instances_IsRemotePanelVisible.htm) | Gets whether the Remote Control Panel is currently visible. |
| Public propertyStatic member | [MarkovChain](P_Grasshopper_Instances_MarkovChain.htm) | Gets the MarkovChain instance cached by the Instance Server. The Markov chain will be instantiated if it hasn't been already. |
| Public propertyStatic member | [MruServer](P_Grasshopper_Instances_MruServer.htm) | Gets the MRU\_Server instance cached by the Instance Server. The MRU\_Server will be instantiated the first time this property accessed. |
| Public propertyStatic member | [RcpPanel](P_Grasshopper_Instances_RcpPanel.htm) | Gets the app-domain wide RCP panel instance. If it doesn't exist yet it will be created. |
| Public propertyStatic member | [RunningHeadless](P_Grasshopper_Instances_RunningHeadless.htm) |  |
| Public propertyStatic member | [Settings](P_Grasshopper_Instances_Settings.htm) | Represents the default settings database. Feel free to add your own settings to this database. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [DocumentEditorFadeIn](M_Grasshopper_Instances_DocumentEditorFadeIn.htm) | Calls the FadeIn() method on the DocumentEditor if it exists. |
| Public methodStatic member | [DocumentEditorFadeOut](M_Grasshopper_Instances_DocumentEditorFadeOut.htm) | Calls the FadeOut() method on the DocumentEditor if it exists. |
| Public methodStatic member | [EnforceInvariantCulture](M_Grasshopper_Instances_EnforceInvariantCulture.htm) | If the Setting "EnforceInvariantCulture" is set to False, this function does nothing |
| Public methodStatic member | [HideRemotePanel](M_Grasshopper_Instances_HideRemotePanel.htm) | Hides the remote control panel. |
| Public methodStatic member | [Interop](M_Grasshopper_Instances_Interop.htm) | Gets the Grasshopper 1.0 interop object, i.e. an instance of GrasshopperPlugin.GrasshopperInterop as exposed via the GetInteropObject() method on the Grasshopper 1.0 plugin object. |
| Public methodStatic member | [InvalidateCanvas](M_Grasshopper_Instances_InvalidateCanvas.htm) | Invalidates the currently active Grasshopper Canvas, causing a redraw sometime in the foreseeable future. |
| Public methodStatic member | [RedrawAll](M_Grasshopper_Instances_RedrawAll.htm) | Forces a redraw of both the active canvas and the Rhino viewports on the active document. |
| Public methodStatic member | [RedrawCanvas](M_Grasshopper_Instances_RedrawCanvas.htm) | Forces a redraw of the currently active Grasshopper Canvas. |
| Public methodStatic member | [ReloadMemoryAssemblies](M_Grasshopper_Instances_ReloadMemoryAssemblies.htm) | Unload and attempt to reload all plugin assemblies that were loaded via the COFF pipeline. |
| Public methodStatic member | [ShowRemotePanel](M_Grasshopper_Instances_ShowRemotePanel.htm) | Shows the remote control panel. |
| Public methodStatic member | [UnloadAllObjects](M_Grasshopper_Instances_UnloadAllObjects.htm) | Clears and unloads all cached objects. This function is called by the \_GrasshopperUnloadPlugin command. Please don't use it. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public eventStatic member | [CanvasCreated](E_Grasshopper_Instances_CanvasCreated.htm) | Raised when the main canvas is created. |
| Public eventStatic member | [CanvasDestroyed](E_Grasshopper_Instances_CanvasDestroyed.htm) | Raised when the main canvas is destroyed. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public fieldStatic member | [LoadOneByOne](F_Grasshopper_Instances_LoadOneByOne.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)