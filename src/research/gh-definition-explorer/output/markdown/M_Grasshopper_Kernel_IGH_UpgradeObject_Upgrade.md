# M_Grasshopper_Kernel_IGH_UpgradeObject_Upgrade

﻿ IGH\_UpgradeObject.Upgrade Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_UpgradeObject Interface](../html/T_Grasshopper_Kernel_IGH_UpgradeObject.htm "IGH_UpgradeObject Interface")

[IGH\_UpgradeObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_UpgradeObject.htm "IGH_UpgradeObject Methods")

[Upgrade Method](../html/M_Grasshopper_Kernel_IGH_UpgradeObject_Upgrade.htm "Upgrade Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_UpgradeObjectAddLanguageSpecificTextSet("LST1F3B2FC8\_0?cpp=::|nu=.");Upgrade Method |

Upgrade an existing object.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
IGH_DocumentObject Upgrade(
	IGH_DocumentObject target,
	GH_Document document
)
```

```
Function Upgrade ( 
	target As IGH_DocumentObject,
	document As GH_Document
) As IGH_DocumentObject
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

target
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST1F3B2FC8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm)  
    Object to upgrade.

document
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST1F3B2FC8\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Document](T_Grasshopper_Kernel_GH_Document.htm)  
    Document that contains the object.

#### Return Value

Type: [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm)  
The newly created object on success, null on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_UpgradeObject Interface](T_Grasshopper_Kernel_IGH_UpgradeObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)