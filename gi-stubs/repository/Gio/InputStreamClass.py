# encoding: utf-8
# module gi.repository.Gio
# from /usr/lib64/girepository-1.0/Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class InputStreamClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        InputStreamClass()
    """
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

    close_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    close_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    close_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skip_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skip_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(InputStreamClass), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'InputStreamClass' objects>, '__weakref__': <attribute '__weakref__' of 'InputStreamClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f28ddea1900>, 'read_fn': <property object at 0x7f28ddea19f0>, 'skip': <property object at 0x7f28ddea1ae0>, 'close_fn': <property object at 0x7f28ddea1bd0>, 'read_async': <property object at 0x7f28ddea1cc0>, 'read_finish': <property object at 0x7f28ddea1db0>, 'skip_async': <property object at 0x7f28ddea1ea0>, 'skip_finish': <property object at 0x7f28ddea1f90>, 'close_async': <property object at 0x7f28ddea20e0>, 'close_finish': <property object at 0x7f28ddea21d0>, '_g_reserved1': <property object at 0x7f28ddea22c0>, '_g_reserved2': <property object at 0x7f28ddea23b0>, '_g_reserved3': <property object at 0x7f28ddea24a0>, '_g_reserved4': <property object at 0x7f28ddea2590>, '_g_reserved5': <property object at 0x7f28ddea2680>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(InputStreamClass)


