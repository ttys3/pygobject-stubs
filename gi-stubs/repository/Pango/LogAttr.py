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


class LogAttr(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        LogAttr()
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

    backspace_deletes_character = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_char_break = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_cursor_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_expandable_space = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_line_break = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_mandatory_break = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_sentence_boundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_sentence_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_sentence_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_white = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_word_boundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_word_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_word_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(LogAttr), '__module__': 'gi.repository.Pango', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'LogAttr' objects>, '__weakref__': <attribute '__weakref__' of 'LogAttr' objects>, '__doc__': None, 'is_line_break': <property object at 0x7f24746fc9a0>, 'is_mandatory_break': <property object at 0x7f24746fcae0>, 'is_char_break': <property object at 0x7f24746fcbd0>, 'is_white': <property object at 0x7f24746fccc0>, 'is_cursor_position': <property object at 0x7f24746fce00>, 'is_word_start': <property object at 0x7f24746fcef0>, 'is_word_end': <property object at 0x7f24746fd040>, 'is_sentence_boundary': <property object at 0x7f24746fd180>, 'is_sentence_start': <property object at 0x7f24746fd2c0>, 'is_sentence_end': <property object at 0x7f24746fd3b0>, 'backspace_deletes_character': <property object at 0x7f24746fd4f0>, 'is_expandable_space': <property object at 0x7f24746fd630>, 'is_word_boundary': <property object at 0x7f24746fd770>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(LogAttr)


