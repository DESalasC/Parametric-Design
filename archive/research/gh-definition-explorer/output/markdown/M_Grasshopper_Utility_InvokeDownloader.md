# M_Grasshopper_Utility_InvokeDownloader

﻿ Utility.InvokeDownloader Method 

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
| UtilityAddLanguageSpecificTextSet("LST6DBB43EA\_0?cpp=::|nu=.");InvokeDownloader Method |

Start an asynchronous download operation.
The download runs in a separate appdomain. After triggering that process this method returns immediately.

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void InvokeDownloader(
	string sourceUri,
	string targetUri,
	bool silent
)
```

```
Public Shared Sub InvokeDownloader ( 
	sourceUri As String,
	targetUri As String,
	silent As Boolean
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

sourceUri
:   Type: [SystemAddLanguageSpecificTextSet("LST6DBB43EA\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Uri of data to download.

targetUri
:   Type: [SystemAddLanguageSpecificTextSet("LST6DBB43EA\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Uri of file on local disk where to store downloaded data.

silent
:   Type: [SystemAddLanguageSpecificTextSet("LST6DBB43EA\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true the download will not display any user interface.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Utility Class](T_Grasshopper_Utility.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)