# T_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs

﻿ GH\_CanvasDocumentChangedEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_CanvasDocumentChangedEventArgs Class](../html/T_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs.htm "GH_CanvasDocumentChangedEventArgs Class")

[GH\_CanvasDocumentChangedEventArgs Constructor](../html/M_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs__ctor.htm "GH_CanvasDocumentChangedEventArgs Constructor ")

[GH\_CanvasDocumentChangedEventArgs Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs.htm "GH_CanvasDocumentChangedEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CanvasDocumentChangedEventArgs Class |

These arguments are used in the DocumentChanged event on GH\_Canvas.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTC4522C1A\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTC4522C1A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LSTC4522C1A\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CanvasDocumentChangedEventArgs

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_CanvasDocumentChangedEventArgs : EventArgs
```

```
Public Class GH_CanvasDocumentChangedEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_CanvasDocumentChangedEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_CanvasDocumentChangedEventArgs](M_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs__ctor.htm) | Initializes a new instance of the GH\_CanvasDocumentChangedEventArgs class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [NewDocument](P_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs_NewDocument.htm) | Gets the document which has just been loaded into the canvas. |
| Public property | [OldDocument](P_Grasshopper_GUI_Canvas_GH_CanvasDocumentChangedEventArgs_OldDocument.htm) | Gets the document which was previously loaded into the canvas. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)