# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


from .object import object

class ValueList(object):
    """
    :Constructors:
    
    ::
    
        ValueList(**properties)
    """
    def append_and_take_value(self, value, append_value): # real signature unknown; restored from __doc__
        """ append_and_take_value(value:GObject.Value, append_value:GObject.Value) """
        pass

    def append_value(self, value, append_value): # real signature unknown; restored from __doc__
        """ append_value(value:GObject.Value, append_value:GObject.Value) """
        pass

    def concat(self, value1, value2): # real signature unknown; restored from __doc__
        """ concat(value1:GObject.Value, value2:GObject.Value) -> dest:GObject.Value """
        pass

    def get_size(self, value): # real signature unknown; restored from __doc__
        """ get_size(value:GObject.Value) -> int """
        return 0

    def get_value(self, value, index): # real signature unknown; restored from __doc__
        """ get_value(value:GObject.Value, index:int) -> GObject.Value """
        pass

    def merge(self, value1, value2): # real signature unknown; restored from __doc__
        """ merge(value1:GObject.Value, value2:GObject.Value) -> dest:GObject.Value """
        pass

    def prepend_value(self, value, prepend_value): # real signature unknown; restored from __doc__
        """ prepend_value(value:GObject.Value, prepend_value:GObject.Value) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ValueList), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstValueList (228)>, '__dict__': <attribute '__dict__' of 'ValueList' objects>, '__weakref__': <attribute '__weakref__' of 'ValueList' objects>, '__doc__': None, '__gsignals__': {}, 'append_and_take_value': gi.FunctionInfo(append_and_take_value), 'append_value': gi.FunctionInfo(append_value), 'concat': gi.FunctionInfo(concat), 'get_size': gi.FunctionInfo(get_size), 'get_value': gi.FunctionInfo(get_value), 'merge': gi.FunctionInfo(merge), 'prepend_value': gi.FunctionInfo(prepend_value)})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstValueList (228)>'
    __info__ = ObjectInfo(ValueList)


