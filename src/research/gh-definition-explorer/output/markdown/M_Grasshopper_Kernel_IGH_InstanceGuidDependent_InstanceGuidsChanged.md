# M_Grasshopper_Kernel_IGH_InstanceGuidDependent_InstanceGuidsChanged

﻿ IGH\_InstanceGuidDependent.InstanceGuidsChanged Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_InstanceGuidDependent Interface](../html/T_Grasshopper_Kernel_IGH_InstanceGuidDependent.htm "IGH_InstanceGuidDependent Interface")

[IGH\_InstanceGuidDependent Methods](../html/Methods_T_Grasshopper_Kernel_IGH_InstanceGuidDependent.htm "IGH_InstanceGuidDependent Methods")

[InstanceGuidsChanged Method](../html/M_Grasshopper_Kernel_IGH_InstanceGuidDependent_InstanceGuidsChanged.htm "InstanceGuidsChanged Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_InstanceGuidDependentAddLanguageSpecificTextSet("LSTF74EDB07\_0?cpp=::|nu=.");InstanceGuidsChanged Method |

This method will be called by the GH\_Document that owns this object after
it mutates some or all of it's object InstanceIds.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void InstanceGuidsChanged(
	SortedDictionary<Guid, Guid> map
)
```

```
Sub InstanceGuidsChanged ( 
	map As SortedDictionary(Of Guid, Guid)
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

map
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LSTF74EDB07\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");SortedDictionary](https://docs.microsoft.com/dotnet/api/system.collections.generic.sorteddictionary-2)AddLanguageSpecificTextSet("LSTF74EDB07\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Guid](https://docs.microsoft.com/dotnet/api/system.guid), [Guid](https://docs.microsoft.com/dotnet/api/system.guid)AddLanguageSpecificTextSet("LSTF74EDB07\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    A translation dictionary of old InstanceID keys (no longer existent) and new InstanceID values.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_InstanceGuidDependent Interface](T_Grasshopper_Kernel_IGH_InstanceGuidDependent.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)