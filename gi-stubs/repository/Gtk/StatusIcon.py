# encoding: utf-8
# module gi.repository.Gtk
# from /usr/lib64/girepository-1.0/Gtk-3.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class StatusIcon(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        StatusIcon(**properties)
        new() -> Gtk.StatusIcon
        new_from_file(filename:str) -> Gtk.StatusIcon
        new_from_gicon(icon:Gio.Icon) -> Gtk.StatusIcon
        new_from_icon_name(icon_name:str) -> Gtk.StatusIcon
        new_from_pixbuf(pixbuf:GdkPixbuf.Pixbuf) -> Gtk.StatusIcon
        new_from_stock(stock_id:str) -> Gtk.StatusIcon
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_activate(self, *args, **kwargs): # real signature unknown
        """ activate(self) """
        pass

    def do_button_press_event(self, *args, **kwargs): # real signature unknown
        """ button_press_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_button_release_event(self, *args, **kwargs): # real signature unknown
        """ button_release_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_popup_menu(self, *args, **kwargs): # real signature unknown
        """ popup_menu(self, button:int, activate_time:int) """
        pass

    def do_query_tooltip(self, *args, **kwargs): # real signature unknown
        """ query_tooltip(self, x:int, y:int, keyboard_mode:bool, tooltip:Gtk.Tooltip) -> bool """
        pass

    def do_scroll_event(self, *args, **kwargs): # real signature unknown
        """ scroll_event(self, event:Gdk.EventScroll) -> bool """
        pass

    def do_size_changed(self, *args, **kwargs): # real signature unknown
        """ size_changed(self, size:int) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_geometry(self): # real signature unknown; restored from __doc__
        """ get_geometry(self) -> bool, screen:Gdk.Screen, area:Gdk.Rectangle, orientation:Gtk.Orientation """
        return False

    def get_gicon(self): # real signature unknown; restored from __doc__
        """ get_gicon(self) -> Gio.Icon or None """
        pass

    def get_has_tooltip(self): # real signature unknown; restored from __doc__
        """ get_has_tooltip(self) -> bool """
        return False

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str or None """
        return ""

    def get_pixbuf(self): # real signature unknown; restored from __doc__
        """ get_pixbuf(self) -> GdkPixbuf.Pixbuf or None """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Gdk.Screen """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_stock(self): # real signature unknown; restored from __doc__
        """ get_stock(self) -> str or None """
        return ""

    def get_storage_type(self): # real signature unknown; restored from __doc__
        """ get_storage_type(self) -> Gtk.ImageType """
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_tooltip_markup(self): # real signature unknown; restored from __doc__
        """ get_tooltip_markup(self) -> str or None """
        return ""

    def get_tooltip_text(self): # real signature unknown; restored from __doc__
        """ get_tooltip_text(self) -> str or None """
        return ""

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
        return False

    def get_x11_window_id(self): # real signature unknown; restored from __doc__
        """ get_x11_window_id(self) -> int """
        return 0

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_embedded(self): # real signature unknown; restored from __doc__
        """ is_embedded(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gtk.StatusIcon """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_file(self, filename): # real signature unknown; restored from __doc__
        """ new_from_file(filename:str) -> Gtk.StatusIcon """
        pass

    def new_from_gicon(self, icon): # real signature unknown; restored from __doc__
        """ new_from_gicon(icon:Gio.Icon) -> Gtk.StatusIcon """
        pass

    def new_from_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ new_from_icon_name(icon_name:str) -> Gtk.StatusIcon """
        pass

    def new_from_pixbuf(self, pixbuf): # real signature unknown; restored from __doc__
        """ new_from_pixbuf(pixbuf:GdkPixbuf.Pixbuf) -> Gtk.StatusIcon """
        pass

    def new_from_stock(self, stock_id): # real signature unknown; restored from __doc__
        """ new_from_stock(stock_id:str) -> Gtk.StatusIcon """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def position_menu(self, menu, x, y, user_data): # real signature unknown; restored from __doc__
        """ position_menu(menu:Gtk.Menu, x:int, y:int, user_data:Gtk.StatusIcon) -> x:int, y:int, push_in:bool """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_from_file(self, filename): # real signature unknown; restored from __doc__
        """ set_from_file(self, filename:str) """
        pass

    def set_from_gicon(self, icon): # real signature unknown; restored from __doc__
        """ set_from_gicon(self, icon:Gio.Icon) """
        pass

    def set_from_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ set_from_icon_name(self, icon_name:str) """
        pass

    def set_from_pixbuf(self, pixbuf=None): # real signature unknown; restored from __doc__
        """ set_from_pixbuf(self, pixbuf:GdkPixbuf.Pixbuf=None) """
        pass

    def set_from_stock(self, stock_id): # real signature unknown; restored from __doc__
        """ set_from_stock(self, stock_id:str) """
        pass

    def set_has_tooltip(self, has_tooltip): # real signature unknown; restored from __doc__
        """ set_has_tooltip(self, has_tooltip:bool) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_screen(self, screen): # real signature unknown; restored from __doc__
        """ set_screen(self, screen:Gdk.Screen) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_tooltip_markup(self, markup=None): # real signature unknown; restored from __doc__
        """ set_tooltip_markup(self, markup:str=None) """
        pass

    def set_tooltip_text(self, text): # real signature unknown; restored from __doc__
        """ set_tooltip_text(self, text:str) """
        pass

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, **properties): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __subclasshook__(self, *args, **kwargs): # real signature unknown
        """
        Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fe82eb2d100>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(StatusIcon), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkStatusIcon (94846038765488)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_file': gi.FunctionInfo(new_from_file), 'new_from_gicon': gi.FunctionInfo(new_from_gicon), 'new_from_icon_name': gi.FunctionInfo(new_from_icon_name), 'new_from_pixbuf': gi.FunctionInfo(new_from_pixbuf), 'new_from_stock': gi.FunctionInfo(new_from_stock), 'position_menu': gi.FunctionInfo(position_menu), 'get_geometry': gi.FunctionInfo(get_geometry), 'get_gicon': gi.FunctionInfo(get_gicon), 'get_has_tooltip': gi.FunctionInfo(get_has_tooltip), 'get_icon_name': gi.FunctionInfo(get_icon_name), 'get_pixbuf': gi.FunctionInfo(get_pixbuf), 'get_screen': gi.FunctionInfo(get_screen), 'get_size': gi.FunctionInfo(get_size), 'get_stock': gi.FunctionInfo(get_stock), 'get_storage_type': gi.FunctionInfo(get_storage_type), 'get_title': gi.FunctionInfo(get_title), 'get_tooltip_markup': gi.FunctionInfo(get_tooltip_markup), 'get_tooltip_text': gi.FunctionInfo(get_tooltip_text), 'get_visible': gi.FunctionInfo(get_visible), 'get_x11_window_id': gi.FunctionInfo(get_x11_window_id), 'is_embedded': gi.FunctionInfo(is_embedded), 'set_from_file': gi.FunctionInfo(set_from_file), 'set_from_gicon': gi.FunctionInfo(set_from_gicon), 'set_from_icon_name': gi.FunctionInfo(set_from_icon_name), 'set_from_pixbuf': gi.FunctionInfo(set_from_pixbuf), 'set_from_stock': gi.FunctionInfo(set_from_stock), 'set_has_tooltip': gi.FunctionInfo(set_has_tooltip), 'set_name': gi.FunctionInfo(set_name), 'set_screen': gi.FunctionInfo(set_screen), 'set_title': gi.FunctionInfo(set_title), 'set_tooltip_markup': gi.FunctionInfo(set_tooltip_markup), 'set_tooltip_text': gi.FunctionInfo(set_tooltip_text), 'set_visible': gi.FunctionInfo(set_visible), 'do_activate': gi.VFuncInfo(activate), 'do_button_press_event': gi.VFuncInfo(button_press_event), 'do_button_release_event': gi.VFuncInfo(button_release_event), 'do_popup_menu': gi.VFuncInfo(popup_menu), 'do_query_tooltip': gi.VFuncInfo(query_tooltip), 'do_scroll_event': gi.VFuncInfo(scroll_event), 'do_size_changed': gi.VFuncInfo(size_changed), 'parent_instance': <property object at 0x7fe830f6eb30>, 'priv': <property object at 0x7fe830f6ea90>})"
    __gdoc__ = 'Object GtkStatusIcon\n\nSignals from GtkStatusIcon:\n  size-changed (gint) -> gboolean\n  button-press-event (GdkEvent) -> gboolean\n  button-release-event (GdkEvent) -> gboolean\n  scroll-event (GdkEvent) -> gboolean\n  query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean\n  popup-menu (guint, guint)\n  activate ()\n\nProperties from GtkStatusIcon:\n  pixbuf -> GdkPixbuf: Pixbuf\n    A GdkPixbuf to display\n  file -> gchararray: Filename\n    Filename to load and display\n  stock -> gchararray: Stock ID\n    Stock ID for a stock image to display\n  icon-name -> gchararray: Icon Name\n    The name of the icon from the icon theme\n  gicon -> GIcon: GIcon\n    The GIcon being displayed\n  storage-type -> GtkImageType: Storage type\n    The representation being used for image data\n  size -> gint: Size\n    The size of the icon\n  screen -> GdkScreen: Screen\n    The screen where this status icon will be displayed\n  visible -> gboolean: Visible\n    Whether the status icon is visible\n  orientation -> GtkOrientation: Orientation\n    The orientation of the tray\n  embedded -> gboolean: Embedded\n    Whether the status icon is embedded\n  has-tooltip -> gboolean: Has tooltip\n    Whether this tray icon has a tooltip\n  tooltip-text -> gchararray: Tooltip Text\n    The contents of the tooltip for this widget\n  tooltip-markup -> gchararray: Tooltip markup\n    The contents of the tooltip for this tray icon\n  title -> gchararray: Title\n    The title of this tray icon\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkStatusIcon (94846038765488)>'
    __info__ = ObjectInfo(StatusIcon)


