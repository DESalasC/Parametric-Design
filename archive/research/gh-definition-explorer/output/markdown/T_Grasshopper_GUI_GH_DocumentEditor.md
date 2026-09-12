# T_Grasshopper_GUI_GH_DocumentEditor

﻿ GH\_DocumentEditor Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_DocumentEditor Class](../html/T_Grasshopper_GUI_GH_DocumentEditor.htm "GH_DocumentEditor Class")

[GH\_DocumentEditor Constructor](../html/M_Grasshopper_GUI_GH_DocumentEditor__ctor.htm "GH_DocumentEditor Constructor ")

[GH\_DocumentEditor Properties](../html/Properties_T_Grasshopper_GUI_GH_DocumentEditor.htm "GH_DocumentEditor Properties")

[GH\_DocumentEditor Methods](../html/Methods_T_Grasshopper_GUI_GH_DocumentEditor.htm "GH_DocumentEditor Methods")

[GH\_DocumentEditor Events](../html/Events_T_Grasshopper_GUI_GH_DocumentEditor.htm "GH_DocumentEditor Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentEditor Class |

The Grasshopper main window.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST383023EE\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST383023EE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");MarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
    [System.ComponentModelAddLanguageSpecificTextSet("LST383023EE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Component](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
      [System.Windows.FormsAddLanguageSpecificTextSet("LST383023EE\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Control](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
        [System.Windows.FormsAddLanguageSpecificTextSet("LST383023EE\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
          [System.Windows.FormsAddLanguageSpecificTextSet("LST383023EE\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ContainerControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol)  
            [System.Windows.FormsAddLanguageSpecificTextSet("LST383023EE\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Form](https://docs.microsoft.com/dotnet/api/system.windows.forms.form)  
              Grasshopper.GUIAddLanguageSpecificTextSet("LST383023EE\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocumentEditor

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DocumentEditor : Form
```

```
Public Class GH_DocumentEditor
	Inherits Form
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocumentEditor type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DocumentEditor](M_Grasshopper_GUI_GH_DocumentEditor__ctor.htm) | Initializes a new instance of the GH\_DocumentEditor class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Collapsed](P_Grasshopper_GUI_GH_DocumentEditor_Collapsed.htm) | Gets a value indicating whether or not the form is currently collapsed. |
| Protected property | [CreateParams](P_Grasshopper_GUI_GH_DocumentEditor_CreateParams.htm) | (Overrides [FormAddLanguageSpecificTextSet("LST383023EE\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");CreateParams](https://docs.microsoft.com/dotnet/api/system.windows.forms.form.createparams#system-windows-forms-form-createparams).) |
| Public property | [FormShepard](P_Grasshopper_GUI_GH_DocumentEditor_FormShepard.htm) | Gets the form shepard for this window. Register your modeless dialogs with this shepard if you want to be popular. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [ClearStatusBar](M_Grasshopper_GUI_GH_DocumentEditor_ClearStatusBar.htm) | Clear the Grasshopper status-bar. |
| Public method | [CloseForReal](M_Grasshopper_GUI_GH_DocumentEditor_CloseForReal.htm) | Really, *really* close the window. |
| Public method | [CollapseForm](M_Grasshopper_GUI_GH_DocumentEditor_CollapseForm.htm) | Collapses the form into the title bar area. |
| Public method | [DisableUI](M_Grasshopper_GUI_GH_DocumentEditor_DisableUI.htm) | Disable all modifier UI. |
| Protected method | [Dispose](M_Grasshopper_GUI_GH_DocumentEditor_Dispose.htm) | Releases the unmanaged resources used by the GH\_DocumentEditor and optionally releases the managed resources (Overrides [FormAddLanguageSpecificTextSet("LST383023EE\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");Dispose(Boolean)](https://docs.microsoft.com/dotnet/api/system.windows.forms.form.dispose#system-windows-forms-form-dispose(system-boolean)).) |
| Public method | [EnableUI](M_Grasshopper_GUI_GH_DocumentEditor_EnableUI.htm) | Enable all modifier UI. |
| Public method | [ExpandForm](M_Grasshopper_GUI_GH_DocumentEditor_ExpandForm.htm) | Expands the form if it is currenly collapsed. |
| Public method | [FadeIn](M_Grasshopper_GUI_GH_DocumentEditor_FadeIn.htm) | Call this method if the prompt switches back to Grasshopper. |
| Public method | [FadeOut](M_Grasshopper_GUI_GH_DocumentEditor_FadeOut.htm) | Call this method if the prompt switches to Rhino. |
| Public method | [FixCanvasToolbarState](M_Grasshopper_GUI_GH_DocumentEditor_FixCanvasToolbarState.htm) | Enabled/Disables the appropriate buttons depending on whether there is a document loaded on the canvas. |
| Public method | [ScriptAccess\_CloseAllDocuments](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_CloseAllDocuments.htm) | Closes all documents in the Document Queue. |
| Public method | [ScriptAccess\_CloseDocument](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_CloseDocument.htm) | Closes the currently active document and loads the next available document into the canvas. Changes will not be saved. |
| Public method | [ScriptAccess\_IsDocument](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_IsDocument.htm) | Returns true if there is an active document. |
| Public method | [ScriptAccess\_IsDocumentModified](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_IsDocumentModified.htm) | Gets the modified flag of the currently loaded document. |
| Public method | [ScriptAccess\_NewDocument](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_NewDocument.htm) | Creates a new document and loads it into the Canvas. |
| Public method | [ScriptAccess\_OpenDocumentAddLanguageSpecificTextSet("LST383023EE\_10?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_OpenDocument.htm) | Displays a command line interface for File Open... then loads that file into the Canvas. |
| Public method | [ScriptAccess\_OpenDocument(String)](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_OpenDocument_1.htm) | Loads a specific file off the hard disk into the Canvas. |
| Public method | [ScriptAccess\_SaveDocument](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_SaveDocument.htm) | Saves the document currently loaded in the Canvas. If the document hasn't been saved before then a Save... dialog box will be shown. |
| Public method | [ScriptAccess\_SaveDocumentAsAddLanguageSpecificTextSet("LST383023EE\_11?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_SaveDocumentAs.htm) | Saves the currently active document to disk. |
| Public method | [ScriptAccess\_SaveDocumentAs(String)](M_Grasshopper_GUI_GH_DocumentEditor_ScriptAccess_SaveDocumentAs_1.htm) | Saves the currently active document to disk. |
| Public method | [SetStatusBarEvent](M_Grasshopper_GUI_GH_DocumentEditor_SetStatusBarEvent.htm) | Set a new message on the Grasshopper status bar. |
| Public method | [ToggleForm](M_Grasshopper_GUI_GH_DocumentEditor_ToggleForm.htm) | Collapses the form if it's currently expanded or expands the form if it's currently collapsed. |
| Protected method | [WndProc](M_Grasshopper_GUI_GH_DocumentEditor_WndProc.htm) | WndProc is overridden in order to allow for title-bar double-click (un)folding. (Overrides [FormAddLanguageSpecificTextSet("LST383023EE\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");WndProc(MessageAddLanguageSpecificTextSet("LST383023EE\_13?cpp=%");)](https://docs.microsoft.com/dotnet/api/system.windows.forms.form.wndproc#system-windows-forms-form-wndproc(system-windows-forms-message@)).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public eventStatic member | [AggregateShortcutMenuItems](E_Grasshopper_GUI_GH_DocumentEditor_AggregateShortcutMenuItems.htm) | This event is raised whenever a GH\_DocumentEditor collects all shortcuttable menu items. If you added items to the menu and you want to be able to have custom shortcuts on these items, you must handle this event and insert your own items. |
| Public event | [EditorFoldStateChanged](E_Grasshopper_GUI_GH_DocumentEditor_EditorFoldStateChanged.htm) | This event is raised whenever the main windows folds or unfolds. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Extension Methods

|  | Name | Description |
| --- | --- | --- |
| Public Extension Method | [ToEtoAddLanguageSpecificTextSet("LST383023EE\_14?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_EtoExtensions_ToEto_8.htm) | Overloaded. (Defined by [EtoExtensions](T_Grasshopper_EtoExtensions.htm).) |
| Public Extension Method | [ToEtoAddLanguageSpecificTextSet("LST383023EE\_15?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_EtoExtensions_ToEto_7.htm) | Overloaded. (Defined by [EtoExtensions](T_Grasshopper_EtoExtensions.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)