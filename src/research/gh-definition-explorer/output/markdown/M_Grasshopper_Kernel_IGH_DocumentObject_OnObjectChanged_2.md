# M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_2

﻿ IGH\_DocumentObject.OnObjectChanged Method (GH\_ObjectEventType, Object)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DocumentObject Interface](../html/T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Interface")

[IGH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Methods")

[OnObjectChanged Method](../html/Overload_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged.htm "OnObjectChanged Method ")

[OnObjectChanged Method (GH\_ObjectChangedEventArgs)](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged.htm "OnObjectChanged Method (GH_ObjectChangedEventArgs)")

[OnObjectChanged Method (GH\_ObjectEventType)](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_1.htm "OnObjectChanged Method (GH_ObjectEventType)")

[OnObjectChanged Method (String)](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_3.htm "OnObjectChanged Method (String)")

[OnObjectChanged Method (GH\_ObjectEventType, Object)](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_2.htm "OnObjectChanged Method (GH_ObjectEventType, Object)")

[OnObjectChanged Method (String, Object)](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_4.htm "OnObjectChanged Method (String, Object)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DocumentObjectAddLanguageSpecificTextSet("LST3170558A\_0?cpp=::|nu=.");OnObjectChanged Method (GH\_ObjectEventType, Object) |

Raises the ObjectChanged event on the current (!not the top level!) object.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void OnObjectChanged(
	GH_ObjectEventType eventType,
	Object tag
)
```

```
Sub OnObjectChanged ( 
	eventType As GH_ObjectEventType,
	tag As Object
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

eventType
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST3170558A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ObjectEventType](T_Grasshopper_Kernel_GH_ObjectEventType.htm)  
    Type of change.

tag
:   Type: [SystemAddLanguageSpecificTextSet("LST3170558A\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
    Tag to apply to the event arguments.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DocumentObject Interface](T_Grasshopper_Kernel_IGH_DocumentObject.htm)

[OnObjectChanged Overload](Overload_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)