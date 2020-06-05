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


class VfsClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        VfsClass()
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

    add_writable_namespaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deserialize_icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_file_for_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_file_for_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_supported_uri_schemes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    local_file_add_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    local_file_moved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    local_file_removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    local_file_set_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parse_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VfsClass), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'VfsClass' objects>, '__weakref__': <attribute '__weakref__' of 'VfsClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f28dd60bef0>, 'is_active': <property object at 0x7f28dd610040>, 'get_file_for_path': <property object at 0x7f28dd610180>, 'get_file_for_uri': <property object at 0x7f28dd610270>, 'get_supported_uri_schemes': <property object at 0x7f28dd610360>, 'parse_name': <property object at 0x7f28dd610400>, 'local_file_add_info': <property object at 0x7f28dd610540>, 'add_writable_namespaces': <property object at 0x7f28dd610680>, 'local_file_set_attributes': <property object at 0x7f28dd6107c0>, 'local_file_removed': <property object at 0x7f28dd610900>, 'local_file_moved': <property object at 0x7f28dd610a40>, 'deserialize_icon': <property object at 0x7f28dd610b80>, '_g_reserved1': <property object at 0x7f28dd610c70>, '_g_reserved2': <property object at 0x7f28dd610d60>, '_g_reserved3': <property object at 0x7f28dd610e50>, '_g_reserved4': <property object at 0x7f28dd610f40>, '_g_reserved5': <property object at 0x7f28dd60f090>, '_g_reserved6': <property object at 0x7f28dd60f180>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(VfsClass)


