# encoding: utf-8
# module gi.repository.Gtk
# from /usr/lib64/girepository-1.0/Gtk-3.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class RcProperty(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        RcProperty()
    """
    def parse_border(self, pspec, gstring, property_value): # real signature unknown; restored from __doc__
        """ parse_border(pspec:GObject.ParamSpec, gstring:GLib.String, property_value:GObject.Value) -> bool """
        return False

    def parse_color(self, pspec, gstring, property_value): # real signature unknown; restored from __doc__
        """ parse_color(pspec:GObject.ParamSpec, gstring:GLib.String, property_value:GObject.Value) -> bool """
        return False

    def parse_enum(self, pspec, gstring, property_value): # real signature unknown; restored from __doc__
        """ parse_enum(pspec:GObject.ParamSpec, gstring:GLib.String, property_value:GObject.Value) -> bool """
        return False

    def parse_flags(self, pspec, gstring, property_value): # real signature unknown; restored from __doc__
        """ parse_flags(pspec:GObject.ParamSpec, gstring:GLib.String, property_value:GObject.Value) -> bool """
        return False

    def parse_requisition(self, pspec, gstring, property_value): # real signature unknown; restored from __doc__
        """ parse_requisition(pspec:GObject.ParamSpec, gstring:GLib.String, property_value:GObject.Value) -> bool """
        return False

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

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    property_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RcProperty), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'RcProperty' objects>, '__weakref__': <attribute '__weakref__' of 'RcProperty' objects>, '__doc__': None, 'type_name': <property object at 0x7fe830faf130>, 'property_name': <property object at 0x7fe830faf220>, 'origin': <property object at 0x7fe830faf310>, 'value': <property object at 0x7fe830faf400>, 'parse_border': gi.FunctionInfo(parse_border), 'parse_color': gi.FunctionInfo(parse_color), 'parse_enum': gi.FunctionInfo(parse_enum), 'parse_flags': gi.FunctionInfo(parse_flags), 'parse_requisition': gi.FunctionInfo(parse_requisition)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(RcProperty)


