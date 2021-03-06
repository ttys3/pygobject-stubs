# encoding: utf-8
# module gi.repository.WebKit2
# from /usr/lib64/girepository-1.0/WebKit2-4.0.typelib
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
import gobject as __gobject


class ContextMenuAction(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BOLD = 27
    COPY = 14
    COPY_AUDIO_LINK_TO_CLIPBOARD = 35
    COPY_IMAGE_TO_CLIPBOARD = 7
    COPY_IMAGE_URL_TO_CLIPBOARD = 8
    COPY_LINK_TO_CLIPBOARD = 4
    COPY_VIDEO_LINK_TO_CLIPBOARD = 34
    CUSTOM = 10000
    CUT = 15
    DELETE = 17
    DOWNLOAD_AUDIO_TO_DISK = 43
    DOWNLOAD_IMAGE_TO_DISK = 6
    DOWNLOAD_LINK_TO_DISK = 3
    DOWNLOAD_VIDEO_TO_DISK = 42
    ENTER_VIDEO_FULLSCREEN = 38
    FONT_MENU = 26
    GO_BACK = 10
    GO_FORWARD = 11
    IGNORE_GRAMMAR = 25
    IGNORE_SPELLING = 23
    INPUT_METHODS = 19
    INSERT_EMOJI = 44
    INSPECT_ELEMENT = 31
    ITALIC = 28
    LEARN_SPELLING = 24
    MEDIA_MUTE = 41
    MEDIA_PAUSE = 40
    MEDIA_PLAY = 39
    NO_ACTION = 0
    NO_GUESSES_FOUND = 22
    OPEN_AUDIO_IN_NEW_WINDOW = 33
    OPEN_FRAME_IN_NEW_WINDOW = 9
    OPEN_IMAGE_IN_NEW_WINDOW = 5
    OPEN_LINK = 1
    OPEN_LINK_IN_NEW_WINDOW = 2
    OPEN_VIDEO_IN_NEW_WINDOW = 32
    OUTLINE = 30
    PASTE = 16
    RELOAD = 13
    SELECT_ALL = 18
    SPELLING_GUESS = 21
    STOP = 12
    TOGGLE_MEDIA_CONTROLS = 36
    TOGGLE_MEDIA_LOOP = 37
    UNDERLINE = 29
    UNICODE = 20
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.WebKit2', '__dict__': <attribute '__dict__' of 'ContextMenuAction' objects>, '__doc__': None, '__gtype__': <GType WebKitContextMenuAction (94869774633056)>, '__enum_values__': {0: <enum WEBKIT_CONTEXT_MENU_ACTION_NO_ACTION of type WebKit2.ContextMenuAction>, 1: <enum WEBKIT_CONTEXT_MENU_ACTION_OPEN_LINK of type WebKit2.ContextMenuAction>, 2: <enum WEBKIT_CONTEXT_MENU_ACTION_OPEN_LINK_IN_NEW_WINDOW of type WebKit2.ContextMenuAction>, 3: <enum WEBKIT_CONTEXT_MENU_ACTION_DOWNLOAD_LINK_TO_DISK of type WebKit2.ContextMenuAction>, 4: <enum WEBKIT_CONTEXT_MENU_ACTION_COPY_LINK_TO_CLIPBOARD of type WebKit2.ContextMenuAction>, 5: <enum WEBKIT_CONTEXT_MENU_ACTION_OPEN_IMAGE_IN_NEW_WINDOW of type WebKit2.ContextMenuAction>, 6: <enum WEBKIT_CONTEXT_MENU_ACTION_DOWNLOAD_IMAGE_TO_DISK of type WebKit2.ContextMenuAction>, 7: <enum WEBKIT_CONTEXT_MENU_ACTION_COPY_IMAGE_TO_CLIPBOARD of type WebKit2.ContextMenuAction>, 8: <enum WEBKIT_CONTEXT_MENU_ACTION_COPY_IMAGE_URL_TO_CLIPBOARD of type WebKit2.ContextMenuAction>, 9: <enum WEBKIT_CONTEXT_MENU_ACTION_OPEN_FRAME_IN_NEW_WINDOW of type WebKit2.ContextMenuAction>, 10: <enum WEBKIT_CONTEXT_MENU_ACTION_GO_BACK of type WebKit2.ContextMenuAction>, 11: <enum WEBKIT_CONTEXT_MENU_ACTION_GO_FORWARD of type WebKit2.ContextMenuAction>, 12: <enum WEBKIT_CONTEXT_MENU_ACTION_STOP of type WebKit2.ContextMenuAction>, 13: <enum WEBKIT_CONTEXT_MENU_ACTION_RELOAD of type WebKit2.ContextMenuAction>, 14: <enum WEBKIT_CONTEXT_MENU_ACTION_COPY of type WebKit2.ContextMenuAction>, 15: <enum WEBKIT_CONTEXT_MENU_ACTION_CUT of type WebKit2.ContextMenuAction>, 16: <enum WEBKIT_CONTEXT_MENU_ACTION_PASTE of type WebKit2.ContextMenuAction>, 17: <enum WEBKIT_CONTEXT_MENU_ACTION_DELETE of type WebKit2.ContextMenuAction>, 18: <enum WEBKIT_CONTEXT_MENU_ACTION_SELECT_ALL of type WebKit2.ContextMenuAction>, 19: <enum WEBKIT_CONTEXT_MENU_ACTION_INPUT_METHODS of type WebKit2.ContextMenuAction>, 20: <enum WEBKIT_CONTEXT_MENU_ACTION_UNICODE of type WebKit2.ContextMenuAction>, 21: <enum WEBKIT_CONTEXT_MENU_ACTION_SPELLING_GUESS of type WebKit2.ContextMenuAction>, 22: <enum WEBKIT_CONTEXT_MENU_ACTION_NO_GUESSES_FOUND of type WebKit2.ContextMenuAction>, 23: <enum WEBKIT_CONTEXT_MENU_ACTION_IGNORE_SPELLING of type WebKit2.ContextMenuAction>, 24: <enum WEBKIT_CONTEXT_MENU_ACTION_LEARN_SPELLING of type WebKit2.ContextMenuAction>, 25: <enum WEBKIT_CONTEXT_MENU_ACTION_IGNORE_GRAMMAR of type WebKit2.ContextMenuAction>, 26: <enum WEBKIT_CONTEXT_MENU_ACTION_FONT_MENU of type WebKit2.ContextMenuAction>, 27: <enum WEBKIT_CONTEXT_MENU_ACTION_BOLD of type WebKit2.ContextMenuAction>, 28: <enum WEBKIT_CONTEXT_MENU_ACTION_ITALIC of type WebKit2.ContextMenuAction>, 29: <enum WEBKIT_CONTEXT_MENU_ACTION_UNDERLINE of type WebKit2.ContextMenuAction>, 30: <enum WEBKIT_CONTEXT_MENU_ACTION_OUTLINE of type WebKit2.ContextMenuAction>, 31: <enum WEBKIT_CONTEXT_MENU_ACTION_INSPECT_ELEMENT of type WebKit2.ContextMenuAction>, 32: <enum WEBKIT_CONTEXT_MENU_ACTION_OPEN_VIDEO_IN_NEW_WINDOW of type WebKit2.ContextMenuAction>, 33: <enum WEBKIT_CONTEXT_MENU_ACTION_OPEN_AUDIO_IN_NEW_WINDOW of type WebKit2.ContextMenuAction>, 34: <enum WEBKIT_CONTEXT_MENU_ACTION_COPY_VIDEO_LINK_TO_CLIPBOARD of type WebKit2.ContextMenuAction>, 35: <enum WEBKIT_CONTEXT_MENU_ACTION_COPY_AUDIO_LINK_TO_CLIPBOARD of type WebKit2.ContextMenuAction>, 36: <enum WEBKIT_CONTEXT_MENU_ACTION_TOGGLE_MEDIA_CONTROLS of type WebKit2.ContextMenuAction>, 37: <enum WEBKIT_CONTEXT_MENU_ACTION_TOGGLE_MEDIA_LOOP of type WebKit2.ContextMenuAction>, 38: <enum WEBKIT_CONTEXT_MENU_ACTION_ENTER_VIDEO_FULLSCREEN of type WebKit2.ContextMenuAction>, 39: <enum WEBKIT_CONTEXT_MENU_ACTION_MEDIA_PLAY of type WebKit2.ContextMenuAction>, 40: <enum WEBKIT_CONTEXT_MENU_ACTION_MEDIA_PAUSE of type WebKit2.ContextMenuAction>, 41: <enum WEBKIT_CONTEXT_MENU_ACTION_MEDIA_MUTE of type WebKit2.ContextMenuAction>, 42: <enum WEBKIT_CONTEXT_MENU_ACTION_DOWNLOAD_VIDEO_TO_DISK of type WebKit2.ContextMenuAction>, 43: <enum WEBKIT_CONTEXT_MENU_ACTION_DOWNLOAD_AUDIO_TO_DISK of type WebKit2.ContextMenuAction>, 44: <enum WEBKIT_CONTEXT_MENU_ACTION_INSERT_EMOJI of type WebKit2.ContextMenuAction>, 10000: <enum WEBKIT_CONTEXT_MENU_ACTION_CUSTOM of type WebKit2.ContextMenuAction>}, '__info__': gi.EnumInfo(ContextMenuAction), 'NO_ACTION': <enum WEBKIT_CONTEXT_MENU_ACTION_NO_ACTION of type WebKit2.ContextMenuAction>, 'OPEN_LINK': <enum WEBKIT_CONTEXT_MENU_ACTION_OPEN_LINK of type WebKit2.ContextMenuAction>, 'OPEN_LINK_IN_NEW_WINDOW': <enum WEBKIT_CONTEXT_MENU_ACTION_OPEN_LINK_IN_NEW_WINDOW of type WebKit2.ContextMenuAction>, 'DOWNLOAD_LINK_TO_DISK': <enum WEBKIT_CONTEXT_MENU_ACTION_DOWNLOAD_LINK_TO_DISK of type WebKit2.ContextMenuAction>, 'COPY_LINK_TO_CLIPBOARD': <enum WEBKIT_CONTEXT_MENU_ACTION_COPY_LINK_TO_CLIPBOARD of type WebKit2.ContextMenuAction>, 'OPEN_IMAGE_IN_NEW_WINDOW': <enum WEBKIT_CONTEXT_MENU_ACTION_OPEN_IMAGE_IN_NEW_WINDOW of type WebKit2.ContextMenuAction>, 'DOWNLOAD_IMAGE_TO_DISK': <enum WEBKIT_CONTEXT_MENU_ACTION_DOWNLOAD_IMAGE_TO_DISK of type WebKit2.ContextMenuAction>, 'COPY_IMAGE_TO_CLIPBOARD': <enum WEBKIT_CONTEXT_MENU_ACTION_COPY_IMAGE_TO_CLIPBOARD of type WebKit2.ContextMenuAction>, 'COPY_IMAGE_URL_TO_CLIPBOARD': <enum WEBKIT_CONTEXT_MENU_ACTION_COPY_IMAGE_URL_TO_CLIPBOARD of type WebKit2.ContextMenuAction>, 'OPEN_FRAME_IN_NEW_WINDOW': <enum WEBKIT_CONTEXT_MENU_ACTION_OPEN_FRAME_IN_NEW_WINDOW of type WebKit2.ContextMenuAction>, 'GO_BACK': <enum WEBKIT_CONTEXT_MENU_ACTION_GO_BACK of type WebKit2.ContextMenuAction>, 'GO_FORWARD': <enum WEBKIT_CONTEXT_MENU_ACTION_GO_FORWARD of type WebKit2.ContextMenuAction>, 'STOP': <enum WEBKIT_CONTEXT_MENU_ACTION_STOP of type WebKit2.ContextMenuAction>, 'RELOAD': <enum WEBKIT_CONTEXT_MENU_ACTION_RELOAD of type WebKit2.ContextMenuAction>, 'COPY': <enum WEBKIT_CONTEXT_MENU_ACTION_COPY of type WebKit2.ContextMenuAction>, 'CUT': <enum WEBKIT_CONTEXT_MENU_ACTION_CUT of type WebKit2.ContextMenuAction>, 'PASTE': <enum WEBKIT_CONTEXT_MENU_ACTION_PASTE of type WebKit2.ContextMenuAction>, 'DELETE': <enum WEBKIT_CONTEXT_MENU_ACTION_DELETE of type WebKit2.ContextMenuAction>, 'SELECT_ALL': <enum WEBKIT_CONTEXT_MENU_ACTION_SELECT_ALL of type WebKit2.ContextMenuAction>, 'INPUT_METHODS': <enum WEBKIT_CONTEXT_MENU_ACTION_INPUT_METHODS of type WebKit2.ContextMenuAction>, 'UNICODE': <enum WEBKIT_CONTEXT_MENU_ACTION_UNICODE of type WebKit2.ContextMenuAction>, 'SPELLING_GUESS': <enum WEBKIT_CONTEXT_MENU_ACTION_SPELLING_GUESS of type WebKit2.ContextMenuAction>, 'NO_GUESSES_FOUND': <enum WEBKIT_CONTEXT_MENU_ACTION_NO_GUESSES_FOUND of type WebKit2.ContextMenuAction>, 'IGNORE_SPELLING': <enum WEBKIT_CONTEXT_MENU_ACTION_IGNORE_SPELLING of type WebKit2.ContextMenuAction>, 'LEARN_SPELLING': <enum WEBKIT_CONTEXT_MENU_ACTION_LEARN_SPELLING of type WebKit2.ContextMenuAction>, 'IGNORE_GRAMMAR': <enum WEBKIT_CONTEXT_MENU_ACTION_IGNORE_GRAMMAR of type WebKit2.ContextMenuAction>, 'FONT_MENU': <enum WEBKIT_CONTEXT_MENU_ACTION_FONT_MENU of type WebKit2.ContextMenuAction>, 'BOLD': <enum WEBKIT_CONTEXT_MENU_ACTION_BOLD of type WebKit2.ContextMenuAction>, 'ITALIC': <enum WEBKIT_CONTEXT_MENU_ACTION_ITALIC of type WebKit2.ContextMenuAction>, 'UNDERLINE': <enum WEBKIT_CONTEXT_MENU_ACTION_UNDERLINE of type WebKit2.ContextMenuAction>, 'OUTLINE': <enum WEBKIT_CONTEXT_MENU_ACTION_OUTLINE of type WebKit2.ContextMenuAction>, 'INSPECT_ELEMENT': <enum WEBKIT_CONTEXT_MENU_ACTION_INSPECT_ELEMENT of type WebKit2.ContextMenuAction>, 'OPEN_VIDEO_IN_NEW_WINDOW': <enum WEBKIT_CONTEXT_MENU_ACTION_OPEN_VIDEO_IN_NEW_WINDOW of type WebKit2.ContextMenuAction>, 'OPEN_AUDIO_IN_NEW_WINDOW': <enum WEBKIT_CONTEXT_MENU_ACTION_OPEN_AUDIO_IN_NEW_WINDOW of type WebKit2.ContextMenuAction>, 'COPY_VIDEO_LINK_TO_CLIPBOARD': <enum WEBKIT_CONTEXT_MENU_ACTION_COPY_VIDEO_LINK_TO_CLIPBOARD of type WebKit2.ContextMenuAction>, 'COPY_AUDIO_LINK_TO_CLIPBOARD': <enum WEBKIT_CONTEXT_MENU_ACTION_COPY_AUDIO_LINK_TO_CLIPBOARD of type WebKit2.ContextMenuAction>, 'TOGGLE_MEDIA_CONTROLS': <enum WEBKIT_CONTEXT_MENU_ACTION_TOGGLE_MEDIA_CONTROLS of type WebKit2.ContextMenuAction>, 'TOGGLE_MEDIA_LOOP': <enum WEBKIT_CONTEXT_MENU_ACTION_TOGGLE_MEDIA_LOOP of type WebKit2.ContextMenuAction>, 'ENTER_VIDEO_FULLSCREEN': <enum WEBKIT_CONTEXT_MENU_ACTION_ENTER_VIDEO_FULLSCREEN of type WebKit2.ContextMenuAction>, 'MEDIA_PLAY': <enum WEBKIT_CONTEXT_MENU_ACTION_MEDIA_PLAY of type WebKit2.ContextMenuAction>, 'MEDIA_PAUSE': <enum WEBKIT_CONTEXT_MENU_ACTION_MEDIA_PAUSE of type WebKit2.ContextMenuAction>, 'MEDIA_MUTE': <enum WEBKIT_CONTEXT_MENU_ACTION_MEDIA_MUTE of type WebKit2.ContextMenuAction>, 'DOWNLOAD_VIDEO_TO_DISK': <enum WEBKIT_CONTEXT_MENU_ACTION_DOWNLOAD_VIDEO_TO_DISK of type WebKit2.ContextMenuAction>, 'DOWNLOAD_AUDIO_TO_DISK': <enum WEBKIT_CONTEXT_MENU_ACTION_DOWNLOAD_AUDIO_TO_DISK of type WebKit2.ContextMenuAction>, 'INSERT_EMOJI': <enum WEBKIT_CONTEXT_MENU_ACTION_INSERT_EMOJI of type WebKit2.ContextMenuAction>, 'CUSTOM': <enum WEBKIT_CONTEXT_MENU_ACTION_CUSTOM of type WebKit2.ContextMenuAction>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
        29: 29,
        30: 30,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38,
        39: 39,
        40: 40,
        41: 41,
        42: 42,
        43: 43,
        44: 44,
        10000: 10000,
    }
    __gtype__ = None # (!) real value is '<GType WebKitContextMenuAction (94869774633056)>'
    __info__ = gi.EnumInfo(ContextMenuAction)


