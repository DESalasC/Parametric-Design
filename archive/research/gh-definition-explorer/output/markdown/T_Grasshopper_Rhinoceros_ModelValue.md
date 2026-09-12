# T_Grasshopper_Rhinoceros_ModelValue

﻿ ModelValue Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros](../html/N_Grasshopper_Rhinoceros.htm "Grasshopper.Rhinoceros")

[ModelValue Class](../html/T_Grasshopper_Rhinoceros_ModelValue.htm "ModelValue Class")

[ModelValue Properties](../html/Properties_T_Grasshopper_Rhinoceros_ModelValue.htm "ModelValue Properties")

[ModelValue Methods](../html/Methods_T_Grasshopper_Rhinoceros_ModelValue.htm "ModelValue Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelValue Class |

Represents a value in a Rhino model.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTAB860EC8\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTAB860EC8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelValue  
    [More...](#fullInheritance)

**Namespace:**
 [Grasshopper.Rhinoceros](N_Grasshopper_Rhinoceros.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class ModelValue : IGH_ModelData, 
	ICloneable
```

```
Public MustInherit Class ModelValue
	Implements IGH_ModelData, ICloneable
```

AddLanguageTabSet("ID1EBCA");

The ModelValue type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Protected property | [IsValidWhyNot](P_Grasshopper_Rhinoceros_ModelValue_IsValidWhyNot.htm) |  |
| Protected property | [TypeDescription](P_Grasshopper_Rhinoceros_ModelValue_TypeDescription.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CastToAddLanguageSpecificTextSet("LSTAB860EC8\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTAB860EC8\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Rhinoceros_ModelValue_CastTo__1.htm) |  |
| Protected method | [Clone](M_Grasshopper_Rhinoceros_ModelValue_Clone.htm) |  |
| Protected method | [Read](M_Grasshopper_Rhinoceros_ModelValue_Read.htm) |  |
| Protected methodStatic member | [ReadValueAddLanguageSpecificTextSet("LSTAB860EC8\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTAB860EC8\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Rhinoceros_ModelValue_ReadValue__1.htm) |  |
| Protected method | [ScriptVariable](M_Grasshopper_Rhinoceros_ModelValue_ScriptVariable.htm) |  |
| Public method | [TooltipString](M_Grasshopper_Rhinoceros_ModelValue_TooltipString.htm) |  |
| Public method | [ToString](M_Grasshopper_Rhinoceros_ModelValue_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LSTAB860EC8\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTAB860EC8\_7?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |
| Protected method | [Write](M_Grasshopper_Rhinoceros_ModelValue_Write.htm) |  |
| Protected methodStatic member | [WriteValueAddLanguageSpecificTextSet("LSTAB860EC8\_8?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTAB860EC8\_9?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Rhinoceros_ModelValue_WriteValue__1.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Remarks

This type is the base type of a family of immutable types.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros Namespace](N_Grasshopper_Rhinoceros.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTAB860EC8\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTAB860EC8\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelValue  
    [Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LSTAB860EC8\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");ObjectDisplay](T_Grasshopper_Rhinoceros_Display_ObjectDisplay.htm)  
    [Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LSTAB860EC8\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");ObjectDisplayColor](T_Grasshopper_Rhinoceros_Display_ObjectDisplayColor.htm)  
    [Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LSTAB860EC8\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");ObjectVisibility](T_Grasshopper_Rhinoceros_Display_ObjectVisibility.htm)  
    [Grasshopper.Rhinoceros.DraftingAddLanguageSpecificTextSet("LSTAB860EC8\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelHatchLine](T_Grasshopper_Rhinoceros_Drafting_ModelHatchLine.htm)  
    [Grasshopper.Rhinoceros.DraftingAddLanguageSpecificTextSet("LSTAB860EC8\_16?cs=.|vb=.|cpp=::|nu=.|fs=.");ObjectDrafting](T_Grasshopper_Rhinoceros_Drafting_ObjectDrafting.htm)  
    [Grasshopper.Rhinoceros.DraftingAddLanguageSpecificTextSet("LSTAB860EC8\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");ObjectDraftingColor](T_Grasshopper_Rhinoceros_Drafting_ObjectDraftingColor.htm)  
    [Grasshopper.Rhinoceros.DraftingAddLanguageSpecificTextSet("LSTAB860EC8\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");ObjectDraftingLinetype](T_Grasshopper_Rhinoceros_Drafting_ObjectDraftingLinetype.htm)  
    [Grasshopper.Rhinoceros.DraftingAddLanguageSpecificTextSet("LSTAB860EC8\_19?cs=.|vb=.|cpp=::|nu=.|fs=.");ObjectDraftingLineWidth](T_Grasshopper_Rhinoceros_Drafting_ObjectDraftingLineWidth.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTAB860EC8\_20?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelMeshingParameters](T_Grasshopper_Rhinoceros_ModelMeshingParameters.htm)  
    [Grasshopper.RhinocerosAddLanguageSpecificTextSet("LSTAB860EC8\_21?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelUnitSystem](T_Grasshopper_Rhinoceros_ModelUnitSystem.htm)  
    [Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LSTAB860EC8\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");ObjectRender](T_Grasshopper_Rhinoceros_Render_ObjectRender.htm)  
    [Grasshopper.Rhinoceros.RenderAddLanguageSpecificTextSet("LSTAB860EC8\_23?cs=.|vb=.|cpp=::|nu=.|fs=.");ObjectRenderMaterial](T_Grasshopper_Rhinoceros_Render_ObjectRenderMaterial.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)