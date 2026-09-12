# T_Grasshopper_Documentation_GH_Link

﻿ GH\_Link Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Documentation](../html/N_Grasshopper_Documentation.htm "Grasshopper.Documentation")

[GH\_Link Class](../html/T_Grasshopper_Documentation_GH_Link.htm "GH_Link Class")

[GH\_Link Properties](../html/Properties_T_Grasshopper_Documentation_GH_Link.htm "GH_Link Properties")

[GH\_Link Methods](../html/Methods_T_Grasshopper_Documentation_GH_Link.htm "GH_Link Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Link Class |

Represents a link to another location in the Help or some external address.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST342537CB\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.DocumentationAddLanguageSpecificTextSet("LST342537CB\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Link

**Namespace:**
 [Grasshopper.Documentation](N_Grasshopper_Documentation.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Link : IGH_Content
```

```
Public Class GH_Link
	Implements IGH_Content
```

AddLanguageTabSet("ID1EBCA");

The GH\_Link type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Destination](P_Grasshopper_Documentation_GH_Link_Destination.htm) | Gets the link target. |
| Public property | [IsSharedLink](P_Grasshopper_Documentation_GH_Link_IsSharedLink.htm) | Gets whether this link is a shared link. A shared link should not have text but it should have a non-empty LinkId. |
| Public property | [LinkId](P_Grasshopper_Documentation_GH_Link_LinkId.htm) | Gets the link ID. The link ID is only used for shared links. |
| Public property | [Target](P_Grasshopper_Documentation_GH_Link_Target.htm) | Gets the link type. |
| Public property | [Text](P_Grasshopper_Documentation_GH_Link_Text.htm) | Gets the list text. |
| Public property | [Tooltip](P_Grasshopper_Documentation_GH_Link_Tooltip.htm) | Gets the link tooltip text. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [CreateExternalLink(String, String)](M_Grasshopper_Documentation_GH_Link_CreateExternalLink.htm) |  |
| Public methodStatic member | [CreateExternalLink(String, String, String)](M_Grasshopper_Documentation_GH_Link_CreateExternalLink_1.htm) |  |
| Public methodStatic member | [CreateGlossaryLink(String)](M_Grasshopper_Documentation_GH_Link_CreateGlossaryLink.htm) |  |
| Public methodStatic member | [CreateGlossaryLink(String, String)](M_Grasshopper_Documentation_GH_Link_CreateGlossaryLink_1.htm) |  |
| Public methodStatic member | [CreateSharedLink(String, String)](M_Grasshopper_Documentation_GH_Link_CreateSharedLink.htm) |  |
| Public methodStatic member | [CreateSharedLink(String, String, String)](M_Grasshopper_Documentation_GH_Link_CreateSharedLink_1.htm) |  |
| Public methodStatic member | [CreateTopicLink(String, String)](M_Grasshopper_Documentation_GH_Link_CreateTopicLink.htm) |  |
| Public methodStatic member | [CreateTopicLink(String, String, String)](M_Grasshopper_Documentation_GH_Link_CreateTopicLink_1.htm) |  |
| Public method | [ToString](M_Grasshopper_Documentation_GH_Link_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST342537CB\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST342537CB\_3?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)