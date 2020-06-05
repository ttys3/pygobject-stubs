# encoding: utf-8
# module gi.repository.GObject
# from /usr/lib64/girepository-1.0/GObject-2.0.typelib
# by generator 1.147
# no doc

# imports
from gi.repository.GLib import (GError, IO_ERR, IO_FLAG_APPEND, 
    IO_FLAG_GET_MASK, IO_FLAG_IS_READABLE, IO_FLAG_IS_SEEKABLE, 
    IO_FLAG_IS_WRITEABLE, IO_FLAG_MASK, IO_FLAG_NONBLOCK, IO_FLAG_SET_MASK, 
    IO_HUP, IO_IN, IO_NVAL, IO_OUT, IO_PRI, IO_STATUS_AGAIN, IO_STATUS_EOF, 
    IO_STATUS_ERROR, IO_STATUS_NORMAL, OPTION_ERROR_BAD_VALUE, 
    OPTION_ERROR_FAILED, OPTION_ERROR_UNKNOWN_OPTION, OPTION_FLAG_FILENAME, 
    OPTION_FLAG_HIDDEN, OPTION_FLAG_IN_MAIN, OPTION_FLAG_NOALIAS, 
    OPTION_FLAG_NO_ARG, OPTION_FLAG_OPTIONAL_ARG, OPTION_FLAG_REVERSE, 
    SPAWN_CHILD_INHERITS_STDIN, SPAWN_DO_NOT_REAP_CHILD, 
    SPAWN_FILE_AND_ARGV_ZERO, SPAWN_LEAVE_DESCRIPTORS_OPEN, SPAWN_SEARCH_PATH, 
    SPAWN_STDERR_TO_DEV_NULL, SPAWN_STDOUT_TO_DEV_NULL, 
    filename_display_basename, filename_display_name, get_application_name, 
    get_prgname, main_context_default, main_depth, set_application_name, 
    set_prgname, source_remove, uri_list_extract_uris)

from gi._gi import (GObjectWeakRef, OptionContext, OptionGroup, Pid, 
    add_emission_hook, list_properties, new, signal_new, spawn_async, 
    type_register)

from gobject import (GBoxed, GEnum, GFlags, GInterface, GParamSpec, GPointer, 
    GType, Warning)

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GLib as __gi_repository_GLib
import gi._signalhelper as __gi__signalhelper
import gobject as __gobject


class Closure(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Closure()
        new_object(sizeof_closure:int, object:GObject.Object) -> GObject.Closure
        new_simple(sizeof_closure:int, data=None) -> GObject.Closure
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def invoke(self, param_values, invocation_hint=None): # real signature unknown; restored from __doc__
        """ invoke(self, param_values:list, invocation_hint=None) -> return_value:GObject.Value """
        pass

    def new_object(self, sizeof_closure, p_object): # real signature unknown; restored from __doc__
        """ new_object(sizeof_closure:int, object:GObject.Object) -> GObject.Closure """
        pass

    def new_simple(self, sizeof_closure, data=None): # real signature unknown; restored from __doc__
        """ new_simple(sizeof_closure:int, data=None) -> GObject.Closure """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GObject.Closure """
        pass

    def sink(self): # real signature unknown; restored from __doc__
        """ sink(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    derivative_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    floating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    in_inotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    in_marshal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_invalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    marshal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    meta_marshal_nouse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    notifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_fnotifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_guards = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_inotifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Closure), '__module__': 'gi.repository.GObject', '__gtype__': <GType GClosure (93895379323328)>, '__dict__': <attribute '__dict__' of 'Closure' objects>, '__weakref__': <attribute '__weakref__' of 'Closure' objects>, '__doc__': None, 'ref_count': <property object at 0x7f7c286b7630>, 'meta_marshal_nouse': <property object at 0x7f7c286b7680>, 'n_guards': <property object at 0x7f7c286b7770>, 'n_fnotifiers': <property object at 0x7f7c286b7860>, 'n_inotifiers': <property object at 0x7f7c286b7950>, 'in_inotify': <property object at 0x7f7c286b7a40>, 'floating': <property object at 0x7f7c286b7b30>, 'derivative_flag': <property object at 0x7f7c286b7c20>, 'in_marshal': <property object at 0x7f7c286b7d10>, 'is_invalid': <property object at 0x7f7c286b7e00>, 'marshal': <property object at 0x7f7c286b7ef0>, 'data': <property object at 0x7f7c286b8040>, 'notifiers': <property object at 0x7f7c286b8130>, 'new_object': gi.FunctionInfo(new_object), 'new_simple': gi.FunctionInfo(new_simple), 'invalidate': gi.FunctionInfo(invalidate), 'invoke': gi.FunctionInfo(invoke), 'ref': gi.FunctionInfo(ref), 'sink': gi.FunctionInfo(sink), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType GClosure (93895379323328)>'
    __info__ = StructInfo(Closure)


