# encoding: utf-8
# module gi.repository.GMime
# from /usr/lib64/girepository-1.0/GMime-3.0.typelib
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
import gobject as __gobject


class MultipartClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        MultipartClass()
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

    add = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    contains = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_boundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_part = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index_of = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_at = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_boundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MultipartClass), '__module__': 'gi.repository.GMime', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MultipartClass' objects>, '__weakref__': <attribute '__weakref__' of 'MultipartClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fc97073f310>, 'clear': <property object at 0x7fc97073f400>, 'add': <property object at 0x7fc97073f4f0>, 'insert': <property object at 0x7fc97073f5e0>, 'remove': <property object at 0x7fc97073f6d0>, 'remove_at': <property object at 0x7fc97073f7c0>, 'get_part': <property object at 0x7fc97073f8b0>, 'contains': <property object at 0x7fc97073f9a0>, 'index_of': <property object at 0x7fc97073fa90>, 'get_count': <property object at 0x7fc97073fb80>, 'set_boundary': <property object at 0x7fc97073fc70>, 'get_boundary': <property object at 0x7fc97073fd60>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MultipartClass)


