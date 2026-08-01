# T_Grasshopper_Kernel_GH_ComponentServer

﻿ GH\_ComponentServer Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentServer Class](../html/T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Class")

[GH\_ComponentServer Constructor](../html/M_Grasshopper_Kernel_GH_ComponentServer__ctor.htm "GH_ComponentServer Constructor ")

[GH\_ComponentServer Properties](../html/Properties_T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Properties")

[GH\_ComponentServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Methods")

[GH\_ComponentServer Events](../html/Events_T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentServer Class |

Maintains proxies for all components, parameters and other object types as defined in all grasshopper assemblies.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST727F2FA5\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST727F2FA5\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ComponentServer

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_ComponentServer
```

```
Public NotInheritable Class GH_ComponentServer
```

AddLanguageTabSet("ID1EBCA");

The GH\_ComponentServer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ComponentServer](M_Grasshopper_Kernel_GH_ComponentServer__ctor.htm) | Initializes a new instance of the GH\_ComponentServer class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Aliases](P_Grasshopper_Kernel_GH_ComponentServer_Aliases.htm) | Gets a list of all the defined aliases. |
| Public property | [CompleteRibbonLayout](P_Grasshopper_Kernel_GH_ComponentServer_CompleteRibbonLayout.htm) | Gets the default component layout featuring all non-hidden components and parameters. |
| Public property | [DiscardedProxies](P_Grasshopper_Kernel_GH_ComponentServer_DiscardedProxies.htm) | Returns the total number of IGH\_DocumentObjects that were discarded during assembly parsing. This includes both skipped and replaced proxies. |
| Public property | [GraphProxies](P_Grasshopper_Kernel_GH_ComponentServer_GraphProxies.htm) | Returns a list of all cached GH\_GraphProxy instances. |
| Public property | [IsLoading](P_Grasshopper_Kernel_GH_ComponentServer_IsLoading.htm) | Gets whether the component server is currently executing its external-file load pass. True from entry to LoadExternalFiles until it returns. |
| Public property | [Libraries](P_Grasshopper_Kernel_GH_ComponentServer_Libraries.htm) | Returns a list of Assembly Info objects describing all loaded assemblies. |
| Public property | [LoadingExceptions](P_Grasshopper_Kernel_GH_ComponentServer_LoadingExceptions.htm) | Gets a list of all the exceptions that were recorded during the most recent loading sequence. |
| Public propertyStatic member | [NoLoadExtension](P_Grasshopper_Kernel_GH_ComponentServer_NoLoadExtension.htm) |  |
| Public property | [ObjectProxies](P_Grasshopper_Kernel_GH_ComponentServer_ObjectProxies.htm) | Returns a list of all cached GH\_ObjectProxy instances. |
| Public property | [ObjectProxyNames](P_Grasshopper_Kernel_GH_ComponentServer_ObjectProxyNames.htm) | Returns a specialized string collection of all component names. |
| Public property | [TypeHints](P_Grasshopper_Kernel_GH_ComponentServer_TypeHints.htm) | Gets a list of all IGH\_TypeHint types in all loaded assemblies. |
| Public property | [Upgraders](P_Grasshopper_Kernel_GH_ComponentServer_Upgraders.htm) | Gets a list of all the upgraders that have been cached. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddAlias](M_Grasshopper_Kernel_GH_ComponentServer_AddAlias.htm) | Add an alias to a target. |
| Public method | [AddCategoryIcon](M_Grasshopper_Kernel_GH_ComponentServer_AddCategoryIcon.htm) | Add an icon for a tab category. 16x16 images are required. |
| Public method | [AddCategoryShortName](M_Grasshopper_Kernel_GH_ComponentServer_AddCategoryShortName.htm) | Add an abbreviation for a tab category. 2~4 letter abbreviations are best. |
| Public method | [AddCategorySymbolName](M_Grasshopper_Kernel_GH_ComponentServer_AddCategorySymbolName.htm) | Add a single char category description. |
| Public method | [AliasTargets](M_Grasshopper_Kernel_GH_ComponentServer_AliasTargets.htm) | Get all the target Component IDs for a given alias. |
| Public method | [Clear](M_Grasshopper_Kernel_GH_ComponentServer_Clear.htm) | Clear all caches. |
| Public method | [ClearStaleUserObjects](M_Grasshopper_Kernel_GH_ComponentServer_ClearStaleUserObjects.htm) | Remove all user objects that no longer point to existing files. |
| Public methodStatic member | [CompareProxies](M_Grasshopper_Kernel_GH_ComponentServer_CompareProxies.htm) | Compare two object proxies. Names and exposures are taken into account. |
| Public methodStatic member | [CopyFileToAppropriateFolder](M_Grasshopper_Kernel_GH_ComponentServer_CopyFileToAppropriateFolder.htm) | Copy a GHA or GHUSER file into the appropriate Roaming Application Data folder. Of the file is already in the top-level roaming folder it will not be copied. |
| Public method | [CreateComponentPalette](M_Grasshopper_Kernel_GH_ComponentServer_CreateComponentPalette.htm) |  |
| Public method | [DestroyLoadingUI](M_Grasshopper_Kernel_GH_ComponentServer_DestroyLoadingUI.htm) | Destroy the loading UI (the banner and the progress bar). |
| Public method | [EmitGraph](M_Grasshopper_Kernel_GH_ComponentServer_EmitGraph.htm) | Create a new instance of the IGH\_Graph that matches the id. If no proxy can be matched to the id, a null reference will be returned. |
| Public method | [EmitObject](M_Grasshopper_Kernel_GH_ComponentServer_EmitObject.htm) | Create a new instance of the IGH\_DocumentObject that matches the id. If no proxy can be matched to the id, a null reference will be returned. |
| Public method | [EmitObjectIcon](M_Grasshopper_Kernel_GH_ComponentServer_EmitObjectIcon.htm) | Get the icon that is associated with the given Object ID. |
| Public method | [EmitObjectProxy](M_Grasshopper_Kernel_GH_ComponentServer_EmitObjectProxy.htm) | Get the proxy that is associated with the given Object ID. |
| Public methodStatic member | [ExternalFiles](M_Grasshopper_Kernel_GH_ComponentServer_ExternalFiles.htm) | Get lists of all the external files (GHA, GHUSER and GHCLUSTER) that will be loaded by Grasshopper. Note: this does not equal the files that may already have been loaded, just the files that we'll attempt to load if we were asked to load all plugins now. The list contains no duplicate file paths, but it may contain identical files which won't be filtered until actual loading. |
| Public method | [FindAssembly](M_Grasshopper_Kernel_GH_ComponentServer_FindAssembly.htm) | Gets the assembly that corresponds to the given library ID. |
| Public method | [FindAssemblyByObject(Guid)](M_Grasshopper_Kernel_GH_ComponentServer_FindAssemblyByObject_1.htm) | Gets the assembly that corresponds to the given library ID. |
| Public method | [FindAssemblyByObject(IGH\_DocumentObject)](M_Grasshopper_Kernel_GH_ComponentServer_FindAssemblyByObject.htm) | Gets the assembly that corresponds to the given library ID. |
| Public method | [FindObjectByName](M_Grasshopper_Kernel_GH_ComponentServer_FindObjectByName.htm) | Find an object by name. Obsolete and hidden objects are ignored. Only exact matches are included. |
| Public method | [FindObjects(Guid)](M_Grasshopper_Kernel_GH_ComponentServer_FindObjects.htm) | Find all the objects that are part of a certain library. |
| Public method | [FindObjects(AddLanguageSpecificTextSet("LST727F2FA5\_2?cpp=array&lt;");StringAddLanguageSpecificTextSet("LST727F2FA5\_3?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, Int32, AddLanguageSpecificTextSet("LST727F2FA5\_4?cpp=array&lt;");IGH\_ObjectProxyAddLanguageSpecificTextSet("LST727F2FA5\_5?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");AddLanguageSpecificTextSet("LST727F2FA5\_6?cpp=%");, AddLanguageSpecificTextSet("LST727F2FA5\_7?cpp=array&lt;");DoubleAddLanguageSpecificTextSet("LST727F2FA5\_8?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");AddLanguageSpecificTextSet("LST727F2FA5\_9?cpp=%");)](M_Grasshopper_Kernel_GH_ComponentServer_FindObjects_1.htm) | Searches the list of cached object proxies for objects that might be implied by a search term. |
| Public method | [FindUpgrader](M_Grasshopper_Kernel_GH_ComponentServer_FindUpgrader.htm) | Find the upgrader that can convert from the given target. |
| Public method | [GetAlias](M_Grasshopper_Kernel_GH_ComponentServer_GetAlias.htm) | Gets the alias display string for a given object. |
| Public method | [GetCategoryIcon](M_Grasshopper_Kernel_GH_ComponentServer_GetCategoryIcon.htm) | Get the icon for a specific category. If the icon hasn't been defined, this method will return the default icon. |
| Public method | [GetCategoryShortName](M_Grasshopper_Kernel_GH_ComponentServer_GetCategoryShortName.htm) | Get the abbreviation (short name) for a specific category. If the short name hasn't been defined, this method will return the full name instead. |
| Public method | [GetCategorySymbolName](M_Grasshopper_Kernel_GH_ComponentServer_GetCategorySymbolName.htm) | Get the single char representation for a specific category. If the char hasn't been defined, this method will return the first char of the full name instead. |
| Public method | [IsGraphCached](M_Grasshopper_Kernel_GH_ComponentServer_IsGraphCached.htm) | Tests the graph cache for an existing graph type ID. |
| Public method | [IsObjectCached](M_Grasshopper_Kernel_GH_ComponentServer_IsObjectCached.htm) | Tests the caches for an existing object type ID. |
| Public method | [IsUpgrader](M_Grasshopper_Kernel_GH_ComponentServer_IsUpgrader.htm) | Checks to see if at least one upgrader is defined for a collection of objects. |
| Public method | [LoadAliases](M_Grasshopper_Kernel_GH_ComponentServer_LoadAliases.htm) | Load the Alias table from the settings directory. Only use this function if you suspect the alias table settings file has changed due to some external process. |
| Public methodStatic member | [NewUserObject](M_Grasshopper_Kernel_GH_ComponentServer_NewUserObject.htm) | Create a new UserObject and write it to the Grasshopper User Object folder. |
| Public method | [RemoveCachedGraph](M_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedGraph.htm) | Remove a cache entry from the graph cache. This cannot be undone. |
| Public method | [RemoveCachedObject(Guid)](M_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedObject.htm) | Remove a cache entry from the object cache. This cannot be undone. |
| Public method | [RemoveCachedObject(String)](M_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedObject_1.htm) | Remove the user object (if any) that loads itself from a specified \*.ghuser file. |
| Public method | [SaveAliases](M_Grasshopper_Kernel_GH_ComponentServer_SaveAliases.htm) | Save the alias table to the settings directory. Use this function if you change the alias table while ignoring usual channels. |
| Public method | [SetAlias](M_Grasshopper_Kernel_GH_ComponentServer_SetAlias.htm) | Sets the aliases for a given target. |
| Public methodStatic member | [UpdateRibbonUI](M_Grasshopper_Kernel_GH_ComponentServer_UpdateRibbonUI.htm) | Forces an update of the Ribbon control on the Grasshopper main form. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [GHAFileLoaded](E_Grasshopper_Kernel_GH_ComponentServer_GHAFileLoaded.htm) | Raised whenever a GHA file has been successfully loaded. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)