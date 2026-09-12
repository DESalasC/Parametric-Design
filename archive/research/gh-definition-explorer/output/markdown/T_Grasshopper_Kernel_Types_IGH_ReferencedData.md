# T_Grasshopper_Kernel_Types_IGH_ReferencedData

﻿ IGH\_ReferencedData Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[IGH\_ReferencedData Interface](../html/T_Grasshopper_Kernel_Types_IGH_ReferencedData.htm "IGH_ReferencedData Interface")

[IGH\_ReferencedData Properties](../html/Properties_T_Grasshopper_Kernel_Types_IGH_ReferencedData.htm "IGH_ReferencedData Properties")

[IGH\_ReferencedData Methods](../html/Methods_T_Grasshopper_Kernel_Types_IGH_ReferencedData.htm "IGH_ReferencedData Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ReferencedData Interface |

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_ReferencedData : IGH_Goo
```

```
Public Interface IGH_ReferencedData
	Inherits IGH_Goo
```

AddLanguageTabSet("ID0EBCA");

The IGH\_ReferencedData type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsReferencedData](P_Grasshopper_Kernel_Types_IGH_ReferencedData_IsReferencedData.htm) |  |
| Public property | [IsReferencedDataLoaded](P_Grasshopper_Kernel_Types_IGH_ReferencedData_IsReferencedDataLoaded.htm) |  |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_IGH_Goo_IsValid.htm) | Gets a value indicating whether or not the current value is valid. (Inherited from [IGH\_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).) |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_IGH_Goo_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. (Inherited from [IGH\_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).) |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_IGH_Goo_TypeDescription.htm) | Gets a description of the type of the implementation. (Inherited from [IGH\_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).) |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_IGH_Goo_TypeName.htm) | Gets the name of the type of the implementation. (Inherited from [IGH\_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_IGH_Goo_CastFrom.htm) | Attempt a cast from generic object (Inherited from [IGH\_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).) |
| Public method | [CastToAddLanguageSpecificTextSet("LSTB26AC508\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTB26AC508\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_Types_IGH_Goo_CastTo__1.htm) | Attempt a cast to type T (Inherited from [IGH\_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).) |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_IGH_Goo_Duplicate.htm) | Make a complete duplicate of this instance. No shallow copies. (Inherited from [IGH\_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).) |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_IGH_Goo_EmitProxy.htm) | Create a new proxy for this instance. Return Null if this class does not support proxies. (Inherited from [IGH\_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).) |
| Public method | [LoadReferencedData](M_Grasshopper_Kernel_Types_IGH_ReferencedData_LoadReferencedData.htm) |  |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_IGH_Goo_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disapears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. (Inherited from [IGH\_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).) |
| Public method | [ToString](M_Grasshopper_Kernel_Types_IGH_Goo_ToString.htm) | Creates a string description of the current instance value (Inherited from [IGH\_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm).) |
| Public method | [UnloadReferencedData](M_Grasshopper_Kernel_Types_IGH_ReferencedData_UnloadReferencedData.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)