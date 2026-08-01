# T_Grasshopper_Folders

﻿ Folders Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Folders Class](../html/T_Grasshopper_Folders.htm "Folders Class")

[Folders Properties](../html/Properties_T_Grasshopper_Folders.htm "Folders Properties")

[Folders Methods](../html/Methods_T_Grasshopper_Folders.htm "Folders Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Folders Class |

Provides access to all standard Grasshopper file and folder locations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST924B87BD\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  GrasshopperAddLanguageSpecificTextSet("LST924B87BD\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Folders

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class Folders
```

```
Public NotInheritable Class Folders
```

AddLanguageTabSet("ID1EBCA");

The Folders type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public propertyStatic member | [AppDataFolder](P_Grasshopper_Folders_AppDataFolder.htm) | Gets the appdata folder for Grasshopper. |
| Public propertyStatic member | [AssemblyFolders](P_Grasshopper_Folders_AssemblyFolders.htm) | Gets a list of all the directories from which GHA assemblies are loaded. Note: this is not the same as all folders from which GHA files *were* loaded at startup. This list includes the default Grasshopper folders, custom GHA folders and the locations provided by Rhino.Runtime.HostUtils.GetAssemblySearchPaths(). Folders which do not contain GHA files are omitted, as are duplicate entries. |
| Public propertyStatic member | [AutoSaveFolder](P_Grasshopper_Folders_AutoSaveFolder.htm) | Gets the directory in windows ApplicationData that contains the Grasshopper autosave files. |
| Public propertyStatic member | [ClusterFolders](P_Grasshopper_Folders_ClusterFolders.htm) | Gets a list of all the directories from which GHCLUSTER files are loaded. GHUSER files are loaded from subfolders as well. |
| Public propertyStatic member | [CursorFolder](P_Grasshopper_Folders_CursorFolder.htm) | Gets the directory that contains the cursor files that ship with Grasshopper. |
| Public propertyStatic member | [CustomAssemblyFolders](P_Grasshopper_Folders_CustomAssemblyFolders.htm) | Gets or sets all custom assembly folders. |
| Public propertyStatic member | [DefaultAssemblyFolder](P_Grasshopper_Folders_DefaultAssemblyFolder.htm) | Gets the standard directory in windows ApplicationData that contains 3rd party GHA files. |
| Public propertyStatic member | [DefaultClusterFolder](P_Grasshopper_Folders_DefaultClusterFolder.htm) | Gets the standard directory in windows ApplicationData that contains GHCLUSTER files. |
| Public propertyStatic member | [DefaultTemplateFolder](P_Grasshopper_Folders_DefaultTemplateFolder.htm) | Gets the standard directory in windows ApplicationData that contains template files. |
| Public propertyStatic member | [DefaultUserObjectFolder](P_Grasshopper_Folders_DefaultUserObjectFolder.htm) | Gets the standard directory in windows ApplicationData that contains GHUSER files. |
| Public propertyStatic member | [Desktop](P_Grasshopper_Folders_Desktop.htm) | Gets the desktop directory of the current user profile. |
| Public propertyStatic member | [DownloaderApplication](P_Grasshopper_Folders_DownloaderApplication.htm) | Gets the location where the Downloader.exe should be. If the application is not present, null is returned. |
| Public propertyStatic member | [FileViewerApplication](P_Grasshopper_Folders_FileViewerApplication.htm) | Gets the location where the FileViewer.exe should be. If the application is not present, null is returned. |
| Public propertyStatic member | [IconFolder](P_Grasshopper_Folders_IconFolder.htm) | Gets the directory that contains the icon files that ship with Grasshopper. |
| Public propertyStatic member | [ImageStitcherApplication](P_Grasshopper_Folders_ImageStitcherApplication.htm) | Gets the location where the ImageStitcher.exe should be. If the application is not present, null is returned. |
| Public propertyStatic member | [PluginFolder](P_Grasshopper_Folders_PluginFolder.htm) | Gets the directory that contains the Grasshopper.dll file. |
| Public propertyStatic member | [SDKDownloaderApplication](P_Grasshopper_Folders_SDKDownloaderApplication.htm) | Gets the location where the SDKDownloader.exe should be. If the application is not present, null is returned. |
| Public propertyStatic member | [SettingsFolder](P_Grasshopper_Folders_SettingsFolder.htm) | Gets the folder into which all Grasshopper settings are stored. This folder might not exist until some settings are actually saved. |
| Public propertyStatic member | [TemplateFolders](P_Grasshopper_Folders_TemplateFolders.htm) | Gets a list of all the directories from which template files are loaded. Templates are not loaded from subfolders. |
| Public propertyStatic member | [ToolsFolder](P_Grasshopper_Folders_ToolsFolder.htm) | **Obsolete.**  Gets the directory that contains the additional executables that ship with Grasshopper. |
| Public propertyStatic member | [TutorialFiles](P_Grasshopper_Folders_TutorialFiles.htm) | Gets an array of all the tutorial files. This includes all the files with the \*.gh or \*.ghx extension in the Tutorials folder. Subfolders are not traversed. |
| Public propertyStatic member | [TutorialFolder](P_Grasshopper_Folders_TutorialFolder.htm) | Gets the directory that contains the tutorial files that ship with Grasshopper. |
| Public propertyStatic member | [UserObjectFolders](P_Grasshopper_Folders_UserObjectFolders.htm) | Gets a list of all the directories from which GHUSER files are loaded. GHUSER files are loaded from subfolders as well. |
| Public propertyStatic member | [VersionHistoryFile](P_Grasshopper_Folders_VersionHistoryFile.htm) | Gets the text file location where Grasshopper will save the latest version information. |
| Public propertyStatic member | [VersionHistoryUrl](P_Grasshopper_Folders_VersionHistoryUrl.htm) | Gets the url of the version history data. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [ShowFolderInExplorer](M_Grasshopper_Folders_ShowFolderInExplorer.htm) | Open a specific folder in Windows Explorer. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)