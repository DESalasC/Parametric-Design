# T_Grasshopper_Kernel_GH_UserObject

﻿ GH\_UserObject Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_UserObject Class](../html/T_Grasshopper_Kernel_GH_UserObject.htm "GH_UserObject Class")

[GH\_UserObject Constructor](../html/Overload_Grasshopper_Kernel_GH_UserObject__ctor.htm "GH_UserObject Constructor ")

[GH\_UserObject Properties](../html/Properties_T_Grasshopper_Kernel_GH_UserObject.htm "GH_UserObject Properties")

[GH\_UserObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_UserObject.htm "GH_UserObject Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UserObject Class |

Represents a custom user object. A User Object is an existing IGH\_DocumentObject with
overridden icon, instance description and exposure.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST1D498D86\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST1D498D86\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UserObject

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_UserObject
```

```
Public Class GH_UserObject
```

AddLanguageTabSet("ID1EBCA");

The GH\_UserObject type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_UserObjectAddLanguageSpecificTextSet("LST1D498D86\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_UserObject__ctor.htm) | Empty constructor |
| Public method | [GH\_UserObject(String)](M_Grasshopper_Kernel_GH_UserObject__ctor_1.htm) | Create a new user object from an existing \*.ghuser file. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BaseGuid](P_Grasshopper_Kernel_GH_UserObject_BaseGuid.htm) | Gets or sets the ComponentID of the IGH\_DocumentObject that functions as the base class for this User Object. |
| Public property | [Data](P_Grasshopper_Kernel_GH_UserObject_Data.htm) | Gets or sets the serialized data. This data is used to deserialize a new instance of the base class. |
| Public property | [Description](P_Grasshopper_Kernel_GH_UserObject_Description.htm) | Gets or sets the Instance Description override for this User Object. |
| Public property | [Exposure](P_Grasshopper_Kernel_GH_UserObject_Exposure.htm) | Gets or sets the Exposure of this User Object. |
| Public property | [Guid](P_Grasshopper_Kernel_GH_UserObject_Guid.htm) | Gets or sets the Guid of this User Object. The Guid is created anew during construction and is not stored in the User Object File. You should never have to set this field. |
| Public property | [Icon](P_Grasshopper_Kernel_GH_UserObject_Icon.htm) | Gets or sets the icon associated with this User Object. If the icon hasn't been overridden, then a Default icon is returned. |
| Public property | [Path](P_Grasshopper_Kernel_GH_UserObject_Path.htm) | Gets or sets the file path this User Object is loaded from or saved to. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Clear](M_Grasshopper_Kernel_GH_UserObject_Clear.htm) | Destroy all data except the file path and the ID. |
| Public method | [CreateDefaultPath](M_Grasshopper_Kernel_GH_UserObject_CreateDefaultPath.htm) | Set the Path field for this user object to the default. The default file name is derived from the Description.Name field. This method also ensures the UserObject directory exists. |
| Public method | [InstantiateObject](M_Grasshopper_Kernel_GH_UserObject_InstantiateObject.htm) | Instantiate a new IGH\_DocumentObject from this User Object. |
| Public method | [ReadFromFile](M_Grasshopper_Kernel_GH_UserObject_ReadFromFile.htm) | Force an update of the local data from the file. The Path field must be set for this to work. |
| Public method | [SaveToFile](M_Grasshopper_Kernel_GH_UserObject_SaveToFile.htm) | Save the current User Object state to a file. Any existing file will be overwritten. |
| Public method | [SetDataFromObject](M_Grasshopper_Kernel_GH_UserObject_SetDataFromObject.htm) | Set the Data field content of ths UserObject from a Document object instance. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)