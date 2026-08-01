# T_Grasshopper_Documentation_GH_GlossaryItem

﻿ GH\_GlossaryItem Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Documentation](../html/N_Grasshopper_Documentation.htm "Grasshopper.Documentation")

[GH\_GlossaryItem Class](../html/T_Grasshopper_Documentation_GH_GlossaryItem.htm "GH_GlossaryItem Class")

[GH\_GlossaryItem Properties](../html/Properties_T_Grasshopper_Documentation_GH_GlossaryItem.htm "GH_GlossaryItem Properties")

[GH\_GlossaryItem Methods](../html/Methods_T_Grasshopper_Documentation_GH_GlossaryItem.htm "GH_GlossaryItem Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GlossaryItem Class |

Represents a single glossary entry in the Grasshopper help.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTA04FE125\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.DocumentationAddLanguageSpecificTextSet("LSTA04FE125\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GlossaryItem

**Namespace:**
 [Grasshopper.Documentation](N_Grasshopper_Documentation.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_GlossaryItem
```

```
Public Class GH_GlossaryItem
```

AddLanguageTabSet("ID1EBCA");

The GH\_GlossaryItem type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Author](P_Grasshopper_Documentation_GH_GlossaryItem_Author.htm) | Gets the author of this glossary entry. This field is optional and may not be defined. |
| Public property | [Contact](P_Grasshopper_Documentation_GH_GlossaryItem_Contact.htm) | Gets the contact information for the glossary entry author. This field is optional and may not be defined. |
| Public property | [Descriptions](P_Grasshopper_Documentation_GH_GlossaryItem_Descriptions.htm) | Gets the description (definition) for this glossary entry. |
| Public property | [Path](P_Grasshopper_Documentation_GH_GlossaryItem_Path.htm) | Gets the source file for this glossary entry. |
| Public property | [Pronunciation](P_Grasshopper_Documentation_GH_GlossaryItem_Pronunciation.htm) | Gets the pronunciation guide to the word. This field is optional and may not be defined. |
| Public property | [Synonyms](P_Grasshopper_Documentation_GH_GlossaryItem_Synonyms.htm) | Gets the synonyms for this glossary entry. |
| Public property | [Word](P_Grasshopper_Documentation_GH_GlossaryItem_Word.htm) | Gets the word this glossary entry is about. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [ParseFile](M_Grasshopper_Documentation_GH_GlossaryItem_ParseFile.htm) | Parse a \*.glossary file and return a glossary entry. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)