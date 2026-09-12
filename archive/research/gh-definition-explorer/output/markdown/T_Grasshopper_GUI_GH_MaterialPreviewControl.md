# T_Grasshopper_GUI_GH_MaterialPreviewControl

﻿ GH\_MaterialPreviewControl Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_MaterialPreviewControl Class](../html/T_Grasshopper_GUI_GH_MaterialPreviewControl.htm "GH_MaterialPreviewControl Class")

[GH\_MaterialPreviewControl Constructor](../html/M_Grasshopper_GUI_GH_MaterialPreviewControl__ctor.htm "GH_MaterialPreviewControl Constructor ")

[GH\_MaterialPreviewControl Properties](../html/Properties_T_Grasshopper_GUI_GH_MaterialPreviewControl.htm "GH_MaterialPreviewControl Properties")

[GH\_MaterialPreviewControl Methods](../html/Methods_T_Grasshopper_GUI_GH_MaterialPreviewControl.htm "GH_MaterialPreviewControl Methods")

[GH\_MaterialPreviewControl Events](../html/Events_T_Grasshopper_GUI_GH_MaterialPreviewControl.htm "GH_MaterialPreviewControl Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MaterialPreviewControl Class |

Offers a frontend for Grasshopper Material previews.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST2E4724AF\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST2E4724AF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");MarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
    [System.ComponentModelAddLanguageSpecificTextSet("LST2E4724AF\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Component](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
      [System.Windows.FormsAddLanguageSpecificTextSet("LST2E4724AF\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Control](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)  
        [System.Windows.FormsAddLanguageSpecificTextSet("LST2E4724AF\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ScrollableControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.scrollablecontrol)  
          [System.Windows.FormsAddLanguageSpecificTextSet("LST2E4724AF\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ContainerControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol)  
            [System.Windows.FormsAddLanguageSpecificTextSet("LST2E4724AF\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");UserControl](https://docs.microsoft.com/dotnet/api/system.windows.forms.usercontrol)  
              Grasshopper.GUIAddLanguageSpecificTextSet("LST2E4724AF\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MaterialPreviewControl

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_MaterialPreviewControl : UserControl
```

```
Public Class GH_MaterialPreviewControl
	Inherits UserControl
```

AddLanguageTabSet("ID1EBCA");

The GH\_MaterialPreviewControl type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_MaterialPreviewControl](M_Grasshopper_GUI_GH_MaterialPreviewControl__ctor.htm) | Initializes a new instance of the GH\_MaterialPreviewControl class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Colour](P_Grasshopper_GUI_GH_MaterialPreviewControl_Colour.htm) | Gets or sets the colour of this preview. |
| Public property | [Selected](P_Grasshopper_GUI_GH_MaterialPreviewControl_Selected.htm) | Gets or sets the Selected state of this preview. Selected previews have thick borders drawn around them. |
| Public property | [SelectOnClick](P_Grasshopper_GUI_GH_MaterialPreviewControl_SelectOnClick.htm) | Gets or sets whether this control can be selected. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [Dispose](M_Grasshopper_GUI_GH_MaterialPreviewControl_Dispose.htm) | Releases the unmanaged resources used by the GH\_MaterialPreviewControl and optionally releases the managed resources (Overrides [ContainerControlAddLanguageSpecificTextSet("LST2E4724AF\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");Dispose(Boolean)](https://docs.microsoft.com/dotnet/api/system.windows.forms.containercontrol.dispose#system-windows-forms-containercontrol-dispose(system-boolean)).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [ColourChanged](E_Grasshopper_GUI_GH_MaterialPreviewControl_ColourChanged.htm) |  |
| Public event | [MaterialImagePostPaint](E_Grasshopper_GUI_GH_MaterialPreviewControl_MaterialImagePostPaint.htm) |  |
| Public event | [SelectedChanged](E_Grasshopper_GUI_GH_MaterialPreviewControl_SelectedChanged.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Extension Methods

|  | Name | Description |
| --- | --- | --- |
| Public Extension Method | [ToEto](M_Grasshopper_EtoExtensions_ToEto_7.htm) | (Defined by [EtoExtensions](T_Grasshopper_EtoExtensions.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)