# P_Grasshopper_Folders_AssemblyFolders

﻿ Folders.AssemblyFolders Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Folders Class](../html/T_Grasshopper_Folders.htm "Folders Class")

[Folders Properties](../html/Properties_T_Grasshopper_Folders.htm "Folders Properties")

[AppDataFolder Property](../html/P_Grasshopper_Folders_AppDataFolder.htm "AppDataFolder Property ")

[AssemblyFolders Property](../html/P_Grasshopper_Folders_AssemblyFolders.htm "AssemblyFolders Property ")

[AutoSaveFolder Property](../html/P_Grasshopper_Folders_AutoSaveFolder.htm "AutoSaveFolder Property ")

[ClusterFolders Property](../html/P_Grasshopper_Folders_ClusterFolders.htm "ClusterFolders Property ")

[CursorFolder Property](../html/P_Grasshopper_Folders_CursorFolder.htm "CursorFolder Property ")

[CustomAssemblyFolders Property](../html/P_Grasshopper_Folders_CustomAssemblyFolders.htm "CustomAssemblyFolders Property ")

[DefaultAssemblyFolder Property](../html/P_Grasshopper_Folders_DefaultAssemblyFolder.htm "DefaultAssemblyFolder Property ")

[DefaultClusterFolder Property](../html/P_Grasshopper_Folders_DefaultClusterFolder.htm "DefaultClusterFolder Property ")

[DefaultTemplateFolder Property](../html/P_Grasshopper_Folders_DefaultTemplateFolder.htm "DefaultTemplateFolder Property ")

[DefaultUserObjectFolder Property](../html/P_Grasshopper_Folders_DefaultUserObjectFolder.htm "DefaultUserObjectFolder Property ")

[Desktop Property](../html/P_Grasshopper_Folders_Desktop.htm "Desktop Property ")

[DownloaderApplication Property](../html/P_Grasshopper_Folders_DownloaderApplication.htm "DownloaderApplication Property ")

[FileViewerApplication Property](../html/P_Grasshopper_Folders_FileViewerApplication.htm "FileViewerApplication Property ")

[IconFolder Property](../html/P_Grasshopper_Folders_IconFolder.htm "IconFolder Property ")

[ImageStitcherApplication Property](../html/P_Grasshopper_Folders_ImageStitcherApplication.htm "ImageStitcherApplication Property ")

[PluginFolder Property](../html/P_Grasshopper_Folders_PluginFolder.htm "PluginFolder Property ")

[SDKDownloaderApplication Property](../html/P_Grasshopper_Folders_SDKDownloaderApplication.htm "SDKDownloaderApplication Property ")

[SettingsFolder Property](../html/P_Grasshopper_Folders_SettingsFolder.htm "SettingsFolder Property ")

[TemplateFolders Property](../html/P_Grasshopper_Folders_TemplateFolders.htm "TemplateFolders Property ")

[ToolsFolder Property](../html/P_Grasshopper_Folders_ToolsFolder.htm "ToolsFolder Property ")

[TutorialFiles Property](../html/P_Grasshopper_Folders_TutorialFiles.htm "TutorialFiles Property ")

[TutorialFolder Property](../html/P_Grasshopper_Folders_TutorialFolder.htm "TutorialFolder Property ")

[UserObjectFolders Property](../html/P_Grasshopper_Folders_UserObjectFolders.htm "UserObjectFolders Property ")

[VersionHistoryFile Property](../html/P_Grasshopper_Folders_VersionHistoryFile.htm "VersionHistoryFile Property ")

[VersionHistoryUrl Property](../html/P_Grasshopper_Folders_VersionHistoryUrl.htm "VersionHistoryUrl Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| FoldersAddLanguageSpecificTextSet("LST5D4A03F5\_0?cpp=::|nu=.");AssemblyFolders Property |

Gets a list of all the directories from which GHA assemblies are loaded.
Note: this is not the same as all folders from which GHA files *were* loaded at startup.
This list includes the default Grasshopper folders, custom GHA folders and the locations
provided by Rhino.Runtime.HostUtils.GetAssemblySearchPaths().
Folders which do not contain GHA files are omitted, as are duplicate entries.

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static List<GH_AssemblyFolderInfo> AssemblyFolders { get; }
```

```
Public Shared ReadOnly Property AssemblyFolders As List(Of GH_AssemblyFolderInfo)
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST5D4A03F5\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[GH\_AssemblyFolderInfo](T_Grasshopper_Kernel_GH_AssemblyFolderInfo.htm)AddLanguageSpecificTextSet("LST5D4A03F5\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  

[Missing <value> documentation for "P:Grasshopper.Folders.AssemblyFolders"]

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST5D4A03F5\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[GH\_AssemblyFolderInfo](T_Grasshopper_Kernel_GH_AssemblyFolderInfo.htm)AddLanguageSpecificTextSet("LST5D4A03F5\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list of load target directories.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Folders Class](T_Grasshopper_Folders.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)