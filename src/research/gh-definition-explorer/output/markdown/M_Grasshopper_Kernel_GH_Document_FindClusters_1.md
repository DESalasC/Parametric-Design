# M_Grasshopper_Kernel_GH_Document_FindClusters_1

﻿ GH\_Document.FindClusters Method (String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[FindClusters Method](../html/Overload_Grasshopper_Kernel_GH_Document_FindClusters.htm "FindClusters Method ")

[FindClusters Method (Guid)](../html/M_Grasshopper_Kernel_GH_Document_FindClusters.htm "FindClusters Method (Guid)")

[FindClusters Method (String)](../html/M_Grasshopper_Kernel_GH_Document_FindClusters_1.htm "FindClusters Method (String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LST7ED85365\_0?cpp=::|nu=.");FindClusters Method (String) |

Find all the clusters that have a matching filepath.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public List<GH_Cluster> FindClusters(
	string filepath
)
```

```
Public Function FindClusters ( 
	filepath As String
) As List(Of GH_Cluster)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

filepath
:   Type: [SystemAddLanguageSpecificTextSet("LST7ED85365\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Cluster FilePath to search for.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST7ED85365\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GH\_ClusterAddLanguageSpecificTextSet("LST7ED85365\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list of all the clusters that match the filepath.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[FindClusters Overload](Overload_Grasshopper_Kernel_GH_Document_FindClusters.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)