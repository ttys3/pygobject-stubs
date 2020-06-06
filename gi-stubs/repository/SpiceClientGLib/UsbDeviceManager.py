# encoding: utf-8
# module gi.repository.SpiceClientGLib
# from /usr/lib64/girepository-1.0/SpiceClientGLib-2.0.typelib
# by generator 1.147
"""
An object which wraps an introspection typelib.

    This wrapping creates a python module like representation of the typelib
    using gi repository as a foundation. Accessing attributes of the module
    will dynamically pull them in and create wrappers for the members.
    These members are then cached on this introspection module.
"""

# imports
import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class UsbDeviceManager(__gi_overrides_GObject.Object, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        UsbDeviceManager(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def can_redirect_device(self, device): # real signature unknown; restored from __doc__
        """ can_redirect_device(self, device:SpiceClientGLib.UsbDevice) -> bool """
        return False

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

    def connect_device_async(self, device, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ connect_device_async(self, device:SpiceClientGLib.UsbDevice, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def connect_device_finish(self, res): # real signature unknown; restored from __doc__
        """ connect_device_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def create_shared_cd_device(self, filename): # real signature unknown; restored from __doc__
        """ create_shared_cd_device(self, filename:str) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect_device(self, device): # real signature unknown; restored from __doc__
        """ disconnect_device(self, device:SpiceClientGLib.UsbDevice) """
        pass

    def disconnect_device_async(self, device, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ disconnect_device_async(self, device:SpiceClientGLib.UsbDevice, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def disconnect_device_finish(self, res): # real signature unknown; restored from __doc__
        """ disconnect_device_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def do_auto_connect_failed(self, *args, **kwargs): # real signature unknown
        """ auto_connect_failed(self, device:SpiceClientGLib.UsbDevice, error:error) """
        pass

    def do_device_added(self, *args, **kwargs): # real signature unknown
        """ device_added(self, device:SpiceClientGLib.UsbDevice) """
        pass

    def do_device_error(self, *args, **kwargs): # real signature unknown
        """ device_error(self, device:SpiceClientGLib.UsbDevice, error:error) """
        pass

    def do_device_removed(self, *args, **kwargs): # real signature unknown
        """ device_removed(self, device:SpiceClientGLib.UsbDevice) """
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

    def get(self, session): # real signature unknown; restored from __doc__
        """ get(session:SpiceClientGLib.Session) -> SpiceClientGLib.UsbDeviceManager """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_devices(self): # real signature unknown; restored from __doc__
        """ get_devices(self) -> list """
        return []

    def get_devices_with_filter(self, filter=None): # real signature unknown; restored from __doc__
        """ get_devices_with_filter(self, filter:str=None) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

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

    def init(self, cancellable=None): # real signature unknown; restored from __doc__
        """ init(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def is_device_connected(self, device): # real signature unknown; restored from __doc__
        """ is_device_connected(self, device:SpiceClientGLib.UsbDevice) -> bool """
        return False

    def is_device_shared_cd(self, device): # real signature unknown; restored from __doc__
        """ is_device_shared_cd(self, device:SpiceClientGLib.UsbDevice) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_redirecting(self): # real signature unknown; restored from __doc__
        """ is_redirecting(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
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

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f9dcd645fa0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(UsbDeviceManager), '__module__': 'gi.repository.SpiceClientGLib', '__gtype__': <GType SpiceUsbDeviceManager (93951199868720)>, '__doc__': None, '__gsignals__': {}, 'get': gi.FunctionInfo(get), 'can_redirect_device': gi.FunctionInfo(can_redirect_device), 'connect_device_async': gi.FunctionInfo(connect_device_async), 'connect_device_finish': gi.FunctionInfo(connect_device_finish), 'create_shared_cd_device': gi.FunctionInfo(create_shared_cd_device), 'disconnect_device': gi.FunctionInfo(disconnect_device), 'disconnect_device_async': gi.FunctionInfo(disconnect_device_async), 'disconnect_device_finish': gi.FunctionInfo(disconnect_device_finish), 'get_devices': gi.FunctionInfo(get_devices), 'get_devices_with_filter': gi.FunctionInfo(get_devices_with_filter), 'is_device_connected': gi.FunctionInfo(is_device_connected), 'is_device_shared_cd': gi.FunctionInfo(is_device_shared_cd), 'is_redirecting': gi.FunctionInfo(is_redirecting), 'do_auto_connect_failed': gi.VFuncInfo(auto_connect_failed), 'do_device_added': gi.VFuncInfo(device_added), 'do_device_error': gi.VFuncInfo(device_error), 'do_device_removed': gi.VFuncInfo(device_removed), 'parent': <property object at 0x7f9dcd619a40>, 'priv': <property object at 0x7f9dcd619b30>})"
    __gdoc__ = 'Object SpiceUsbDeviceManager\n\nSignals from SpiceUsbDeviceManager:\n  device-added (SpiceUsbDevice)\n  device-removed (SpiceUsbDevice)\n  auto-connect-failed (SpiceUsbDevice, GError)\n  device-error (SpiceUsbDevice, GError)\n\nProperties from SpiceUsbDeviceManager:\n  session -> SpiceSession: Session\n    SpiceSession\n  auto-connect -> gboolean: Auto Connect\n    Auto connect plugged in USB devices\n  auto-connect-filter -> gchararray: Auto Connect Filter \n    Filter determining which USB devices to auto connect\n  redirect-on-connect -> gchararray: Redirect on connect\n    Filter selecting USB devices to redirect on connect\n  free-channels -> gint: Free channels\n    The number of available channels for redirecting USB devices\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType SpiceUsbDeviceManager (93951199868720)>'
    __info__ = ObjectInfo(UsbDeviceManager)


