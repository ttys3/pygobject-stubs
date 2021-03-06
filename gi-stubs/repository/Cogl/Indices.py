# encoding: utf-8
# module gi.repository.Cogl
# from /usr/lib64/girepository-1.0/Cogl-1.0.typelib
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
import gobject as __gobject


from .Object import Object

class Indices(Object):
    """
    :Constructors:
    
    ::
    
        Indices(**properties)
        new(context:Cogl.Context, type:Cogl.IndicesType, indices_data=None, n_indices:int) -> Cogl.Indices
        new_for_buffer(type:Cogl.IndicesType, buffer:Cogl.IndexBuffer, offset:int) -> Cogl.Indices
    """
    def get_offset(self): # real signature unknown; restored from __doc__
        """ get_offset(self) -> int """
        return 0

    def get_type(self): # real signature unknown; restored from __doc__
        """ get_type(self) -> Cogl.IndicesType """
        pass

    def new(self, context, type, indices_data=None, n_indices): # real signature unknown; restored from __doc__
        """ new(context:Cogl.Context, type:Cogl.IndicesType, indices_data=None, n_indices:int) -> Cogl.Indices """
        pass

    def new_for_buffer(self, type, buffer, offset): # real signature unknown; restored from __doc__
        """ new_for_buffer(type:Cogl.IndicesType, buffer:Cogl.IndexBuffer, offset:int) -> Cogl.Indices """
        pass

    def set_offset(self, offset): # real signature unknown; restored from __doc__
        """ set_offset(self, offset:int) """
        pass

    def value_get_object(self, value): # real signature unknown; restored from __doc__
        """ value_get_object(value:GObject.Value) """
        pass

    def value_set_object(self, value, p_object=None): # real signature unknown; restored from __doc__
        """ value_set_object(value:GObject.Value, object=None) """
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Indices), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglIndices (93970932155504)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_for_buffer': gi.FunctionInfo(new_for_buffer), 'get_offset': gi.FunctionInfo(get_offset), 'get_type': gi.FunctionInfo(get_type), 'set_offset': gi.FunctionInfo(set_offset)})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CoglIndices (93970932155504)>'
    __info__ = ObjectInfo(Indices)


