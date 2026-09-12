# T_Grasshopper_Kernel_GH_ValueProxy_1

﻿ GH\_ValueProxy(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ValueProxy(T) Class](../html/T_Grasshopper_Kernel_GH_ValueProxy_1.htm "GH_ValueProxy(T) Class")

[GH\_ValueProxy(T) Constructor](../html/M_Grasshopper_Kernel_GH_ValueProxy_1__ctor.htm "GH_ValueProxy(T) Constructor ")

[GH\_ValueProxy(T) Properties](../html/Properties_T_Grasshopper_Kernel_GH_ValueProxy_1.htm "GH_ValueProxy(T) Properties")

[GH\_ValueProxy(T) Methods](../html/Methods_T_Grasshopper_Kernel_GH_ValueProxy_1.htm "GH_ValueProxy(T) Methods")

[GH\_ValueProxy(T) Fields](../html/Fields_T_Grasshopper_Kernel_GH_ValueProxy_1.htm "GH_ValueProxy(T) Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ValueProxyAddLanguageSpecificTextSet("LSTE455D31A\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTE455D31A\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

Represents the abstract base implementation of the IGH\_ValueProxy interface.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTE455D31A\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTE455D31A\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ValueProxyAddLanguageSpecificTextSet("LSTE455D31A\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE455D31A\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_ValueProxy<T> : IGH_ValueProxy
```

```
Public MustInherit Class GH_ValueProxy(Of T)
	Implements IGH_ValueProxy
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T
:   The type of this implementation

The GH\_ValueProxyAddLanguageSpecificTextSet("LSTE455D31A\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE455D31A\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_ValueProxyAddLanguageSpecificTextSet("LSTE455D31A\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE455D31A\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](M_Grasshopper_Kernel_GH_ValueProxy_1__ctor.htm) | Default constructor for the base class. All derived classes must call this constructor. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValid](P_Grasshopper_Kernel_GH_ValueProxy_1_IsValid.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Duplicate](M_Grasshopper_Kernel_GH_ValueProxy_1_Duplicate.htm) |  |
| Public method | [Duplicate\_T](M_Grasshopper_Kernel_GH_ValueProxy_1_Duplicate_T.htm) |  |
| Public method | [FromString](M_Grasshopper_Kernel_GH_ValueProxy_1_FromString.htm) | Performs the String->Value parsing. The default implementation always returns False. |
| Public method | [MutateString](M_Grasshopper_Kernel_GH_ValueProxy_1_MutateString.htm) |  |
| Public method | [ToString](M_Grasshopper_Kernel_GH_ValueProxy_1_ToString.htm) | Performs a default ToString operation on the local value. If the value is Nothing, an empty String is returned. (Overrides [ObjectAddLanguageSpecificTextSet("LSTE455D31A\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTE455D31A\_11?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_IsStringProxy](F_Grasshopper_Kernel_GH_ValueProxy_1_m_IsStringProxy.htm) |  |
| Protected field | [m\_Name](F_Grasshopper_Kernel_GH_ValueProxy_1_m_Name.htm) |  |
| Protected field | [m\_UserString](F_Grasshopper_Kernel_GH_ValueProxy_1_m_UserString.htm) |  |
| Protected field | [m\_Valid](F_Grasshopper_Kernel_GH_ValueProxy_1_m_Valid.htm) |  |
| Protected field | [m\_Value](F_Grasshopper_Kernel_GH_ValueProxy_1_m_Value.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)