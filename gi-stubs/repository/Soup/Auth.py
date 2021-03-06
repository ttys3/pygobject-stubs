# encoding: utf-8
# module gi.repository.Soup
# from /usr/lib64/girepository-1.0/Soup-2.4.typelib
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


class Auth(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Auth(**properties)
        new(type:GType, msg:Soup.Message, auth_header:str) -> Soup.Auth or None
    """
    def authenticate(self, username, password): # real signature unknown; restored from __doc__
        """ authenticate(self, username:str, password:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def can_authenticate(self): # real signature unknown; restored from __doc__
        """ can_authenticate(self) -> bool """
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

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_authenticate(self, *args, **kwargs): # real signature unknown
        """ authenticate(self, username:str, password:str) """
        pass

    def do_can_authenticate(self, *args, **kwargs): # real signature unknown
        """ can_authenticate(self) -> bool """
        pass

    def do_get_authorization(self, *args, **kwargs): # real signature unknown
        """ get_authorization(self, msg:Soup.Message) -> str """
        pass

    def do_get_protection_space(self, *args, **kwargs): # real signature unknown
        """ get_protection_space(self, source_uri:Soup.URI) -> list """
        pass

    def do_is_authenticated(self, *args, **kwargs): # real signature unknown
        """ is_authenticated(self) -> bool """
        pass

    def do_is_ready(self, *args, **kwargs): # real signature unknown
        """ is_ready(self, msg:Soup.Message) -> bool """
        pass

    def do_update(self, *args, **kwargs): # real signature unknown
        """ update(self, msg:Soup.Message, auth_header:dict) -> bool """
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

    def get_authorization(self, msg): # real signature unknown; restored from __doc__
        """ get_authorization(self, msg:Soup.Message) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_host(self): # real signature unknown; restored from __doc__
        """ get_host(self) -> str """
        return ""

    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_protection_space(self, source_uri): # real signature unknown; restored from __doc__
        """ get_protection_space(self, source_uri:Soup.URI) -> list """
        return []

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_realm(self): # real signature unknown; restored from __doc__
        """ get_realm(self) -> str """
        return ""

    def get_saved_password(self, user): # real signature unknown; restored from __doc__
        """ get_saved_password(self, user:str) -> str """
        return ""

    def get_saved_users(self): # real signature unknown; restored from __doc__
        """ get_saved_users(self) -> list """
        return []

    def get_scheme_name(self): # real signature unknown; restored from __doc__
        """ get_scheme_name(self) -> str """
        return ""

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

    def has_saved_password(self, username, password): # real signature unknown; restored from __doc__
        """ has_saved_password(self, username:str, password:str) """
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

    def is_authenticated(self): # real signature unknown; restored from __doc__
        """ is_authenticated(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_for_proxy(self): # real signature unknown; restored from __doc__
        """ is_for_proxy(self) -> bool """
        return False

    def is_ready(self, msg): # real signature unknown; restored from __doc__
        """ is_ready(self, msg:Soup.Message) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, type, msg, auth_header): # real signature unknown; restored from __doc__
        """ new(type:GType, msg:Soup.Message, auth_header:str) -> Soup.Auth or None """
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

    def save_password(self, username, password): # real signature unknown; restored from __doc__
        """ save_password(self, username:str, password:str) """
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

    def update(self, msg, auth_header): # real signature unknown; restored from __doc__
        """ update(self, msg:Soup.Message, auth_header:str) -> bool """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    realm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f8e485d8d00>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Auth), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupAuth (94750593422528)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'authenticate': gi.FunctionInfo(authenticate), 'can_authenticate': gi.FunctionInfo(can_authenticate), 'get_authorization': gi.FunctionInfo(get_authorization), 'get_host': gi.FunctionInfo(get_host), 'get_info': gi.FunctionInfo(get_info), 'get_protection_space': gi.FunctionInfo(get_protection_space), 'get_realm': gi.FunctionInfo(get_realm), 'get_saved_password': gi.FunctionInfo(get_saved_password), 'get_saved_users': gi.FunctionInfo(get_saved_users), 'get_scheme_name': gi.FunctionInfo(get_scheme_name), 'has_saved_password': gi.FunctionInfo(has_saved_password), 'is_authenticated': gi.FunctionInfo(is_authenticated), 'is_for_proxy': gi.FunctionInfo(is_for_proxy), 'is_ready': gi.FunctionInfo(is_ready), 'save_password': gi.FunctionInfo(save_password), 'update': gi.FunctionInfo(update), 'do_authenticate': gi.VFuncInfo(authenticate), 'do_can_authenticate': gi.VFuncInfo(can_authenticate), 'do_get_authorization': gi.VFuncInfo(get_authorization), 'do_get_protection_space': gi.VFuncInfo(get_protection_space), 'do_is_authenticated': gi.VFuncInfo(is_authenticated), 'do_is_ready': gi.VFuncInfo(is_ready), 'do_update': gi.VFuncInfo(update), 'parent': <property object at 0x7f8e485fe9f0>, 'realm': <property object at 0x7f8e485fec20>})"
    __gdoc__ = 'Object SoupAuth\n\nProperties from SoupAuth:\n  scheme-name -> gchararray: Scheme name\n    Authentication scheme name\n  realm -> gchararray: Realm\n    Authentication realm\n  host -> gchararray: Host\n    Authentication host\n  is-for-proxy -> gboolean: For Proxy\n    Whether or not the auth is for a proxy server\n  is-authenticated -> gboolean: Authenticated\n    Whether or not the auth is authenticated\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType SoupAuth (94750593422528)>'
    __info__ = ObjectInfo(Auth)


