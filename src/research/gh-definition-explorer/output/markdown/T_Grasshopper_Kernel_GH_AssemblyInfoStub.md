# T_Grasshopper_Kernel_GH_AssemblyInfoStub

﻿ GH\_AssemblyInfoStub Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_AssemblyInfoStub Class](../html/T_Grasshopper_Kernel_GH_AssemblyInfoStub.htm "GH_AssemblyInfoStub Class")

[GH\_AssemblyInfoStub Constructor](../html/M_Grasshopper_Kernel_GH_AssemblyInfoStub__ctor.htm "GH_AssemblyInfoStub Constructor ")

[GH\_AssemblyInfoStub Properties](../html/Properties_T_Grasshopper_Kernel_GH_AssemblyInfoStub.htm "GH_AssemblyInfoStub Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AssemblyInfoStub Class |

Provides basic properties for a GHA assembly that does not expose a type that derives from GH\_AssemblyInfo.
This type is created automatically when a GH\_AssemblyInfo type is not found in an assembly.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTBE9E3B4E\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.KernelAddLanguageSpecificTextSet("LSTBE9E3B4E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LSTBE9E3B4E\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AssemblyInfoStub

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_AssemblyInfoStub : GH_AssemblyInfo
```

```
Public NotInheritable Class GH_AssemblyInfoStub
	Inherits GH_AssemblyInfo
```

AddLanguageTabSet("ID1EBCA");

The GH\_AssemblyInfoStub type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_AssemblyInfoStub](M_Grasshopper_Kernel_GH_AssemblyInfoStub__ctor.htm) | Initializes a new instance of the GH\_AssemblyInfoStub class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Assembly](P_Grasshopper_Kernel_GH_AssemblyInfo_Assembly.htm) | Gets the actual assembly that this info object describes. (Inherited from [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm).) |
| Public property | [AssemblyName](P_Grasshopper_Kernel_GH_AssemblyInfoStub_AssemblyName.htm) | (Overrides GH\_AssemblyInfo.AssemblyName.) |
| Public property | [AssemblyVersion](P_Grasshopper_Kernel_GH_AssemblyInfoStub_AssemblyVersion.htm) | (Overrides GH\_AssemblyInfo.AssemblyVersion.) |
| Public property | [AuthorContact](P_Grasshopper_Kernel_GH_AssemblyInfo_AuthorContact.htm) | Gets the contact information for the author. This can be email, phone, fax, address or all of the above. Return null if you do not wish to associate contact details with this assembly. (Inherited from [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm).) |
| Public property | [AuthorName](P_Grasshopper_Kernel_GH_AssemblyInfo_AuthorName.htm) | Gets the name of the individual/company/organisation that is responsible for this assembly. Return null if you do not wish to associate an author with this assembly. (Inherited from [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm).) |
| Public property | [Description](P_Grasshopper_Kernel_GH_AssemblyInfo_Description.htm) | Gets the human readable description of this assembly. Return null if you do not wish to associate a description with this assembly. (Inherited from [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm).) |
| Public property | [Icon](P_Grasshopper_Kernel_GH_AssemblyInfo_Icon.htm) | Gets a 24x24 icon that represents this assembly. Return null if you do not wish to associate an icon with this assembly. (Inherited from [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm).) |
| Public property | [Id](P_Grasshopper_Kernel_GH_AssemblyInfo_Id.htm) | Gets the Id of this assembly. By default the Id is a hash of the name. (Inherited from [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm).) |
| Public property | [IsCoreLibrary](P_Grasshopper_Kernel_GH_AssemblyInfo_IsCoreLibrary.htm) | Gets whether this library is a Grasshopper core library. Core libraries are installed along with Grasshopper and thus should always be available anywhere. (Inherited from [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm).) |
| Public property | [License](P_Grasshopper_Kernel_GH_AssemblyInfo_License.htm) | Gets the license type for this assembly. (Inherited from [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm).) |
| Public property | [LoadingMechanism](P_Grasshopper_Kernel_GH_AssemblyInfo_LoadingMechanism.htm) | Gets the mechanism used to load this assembly. (Inherited from [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm).) |
| Public property | [Location](P_Grasshopper_Kernel_GH_AssemblyInfo_Location.htm) | Gets the location this assembly was loaded from. (Inherited from [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm).) |
| Public property | [Name](P_Grasshopper_Kernel_GH_AssemblyInfo_Name.htm) | Gets the human readable name of this assembly. Return null if you do not wish to associate a name with this assembly. (Inherited from [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm).) |
| Public property | [Version](P_Grasshopper_Kernel_GH_AssemblyInfo_Version.htm) | Gets the version code for this assembly. (Inherited from [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)