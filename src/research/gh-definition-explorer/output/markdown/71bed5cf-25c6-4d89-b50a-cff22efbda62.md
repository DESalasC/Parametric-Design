# 71bed5cf-25c6-4d89-b50a-cff22efbda62

﻿ Project Setup (VS.Express) 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Development](../html/8b9acc0a-5165-4427-aea5-1873faffb4ff.htm "Development")

[GHA Assembly Wizards](../html/d5ac95cc-3592-49a7-9162-d1bd981fb6c5.htm "GHA Assembly Wizards")

[Assembly Hierarchy](../html/bc188193-19ff-4ae5-a3ed-2e78c34a306e.htm "Assembly Hierarchy")

[Project Setup (VB.NET)](../html/99f64b89-5975-4ebe-adc6-24da038e915f.htm "Project Setup (VB.NET)")

[Project Setup (C#)](../html/f00ac74b-492c-44fe-8da3-b28265dc820f.htm "Project Setup (C#)")

[Project Setup (VS.Express)](../html/71bed5cf-25c6-4d89-b50a-cff22efbda62.htm "Project Setup (VS.Express)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Project Setup (VS.Express) |

**Please note that we now have
[Assembly Wizards for Grasshopper](d5ac95cc-3592-49a7-9162-d1bd981fb6c5.htm)
and it is no longer necessary to manually
create a GHA project in Visual Studio.**

If you are using the Express version of Visual Studio, then you might not be able to
apply all required settings through the VS User Interface. In this case you'll have to modify the
project files manually to apply the settings.

**If you are using Visual Studio Professional, you can safely ignore this page.**

This document outlines how to manually modify *csproj* and
*vbproj* files.

- [Override Configuration Folders](#ManualConfigurationMerge)
- [Add Post-Build Events](#ManualPostBuildEvents)
- [Set Debug Start Action](#ManualDebugStartAction)

![](../icons/SectionExpanded.png)Override Configuration Folders

It is useful to override the Visual Studio default behaviour regarding build configuration
output. By default, DEBUG and RELEASE configurations (or 'flavours') are outputted to unique
folders. This can cause confusion during debugging.

In order to override the output folders, open the project file in a text editor.
If you're using VB then the project file will have the *\*.vbproj* extension.
If you're using C# then the project file will have the *\*.csproj* extension.
Ideally you should use a text editor that understands xml-formatting, but Notepad will do.

Inside the project file, locate the property group that has to do with the Debug and Release
configurations. They will probably be called:

XML

[Copy](# "Copy")

```
<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">
<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Release|AnyCPU' ">
```

AddLanguageTabSet("ID0EAEAACAAA");
Inside these property groups you will find OutputPath nodes:

XML

[Copy](# "Copy")

```
<OutputPath>bin\Debug\</OutputPath>
<OutputPath>bin\Release\</OutputPath>
```

AddLanguageTabSet("ID0EACAACAAA");
You'll have to change these to point to the same folder. We recommend:

XML

[Copy](# "Copy")

```
<OutputPath>bin\</OutputPath>
```

AddLanguageTabSet("ID0EAAAACAAA");

![](../icons/SectionExpanded.png)Add Post-Build Events

It is vital to add a Post-Build event to a Grasshopper Component Library since
Grasshopper will only consider *\*.gha* files during plug-in loading.
Since your project is a *Class Library*, it will automatically
be compiled into a *\*.dll* file.

In order to override the output folders, open the project file in a text editor.
If you're using VB then the project file will have the *\*.vbproj* extension.
If you're using C# then the project file will have the *\*.csproj* extension.
Ideally you should use a text editor that understands xml-formatting, but Notepad will do.

By default, a project file (vbproj for VB.NET; csproj for C#) does not contain any
Build Events, so you'll have to add the entire section in the project file Xml data.
Navigate towards the bottom of the project file. Just before the closing </Project>
tag, insert the following PropertyGroup:

XML

[Copy](# "Copy")

```
<PropertyGroup>
  <PostBuildEvent>Copy "$(TargetPath)" "$(TargetDir)\$(ProjectName).gha"
                  Erase "$(TargetPath)"
  </PostBuildEvent>
</PropertyGroup>
```

AddLanguageTabSet("ID0EAAAABAAA");

![](../icons/SectionExpanded.png)Set Debug Start Action

It is not possible to directly debug a Grasshopper Component Library, since it must
be loaded by Grasshopper, which in turn must be loaded by Rhinoceros. So, in order to debug
a *\*.gha* file you must first start Rhino. This is called a
*Debug Start Action* and VS Express does not allow you to set one
via its own UI.

TODO, Finish this topic...

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)