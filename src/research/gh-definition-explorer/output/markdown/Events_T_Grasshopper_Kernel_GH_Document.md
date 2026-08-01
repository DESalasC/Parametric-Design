# Events_T_Grasshopper_Kernel_GH_Document

﻿ GH\_Document Events

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Events](../html/Events_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Events")

[ContextChanged Event](../html/E_Grasshopper_Kernel_GH_Document_ContextChanged.htm "ContextChanged Event")

[DefaultPreviewColourChanged Event](../html/E_Grasshopper_Kernel_GH_Document_DefaultPreviewColourChanged.htm "DefaultPreviewColourChanged Event")

[DefaultSelectedPreviewColourChanged Event](../html/E_Grasshopper_Kernel_GH_Document_DefaultSelectedPreviewColourChanged.htm "DefaultSelectedPreviewColourChanged Event")

[EnabledChanged Event](../html/E_Grasshopper_Kernel_GH_Document_EnabledChanged.htm "EnabledChanged Event")

[EnableSolutionsChanged Event](../html/E_Grasshopper_Kernel_GH_Document_EnableSolutionsChanged.htm "EnableSolutionsChanged Event")

[FilePathChanged Event](../html/E_Grasshopper_Kernel_GH_Document_FilePathChanged.htm "FilePathChanged Event")

[ModifiedChanged Event](../html/E_Grasshopper_Kernel_GH_Document_ModifiedChanged.htm "ModifiedChanged Event")

[ObjectsAdded Event](../html/E_Grasshopper_Kernel_GH_Document_ObjectsAdded.htm "ObjectsAdded Event")

[ObjectsDeleted Event](../html/E_Grasshopper_Kernel_GH_Document_ObjectsDeleted.htm "ObjectsDeleted Event")

[SettingsChanged Event](../html/E_Grasshopper_Kernel_GH_Document_SettingsChanged.htm "SettingsChanged Event")

[SolutionEnd Event](../html/E_Grasshopper_Kernel_GH_Document_SolutionEnd.htm "SolutionEnd Event")

[SolutionStart Event](../html/E_Grasshopper_Kernel_GH_Document_SolutionStart.htm "SolutionStart Event")

[UndoStateChanged Event](../html/E_Grasshopper_Kernel_GH_Document_UndoStateChanged.htm "UndoStateChanged Event")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Document Events |

The [GH\_Document](T_Grasshopper_Kernel_GH_Document.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [ContextChanged](E_Grasshopper_Kernel_GH_Document_ContextChanged.htm) | The context for this document was changed. |
| Public eventStatic member | [DefaultPreviewColourChanged](E_Grasshopper_Kernel_GH_Document_DefaultPreviewColourChanged.htm) | This even is raised whenever the global default for Normal preview colour is changed. |
| Public eventStatic member | [DefaultSelectedPreviewColourChanged](E_Grasshopper_Kernel_GH_Document_DefaultSelectedPreviewColourChanged.htm) | This even is raised whenever the global default for Selected preview colour is changed. |
| Public event | [EnabledChanged](E_Grasshopper_Kernel_GH_Document_EnabledChanged.htm) | The Enabled state was changed on this document. |
| Public eventStatic member | [EnableSolutionsChanged](E_Grasshopper_Kernel_GH_Document_EnableSolutionsChanged.htm) | Raised whenever the Shared EnabledSolutions property is changed. |
| Public event | [FilePathChanged](E_Grasshopper_Kernel_GH_Document_FilePathChanged.htm) | Raised whenever the FilePath of the document is modified. |
| Public event | [ModifiedChanged](E_Grasshopper_Kernel_GH_Document_ModifiedChanged.htm) | The modified flag on the document was changed. |
| Public event | [ObjectsAdded](E_Grasshopper_Kernel_GH_Document_ObjectsAdded.htm) | Raised after a collection of objects was added to the document. |
| Public event | [ObjectsDeleted](E_Grasshopper_Kernel_GH_Document_ObjectsDeleted.htm) | Raised after a collection of objects was removed from the document. At this point, the objects still exist, but they no longer belong to this document. |
| Public event | [SettingsChanged](E_Grasshopper_Kernel_GH_Document_SettingsChanged.htm) | Some settings of the document were changed. |
| Public event | [SolutionEnd](E_Grasshopper_Kernel_GH_Document_SolutionEnd.htm) | This event is raised whenever a new solution request has been handled. Even if the document is locked. |
| Public event | [SolutionStart](E_Grasshopper_Kernel_GH_Document_SolutionStart.htm) | This event is raised whenever a new solution is requested. Even if the document is locked. |
| Public event | [UndoStateChanged](E_Grasshopper_Kernel_GH_Document_UndoStateChanged.htm) | Raised whenever there is a change to the document undo/redo stack. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)