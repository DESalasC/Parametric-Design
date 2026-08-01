# M_Grasshopper_Kernel_IGH_Attributes_AppendToAttributeTree

﻿ IGH\_Attributes.AppendToAttributeTree Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_Attributes Interface](../html/T_Grasshopper_Kernel_IGH_Attributes.htm "IGH_Attributes Interface")

[IGH\_Attributes Methods](../html/Methods_T_Grasshopper_Kernel_IGH_Attributes.htm "IGH_Attributes Methods")

[AppendToAttributeTree Method](../html/M_Grasshopper_Kernel_IGH_Attributes_AppendToAttributeTree.htm "AppendToAttributeTree Method ")

[ExpireLayout Method](../html/M_Grasshopper_Kernel_IGH_Attributes_ExpireLayout.htm "ExpireLayout Method ")

[InvalidateCanvas Method](../html/M_Grasshopper_Kernel_IGH_Attributes_InvalidateCanvas.htm "InvalidateCanvas Method ")

[IsMenuRegion Method](../html/M_Grasshopper_Kernel_IGH_Attributes_IsMenuRegion.htm "IsMenuRegion Method ")

[IsPickRegion Method](../html/Overload_Grasshopper_Kernel_IGH_Attributes_IsPickRegion.htm "IsPickRegion Method ")

[NewInstanceGuid Method](../html/Overload_Grasshopper_Kernel_IGH_Attributes_NewInstanceGuid.htm "NewInstanceGuid Method ")

[PerformLayout Method](../html/M_Grasshopper_Kernel_IGH_Attributes_PerformLayout.htm "PerformLayout Method ")

[RenderToCanvas Method](../html/M_Grasshopper_Kernel_IGH_Attributes_RenderToCanvas.htm "RenderToCanvas Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_AttributesAddLanguageSpecificTextSet("LSTA067CC79\_0?cpp=::|nu=.");AppendToAttributeTree Method |

Recursively append these attributes and all child attributes to the attribute list.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void AppendToAttributeTree(
	List<IGH_Attributes> attributes
)
```

```
Sub AppendToAttributeTree ( 
	attributes As List(Of IGH_Attributes)
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

attributes
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LSTA067CC79\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LSTA067CC79\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_Attributes](T_Grasshopper_Kernel_IGH_Attributes.htm)AddLanguageSpecificTextSet("LSTA067CC79\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    List to append to.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Attributes Interface](T_Grasshopper_Kernel_IGH_Attributes.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)