# encoding: utf-8
# module gi.repository.Vips
# from /usr/lib64/girepository-1.0/Vips-8.0.typelib
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


class Area(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Area()
        new(free_fn:Vips.CallbackFn, data=None) -> Vips.Area
        new_array(type:GType, sizeof_type:int, n:int) -> Vips.Area
        new_array_object(n:int) -> Vips.Area
    """
    def area_get_data(self, length, n, type, sizeof_type): # real signature unknown; restored from __doc__
        """ area_get_data(self, length:int, n:int, type:GType, sizeof_type:int) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Vips.Area """
        pass

    def new(self, free_fn, data=None): # real signature unknown; restored from __doc__
        """ new(free_fn:Vips.CallbackFn, data=None) -> Vips.Area """
        pass

    def new_array(self, type, sizeof_type, n): # real signature unknown; restored from __doc__
        """ new_array(type:GType, sizeof_type:int, n:int) -> Vips.Area """
        pass

    def new_array_object(self, n): # real signature unknown; restored from __doc__
        """ new_array_object(n:int) -> Vips.Area """
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

    count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    free_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sizeof_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Area), '__module__': 'gi.repository.Vips', '__gtype__': <GType VipsArea (94317410437408)>, '__dict__': <attribute '__dict__' of 'Area' objects>, '__weakref__': <attribute '__weakref__' of 'Area' objects>, '__doc__': None, 'data': <property object at 0x7f41868c8090>, 'length': <property object at 0x7f41868c80e0>, 'n': <property object at 0x7f41868c8130>, 'count': <property object at 0x7f41868c8180>, 'lock': <property object at 0x7f41868c8270>, 'free_fn': <property object at 0x7f41868c8360>, 'type': <property object at 0x7f41868c8450>, 'sizeof_type': <property object at 0x7f41868c8540>, 'new': gi.FunctionInfo(new), 'new_array': gi.FunctionInfo(new_array), 'new_array_object': gi.FunctionInfo(new_array_object), 'area_get_data': gi.FunctionInfo(area_get_data), 'copy': gi.FunctionInfo(copy), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType VipsArea (94317410437408)>'
    __info__ = StructInfo(Area)


