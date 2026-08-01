# M_Grasshopper_Utility_TernaryIf__1

﻿ Utility.TernaryIf(T) Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Utility Class](../html/T_Grasshopper_Utility.htm "Utility Class")

[Utility Methods](../html/Methods_T_Grasshopper_Utility.htm "Utility Methods")

[DocumentAngleTolerance Method](../html/M_Grasshopper_Utility_DocumentAngleTolerance.htm "DocumentAngleTolerance Method ")

[DocumentTolerance Method](../html/M_Grasshopper_Utility_DocumentTolerance.htm "DocumentTolerance Method ")

[DocumentUnits Method](../html/M_Grasshopper_Utility_DocumentUnits.htm "DocumentUnits Method ")

[FixNewlines Method](../html/Overload_Grasshopper_Utility_FixNewlines.htm "FixNewlines Method ")

[InvokeDownloader Method](../html/M_Grasshopper_Utility_InvokeDownloader.htm "InvokeDownloader Method ")

[InvokeGetter Method](../html/M_Grasshopper_Utility_InvokeGetter.htm "InvokeGetter Method ")

[InvokeGetterSafe Method](../html/M_Grasshopper_Utility_InvokeGetterSafe.htm "InvokeGetterSafe Method ")

[InvokeMethod Method](../html/Overload_Grasshopper_Utility_InvokeMethod.htm "InvokeMethod Method ")

[InvokeMethodSafe Method](../html/Overload_Grasshopper_Utility_InvokeMethodSafe.htm "InvokeMethodSafe Method ")

[InvokeSetter Method](../html/M_Grasshopper_Utility_InvokeSetter.htm "InvokeSetter Method ")

[InvokeSetterSafe Method](../html/M_Grasshopper_Utility_InvokeSetterSafe.htm "InvokeSetterSafe Method ")

[LikeOperator Method](../html/M_Grasshopper_Utility_LikeOperator.htm "LikeOperator Method ")

[SetDefaultTolerances Method](../html/M_Grasshopper_Utility_SetDefaultTolerances.htm "SetDefaultTolerances Method ")

[SetDefaultUnits Method](../html/M_Grasshopper_Utility_SetDefaultUnits.htm "SetDefaultUnits Method ")

[TernaryIf(T) Method](../html/M_Grasshopper_Utility_TernaryIf__1.htm "TernaryIf(T) Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| UtilityAddLanguageSpecificTextSet("LST25DD970\_0?cpp=::|nu=.");TernaryIfAddLanguageSpecificTextSet("LST25DD970\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST25DD970\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Method |

**Note: This API is now obsolete.**

Type safe implementation of the IIf conditional statement.

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
[ObsoleteAttribute("Ternary conditionals are now part of the standard C# and VB language spec. Consider using those instead.")]
public static T TernaryIf<T>(
	bool condition,
	T A,
	T B
)
```

```
<ObsoleteAttribute("Ternary conditionals are now part of the standard C# and VB language spec. Consider using those instead.")>
Public Shared Function TernaryIf(Of T) ( 
	condition As Boolean,
	A As T,
	B As T
) As T
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

condition
:   Type: [SystemAddLanguageSpecificTextSet("LST25DD970\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, A is returned.

A
:   Type: T  
    Value to return when condition evaluates to true.

B
:   Type: T  
    Value to return when condition evaluates to false.

#### Type Parameters

T
:   Type of statement.

#### Return Value

Type: T

![](../icons/SectionExpanded.png)See Also

#### Reference

[Utility Class](T_Grasshopper_Utility.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)