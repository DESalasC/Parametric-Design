# M_Grasshopper_Rhinoceros_Render_ModelRenderContent_DuplicateContent__1

﻿ ModelRenderContent.DuplicateContent(TContent) Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Rhinoceros.Render](../html/N_Grasshopper_Rhinoceros_Render.htm "Grasshopper.Rhinoceros.Render")

[ModelRenderContent Class](../html/T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm "ModelRenderContent Class")

[ModelRenderContent Methods](../html/Methods_T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm "ModelRenderContent Methods")

[DuplicateContent(TContent) Method](../html/M_Grasshopper_Rhinoceros_Render_ModelRenderContent_DuplicateContent__1.htm "DuplicateContent(TContent) Method ")

[ToAttributes Method](../html/M_Grasshopper_Rhinoceros_Render_ModelRenderContent_ToAttributes.htm "ToAttributes Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| ModelRenderContentAddLanguageSpecificTextSet("LSTDF06799C\_0?cpp=::|nu=.");DuplicateContentAddLanguageSpecificTextSet("LSTDF06799C\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TContentAddLanguageSpecificTextSet("LSTDF06799C\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Method |

**Namespace:**
 [Grasshopper.Rhinoceros.Render](N_Grasshopper_Rhinoceros_Render.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected internal static TContent DuplicateContent<TContent>(
	TContent renderContent,
	out string name,
	out string notes,
	out string tags
)
where TContent : RenderContent
```

```
Protected Friend Shared Function DuplicateContent(Of TContent As RenderContent) ( 
	renderContent As TContent,
	<OutAttribute> ByRef name As String,
	<OutAttribute> ByRef notes As String,
	<OutAttribute> ByRef tags As String
) As TContent
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

renderContent
:   Type: TContent

name
:   Type: [SystemAddLanguageSpecificTextSet("LSTDF06799C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LSTDF06799C\_4?cpp=%");

notes
:   Type: [SystemAddLanguageSpecificTextSet("LSTDF06799C\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LSTDF06799C\_6?cpp=%");

tags
:   Type: [SystemAddLanguageSpecificTextSet("LSTDF06799C\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LSTDF06799C\_8?cpp=%");

#### Type Parameters

TContent

#### Return Value

Type: TContent

![](../icons/SectionExpanded.png)See Also

#### Reference

[ModelRenderContent Class](T_Grasshopper_Rhinoceros_Render_ModelRenderContent.htm)

[Grasshopper.Rhinoceros.Render Namespace](N_Grasshopper_Rhinoceros_Render.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)