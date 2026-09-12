# M_Grasshopper_Kernel_GH_ComponentServer_GetCategoryShortName

﻿ GH\_ComponentServer.GetCategoryShortName Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentServer Class](../html/T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Class")

[GH\_ComponentServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Methods")

[AddAlias Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_AddAlias.htm "AddAlias Method ")

[AddCategoryIcon Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_AddCategoryIcon.htm "AddCategoryIcon Method ")

[AddCategoryShortName Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_AddCategoryShortName.htm "AddCategoryShortName Method ")

[AddCategorySymbolName Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_AddCategorySymbolName.htm "AddCategorySymbolName Method ")

[AliasTargets Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_AliasTargets.htm "AliasTargets Method ")

[Clear Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_Clear.htm "Clear Method ")

[ClearStaleUserObjects Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_ClearStaleUserObjects.htm "ClearStaleUserObjects Method ")

[CompareProxies Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_CompareProxies.htm "CompareProxies Method ")

[CopyFileToAppropriateFolder Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_CopyFileToAppropriateFolder.htm "CopyFileToAppropriateFolder Method ")

[CreateComponentPalette Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_CreateComponentPalette.htm "CreateComponentPalette Method ")

[DestroyLoadingUI Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_DestroyLoadingUI.htm "DestroyLoadingUI Method ")

[EmitGraph Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_EmitGraph.htm "EmitGraph Method ")

[EmitObject Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_EmitObject.htm "EmitObject Method ")

[EmitObjectIcon Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_EmitObjectIcon.htm "EmitObjectIcon Method ")

[EmitObjectProxy Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_EmitObjectProxy.htm "EmitObjectProxy Method ")

[ExternalFiles Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_ExternalFiles.htm "ExternalFiles Method ")

[FindAssembly Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_FindAssembly.htm "FindAssembly Method ")

[FindAssemblyByObject Method](../html/Overload_Grasshopper_Kernel_GH_ComponentServer_FindAssemblyByObject.htm "FindAssemblyByObject Method ")

[FindObjectByName Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_FindObjectByName.htm "FindObjectByName Method ")

[FindObjects Method](../html/Overload_Grasshopper_Kernel_GH_ComponentServer_FindObjects.htm "FindObjects Method ")

[FindUpgrader Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_FindUpgrader.htm "FindUpgrader Method ")

[GetAlias Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_GetAlias.htm "GetAlias Method ")

[GetCategoryIcon Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_GetCategoryIcon.htm "GetCategoryIcon Method ")

[GetCategoryShortName Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_GetCategoryShortName.htm "GetCategoryShortName Method ")

[GetCategorySymbolName Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_GetCategorySymbolName.htm "GetCategorySymbolName Method ")

[IsGraphCached Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_IsGraphCached.htm "IsGraphCached Method ")

[IsObjectCached Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_IsObjectCached.htm "IsObjectCached Method ")

[IsUpgrader Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_IsUpgrader.htm "IsUpgrader Method ")

[LoadAliases Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_LoadAliases.htm "LoadAliases Method ")

[NewUserObject Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_NewUserObject.htm "NewUserObject Method ")

[RemoveCachedGraph Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedGraph.htm "RemoveCachedGraph Method ")

[RemoveCachedObject Method](../html/Overload_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedObject.htm "RemoveCachedObject Method ")

[SaveAliases Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_SaveAliases.htm "SaveAliases Method ")

[SetAlias Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_SetAlias.htm "SetAlias Method ")

[UpdateRibbonUI Method](../html/M_Grasshopper_Kernel_GH_ComponentServer_UpdateRibbonUI.htm "UpdateRibbonUI Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentServerAddLanguageSpecificTextSet("LST482C8DC9\_0?cpp=::|nu=.");GetCategoryShortName Method |

Get the abbreviation (short name) for a specific category. If the short name hasn't been defined,
this method will return the full name instead.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public string GetCategoryShortName(
	string fullName
)
```

```
Public Function GetCategoryShortName ( 
	fullName As String
) As String
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

fullName
:   Type: [SystemAddLanguageSpecificTextSet("LST482C8DC9\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Full name of category.

#### Return Value

Type: [String](https://docs.microsoft.com/dotnet/api/system.string)  
The abbreviated name or the full name.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentServer Class](T_Grasshopper_Kernel_GH_ComponentServer.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)