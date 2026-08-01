# M_Grasshopper_Kernel_GH_Document_Write_1

﻿ GH\_Document.Write Method (GH\_IWriter, IList(IGH\_DocumentObject))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[Write Method](../html/Overload_Grasshopper_Kernel_GH_Document_Write.htm "Write Method ")

[Write Method (GH\_IWriter)](../html/M_Grasshopper_Kernel_GH_Document_Write.htm "Write Method (GH_IWriter)")

[Write Method (GH\_IWriter, IList(IGH\_DocumentObject))](../html/M_Grasshopper_Kernel_GH_Document_Write_1.htm "Write Method (GH_IWriter, IList(IGH_DocumentObject))")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LST37EBB108\_0?cpp=::|nu=.");Write Method (GH\_IWriter, IListAddLanguageSpecificTextSet("LST37EBB108\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_DocumentObjectAddLanguageSpecificTextSet("LST37EBB108\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Special function that allows writing of a custom object list.
This function is used when partial documents need to be serialized
such as when exporting or during clipboard operations.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool Write(
	GH_IWriter writer,
	IList<IGH_DocumentObject> objList
)
```

```
Public Function Write ( 
	writer As GH_IWriter,
	objList As IList(Of IGH_DocumentObject)
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

writer
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LST37EBB108\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IWriter](T_GH_IO_Serialization_GH_IWriter.htm)  
    Writer to serialize with.

objList
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST37EBB108\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");IList](https://docs.microsoft.com/dotnet/api/system.collections.generic.ilist-1)AddLanguageSpecificTextSet("LST37EBB108\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm)AddLanguageSpecificTextSet("LST37EBB108\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Object list override

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[Write Overload](Overload_Grasshopper_Kernel_GH_Document_Write.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)