# encoding: utf-8
# module gi.repository.Gladeui
# from /usr/lib64/girepository-1.0/Gladeui-2.0.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class PropertyClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        PropertyClass()
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

    dup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    equals_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    load = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tooltip_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PropertyClass), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'PropertyClass' objects>, '__weakref__': <attribute '__weakref__' of 'PropertyClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f1341a494a0>, 'dup': <property object at 0x7f1341a49590>, 'equals_value': <property object at 0x7f1341a49680>, 'set_value': <property object at 0x7f1341a49770>, 'get_value': <property object at 0x7f1341a49860>, 'sync': <property object at 0x7f1341a49950>, 'load': <property object at 0x7f1341a49a40>, 'value_changed': <property object at 0x7f1341a49b30>, 'tooltip_changed': <property object at 0x7f1341a49c20>, 'glade_reserved1': <property object at 0x7f1341a49d10>, 'glade_reserved2': <property object at 0x7f1341a49e00>, 'glade_reserved3': <property object at 0x7f1341a49ef0>, 'glade_reserved4': <property object at 0x7f1341a4c040>, 'glade_reserved5': <property object at 0x7f1341a4c130>, 'glade_reserved6': <property object at 0x7f1341a4c220>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(PropertyClass)


