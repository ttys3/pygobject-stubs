# encoding: utf-8
# module gi.repository.Gcr
# from /usr/lib64/girepository-1.0/Gcr-3.typelib
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
import gi.repository.Gck as __gi_repository_Gck
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class ImportInteraction(__gobject.GInterface):
    # no doc
    def supplement(self, builder, cancellable=None): # real signature unknown; restored from __doc__
        """ supplement(self, builder:Gck.Builder, cancellable:Gio.Cancellable=None) -> Gio.TlsInteractionResult """
        pass

    def supplement_async(self, builder, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ supplement_async(self, builder:Gck.Builder, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def supplement_finish(self, result): # real signature unknown; restored from __doc__
        """ supplement_finish(self, result:Gio.AsyncResult) -> Gio.TlsInteractionResult """
        pass

    def supplement_prep(self, builder): # real signature unknown; restored from __doc__
        """ supplement_prep(self, builder:Gck.Builder) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(ImportInteraction), '__module__': 'gi.repository.Gcr', '__gtype__': <GType GcrImportInteraction (94112497791392)>, '__dict__': <attribute '__dict__' of 'ImportInteraction' objects>, '__weakref__': <attribute '__weakref__' of 'ImportInteraction' objects>, '__doc__': None, '__gsignals__': {}, 'supplement': gi.FunctionInfo(supplement), 'supplement_async': gi.FunctionInfo(supplement_async), 'supplement_finish': gi.FunctionInfo(supplement_finish), 'supplement_prep': gi.FunctionInfo(supplement_prep)})"
    __gdoc__ = 'Interface GcrImportInteraction\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GcrImportInteraction (94112497791392)>'
    __info__ = InterfaceInfo(ImportInteraction)


