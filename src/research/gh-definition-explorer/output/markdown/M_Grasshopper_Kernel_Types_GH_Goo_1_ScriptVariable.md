# M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable

﻿ GH\_Goo(T).ScriptVariable Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_Goo(T) Class](../html/T_Grasshopper_Kernel_Types_GH_Goo_1.htm "GH_Goo(T) Class")

[GH\_Goo(T) Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Goo_1.htm "GH_Goo(T) Methods")

[CastFrom Method](../html/M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm "CastFrom Method ")

[CastTo(Q) Method](../html/M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm "CastTo(Q) Method ")

[Duplicate Method](../html/M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm "Duplicate Method ")

[EmitProxy Method](../html/M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm "EmitProxy Method ")

[Read Method](../html/M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm "Read Method ")

[ScriptVariable Method](../html/M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm "ScriptVariable Method ")

[ToString Method](../html/M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm "ToString Method ")

[Write Method](../html/M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GooAddLanguageSpecificTextSet("LSTD0F2F3CA\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD0F2F3CA\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTD0F2F3CA\_2?cpp=::|nu=.");ScriptVariable Method |

This function will be called when the local IGH\_Goo instance
disappears into a user Script. This would be an excellent place to
cast your IGH\_Goo type to a simple data type.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual Object ScriptVariable()
```

```
Public Overridable Function ScriptVariable As Object
```

AddLanguageTabSet("ID0EBCA");

#### Return Value

Type: [Object](https://docs.microsoft.com/dotnet/api/system.object)  
The default implementation of this function returns the Value instance.

#### Implements

[IGH\_GooAddLanguageSpecificTextSet("LSTD0F2F3CA\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ScriptVariableAddLanguageSpecificTextSet("LSTD0F2F3CA\_4?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Types_IGH_Goo_ScriptVariable.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GooAddLanguageSpecificTextSet("LSTD0F2F3CA\_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD0F2F3CA\_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)