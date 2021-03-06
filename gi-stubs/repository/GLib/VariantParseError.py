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


class VariantParseError(__gobject.GEnum):
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


    BASIC_TYPE_EXPECTED = 1
    CANNOT_INFER_TYPE = 2
    DEFINITE_TYPE_EXPECTED = 3
    FAILED = 0
    INPUT_NOT_AT_END = 4
    INVALID_CHARACTER = 5
    INVALID_FORMAT_STRING = 6
    INVALID_OBJECT_PATH = 7
    INVALID_SIGNATURE = 8
    INVALID_TYPE_STRING = 9
    NO_COMMON_TYPE = 10
    NUMBER_OUT_OF_RANGE = 11
    NUMBER_TOO_BIG = 12
    RECURSION = 18
    TYPE_ERROR = 13
    UNEXPECTED_TOKEN = 14
    UNKNOWN_KEYWORD = 15
    UNTERMINATED_STRING_CONSTANT = 16
    VALUE_EXPECTED = 17
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GLib', '__dict__': <attribute '__dict__' of 'VariantParseError' objects>, '__doc__': None, '__gtype__': <GType PyGLibVariantParseError (94581033988880)>, '__enum_values__': {0: <enum G_VARIANT_PARSE_ERROR_FAILED of type GLib.VariantParseError>, 1: <enum G_VARIANT_PARSE_ERROR_BASIC_TYPE_EXPECTED of type GLib.VariantParseError>, 2: <enum G_VARIANT_PARSE_ERROR_CANNOT_INFER_TYPE of type GLib.VariantParseError>, 3: <enum G_VARIANT_PARSE_ERROR_DEFINITE_TYPE_EXPECTED of type GLib.VariantParseError>, 4: <enum G_VARIANT_PARSE_ERROR_INPUT_NOT_AT_END of type GLib.VariantParseError>, 5: <enum G_VARIANT_PARSE_ERROR_INVALID_CHARACTER of type GLib.VariantParseError>, 6: <enum G_VARIANT_PARSE_ERROR_INVALID_FORMAT_STRING of type GLib.VariantParseError>, 7: <enum G_VARIANT_PARSE_ERROR_INVALID_OBJECT_PATH of type GLib.VariantParseError>, 8: <enum G_VARIANT_PARSE_ERROR_INVALID_SIGNATURE of type GLib.VariantParseError>, 9: <enum G_VARIANT_PARSE_ERROR_INVALID_TYPE_STRING of type GLib.VariantParseError>, 10: <enum G_VARIANT_PARSE_ERROR_NO_COMMON_TYPE of type GLib.VariantParseError>, 11: <enum G_VARIANT_PARSE_ERROR_NUMBER_OUT_OF_RANGE of type GLib.VariantParseError>, 12: <enum G_VARIANT_PARSE_ERROR_NUMBER_TOO_BIG of type GLib.VariantParseError>, 13: <enum G_VARIANT_PARSE_ERROR_TYPE_ERROR of type GLib.VariantParseError>, 14: <enum G_VARIANT_PARSE_ERROR_UNEXPECTED_TOKEN of type GLib.VariantParseError>, 15: <enum G_VARIANT_PARSE_ERROR_UNKNOWN_KEYWORD of type GLib.VariantParseError>, 16: <enum G_VARIANT_PARSE_ERROR_UNTERMINATED_STRING_CONSTANT of type GLib.VariantParseError>, 17: <enum G_VARIANT_PARSE_ERROR_VALUE_EXPECTED of type GLib.VariantParseError>, 18: <enum G_VARIANT_PARSE_ERROR_RECURSION of type GLib.VariantParseError>}, '__info__': gi.EnumInfo(VariantParseError), 'FAILED': <enum G_VARIANT_PARSE_ERROR_FAILED of type GLib.VariantParseError>, 'BASIC_TYPE_EXPECTED': <enum G_VARIANT_PARSE_ERROR_BASIC_TYPE_EXPECTED of type GLib.VariantParseError>, 'CANNOT_INFER_TYPE': <enum G_VARIANT_PARSE_ERROR_CANNOT_INFER_TYPE of type GLib.VariantParseError>, 'DEFINITE_TYPE_EXPECTED': <enum G_VARIANT_PARSE_ERROR_DEFINITE_TYPE_EXPECTED of type GLib.VariantParseError>, 'INPUT_NOT_AT_END': <enum G_VARIANT_PARSE_ERROR_INPUT_NOT_AT_END of type GLib.VariantParseError>, 'INVALID_CHARACTER': <enum G_VARIANT_PARSE_ERROR_INVALID_CHARACTER of type GLib.VariantParseError>, 'INVALID_FORMAT_STRING': <enum G_VARIANT_PARSE_ERROR_INVALID_FORMAT_STRING of type GLib.VariantParseError>, 'INVALID_OBJECT_PATH': <enum G_VARIANT_PARSE_ERROR_INVALID_OBJECT_PATH of type GLib.VariantParseError>, 'INVALID_SIGNATURE': <enum G_VARIANT_PARSE_ERROR_INVALID_SIGNATURE of type GLib.VariantParseError>, 'INVALID_TYPE_STRING': <enum G_VARIANT_PARSE_ERROR_INVALID_TYPE_STRING of type GLib.VariantParseError>, 'NO_COMMON_TYPE': <enum G_VARIANT_PARSE_ERROR_NO_COMMON_TYPE of type GLib.VariantParseError>, 'NUMBER_OUT_OF_RANGE': <enum G_VARIANT_PARSE_ERROR_NUMBER_OUT_OF_RANGE of type GLib.VariantParseError>, 'NUMBER_TOO_BIG': <enum G_VARIANT_PARSE_ERROR_NUMBER_TOO_BIG of type GLib.VariantParseError>, 'TYPE_ERROR': <enum G_VARIANT_PARSE_ERROR_TYPE_ERROR of type GLib.VariantParseError>, 'UNEXPECTED_TOKEN': <enum G_VARIANT_PARSE_ERROR_UNEXPECTED_TOKEN of type GLib.VariantParseError>, 'UNKNOWN_KEYWORD': <enum G_VARIANT_PARSE_ERROR_UNKNOWN_KEYWORD of type GLib.VariantParseError>, 'UNTERMINATED_STRING_CONSTANT': <enum G_VARIANT_PARSE_ERROR_UNTERMINATED_STRING_CONSTANT of type GLib.VariantParseError>, 'VALUE_EXPECTED': <enum G_VARIANT_PARSE_ERROR_VALUE_EXPECTED of type GLib.VariantParseError>, 'RECURSION': <enum G_VARIANT_PARSE_ERROR_RECURSION of type GLib.VariantParseError>})"
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
    }
    __gtype__ = None # (!) real value is '<GType PyGLibVariantParseError (94581033988880)>'
    __info__ = gi.EnumInfo(VariantParseError)


