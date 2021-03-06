# encoding: utf-8
# module gi.repository.EDataBook
# from /usr/lib64/girepository-1.0/EDataBook-1.2.typelib
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
import gi.repository.EBackend as __gi_repository_EBackend
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class DataBookFactory(__gi_repository_EBackend.DataFactory):
    """
    :Constructors:
    
    ::
    
        DataBookFactory(**properties)
        new(backend_per_process:int, cancellable:Gio.Cancellable=None) -> EBackend.DBusServer
    """
    def backend_closed(self, backend): # real signature unknown; restored from __doc__
        """ backend_closed(self, backend:EBackend.Backend) """
        pass

    def backend_closed_by_sender(self, backend, sender): # real signature unknown; restored from __doc__
        """ backend_closed_by_sender(self, backend:EBackend.Backend, sender:str) """
        pass

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

    def construct_path(self): # real signature unknown; restored from __doc__
        """ construct_path(self) -> str """
        return ""

    def create_backend(self, backend_factory, source): # real signature unknown; restored from __doc__
        """ create_backend(self, backend_factory:EBackend.BackendFactory, source:EDataServer.Source) -> EBackend.Backend """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_bus_acquired(self, *args, **kwargs): # real signature unknown
        """ bus_acquired(self, connection:Gio.DBusConnection) """
        pass

    def do_bus_name_acquired(self, *args, **kwargs): # real signature unknown
        """ bus_name_acquired(self, connection:Gio.DBusConnection) """
        pass

    def do_bus_name_lost(self, *args, **kwargs): # real signature unknown
        """ bus_name_lost(self, connection:Gio.DBusConnection) """
        pass

    def do_complete_open(self, *args, **kwargs): # real signature unknown
        """ complete_open(self, invocation:Gio.DBusMethodInvocation, object_path:str, bus_name:str, extension_name:str) """
        pass

    def do_create_backend(self, *args, **kwargs): # real signature unknown
        """ create_backend(self, backend_factory:EBackend.BackendFactory, source:EDataServer.Source) -> EBackend.Backend """
        pass

    def do_open_backend(self, *args, **kwargs): # real signature unknown
        """ open_backend(self, backend:EBackend.Backend, connection:Gio.DBusConnection, cancellable:Gio.Cancellable=None) -> str """
        pass

    def do_quit_server(self, *args, **kwargs): # real signature unknown
        """ quit_server(self, code:EBackend.DBusServerExitCode) """
        pass

    def do_run_server(self, *args, **kwargs): # real signature unknown
        """ run_server(self) -> EBackend.DBusServerExitCode """
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

    def get_backend_per_process(self): # real signature unknown; restored from __doc__
        """ get_backend_per_process(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_registry(self): # real signature unknown; restored from __doc__
        """ get_registry(self) -> EDataServer.SourceRegistry """
        pass

    def get_reload_supported(self): # real signature unknown; restored from __doc__
        """ get_reload_supported(self) -> bool """
        return False

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

    def hold(self): # real signature unknown; restored from __doc__
        """ hold(self) """
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

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_extensions(self, extension_type): # real signature unknown; restored from __doc__
        """ list_extensions(self, extension_type:GType) -> list """
        return []

    def list_opened_backends(self): # real signature unknown; restored from __doc__
        """ list_opened_backends(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def load_extensions(self): # real signature unknown; restored from __doc__
        """ load_extensions(self) """
        pass

    def load_modules(self): # real signature unknown; restored from __doc__
        """ load_modules(self) """
        pass

    def new(self, backend_per_process, cancellable=None): # real signature unknown; restored from __doc__
        """ new(backend_per_process:int, cancellable:Gio.Cancellable=None) -> EBackend.DBusServer """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def open_backend(self, backend, connection, cancellable=None): # real signature unknown; restored from __doc__
        """ open_backend(self, backend:EBackend.Backend, connection:Gio.DBusConnection, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def quit(self, code): # real signature unknown; restored from __doc__
        """ quit(self, code:EBackend.DBusServerExitCode) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_backend_factory(self, backend_name, extension_name): # real signature unknown; restored from __doc__
        """ ref_backend_factory(self, backend_name:str, extension_name:str) -> EBackend.BackendFactory """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run(self, wait_for_client): # real signature unknown; restored from __doc__
        """ run(self, wait_for_client:bool) -> EBackend.DBusServerExitCode """
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

    def spawn_subprocess_backend(self, invocation, uid, extension_name, subprocess_path): # real signature unknown; restored from __doc__
        """ spawn_subprocess_backend(self, invocation:Gio.DBusMethodInvocation, uid:str, extension_name:str, subprocess_path:str) """
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

    def use_backend_per_process(self): # real signature unknown; restored from __doc__
        """ use_backend_per_process(self) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f09d417dd60>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DataBookFactory), '__module__': 'gi.repository.EDataBook', '__gtype__': <GType EDataBookFactory (94654337978560)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'parent': <property object at 0x7f09d0c16db0>, 'priv': <property object at 0x7f09d0c16ef0>})"
    __gdoc__ = 'Object EDataBookFactory\n\nProperties from EDataFactory:\n  registry -> ESourceRegistry: Registry\n    Data source registry\n  reload-supported -> gboolean: Reload Supported\n    Whether the data factory supports Reload\n  backend-per-process -> gint: Backend Per Process\n    Override backend-per-process compile-time option\n\nSignals from EDBusServer:\n  bus-acquired (GDBusConnection)\n  bus-name-acquired (GDBusConnection)\n  bus-name-lost (GDBusConnection)\n  run-server () -> EDBusServerExitCode\n  quit-server (EDBusServerExitCode)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EDataBookFactory (94654337978560)>'
    __info__ = ObjectInfo(DataBookFactory)


