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


class VideoEncoderClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        VideoEncoderClass()
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

    close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    decide_allocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    element_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flush = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    getcaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    negotiate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pre_push = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    propose_allocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sink_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sink_query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src_query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform_meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VideoEncoderClass), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'VideoEncoderClass' objects>, '__weakref__': <attribute '__weakref__' of 'VideoEncoderClass' objects>, '__doc__': None, 'element_class': <property object at 0x7f930d27b590>, 'open': <property object at 0x7f930d27b680>, 'close': <property object at 0x7f930d27b770>, 'start': <property object at 0x7f930d27b860>, 'stop': <property object at 0x7f930d27b950>, 'set_format': <property object at 0x7f930d27ba40>, 'handle_frame': <property object at 0x7f930d27bb30>, 'reset': <property object at 0x7f930d27bc20>, 'finish': <property object at 0x7f930d27bd10>, 'pre_push': <property object at 0x7f930d27be00>, 'getcaps': <property object at 0x7f930d27bef0>, 'sink_event': <property object at 0x7f930d27c040>, 'src_event': <property object at 0x7f930d27c130>, 'negotiate': <property object at 0x7f930d27c220>, 'decide_allocation': <property object at 0x7f930d27c360>, 'propose_allocation': <property object at 0x7f930d27c450>, 'flush': <property object at 0x7f930d27c4f0>, 'sink_query': <property object at 0x7f930d27c5e0>, 'src_query': <property object at 0x7f930d27c6d0>, 'transform_meta': <property object at 0x7f930d27c7c0>, '_gst_reserved': <property object at 0x7f930d27c8b0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(VideoEncoderClass)


