# P_Grasshopper_Kernel_GH_DocumentObject_Obsolete

﻿ GH\_DocumentObject.Obsolete Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentObject Class](../html/T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Class")

[GH\_DocumentObject Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Properties")

[Attributes Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_Attributes.htm "Attributes Property ")

[ComponentGuid Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_ComponentGuid.htm "ComponentGuid Property ")

[Exposure Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_Exposure.htm "Exposure Property ")

[Icon Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_Icon.htm "Icon Property ")

[Icon\_24x24 Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24.htm "Icon_24x24 Property ")

[Icon\_24x24\_Locked Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24_Locked.htm "Icon_24x24_Locked Property ")

[IconDisplayMode Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_IconDisplayMode.htm "IconDisplayMode Property ")

[Obsolete Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_Obsolete.htm "Obsolete Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentObjectAddLanguageSpecificTextSet("LSTDEAD9B12\_0?cpp=::|nu=.");Obsolete Property |

Gets whether this object is obsolete. Default implementation returns true if
the class name contains the string "OBSOLETE" or if this class has been decorated with the
ObsoleteAttribute.
You are free to override this if you want, but I suggest adding the ObsoleteAttribute instead.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual bool Obsolete { get; }
```

```
Public Overridable ReadOnly Property Obsolete As Boolean
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  

[Missing <value> documentation for "P:Grasshopper.Kernel.GH\_DocumentObject.Obsolete"]

#### Implements

[IGH\_DocumentObjectAddLanguageSpecificTextSet("LSTDEAD9B12\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Obsolete](P_Grasshopper_Kernel_IGH_DocumentObject_Obsolete.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentObject Class](T_Grasshopper_Kernel_GH_DocumentObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)