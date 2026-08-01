# P_Grasshopper_Kernel_IGH_ValueProxy_UserString

﻿ IGH\_ValueProxy.UserString Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_ValueProxy Interface](../html/T_Grasshopper_Kernel_IGH_ValueProxy.htm "IGH_ValueProxy Interface")

[IGH\_ValueProxy Properties](../html/Properties_T_Grasshopper_Kernel_IGH_ValueProxy.htm "IGH_ValueProxy Properties")

[IsParsable Property](../html/P_Grasshopper_Kernel_IGH_ValueProxy_IsParsable.htm "IsParsable Property ")

[IsValid Property](../html/P_Grasshopper_Kernel_IGH_ValueProxy_IsValid.htm "IsValid Property ")

[ProxyName Property](../html/P_Grasshopper_Kernel_IGH_ValueProxy_ProxyName.htm "ProxyName Property ")

[ProxyType Property](../html/P_Grasshopper_Kernel_IGH_ValueProxy_ProxyType.htm "ProxyType Property ")

[ProxyValue Property](../html/P_Grasshopper_Kernel_IGH_ValueProxy_ProxyValue.htm "ProxyValue Property ")

[UserString Property](../html/P_Grasshopper_Kernel_IGH_ValueProxy_UserString.htm "UserString Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ValueProxyAddLanguageSpecificTextSet("LSTE077B901\_0?cpp=::|nu=.");UserString Property |

Gets or sets the user-defined string that describes this proxy
This only really makes sense if the Proxy is Parsable.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
string UserString { get; set; }
```

```
Property UserString As String
	Get
	Set
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [String](https://docs.microsoft.com/dotnet/api/system.string)  

[Missing <value> documentation for "P:Grasshopper.Kernel.IGH\_ValueProxy.UserString"]

#### Return Value

Type: [String](https://docs.microsoft.com/dotnet/api/system.string)  
If the proxy contains no user-string, the ToString result is returned instead

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_ValueProxy Interface](T_Grasshopper_Kernel_IGH_ValueProxy.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)