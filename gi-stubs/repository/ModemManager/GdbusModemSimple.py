# encoding: utf-8
# module gi.repository.ModemManager
# from /usr/lib64/girepository-1.0/ModemManager-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class GdbusModemSimple(__gobject.GInterface):
    # no doc
    def call_connect(self, arg_properties, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_connect(self, arg_properties:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_connect_finish(self, res): # real signature unknown; restored from __doc__
        """ call_connect_finish(self, res:Gio.AsyncResult) -> out_bearer:str """
        pass

    def call_connect_sync(self, arg_properties, cancellable=None): # real signature unknown; restored from __doc__
        """ call_connect_sync(self, arg_properties:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_bearer:str """
        pass

    def call_disconnect(self, arg_bearer, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_disconnect(self, arg_bearer:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_disconnect_finish(self, res): # real signature unknown; restored from __doc__
        """ call_disconnect_finish(self, res:Gio.AsyncResult) """
        pass

    def call_disconnect_sync(self, arg_bearer, cancellable=None): # real signature unknown; restored from __doc__
        """ call_disconnect_sync(self, arg_bearer:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_get_status(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_get_status(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_get_status_finish(self, res): # real signature unknown; restored from __doc__
        """ call_get_status_finish(self, res:Gio.AsyncResult) -> out_properties:GLib.Variant """
        pass

    def call_get_status_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_get_status_sync(self, cancellable:Gio.Cancellable=None) -> out_properties:GLib.Variant """
        pass

    def complete_connect(self, invocation, bearer): # real signature unknown; restored from __doc__
        """ complete_connect(self, invocation:Gio.DBusMethodInvocation, bearer:str) """
        pass

    def complete_disconnect(self, invocation): # real signature unknown; restored from __doc__
        """ complete_disconnect(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_get_status(self, invocation, properties): # real signature unknown; restored from __doc__
        """ complete_get_status(self, invocation:Gio.DBusMethodInvocation, properties:GLib.Variant) """
        pass

    def interface_info(self): # real signature unknown; restored from __doc__
        """ interface_info() -> Gio.DBusInterfaceInfo """
        pass

    def override_properties(self, klass, property_id_begin): # real signature unknown; restored from __doc__
        """ override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
        return 0

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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(GdbusModemSimple), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType MmGdbusModemSimple (94631948283504)>, '__dict__': <attribute '__dict__' of 'GdbusModemSimple' objects>, '__weakref__': <attribute '__weakref__' of 'GdbusModemSimple' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_connect': gi.FunctionInfo(call_connect), 'call_connect_finish': gi.FunctionInfo(call_connect_finish), 'call_connect_sync': gi.FunctionInfo(call_connect_sync), 'call_disconnect': gi.FunctionInfo(call_disconnect), 'call_disconnect_finish': gi.FunctionInfo(call_disconnect_finish), 'call_disconnect_sync': gi.FunctionInfo(call_disconnect_sync), 'call_get_status': gi.FunctionInfo(call_get_status), 'call_get_status_finish': gi.FunctionInfo(call_get_status_finish), 'call_get_status_sync': gi.FunctionInfo(call_get_status_sync), 'complete_connect': gi.FunctionInfo(complete_connect), 'complete_disconnect': gi.FunctionInfo(complete_disconnect), 'complete_get_status': gi.FunctionInfo(complete_get_status)})"
    __gdoc__ = 'Interface MmGdbusModemSimple\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType MmGdbusModemSimple (94631948283504)>'
    __info__ = InterfaceInfo(GdbusModemSimple)


