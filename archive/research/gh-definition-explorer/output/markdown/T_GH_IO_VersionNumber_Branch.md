# T_GH_IO_VersionNumber_Branch

﻿ VersionNumber.Branch Enumeration

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO](../html/N_GH_IO.htm "GH_IO")

[GH\_ISerializable Interface](../html/T_GH_IO_GH_ISerializable.htm "GH_ISerializable Interface")

[VersionNumber Structure](../html/T_GH_IO_VersionNumber.htm "VersionNumber Structure")

[VersionNumber.Branch Enumeration](../html/T_GH_IO_VersionNumber_Branch.htm "VersionNumber.Branch Enumeration")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| VersionNumberAddLanguageSpecificTextSet("LSTB6853C38\_0?cpp=::|nu=.");Branch Enumeration |

Build branch, set by the build process.

**Namespace:**
 [GH\_IO](N_GH_IO.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public enum Branch
```

```
Public Enumeration Branch
```

AddLanguageTabSet("ID0EBCA");

![](../icons/SectionExpanded.png)Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | Unset | 0 | Uninitialized value. |
|  | Developer | 1 | Private developer build; should never be released to the public. |
|  | Trunk | 2 | Mainline trunk build. May be released to the public. |
|  | ReleaseCandidate | 3 | Release candidate build. Will be released to the public. |
|  | Release | 4 | Final Release build. Will be released to the public. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IO Namespace](N_GH_IO.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)