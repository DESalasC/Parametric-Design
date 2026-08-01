# M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1

﻿ GH\_GeometricGoo(T).CastTo(Q) Method (Q)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_GeometricGoo(T) Class](../html/T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm "GH_GeometricGoo(T) Class")

[GH\_GeometricGoo(T) Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm "GH_GeometricGoo(T) Methods")

[CastTo Method](../html/Overload_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo.htm "CastTo Method ")

[CastTo(Q) Method (Q)](../html/M_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo__1.htm "CastTo(Q) Method (Q)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GeometricGooAddLanguageSpecificTextSet("LSTB0B52C27\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTB0B52C27\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTB0B52C27\_2?cpp=::|nu=.");CastToAddLanguageSpecificTextSet("LSTB0B52C27\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LSTB0B52C27\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Method (QAddLanguageSpecificTextSet("LSTB0B52C27\_5?cpp=%");) |

Attempt a cast to type T.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public override bool CastTo<Q>(
	out Q target
)
```

```
Public Overrides Function CastTo(Of Q) ( 
	<OutAttribute> ByRef target As Q
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

target
:   Type: QAddLanguageSpecificTextSet("LSTB0B52C27\_6?cpp=%");  
    Pointer to target of cast.

#### Type Parameters

Q
:   Type to cast to

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)Remarks

If false, the target instance contents are not guaranteed to be valid.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GeometricGooAddLanguageSpecificTextSet("LSTB0B52C27\_7?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB0B52C27\_8?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)

[CastTo Overload](Overload_Grasshopper_Kernel_Types_GH_GeometricGoo_1_CastTo.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)