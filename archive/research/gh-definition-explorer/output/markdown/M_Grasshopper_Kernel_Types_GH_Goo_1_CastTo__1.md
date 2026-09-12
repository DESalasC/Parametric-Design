# M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1

﻿ GH\_Goo(T).CastTo(Q) Method 

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
| GH\_GooAddLanguageSpecificTextSet("LST32298A68\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST32298A68\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST32298A68\_2?cpp=::|nu=.");CastToAddLanguageSpecificTextSet("LST32298A68\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST32298A68\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Method |

Attempt a cast to type Q.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual bool CastTo<Q>(
	ref Q target
)
```

```
Public Overridable Function CastTo(Of Q) ( 
	ByRef target As Q
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

target
:   Type: QAddLanguageSpecificTextSet("LST32298A68\_5?cpp=%");  
    Pointer to target of cast.

#### Type Parameters

Q
:   Type to cast to.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

#### Implements

[IGH\_GooAddLanguageSpecificTextSet("LST32298A68\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");CastToAddLanguageSpecificTextSet("LST32298A68\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST32298A68\_8?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(TAddLanguageSpecificTextSet("LST32298A68\_9?cpp=%");)](M_Grasshopper_Kernel_Types_IGH_Goo_CastTo__1.htm)

![](../icons/SectionExpanded.png)Remarks

If false, the target instance contents are not guaranteed to be valid.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GooAddLanguageSpecificTextSet("LST32298A68\_10?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST32298A68\_11?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)