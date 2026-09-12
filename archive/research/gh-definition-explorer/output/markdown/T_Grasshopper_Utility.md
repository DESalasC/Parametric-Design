# T_Grasshopper_Utility

﻿ Utility Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Utility Class](../html/T_Grasshopper_Utility.htm "Utility Class")

[Utility Methods](../html/Methods_T_Grasshopper_Utility.htm "Utility Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Utility Class |

Class with useful static methods.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST4638FFC3\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  GrasshopperAddLanguageSpecificTextSet("LST4638FFC3\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Utility

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class Utility
```

```
Public NotInheritable Class Utility
```

AddLanguageTabSet("ID1EBCA");

The Utility type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [DocumentAngleTolerance](M_Grasshopper_Utility_DocumentAngleTolerance.htm) | Returns the Angle Tolerance in degrees for the model document |
| Public methodStatic member | [DocumentTolerance](M_Grasshopper_Utility_DocumentTolerance.htm) | Returns the Absolute Tolerance of the model document |
| Public methodStatic member | [DocumentUnits](M_Grasshopper_Utility_DocumentUnits.htm) | Returns the unit system for the model document |
| Public methodStatic member | [FixNewlines(String)](M_Grasshopper_Utility_FixNewlines.htm) | Make sure all newlines in a string adhere to the current platform standard. |
| Public methodStatic member | [FixNewlines(String, String)](M_Grasshopper_Utility_FixNewlines_1.htm) | Make sure all newlines in a string have a specific pattern. |
| Public methodStatic member | [InvokeDownloader](M_Grasshopper_Utility_InvokeDownloader.htm) | Start an asynchronous download operation. The download runs in a separate appdomain. After triggering that process this method returns immediately. |
| Public methodStatic member | [InvokeGetter](M_Grasshopper_Utility_InvokeGetter.htm) | Call a getter property via its name. |
| Public methodStatic member | [InvokeGetterSafe](M_Grasshopper_Utility_InvokeGetterSafe.htm) | Call a getter property via its name. No exceptions are thrown. |
| Public methodStatic member | [InvokeMethod(Object, String)](M_Grasshopper_Utility_InvokeMethod.htm) | Call a method via its name. |
| Public methodStatic member | [InvokeMethod(Object, String, AddLanguageSpecificTextSet("LST4638FFC3\_2?cpp=array&lt;");ObjectAddLanguageSpecificTextSet("LST4638FFC3\_3?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Utility_InvokeMethod_1.htm) | Call a method via its name. |
| Public methodStatic member | [InvokeMethodSafe(Object, String)](M_Grasshopper_Utility_InvokeMethodSafe.htm) | Call a method via its name. No exceptions are thrown. |
| Public methodStatic member | [InvokeMethodSafe(Object, String, AddLanguageSpecificTextSet("LST4638FFC3\_4?cpp=array&lt;");ObjectAddLanguageSpecificTextSet("LST4638FFC3\_5?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Utility_InvokeMethodSafe_1.htm) | Call a method via its name. No exceptions are thrown. |
| Public methodStatic member | [InvokeSetter](M_Grasshopper_Utility_InvokeSetter.htm) | Call a setter property via its name. |
| Public methodStatic member | [InvokeSetterSafe](M_Grasshopper_Utility_InvokeSetterSafe.htm) | Call a setter property via its name. No exceptions are thrown. |
| Public methodStatic member | [LikeOperator](M_Grasshopper_Utility_LikeOperator.htm) | Exposes the VB.NET Like operator as a static method. |
| Public methodStatic member | [SetDefaultTolerances](M_Grasshopper_Utility_SetDefaultTolerances.htm) | Utility function to set absolute and angle tolerance fields. |
| Public methodStatic member | [SetDefaultUnits](M_Grasshopper_Utility_SetDefaultUnits.htm) | Utility function to set model unit fields |
| Public methodStatic member | [TernaryIfAddLanguageSpecificTextSet("LST4638FFC3\_6?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST4638FFC3\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Utility_TernaryIf__1.htm) | **Obsolete.**  Type safe implementation of the IIf conditional statement. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)