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


class Buffer(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Buffer()
        new(data:list) -> Soup.Buffer
        new_with_owner(data:list, owner=None, owner_dnotify:GLib.DestroyNotify=None) -> Soup.Buffer
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Soup.Buffer """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_as_bytes(self): # real signature unknown; restored from __doc__
        """ get_as_bytes(self) -> GLib.Bytes """
        pass

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> data:list """
        pass

    def get_owner(self): # real signature unknown; restored from __doc__
        """ get_owner(self) """
        pass

    def new(self, data): # real signature unknown; restored from __doc__
        """ new(data:list) -> Soup.Buffer """
        pass

    def new_subbuffer(self, offset, length): # real signature unknown; restored from __doc__
        """ new_subbuffer(self, offset:int, length:int) -> Soup.Buffer """
        pass

    def new_with_owner(self, data, owner=None, owner_dnotify=None): # real signature unknown; restored from __doc__
        """ new_with_owner(data:list, owner=None, owner_dnotify:GLib.DestroyNotify=None) -> Soup.Buffer """
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

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Buffer), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupBuffer (94750594537440)>, '__dict__': <attribute '__dict__' of 'Buffer' objects>, '__weakref__': <attribute '__weakref__' of 'Buffer' objects>, '__doc__': None, 'data': <property object at 0x7f8e4860bb30>, 'length': <property object at 0x7f8e4860bc20>, 'new': gi.FunctionInfo(new), 'new_with_owner': gi.FunctionInfo(new_with_owner), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_as_bytes': gi.FunctionInfo(get_as_bytes), 'get_data': gi.FunctionInfo(get_data), 'get_owner': gi.FunctionInfo(get_owner), 'new_subbuffer': gi.FunctionInfo(new_subbuffer)})"
    __gtype__ = None # (!) real value is '<GType SoupBuffer (94750594537440)>'
    __info__ = StructInfo(Buffer)

