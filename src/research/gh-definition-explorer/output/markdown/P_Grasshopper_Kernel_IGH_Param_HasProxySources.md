# P_Grasshopper_Kernel_IGH_Param_HasProxySources

﻿ IGH\_Param.HasProxySources Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_Param Interface](../html/T_Grasshopper_Kernel_IGH_Param.htm "IGH_Param Interface")

[IGH\_Param Properties](../html/Properties_T_Grasshopper_Kernel_IGH_Param.htm "IGH_Param Properties")

[Access Property](../html/P_Grasshopper_Kernel_IGH_Param_Access.htm "Access Property ")

[DataMapping Property](../html/P_Grasshopper_Kernel_IGH_Param_DataMapping.htm "DataMapping Property ")

[DataType Property](../html/P_Grasshopper_Kernel_IGH_Param_DataType.htm "DataType Property ")

[HasProxySources Property](../html/P_Grasshopper_Kernel_IGH_Param_HasProxySources.htm "HasProxySources Property ")

[Kind Property](../html/P_Grasshopper_Kernel_IGH_Param_Kind.htm "Kind Property ")

[Optional Property](../html/P_Grasshopper_Kernel_IGH_Param_Optional.htm "Optional Property ")

[ProxySourceCount Property](../html/P_Grasshopper_Kernel_IGH_Param_ProxySourceCount.htm "ProxySourceCount Property ")

[Recipients Property](../html/P_Grasshopper_Kernel_IGH_Param_Recipients.htm "Recipients Property ")

[Reverse Property](../html/P_Grasshopper_Kernel_IGH_Param_Reverse.htm "Reverse Property ")

[Simplify Property](../html/P_Grasshopper_Kernel_IGH_Param_Simplify.htm "Simplify Property ")

[SourceCount Property](../html/P_Grasshopper_Kernel_IGH_Param_SourceCount.htm "SourceCount Property ")

[Sources Property](../html/P_Grasshopper_Kernel_IGH_Param_Sources.htm "Sources Property ")

[StateTags Property](../html/P_Grasshopper_Kernel_IGH_Param_StateTags.htm "StateTags Property ")

[Type Property](../html/P_Grasshopper_Kernel_IGH_Param_Type.htm "Type Property ")

[TypeName Property](../html/P_Grasshopper_Kernel_IGH_Param_TypeName.htm "TypeName Property ")

[VolatileData Property](../html/P_Grasshopper_Kernel_IGH_Param_VolatileData.htm "VolatileData Property ")

[VolatileDataCount Property](../html/P_Grasshopper_Kernel_IGH_Param_VolatileDataCount.htm "VolatileDataCount Property ")

[WireDisplay Property](../html/P_Grasshopper_Kernel_IGH_Param_WireDisplay.htm "WireDisplay Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ParamAddLanguageSpecificTextSet("LST32AAFE4B\_0?cpp=::|nu=.");HasProxySources Property |

Gets a value indicating whether or not this parameter maintains proxy sources.
Proxy sources are used during file IO, when actual sources might not be available yet.
Once an IO operation has been completed there should be no more proxy sources.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool HasProxySources { get; }
```

```
ReadOnly Property HasProxySources As Boolean
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  

[Missing <value> documentation for "P:Grasshopper.Kernel.IGH\_Param.HasProxySources"]

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the parameter has at least one proxy source, false if not.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Param Interface](T_Grasshopper_Kernel_IGH_Param.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)