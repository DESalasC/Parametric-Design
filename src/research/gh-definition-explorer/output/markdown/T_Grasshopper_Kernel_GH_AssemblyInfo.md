# T_Grasshopper_Kernel_GH_AssemblyInfo

﻿ GH\_AssemblyInfo Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_AssemblyInfo Class](../html/T_Grasshopper_Kernel_GH_AssemblyInfo.htm "GH_AssemblyInfo Class")

[GH\_AssemblyInfo Constructor](../html/M_Grasshopper_Kernel_GH_AssemblyInfo__ctor.htm "GH_AssemblyInfo Constructor ")

[GH\_AssemblyInfo Properties](../html/Properties_T_Grasshopper_Kernel_GH_AssemblyInfo.htm "GH_AssemblyInfo Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AssemblyInfo Class |

Implement this interface once (and once only) in a GHA project if you wish to
add additional information about your library to Grasshopper. Note you must supply
an empty constructor.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTC57534B1\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTC57534B1\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AssemblyInfo  
    [Grasshopper.KernelAddLanguageSpecificTextSet("LSTC57534B1\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AssemblyInfoStub](T_Grasshopper_Kernel_GH_AssemblyInfoStub.htm)

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_AssemblyInfo
```

```
Public MustInherit Class GH_AssemblyInfo
```

AddLanguageTabSet("ID1EBCA");

The GH\_AssemblyInfo type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_AssemblyInfo](M_Grasshopper_Kernel_GH_AssemblyInfo__ctor.htm) | Initializes a new instance of the GH\_AssemblyInfo class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Assembly](P_Grasshopper_Kernel_GH_AssemblyInfo_Assembly.htm) | Gets the actual assembly that this info object describes. |
| Public property | [AuthorContact](P_Grasshopper_Kernel_GH_AssemblyInfo_AuthorContact.htm) | Gets the contact information for the author. This can be email, phone, fax, address or all of the above. Return null if you do not wish to associate contact details with this assembly. |
| Public property | [AuthorName](P_Grasshopper_Kernel_GH_AssemblyInfo_AuthorName.htm) | Gets the name of the individual/company/organisation that is responsible for this assembly. Return null if you do not wish to associate an author with this assembly. |
| Public property | [Description](P_Grasshopper_Kernel_GH_AssemblyInfo_Description.htm) | Gets the human readable description of this assembly. Return null if you do not wish to associate a description with this assembly. |
| Public property | [Icon](P_Grasshopper_Kernel_GH_AssemblyInfo_Icon.htm) | Gets a 24x24 icon that represents this assembly. Return null if you do not wish to associate an icon with this assembly. |
| Public property | [Id](P_Grasshopper_Kernel_GH_AssemblyInfo_Id.htm) | Gets the Id of this assembly. By default the Id is a hash of the name. |
| Public property | [IsCoreLibrary](P_Grasshopper_Kernel_GH_AssemblyInfo_IsCoreLibrary.htm) | Gets whether this library is a Grasshopper core library. Core libraries are installed along with Grasshopper and thus should always be available anywhere. |
| Public property | [License](P_Grasshopper_Kernel_GH_AssemblyInfo_License.htm) | Gets the license type for this assembly. |
| Public property | [LoadingMechanism](P_Grasshopper_Kernel_GH_AssemblyInfo_LoadingMechanism.htm) | Gets the mechanism used to load this assembly. |
| Public property | [Location](P_Grasshopper_Kernel_GH_AssemblyInfo_Location.htm) | Gets the location this assembly was loaded from. |
| Public property | [Name](P_Grasshopper_Kernel_GH_AssemblyInfo_Name.htm) | Gets the human readable name of this assembly. Return null if you do not wish to associate a name with this assembly. |
| Public property | [Version](P_Grasshopper_Kernel_GH_AssemblyInfo_Version.htm) | Gets the version code for this assembly. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)