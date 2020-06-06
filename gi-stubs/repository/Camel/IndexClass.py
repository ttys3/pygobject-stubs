# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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


class IndexClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        IndexClass()
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

    add_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    find = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    find_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    words = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(IndexClass), '__module__': 'gi.repository.Camel', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'IndexClass' objects>, '__weakref__': <attribute '__weakref__' of 'IndexClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f7b34fe15e0>, 'sync': <property object at 0x7f7b34fe16d0>, 'compress': <property object at 0x7f7b34fe17c0>, 'delete_': <property object at 0x7f7b34fe18b0>, 'rename': <property object at 0x7f7b34fe19a0>, 'has_name': <property object at 0x7f7b34fe1a90>, 'add_name': <property object at 0x7f7b34fe1b80>, 'write_name': <property object at 0x7f7b34fe1c70>, 'find_name': <property object at 0x7f7b34fe1d60>, 'delete_name': <property object at 0x7f7b34fe1e50>, 'find': <property object at 0x7f7b34fe1f40>, 'words': <property object at 0x7f7b34fe2090>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(IndexClass)

