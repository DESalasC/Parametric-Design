# M_Grasshopper_Kernel_GH_ComponentParamServer_Sync

﻿ GH\_ComponentParamServer.Sync Method (GH\_ComponentParamServer.IGH\_SyncObject)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentParamServer Class](../html/T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Class")

[GH\_ComponentParamServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Methods")

[Sync Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_Sync.htm "Sync Method ")

[Sync Method (GH\_ComponentParamServer.IGH\_SyncObject)](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_Sync.htm "Sync Method (GH_ComponentParamServer.IGH_SyncObject)")

[Sync Method (Object)](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_Sync_2.htm "Sync Method (Object)")

[Sync Method (GH\_ComponentParamServer.IGH\_SyncObject, Int32)](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_Sync_1.htm "Sync Method (GH_ComponentParamServer.IGH_SyncObject, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentParamServerAddLanguageSpecificTextSet("LST534F9BD3\_0?cpp=::|nu=.");Sync Method (GH\_ComponentParamServerAddLanguageSpecificTextSet("LST534F9BD3\_1?cpp=::|nu=.");IGH\_SyncObject) |

Sync changes from a prerecorded state.
All param references in the sync object which are no longer
present in the current server will be properly deleted.
The sync object will be reset in the process, so you can only call this function
with a specific Sync object once.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void Sync(
	GH_ComponentParamServerAddLanguageSpecificTextSet("LST534F9BD3_2?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH_SyncObject sync_data
)
```

```
Public Sub Sync ( 
	sync_data As GH_ComponentParamServerAddLanguageSpecificTextSet("LST534F9BD3_3?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH_SyncObject
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

sync\_data
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST534F9BD3\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ComponentParamServerAddLanguageSpecificTextSet("LST534F9BD3\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_SyncObject](T_Grasshopper_Kernel_GH_ComponentParamServer_IGH_SyncObject.htm)  
    Sync object. Should be obtained by calling EmitSyncObject()

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentParamServer Class](T_Grasshopper_Kernel_GH_ComponentParamServer.htm)

[Sync Overload](Overload_Grasshopper_Kernel_GH_ComponentParamServer_Sync.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)