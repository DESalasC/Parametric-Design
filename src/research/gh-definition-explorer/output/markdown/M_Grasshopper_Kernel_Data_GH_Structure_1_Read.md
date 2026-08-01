# M_Grasshopper_Kernel_Data_GH_Structure_1_Read

﻿ GH\_Structure(T).Read Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Structure(T) Class](../html/T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Class")

[GH\_Structure(T) Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Methods")

[AllData Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_AllData.htm "AllData Method ")

[Append Method](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_Append.htm "Append Method ")

[AppendRange Method](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_AppendRange.htm "AppendRange Method ")

[Clear Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_Clear.htm "Clear Method ")

[ClearData Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_ClearData.htm "ClearData Method ")

[DataDescription Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_DataDescription.htm "DataDescription Method ")

[Duplicate Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_Duplicate.htm "Duplicate Method ")

[DuplicateCast(Q) Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_DuplicateCast__1.htm "DuplicateCast(Q) Method ")

[EnsureCapacity Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_EnsureCapacity.htm "EnsureCapacity Method ")

[EnsurePath Method](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_EnsurePath.htm "EnsurePath Method ")

[ExpandPath Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_ExpandPath.htm "ExpandPath Method ")

[Flatten Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_Flatten.htm "Flatten Method ")

[FlattenData Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_FlattenData.htm "FlattenData Method ")

[GetEnumerator Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_GetEnumerator.htm "GetEnumerator Method ")

[GetEnumerator\_Generic Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_GetEnumerator_Generic.htm "GetEnumerator_Generic Method ")

[Graft Method](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_Graft.htm "Graft Method ")

[Insert Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_Insert.htm "Insert Method ")

[LongestPathIndex Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_LongestPathIndex.htm "LongestPathIndex Method ")

[MergeStructure Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_MergeStructure.htm "MergeStructure Method ")

[PathExists Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_PathExists.htm "PathExists Method ")

[PathIndex Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_PathIndex.htm "PathIndex Method ")

[Read Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_Read.htm "Read Method ")

[RemoveData Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_RemoveData.htm "RemoveData Method ")

[RemovePath Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_RemovePath.htm "RemovePath Method ")

[ReplacePath Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_ReplacePath.htm "ReplacePath Method ")

[Reverse Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_Reverse.htm "Reverse Method ")

[ShallowDuplicate Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_ShallowDuplicate.htm "ShallowDuplicate Method ")

[ShortestPathIndex Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_ShortestPathIndex.htm "ShortestPathIndex Method ")

[Simplify Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_Simplify.htm "Simplify Method ")

[ToString Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_ToString.htm "ToString Method ")

[TrimExcess Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_TrimExcess.htm "TrimExcess Method ")

[Write Method](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StructureAddLanguageSpecificTextSet("LST1E558B37\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST1E558B37\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST1E558B37\_2?cpp=::|nu=.");Read Method |

Read the entire GH\_Structure from an archive.
This method relies on the the serialization of the IGH\_Goo items it contains.
Also, the IGH\_Goo T generic must have a public constructor that takes no arguments.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool Read(
	GH_IReader reader
)
```

```
Public Function Read ( 
	reader As GH_IReader
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

reader
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LST1E558B37\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IReader](T_GH_IO_Serialization_GH_IReader.htm)  
    Archive to read from.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

#### Implements

[GH\_ISerializableAddLanguageSpecificTextSet("LST1E558B37\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_GH_IO_GH_ISerializable_Read.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_StructureAddLanguageSpecificTextSet("LST1E558B37\_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1E558B37\_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)