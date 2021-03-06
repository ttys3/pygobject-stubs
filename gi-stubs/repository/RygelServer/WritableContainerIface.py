# encoding: utf-8
# module gi.repository.RygelServer
# from /usr/lib64/girepository-1.0/RygelServer-2.6.typelib
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
import gi.repository.Gee as __gi_repository_Gee
import gi.repository.GUPnP as __gi_repository_GUPnP
import gi.repository.RygelCore as __gi_repository_RygelCore
import gobject as __gobject


class WritableContainerIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        WritableContainerIface()
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

    add_container = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add_container_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add_item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add_item_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add_reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add_reference_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_create_classes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_container = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_container_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_item_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_create_classes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(WritableContainerIface), '__module__': 'gi.repository.RygelServer', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'WritableContainerIface' objects>, '__weakref__': <attribute '__weakref__' of 'WritableContainerIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7fe1d1692a90>, 'add_item': <property object at 0x7fe1d1692b80>, 'add_item_finish': <property object at 0x7fe1d1692c70>, 'add_container': <property object at 0x7fe1d1692d60>, 'add_container_finish': <property object at 0x7fe1d1692ea0>, 'add_reference': <property object at 0x7fe1d1692f40>, 'add_reference_finish': <property object at 0x7fe1d16940e0>, 'remove_item': <property object at 0x7fe1d1694180>, 'remove_item_finish': <property object at 0x7fe1d16942c0>, 'remove_container': <property object at 0x7fe1d16943b0>, 'remove_container_finish': <property object at 0x7fe1d16944a0>, 'get_create_classes': <property object at 0x7fe1d1694590>, 'set_create_classes': <property object at 0x7fe1d1694680>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(WritableContainerIface)


