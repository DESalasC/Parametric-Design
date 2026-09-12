# M_GH_IO_Serialization_GH_IWriter_SetDoubleArray

﻿ GH\_IWriter.SetDoubleArray Method (String, Double[])

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetDoubleArray Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDoubleArray.htm "SetDoubleArray Method ")

[SetDoubleArray Method (String, Double[])](../html/M_GH_IO_Serialization_GH_IWriter_SetDoubleArray.htm "SetDoubleArray Method (String, Double[])")

[SetDoubleArray Method (String, Int32, Double[])](../html/M_GH_IO_Serialization_GH_IWriter_SetDoubleArray_1.htm "SetDoubleArray Method (String, Int32, Double[])")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LSTF42A2E1D\_0?cpp=::|nu=.");SetDoubleArray Method (String, AddLanguageSpecificTextSet("LSTF42A2E1D\_1?cpp=array&lt;");DoubleAddLanguageSpecificTextSet("LSTF42A2E1D\_2?cpp=&gt;|vb=()|nu=[]");) |

Add a new data item to this chunk.
The name must be unique or an exception will be thrown.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void SetDoubleArray(
	string item_name,
	double[] item_value
)
```

```
Sub SetDoubleArray ( 
	item_name As String,
	item_value As Double()
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTF42A2E1D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: AddLanguageSpecificTextSet("LSTF42A2E1D\_4?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LSTF42A2E1D\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)AddLanguageSpecificTextSet("LSTF42A2E1D\_6?cpp=&gt;|vb=()|nu=[]");  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetDoubleArray Overload](Overload_GH_IO_Serialization_GH_IWriter_SetDoubleArray.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)