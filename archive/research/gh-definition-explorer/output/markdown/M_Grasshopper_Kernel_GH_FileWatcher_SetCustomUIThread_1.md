# M_Grasshopper_Kernel_GH_FileWatcher_SetCustomUIThread_1

﻿ GH\_FileWatcher.SetCustomUIThread Method (Form)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_FileWatcher Class](../html/T_Grasshopper_Kernel_GH_FileWatcher.htm "GH_FileWatcher Class")

[GH\_FileWatcher Methods](../html/Methods_T_Grasshopper_Kernel_GH_FileWatcher.htm "GH_FileWatcher Methods")

[SetCustomUIThread Method](../html/Overload_Grasshopper_Kernel_GH_FileWatcher_SetCustomUIThread.htm "SetCustomUIThread Method ")

[SetCustomUIThread Method (Control)](../html/M_Grasshopper_Kernel_GH_FileWatcher_SetCustomUIThread.htm "SetCustomUIThread Method (Control)")

[SetCustomUIThread Method (Form)](../html/M_Grasshopper_Kernel_GH_FileWatcher_SetCustomUIThread_1.htm "SetCustomUIThread Method (Form)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FileWatcherAddLanguageSpecificTextSet("LST33EB3A6F\_0?cpp=::|nu=.");SetCustomUIThread Method (Form) |

If you want to override the default Invoke behaviour, you must set
InvokeOnDefaultThread to False and supply either a custom Control or a Form.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void SetCustomUIThread(
	Form target
)
```

```
Public Sub SetCustomUIThread ( 
	target As Form
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

target
:   Type: [System.Windows.FormsAddLanguageSpecificTextSet("LST33EB3A6F\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Form](https://docs.microsoft.com/dotnet/api/system.windows.forms.form)  
    GUI target object which will be used for Invoking File System Events.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_FileWatcher Class](T_Grasshopper_Kernel_GH_FileWatcher.htm)

[SetCustomUIThread Overload](Overload_Grasshopper_Kernel_GH_FileWatcher_SetCustomUIThread.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)