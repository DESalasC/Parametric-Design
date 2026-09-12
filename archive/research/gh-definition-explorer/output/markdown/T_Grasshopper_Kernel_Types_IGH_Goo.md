# T_Grasshopper_Kernel_Types_IGH_Goo

﻿ IGH\_Goo Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[IGH\_Goo Interface](../html/T_Grasshopper_Kernel_Types_IGH_Goo.htm "IGH_Goo Interface")

[IGH\_Goo Properties](../html/Properties_T_Grasshopper_Kernel_Types_IGH_Goo.htm "IGH_Goo Properties")

[IGH\_Goo Methods](../html/Methods_T_Grasshopper_Kernel_Types_IGH_Goo.htm "IGH_Goo Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_Goo Interface |

Base interface for all Data inside Grasshopper. Every parameter must implement a type of Goo.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_Goo : GH_ISerializable
```

```
Public Interface IGH_Goo
	Inherits GH_ISerializable
```

AddLanguageTabSet("ID0EBCA");

The IGH\_Goo type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValid](P_Grasshopper_Kernel_Types_IGH_Goo_IsValid.htm) | Gets a value indicating whether or not the current value is valid. |
| Public property | [IsValidWhyNot](P_Grasshopper_Kernel_Types_IGH_Goo_IsValidWhyNot.htm) | Gets a string describing the state of "invalidness". If the instance *is* valid, then this property should return Nothing or String.Empty. |
| Public property | [TypeDescription](P_Grasshopper_Kernel_Types_IGH_Goo_TypeDescription.htm) | Gets a description of the type of the implementation. |
| Public property | [TypeName](P_Grasshopper_Kernel_Types_IGH_Goo_TypeName.htm) | Gets the name of the type of the implementation. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastFrom](M_Grasshopper_Kernel_Types_IGH_Goo_CastFrom.htm) | Attempt a cast from generic object |
| Public method | [CastToAddLanguageSpecificTextSet("LST2D52676\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST2D52676\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_Types_IGH_Goo_CastTo__1.htm) | Attempt a cast to type T |
| Public method | [Duplicate](M_Grasshopper_Kernel_Types_IGH_Goo_Duplicate.htm) | Make a complete duplicate of this instance. No shallow copies. |
| Public method | [EmitProxy](M_Grasshopper_Kernel_Types_IGH_Goo_EmitProxy.htm) | Create a new proxy for this instance. Return Null if this class does not support proxies. |
| Public method | [Read](M_GH_IO_GH_ISerializable_Read.htm) | This method is called whenever the instance is required to deserialize itself. (Inherited from [GH\_ISerializable](T_GH_IO_GH_ISerializable.htm).) |
| Public method | [ScriptVariable](M_Grasshopper_Kernel_Types_IGH_Goo_ScriptVariable.htm) | This function will be called when the local IGH\_Goo instance disapears into a user Script. This would be an excellent place to cast your IGH\_Goo type to a simple data type. |
| Public method | [ToString](M_Grasshopper_Kernel_Types_IGH_Goo_ToString.htm) | Creates a string description of the current instance value |
| Public method | [Write](M_GH_IO_GH_ISerializable_Write.htm) | This method is called whenever the instance is required to serialize itself. (Inherited from [GH\_ISerializable](T_GH_IO_GH_ISerializable.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)