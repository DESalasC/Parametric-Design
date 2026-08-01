# T_Grasshopper_Rhinoceros_Display_ModelView

﻿ ModelView Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Display](../html/N_Grasshopper_Rhinoceros_Display.htm "Grasshopper.Rhinoceros.Display")

[ModelView Class](../html/T_Grasshopper_Rhinoceros_Display_ModelView.htm "ModelView Class")

[ModelView Constructor](../html/Overload_Grasshopper_Rhinoceros_Display_ModelView__ctor.htm "ModelView Constructor ")

[ModelView Properties](../html/Properties_T_Grasshopper_Rhinoceros_Display_ModelView.htm "ModelView Properties")

[ModelView Methods](../html/Methods_T_Grasshopper_Rhinoceros_Display_ModelView.htm "ModelView Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelView Class |

Represents a 3D view frustum. Wraps the functionality of the ViewportInfo type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST3AD63C0C\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Rhinoceros.DisplayAddLanguageSpecificTextSet("LST3AD63C0C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ModelView

**Namespace:**
 [Grasshopper.Rhinoceros.Display](N_Grasshopper_Rhinoceros_Display.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class ModelView : IGH_GeometricGoo, 
	IEquatable<ModelView>, IGH_PreviewData, IGH_BakeAwareData
```

```
Public NotInheritable Class ModelView
	Implements IGH_GeometricGoo, IEquatable(Of ModelView), 
	IGH_PreviewData, IGH_BakeAwareData
```

AddLanguageTabSet("ID1EBCA");

The ModelView type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ModelViewAddLanguageSpecificTextSet("LST3AD63C0C\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Rhinoceros_Display_ModelView__ctor.htm) | Initializes a new instance of the ModelView class |
| Public method | [ModelView(Guid)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_7.htm) | Create a new referenced view that references a RhinoView or NamedView object with the specified ref\_guid. |
| Public method | [ModelView(ModelView)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_1.htm) | Initializes a new instance of the ModelView class |
| Public method | [ModelView(RhinoView)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_2.htm) | Initializes a new instance of the ModelView class |
| Public method | [ModelView(RhinoViewport)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_3.htm) | Initializes a new instance of the ModelView class |
| Public method | [ModelView(ViewInfo)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_4.htm) | Initializes a new instance of the ModelView class |
| Public method | [ModelView(ViewportInfo)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_5.htm) | Initializes a new instance of the ModelView class |
| Public method | [ModelView(ViewportInfo, String)](M_Grasshopper_Rhinoceros_Display_ModelView__ctor_6.htm) | Initializes a new instance of the ModelView class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValid](P_Grasshopper_Rhinoceros_Display_ModelView_IsValid.htm) |  |
| Public property | [Title](P_Grasshopper_Rhinoceros_Display_ModelView_Title.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Cast](M_Grasshopper_Rhinoceros_Display_ModelView_Cast.htm) |  |
| Protected method | [CastToAddLanguageSpecificTextSet("LST3AD63C0C\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST3AD63C0C\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Rhinoceros_Display_ModelView_CastTo__1.htm) |  |
| Public method | [Equals(ModelView)](M_Grasshopper_Rhinoceros_Display_ModelView_Equals.htm) |  |
| Public method | [Equals(Object)](M_Grasshopper_Rhinoceros_Display_ModelView_Equals_1.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST3AD63C0C\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Equals(Object)](https://docs.microsoft.com/dotnet/api/system.object.equals#system-object-equals(system-object)).) |
| Public method | [GetBoundingBox](M_Grasshopper_Rhinoceros_Display_ModelView_GetBoundingBox.htm) |  |
| Public method | [GetHashCode](M_Grasshopper_Rhinoceros_Display_ModelView_GetHashCode.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST3AD63C0C\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GetHashCodeAddLanguageSpecificTextSet("LST3AD63C0C\_7?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-object-gethashcode).) |
| Public method | [Morph](M_Grasshopper_Rhinoceros_Display_ModelView_Morph.htm) |  |
| Public method | [ToString](M_Grasshopper_Rhinoceros_Display_ModelView_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST3AD63C0C\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST3AD63C0C\_9?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |
| Public method | [ToViewportInfo](M_Grasshopper_Rhinoceros_Display_ModelView_ToViewportInfo.htm) |  |
| Public method | [Transform](M_Grasshopper_Rhinoceros_Display_ModelView_Transform.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Display Namespace](N_Grasshopper_Rhinoceros_Display.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)