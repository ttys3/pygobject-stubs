# encoding: utf-8
# module gi.repository.Pango
# from /usr/lib64/girepository-1.0/Pango-1.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


class Item(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Item()
        new() -> Pango.Item
    """
    def apply_attrs(self, iter): # real signature unknown; restored from __doc__
        """ apply_attrs(self, iter:Pango.AttrIterator) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Pango.Item or None """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Pango.Item """
        pass

    def split(self, split_index, split_offset): # real signature unknown; restored from __doc__
        """ split(self, split_index:int, split_offset:int) -> Pango.Item """
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> Pango.Item """
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

    analysis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_chars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Item), '__module__': 'gi.repository.Pango', '__gtype__': <GType PangoItem (94752681037488)>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None, 'offset': <property object at 0x7f24746f9950>, 'length': <property object at 0x7f24746f9a40>, 'num_chars': <property object at 0x7f24746f9b30>, 'analysis': <property object at 0x7f24746f9c20>, 'new': gi.FunctionInfo(new), 'apply_attrs': gi.FunctionInfo(apply_attrs), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'split': gi.FunctionInfo(split), '__new__': <staticmethod object at 0x7f24746f2fa0>, '__init__': <function nothing at 0x7f2474a83430>})"
    __gtype__ = None # (!) real value is '<GType PangoItem (94752681037488)>'
    __info__ = StructInfo(Item)


