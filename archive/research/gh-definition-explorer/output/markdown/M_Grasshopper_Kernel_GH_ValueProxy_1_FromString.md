# M_Grasshopper_Kernel_GH_ValueProxy_1_FromString

﻿ GH\_ValueProxy(T).FromString Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ValueProxy(T) Class](../html/T_Grasshopper_Kernel_GH_ValueProxy_1.htm "GH_ValueProxy(T) Class")

[GH\_ValueProxy(T) Methods](../html/Methods_T_Grasshopper_Kernel_GH_ValueProxy_1.htm "GH_ValueProxy(T) Methods")

[Duplicate Method](../html/M_Grasshopper_Kernel_GH_ValueProxy_1_Duplicate.htm "Duplicate Method ")

[Duplicate\_T Method](../html/M_Grasshopper_Kernel_GH_ValueProxy_1_Duplicate_T.htm "Duplicate_T Method ")

[FromString Method](../html/M_Grasshopper_Kernel_GH_ValueProxy_1_FromString.htm "FromString Method ")

[MutateString Method](../html/M_Grasshopper_Kernel_GH_ValueProxy_1_MutateString.htm "MutateString Method ")

[ToString Method](../html/M_Grasshopper_Kernel_GH_ValueProxy_1_ToString.htm "ToString Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ValueProxyAddLanguageSpecificTextSet("LST180D3D3C\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST180D3D3C\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST180D3D3C\_2?cpp=::|nu=.");FromString Method |

Performs the String->Value parsing. The default implementation always returns False.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual bool FromString(
	string in
)
```

```
Public Overridable Function FromString ( 
	in As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

in
:   Type: [SystemAddLanguageSpecificTextSet("LST180D3D3C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The String to parse

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True in cae of success, False in case of failure.

#### Implements

[IGH\_ValueProxyAddLanguageSpecificTextSet("LST180D3D3C\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");FromString(String)](M_Grasshopper_Kernel_IGH_ValueProxy_FromString.htm)

![](../icons/SectionExpanded.png)Remarks

The result of the parse is stored in the local value pointer.
If this function returns False there is no guarantee the local value is still valid.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ValueProxyAddLanguageSpecificTextSet("LST180D3D3C\_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST180D3D3C\_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_ValueProxy_1.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)