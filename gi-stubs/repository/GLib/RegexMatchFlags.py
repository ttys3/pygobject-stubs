# encoding: utf-8
# module gi.repository.GLib
# from /usr/lib64/girepository-1.0/GLib-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi._option as option # /usr/lib64/python3.8/site-packages/gi/_option.py
from gi._gi import OptionContext, OptionGroup, Pid, spawn_async

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gobject as __gobject


class RegexMatchFlags(__gobject.GFlags):
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
        """ Helper for pickle. """
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

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ANCHORED = 16
    BSR_ANY = 16777216
    BSR_ANYCRLF = 8388608
    NEWLINE_ANY = 4194304
    NEWLINE_ANYCRLF = 5242880
    NEWLINE_CR = 1048576
    NEWLINE_CRLF = 3145728
    NEWLINE_LF = 2097152
    NOTBOL = 128
    NOTEMPTY = 1024
    NOTEMPTY_ATSTART = 268435456
    NOTEOL = 256
    PARTIAL = 32768
    PARTIAL_HARD = 134217728
    PARTIAL_SOFT = 32768
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GLib', '__dict__': <attribute '__dict__' of 'RegexMatchFlags' objects>, '__doc__': None, '__gtype__': <GType PyGLibRegexMatchFlags (94581033840544)>, '__flags_values__': {16: <flags G_REGEX_MATCH_ANCHORED of type GLib.RegexMatchFlags>, 128: <flags G_REGEX_MATCH_NOTBOL of type GLib.RegexMatchFlags>, 256: <flags G_REGEX_MATCH_NOTEOL of type GLib.RegexMatchFlags>, 1024: <flags G_REGEX_MATCH_NOTEMPTY of type GLib.RegexMatchFlags>, 32768: <flags G_REGEX_MATCH_PARTIAL | G_REGEX_MATCH_PARTIAL_SOFT of type GLib.RegexMatchFlags>, 1048576: <flags G_REGEX_MATCH_NEWLINE_CR of type GLib.RegexMatchFlags>, 2097152: <flags G_REGEX_MATCH_NEWLINE_LF of type GLib.RegexMatchFlags>, 3145728: <flags G_REGEX_MATCH_NEWLINE_CR | G_REGEX_MATCH_NEWLINE_LF | G_REGEX_MATCH_NEWLINE_CRLF of type GLib.RegexMatchFlags>, 4194304: <flags G_REGEX_MATCH_NEWLINE_ANY of type GLib.RegexMatchFlags>, 5242880: <flags G_REGEX_MATCH_NEWLINE_CR | G_REGEX_MATCH_NEWLINE_ANY | G_REGEX_MATCH_NEWLINE_ANYCRLF of type GLib.RegexMatchFlags>, 8388608: <flags G_REGEX_MATCH_BSR_ANYCRLF of type GLib.RegexMatchFlags>, 16777216: <flags G_REGEX_MATCH_BSR_ANY of type GLib.RegexMatchFlags>, 134217728: <flags G_REGEX_MATCH_PARTIAL_HARD of type GLib.RegexMatchFlags>, 268435456: <flags G_REGEX_MATCH_NOTEMPTY_ATSTART of type GLib.RegexMatchFlags>}, '__info__': gi.EnumInfo(RegexMatchFlags), 'ANCHORED': <flags G_REGEX_MATCH_ANCHORED of type GLib.RegexMatchFlags>, 'NOTBOL': <flags G_REGEX_MATCH_NOTBOL of type GLib.RegexMatchFlags>, 'NOTEOL': <flags G_REGEX_MATCH_NOTEOL of type GLib.RegexMatchFlags>, 'NOTEMPTY': <flags G_REGEX_MATCH_NOTEMPTY of type GLib.RegexMatchFlags>, 'PARTIAL': <flags G_REGEX_MATCH_PARTIAL | G_REGEX_MATCH_PARTIAL_SOFT of type GLib.RegexMatchFlags>, 'NEWLINE_CR': <flags G_REGEX_MATCH_NEWLINE_CR of type GLib.RegexMatchFlags>, 'NEWLINE_LF': <flags G_REGEX_MATCH_NEWLINE_LF of type GLib.RegexMatchFlags>, 'NEWLINE_CRLF': <flags G_REGEX_MATCH_NEWLINE_CR | G_REGEX_MATCH_NEWLINE_LF | G_REGEX_MATCH_NEWLINE_CRLF of type GLib.RegexMatchFlags>, 'NEWLINE_ANY': <flags G_REGEX_MATCH_NEWLINE_ANY of type GLib.RegexMatchFlags>, 'NEWLINE_ANYCRLF': <flags G_REGEX_MATCH_NEWLINE_CR | G_REGEX_MATCH_NEWLINE_ANY | G_REGEX_MATCH_NEWLINE_ANYCRLF of type GLib.RegexMatchFlags>, 'BSR_ANYCRLF': <flags G_REGEX_MATCH_BSR_ANYCRLF of type GLib.RegexMatchFlags>, 'BSR_ANY': <flags G_REGEX_MATCH_BSR_ANY of type GLib.RegexMatchFlags>, 'PARTIAL_SOFT': <flags G_REGEX_MATCH_PARTIAL | G_REGEX_MATCH_PARTIAL_SOFT of type GLib.RegexMatchFlags>, 'PARTIAL_HARD': <flags G_REGEX_MATCH_PARTIAL_HARD of type GLib.RegexMatchFlags>, 'NOTEMPTY_ATSTART': <flags G_REGEX_MATCH_NOTEMPTY_ATSTART of type GLib.RegexMatchFlags>})"
    __flags_values__ = {
        16: 16,
        128: 128,
        256: 256,
        1024: 1024,
        32768: 32768,
        1048576: 1048576,
        2097152: 2097152,
        3145728: 3145728,
        4194304: 4194304,
        5242880: 5242880,
        8388608: 8388608,
        16777216: 16777216,
        134217728: 134217728,
        268435456: 268435456,
    }
    __gtype__ = None # (!) real value is '<GType PyGLibRegexMatchFlags (94581033840544)>'
    __info__ = gi.EnumInfo(RegexMatchFlags)


