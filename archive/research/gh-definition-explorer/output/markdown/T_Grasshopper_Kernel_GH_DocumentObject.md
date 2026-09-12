# T_Grasshopper_Kernel_GH_DocumentObject

﻿ GH\_DocumentObject Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentObject Class](../html/T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Class")

[GH\_DocumentObject Constructor](../html/Overload_Grasshopper_Kernel_GH_DocumentObject__ctor.htm "GH_DocumentObject Constructor ")

[GH\_DocumentObject Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Properties")

[GH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Methods")

[GH\_DocumentObject Events](../html/Events_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Events")

[GH\_DocumentObject Fields](../html/Fields_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentObject Class |

Standard implementation of IGH\_DocumentObject.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTDF27EA82\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.KernelAddLanguageSpecificTextSet("LSTDF27EA82\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LSTDF27EA82\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocumentObject  
      [Grasshopper.KernelAddLanguageSpecificTextSet("LSTDF27EA82\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm)

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_DocumentObject : GH_InstanceDescription, 
	IGH_DocumentObject
```

```
Public MustInherit Class GH_DocumentObject
	Inherits GH_InstanceDescription
	Implements IGH_DocumentObject
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocumentObject type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_DocumentObject(IGH\_InstanceDescription)](M_Grasshopper_Kernel_GH_DocumentObject__ctor.htm) | Initializes a new instance of the GH\_DocumentObject class |
| Protected method | [GH\_DocumentObject(String, String, String, String, String)](M_Grasshopper_Kernel_GH_DocumentObject__ctor_1.htm) | Initializes a new instance of the GH\_DocumentObject class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Attributes](P_Grasshopper_Kernel_GH_DocumentObject_Attributes.htm) | Gets or sets the attributes that are associated with this object. Only set custom attributes if you know what you are doing. |
| Public property | [Category](P_Grasshopper_Kernel_GH_InstanceDescription_Category.htm) | Gets or sets the Category in which this object belongs. If HasCategory() returns false, this field has no meaning. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [ComponentGuid](P_Grasshopper_Kernel_GH_DocumentObject_ComponentGuid.htm) | Returns a consistent ID for this object type. Every object must supply a unique and unchanging ID that is used to identify objects of the same type. |
| Public property | [Description](P_Grasshopper_Kernel_GH_InstanceDescription_Description.htm) | Gets or sets the description of the object. This field typically remains fixed during the lifetime of an object. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Exposure](P_Grasshopper_Kernel_GH_DocumentObject_Exposure.htm) | Gets the exposure of this object in the Graphical User Interface. The default is to expose everywhere. |
| Public property | [HasCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasCategory.htm) | Gets whether or not the Category field has been set. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [HasSubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasSubCategory.htm) | Gets whether or not the SubCategory field has been set. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Protected property | [Icon](P_Grasshopper_Kernel_GH_DocumentObject_Icon.htm) | Override this function to supply a custom icon (24x24 pixels). The result of this property is cached, so don't worry if icon retrieval is not very fast. |
| Public property | [Icon\_24x24](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24.htm) | The icon associated with this object. |
| Public property | [Icon\_24x24\_Locked](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24_Locked.htm) | The greyscale icon of this object. |
| Public property | [IconDisplayMode](P_Grasshopper_Kernel_GH_DocumentObject_IconDisplayMode.htm) | Gets the current display mode of the object. |
| Public property | [InstanceDescription](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceDescription.htm) | Gets a description of the current state of the object. This field is usually the same as the Description() field, but it might be variable when overridden. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [InstanceGuid](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceGuid.htm) | Gets the ID of this runtime instance. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Keywords](P_Grasshopper_Kernel_GH_InstanceDescription_Keywords.htm) | Gets a list of additional keywords that describe the object. Typically this list is empty but you can override this property to aid in object searches. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Name](P_Grasshopper_Kernel_GH_InstanceDescription_Name.htm) | Gets or sets the name of the object. This field typically remains fixed during the lifetime of an object. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [NickName](P_Grasshopper_Kernel_GH_InstanceDescription_NickName.htm) | Gets or sets the nickname of the object. This field can be changed by the user. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Obsolete](P_Grasshopper_Kernel_GH_DocumentObject_Obsolete.htm) | Gets whether this object is obsolete. Default implementation returns true if the class name contains the string "OBSOLETE" or if this class has been decorated with the ObsoleteAttribute. You are free to override this if you want, but I suggest adding the ObsoleteAttribute instead. |
| Public property | [SubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_SubCategory.htm) | Gets or sets the SubCategory in which this object belongs. If HasSubCategory() returns false, this field has no meaning. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddedToDocument](M_Grasshopper_Kernel_GH_DocumentObject_AddedToDocument.htm) | This method will be called when an object is added to a document. Override this method if you want to handle such events. |
| Public method | [AppendMenuItems](M_Grasshopper_Kernel_GH_DocumentObject_AppendMenuItems.htm) | This function is called when a context menu is about to be displayed. Override it to set custom items. |
| Public method | [CopyFrom](M_Grasshopper_Kernel_GH_InstanceDescription_CopyFrom.htm) | Copy all fields (except the instance ID) from another instance description. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public method | [CreateAttributes](M_Grasshopper_Kernel_GH_DocumentObject_CreateAttributes.htm) | This function creates the stand-alone attributes for this object. If you wish to supply your own Attributes, you must override this function. |
| Protected method | [DestroyIconCache](M_Grasshopper_Kernel_GH_DocumentObject_DestroyIconCache.htm) | Call this method to erase the existing icon cache. You must call this if you want to change the display icon of an object. |
| Public method | [DocumentContextChanged](M_Grasshopper_Kernel_GH_DocumentObject_DocumentContextChanged.htm) | This method will be called when the document that owns this object moves into a different context. |
| Public method | [ExpirePreview](M_Grasshopper_Kernel_GH_DocumentObject_ExpirePreview.htm) | Call this function when you suspect that the preview has expired for this object. This will cause the display cache to be eradicated. |
| Public method | [ExpireSolution](M_Grasshopper_Kernel_GH_DocumentObject_ExpireSolution.htm) | Call this function whenever you do something which expires the current solution. This will make sure all caches are erased, all downstream objects are expired and that the event is raised. The default implementation merely places a call to OnSolutionExpired(), override this function in derived classes to make sure you clear local data caches and expire downstream objects. |
| Protected method | [GetValue(String, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue.htm) | Get a boolean value from the component value table. |
| Protected method | [GetValue(String, Double)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_1.htm) | Get a double value from the component value table. |
| Protected method | [GetValue(String, Color)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_2.htm) | Get a color value from the component value table. |
| Protected method | [GetValue(String, Int32)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_3.htm) | Get an integer value from the component value table. |
| Protected method | [GetValue(String, String)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_4.htm) | Get a string value from the component value table. |
| Protected method | [HtmlHelp\_Source](M_Grasshopper_Kernel_GH_DocumentObject_HtmlHelp_Source.htm) | Return a String which contains HTML formatted source for the help topic. If you want to pass a URL that points to a remote page, then prefix the URL with a GOTO: tag, like so: GOTO:http://www.YourWebAddressHere.com |
| Public method | [IsolateObject](M_Grasshopper_Kernel_GH_DocumentObject_IsolateObject.htm) | Destroy all connections to other objects. |
| Public methodStatic member | [Menu\_AppendColourPicker](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendColourPicker.htm) | Add a colour picker to a menu. |
| Public methodStatic member | [Menu\_AppendCustomItem(ToolStripDropDown, Control)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendCustomItem.htm) | Utility function for inserting exotic controls into dropdown menus. |
| Public methodStatic member | [Menu\_AppendCustomItem(ToolStripDropDown, Control, KeyDownEventHandler)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendCustomItem_1.htm) | Utility function for inserting exotic controls into dropdown menus. |
| Public methodStatic member | [Menu\_AppendCustomItem(ToolStripDropDown, Control, KeyDownEventHandler, Boolean, Int32, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendCustomItem_2.htm) | Utility function for inserting exotic controls into dropdown menus. |
| Public methodStatic member | [Menu\_AppendDigitScrollerItem](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendDigitScrollerItem.htm) | Utility function for inserting a digit scroller into menus. |
| Public methodStatic member | [Menu\_AppendItem(ToolStrip, String)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem.htm) | Utility function for appending generic menu items. |
| Public methodStatic member | [Menu\_AppendItem(ToolStrip, String, EventHandler)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_1.htm) | Utility function for appending generic menu items. |
| Public methodStatic member | [Menu\_AppendItem(ToolStrip, String, EventHandler, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_2.htm) | Utility function for appending generic menu items. |
| Public methodStatic member | [Menu\_AppendItem(ToolStrip, String, EventHandler, Image)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_4.htm) | Utility function for appending generic menu items. |
| Public methodStatic member | [Menu\_AppendItem(ToolStrip, String, EventHandler, Boolean, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_3.htm) | Utility function for appending generic menu items. |
| Public methodStatic member | [Menu\_AppendItem(ToolStrip, String, EventHandler, Image, Object)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_6.htm) | Utility function for appending generic menu items. |
| Public methodStatic member | [Menu\_AppendItem(ToolStrip, String, EventHandler, Image, Boolean, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem_5.htm) | Utility function for appending generic menu items. |
| Protected method | [Menu\_AppendObjectHelp](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectHelp.htm) | Appends the default object Help menu item. |
| Protected method | [Menu\_AppendObjectName](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectName.htm) | Appends the old-fashioned object name menu item. If you also want the Display mode toggle then use Menu\_AppendObjectNameEx() |
| Protected method | [Menu\_AppendObjectNameEx](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectNameEx.htm) | Appends the default object name + display mode menu item. |
| Protected method | [Menu\_AppendPublish](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendPublish.htm) | Appends the default item for publishing to RCP. This menu will only appear if the current class implement IRcpAwareObject |
| Public methodStatic member | [Menu\_AppendSeparator](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendSeparator.htm) | Utility function for appending separators to a menu dropdown. If the dropdown is empty or if it already has a separator at the bottom, nothing will happen. |
| Public methodStatic member | [Menu\_AppendTextItem(ToolStripDropDown, String, GH\_MenuTextBoxAddLanguageSpecificTextSet("LSTDF27EA82\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");KeyDownEventHandler, GH\_MenuTextBoxAddLanguageSpecificTextSet("LSTDF27EA82\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");TextChangedEventHandler, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendTextItem.htm) | Utility function for inserting text boxes into menus. |
| Public methodStatic member | [Menu\_AppendTextItem(ToolStripDropDown, String, GH\_MenuTextBoxAddLanguageSpecificTextSet("LSTDF27EA82\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");KeyDownEventHandler, GH\_MenuTextBoxAddLanguageSpecificTextSet("LSTDF27EA82\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");TextChangedEventHandler, Boolean, Int32, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendTextItem_1.htm) | Utility function for inserting text boxes into menus. |
| Public methodStatic member | [Menu\_MoveItem(ToolStripItem, AddLanguageSpecificTextSet("LSTDF27EA82\_8?cpp=array&lt;");StringAddLanguageSpecificTextSet("LSTDF27EA82\_9?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_MoveItem_1.htm) | Utility function for moving menu items. |
| Public methodStatic member | [Menu\_MoveItem(ToolStripItem, Boolean, AddLanguageSpecificTextSet("LSTDF27EA82\_10?cpp=array&lt;");StringAddLanguageSpecificTextSet("LSTDF27EA82\_11?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_DocumentObject_Menu_MoveItem.htm) | Utility function for moving menu items. |
| Public method | [MovedBetweenDocuments](M_Grasshopper_Kernel_GH_DocumentObject_MovedBetweenDocuments.htm) | This method will be called when an object is moved from one document to another. Override this method if you want to handle such events. |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LSTDF27EA82\_12?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid.htm) | Generate a new random instance GUID (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public method | [NewInstanceGuid(Guid)](M_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid_1.htm) | Set the instance ID to be a specific GUID. This is very dangerous, only use this function if you're 6"4' and your first name is David. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public method | [OnAttributesChanged](M_Grasshopper_Kernel_GH_DocumentObject_OnAttributesChanged.htm) | Raises the AttributesChanged event on the toplevel object. |
| Public method | [OnDisplayExpired](M_Grasshopper_Kernel_GH_DocumentObject_OnDisplayExpired.htm) | Raises the DisplayExpired event on the toplevel object. |
| Public method | [OnObjectChanged(GH\_ObjectChangedEventArgs)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged.htm) |  |
| Public method | [OnObjectChanged(GH\_ObjectEventType)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_1.htm) |  |
| Public method | [OnObjectChanged(String)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_3.htm) |  |
| Public method | [OnObjectChanged(GH\_ObjectEventType, Object)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_2.htm) |  |
| Public method | [OnObjectChanged(String, Object)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_4.htm) |  |
| Public method | [OnPingDocument](M_Grasshopper_Kernel_GH_DocumentObject_OnPingDocument.htm) | Raise the PingDocument Event on the toplevel object and try to find the document which owns this object. |
| Public method | [OnPreviewExpired](M_Grasshopper_Kernel_GH_DocumentObject_OnPreviewExpired.htm) | Raises the PreviewExpired event on the toplevel object. |
| Public method | [OnSolutionExpired](M_Grasshopper_Kernel_GH_DocumentObject_OnSolutionExpired.htm) | Raises the SolutionExpired event on the toplevel object. You probably want to call ExpireSolution() instead of this method directly. |
| Public method | [Read](M_Grasshopper_Kernel_GH_DocumentObject_Read.htm) | (Overrides [GH\_InstanceDescriptionAddLanguageSpecificTextSet("LSTDF27EA82\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_GH_InstanceDescription_Read.htm).) |
| Public method | [ReadFull](M_Grasshopper_Kernel_GH_InstanceDescription_ReadFull.htm) | GH\_InstanceDescription does not by default serialize all fields. Use this function to read *all* fields from the archive. This method is compatible with the default Write()/Read() operations. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public method | [RecordUndoEvent(GH\_UndoRecord)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent.htm) | Record an entire undo record. |
| Public method | [RecordUndoEvent(String)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_1.htm) | Record a generic object change undo event. |
| Public method | [RecordUndoEvent(String, IGH\_UndoAction)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_2.htm) | Record a specific object change undo event. |
| Public method | [RemovedFromDocument](M_Grasshopper_Kernel_GH_DocumentObject_RemovedFromDocument.htm) | This method will be called when an object is removed from a document. Override this method if you want to handle such events. |
| Public method | [SetIconOverride](M_Grasshopper_Kernel_GH_DocumentObject_SetIconOverride.htm) | Set a new custom icon override for this object. |
| Protected method | [SetValue(String, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue.htm) | Set a named value. This value will be serialized with the component. |
| Protected method | [SetValue(String, Double)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_1.htm) | Set a named value. This value will be serialized with the component. |
| Protected method | [SetValue(String, Color)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_2.htm) | Set a named value. This value will be serialized with the component. |
| Protected method | [SetValue(String, Int32)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_3.htm) | Set a named value. This value will be serialized with the component. |
| Protected method | [SetValue(String, String)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_4.htm) | Set a named value. This value will be serialized with the component. |
| Public method | [TriggerAutoSaveAddLanguageSpecificTextSet("LSTDF27EA82\_14?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_1.htm) | Triggers the AutoSave function on the owner document with a custom flag. |
| Public method | [TriggerAutoSave(Guid)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_3.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger, Guid)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_2.htm) | Triggers the AutoSave function on the owner document with a custom flag. |
| Protected method | [ValuesChanged](M_Grasshopper_Kernel_GH_DocumentObject_ValuesChanged.htm) | Override this method if you want to respond to changes to the value table. The base implementation is empty, so you don't have to call it. |
| Public method | [Write](M_Grasshopper_Kernel_GH_DocumentObject_Write.htm) | (Overrides [GH\_InstanceDescriptionAddLanguageSpecificTextSet("LSTDF27EA82\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_GH_InstanceDescription_Write.htm).) |
| Public method | [WriteFull](M_Grasshopper_Kernel_GH_InstanceDescription_WriteFull.htm) | GH\_InstanceDescription does not by default serialize all fields. Use this function to write *all* fields to the archive. This method is compatible with the default Write()/Read() operations. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [AttributesChanged](E_Grasshopper_Kernel_GH_DocumentObject_AttributesChanged.htm) | Raised whenever the number or kind of attributes changes. This event is handled by GH\_Documents who subsequently wipe their attribute caches. |
| Public event | [DisplayExpired](E_Grasshopper_Kernel_GH_DocumentObject_DisplayExpired.htm) | Raised whenever the display (on the Canvas) of a certain object becomes invalid. |
| Public event | [ObjectChanged](E_Grasshopper_Kernel_GH_DocumentObject_ObjectChanged.htm) |  |
| Public event | [PingDocument](E_Grasshopper_Kernel_GH_DocumentObject_PingDocument.htm) | Raised whenever an object needs to know which GH\_Document it belongs to. |
| Public event | [PreviewExpired](E_Grasshopper_Kernel_GH_DocumentObject_PreviewExpired.htm) | Raised whenever the display (in the Rhino viewports) of a certain object becomes invalid. |
| Public event | [SolutionExpired](E_Grasshopper_Kernel_GH_DocumentObject_SolutionExpired.htm) | Raised whenever the solution of a certain object becomes invalid. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_attributes](F_Grasshopper_Kernel_GH_DocumentObject_m_attributes.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)