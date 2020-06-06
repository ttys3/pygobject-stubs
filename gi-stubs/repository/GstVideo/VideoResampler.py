# encoding: utf-8
# module gi.repository.GstVideo
# from /usr/lib64/girepository-1.0/GstVideo-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


class VideoResampler(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        VideoResampler()
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def init(self, method, flags, n_phases, n_taps, shift, in_size, out_size, options): # real signature unknown; restored from __doc__
        """ init(self, method:GstVideo.VideoResamplerMethod, flags:GstVideo.VideoResamplerFlags, n_phases:int, n_taps:int, shift:float, in_size:int, out_size:int, options:Gst.Structure) -> bool """
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

    in_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_taps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_phases = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_taps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    out_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    phase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    taps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VideoResampler), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'VideoResampler' objects>, '__weakref__': <attribute '__weakref__' of 'VideoResampler' objects>, '__doc__': None, 'in_size': <property object at 0x7f930d2a1770>, 'out_size': <property object at 0x7f930d2a1860>, 'max_taps': <property object at 0x7f930d2a1950>, 'n_phases': <property object at 0x7f930d2a1a40>, 'offset': <property object at 0x7f930d2a1b30>, 'phase': <property object at 0x7f930d2a1c20>, 'n_taps': <property object at 0x7f930d2a1d10>, 'taps': <property object at 0x7f930d2a1e00>, '_gst_reserved': <property object at 0x7f930d2a1ef0>, 'clear': gi.FunctionInfo(clear), 'init': gi.FunctionInfo(init)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(VideoResampler)


