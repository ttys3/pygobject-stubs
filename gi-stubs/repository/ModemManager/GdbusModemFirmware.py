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


class GdbusModemFirmware(__gobject.GInterface):
    # no doc
    def call_list(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_list(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_list_finish(self, res): # real signature unknown; restored from __doc__
        """ call_list_finish(self, res:Gio.AsyncResult) -> out_selected:str, out_installed:GLib.Variant """
        pass

    def call_list_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_list_sync(self, cancellable:Gio.Cancellable=None) -> out_selected:str, out_installed:GLib.Variant """
        pass

    def call_select(self, arg_uniqueid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_select(self, arg_uniqueid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_select_finish(self, res): # real signature unknown; restored from __doc__
        """ call_select_finish(self, res:Gio.AsyncResult) """
        pass

    def call_select_sync(self, arg_uniqueid, cancellable=None): # real signature unknown; restored from __doc__
        """ call_select_sync(self, arg_uniqueid:str, cancellable:Gio.Cancellable=None) """
        pass

    def complete_list(self, invocation, selected, installed): # real signature unknown; restored from __doc__
        """ complete_list(self, invocation:Gio.DBusMethodInvocation, selected:str, installed:GLib.Variant) """
        pass

    def complete_select(self, invocation): # real signature unknown; restored from __doc__
        """ complete_select(self, invocation:Gio.DBusMethodInvocation) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(GdbusModemFirmware), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType MmGdbusModemFirmware (94631948344640)>, '__dict__': <attribute '__dict__' of 'GdbusModemFirmware' objects>, '__weakref__': <attribute '__weakref__' of 'GdbusModemFirmware' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_list': gi.FunctionInfo(call_list), 'call_list_finish': gi.FunctionInfo(call_list_finish), 'call_list_sync': gi.FunctionInfo(call_list_sync), 'call_select': gi.FunctionInfo(call_select), 'call_select_finish': gi.FunctionInfo(call_select_finish), 'call_select_sync': gi.FunctionInfo(call_select_sync), 'complete_list': gi.FunctionInfo(complete_list), 'complete_select': gi.FunctionInfo(complete_select)})"
    __gdoc__ = 'Interface MmGdbusModemFirmware\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType MmGdbusModemFirmware (94631948344640)>'
    __info__ = InterfaceInfo(GdbusModemFirmware)


