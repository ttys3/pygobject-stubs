# encoding: utf-8
# module gi.repository.PackageKitGlib
# from /usr/lib64/girepository-1.0/PackageKitGlib-1.0.typelib
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
import gobject as __gobject


class FilterEnum(__gobject.GEnum):
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

    def from_string(self, filter): # real signature unknown; restored from __doc__
        """ from_string(filter:str) -> PackageKitGlib.FilterEnum """
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

    def to_string(self, filter): # real signature unknown; restored from __doc__
        """ to_string(filter:PackageKitGlib.FilterEnum) -> str """
        return ""

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


    APPLICATION = 24
    ARCH = 18
    BASENAME = 14
    COLLECTIONS = 22
    DEVELOPMENT = 4
    DOWNLOADED = 26
    FREE = 8
    GUI = 6
    INSTALLED = 2
    LAST = 28
    NEWEST = 16
    NONE = 1
    NOT_APPLICATION = 25
    NOT_ARCH = 19
    NOT_BASENAME = 15
    NOT_COLLECTIONS = 23
    NOT_DEVELOPMENT = 5
    NOT_DOWNLOADED = 27
    NOT_FREE = 9
    NOT_GUI = 7
    NOT_INSTALLED = 3
    NOT_NEWEST = 17
    NOT_SOURCE = 21
    NOT_SUPPORTED = 13
    NOT_VISIBLE = 11
    SOURCE = 20
    SUPPORTED = 12
    UNKNOWN = 0
    VISIBLE = 10
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.PackageKitGlib', '__dict__': <attribute '__dict__' of 'FilterEnum' objects>, '__doc__': None, '__gtype__': <GType PkFilterEnum (94016447152640)>, '__enum_values__': {0: <enum PK_FILTER_ENUM_UNKNOWN of type PackageKitGlib.FilterEnum>, 1: <enum PK_FILTER_ENUM_NONE of type PackageKitGlib.FilterEnum>, 2: <enum PK_FILTER_ENUM_INSTALLED of type PackageKitGlib.FilterEnum>, 3: <enum PK_FILTER_ENUM_NOT_INSTALLED of type PackageKitGlib.FilterEnum>, 4: <enum PK_FILTER_ENUM_DEVELOPMENT of type PackageKitGlib.FilterEnum>, 5: <enum PK_FILTER_ENUM_NOT_DEVELOPMENT of type PackageKitGlib.FilterEnum>, 6: <enum PK_FILTER_ENUM_GUI of type PackageKitGlib.FilterEnum>, 7: <enum PK_FILTER_ENUM_NOT_GUI of type PackageKitGlib.FilterEnum>, 8: <enum PK_FILTER_ENUM_FREE of type PackageKitGlib.FilterEnum>, 9: <enum PK_FILTER_ENUM_NOT_FREE of type PackageKitGlib.FilterEnum>, 10: <enum PK_FILTER_ENUM_VISIBLE of type PackageKitGlib.FilterEnum>, 11: <enum PK_FILTER_ENUM_NOT_VISIBLE of type PackageKitGlib.FilterEnum>, 12: <enum PK_FILTER_ENUM_SUPPORTED of type PackageKitGlib.FilterEnum>, 13: <enum PK_FILTER_ENUM_NOT_SUPPORTED of type PackageKitGlib.FilterEnum>, 14: <enum PK_FILTER_ENUM_BASENAME of type PackageKitGlib.FilterEnum>, 15: <enum PK_FILTER_ENUM_NOT_BASENAME of type PackageKitGlib.FilterEnum>, 16: <enum PK_FILTER_ENUM_NEWEST of type PackageKitGlib.FilterEnum>, 17: <enum PK_FILTER_ENUM_NOT_NEWEST of type PackageKitGlib.FilterEnum>, 18: <enum PK_FILTER_ENUM_ARCH of type PackageKitGlib.FilterEnum>, 19: <enum PK_FILTER_ENUM_NOT_ARCH of type PackageKitGlib.FilterEnum>, 20: <enum PK_FILTER_ENUM_SOURCE of type PackageKitGlib.FilterEnum>, 21: <enum PK_FILTER_ENUM_NOT_SOURCE of type PackageKitGlib.FilterEnum>, 22: <enum PK_FILTER_ENUM_COLLECTIONS of type PackageKitGlib.FilterEnum>, 23: <enum PK_FILTER_ENUM_NOT_COLLECTIONS of type PackageKitGlib.FilterEnum>, 24: <enum PK_FILTER_ENUM_APPLICATION of type PackageKitGlib.FilterEnum>, 25: <enum PK_FILTER_ENUM_NOT_APPLICATION of type PackageKitGlib.FilterEnum>, 26: <enum PK_FILTER_ENUM_DOWNLOADED of type PackageKitGlib.FilterEnum>, 27: <enum PK_FILTER_ENUM_NOT_DOWNLOADED of type PackageKitGlib.FilterEnum>, 28: <enum PK_FILTER_ENUM_LAST of type PackageKitGlib.FilterEnum>}, '__info__': gi.EnumInfo(FilterEnum), 'UNKNOWN': <enum PK_FILTER_ENUM_UNKNOWN of type PackageKitGlib.FilterEnum>, 'NONE': <enum PK_FILTER_ENUM_NONE of type PackageKitGlib.FilterEnum>, 'INSTALLED': <enum PK_FILTER_ENUM_INSTALLED of type PackageKitGlib.FilterEnum>, 'NOT_INSTALLED': <enum PK_FILTER_ENUM_NOT_INSTALLED of type PackageKitGlib.FilterEnum>, 'DEVELOPMENT': <enum PK_FILTER_ENUM_DEVELOPMENT of type PackageKitGlib.FilterEnum>, 'NOT_DEVELOPMENT': <enum PK_FILTER_ENUM_NOT_DEVELOPMENT of type PackageKitGlib.FilterEnum>, 'GUI': <enum PK_FILTER_ENUM_GUI of type PackageKitGlib.FilterEnum>, 'NOT_GUI': <enum PK_FILTER_ENUM_NOT_GUI of type PackageKitGlib.FilterEnum>, 'FREE': <enum PK_FILTER_ENUM_FREE of type PackageKitGlib.FilterEnum>, 'NOT_FREE': <enum PK_FILTER_ENUM_NOT_FREE of type PackageKitGlib.FilterEnum>, 'VISIBLE': <enum PK_FILTER_ENUM_VISIBLE of type PackageKitGlib.FilterEnum>, 'NOT_VISIBLE': <enum PK_FILTER_ENUM_NOT_VISIBLE of type PackageKitGlib.FilterEnum>, 'SUPPORTED': <enum PK_FILTER_ENUM_SUPPORTED of type PackageKitGlib.FilterEnum>, 'NOT_SUPPORTED': <enum PK_FILTER_ENUM_NOT_SUPPORTED of type PackageKitGlib.FilterEnum>, 'BASENAME': <enum PK_FILTER_ENUM_BASENAME of type PackageKitGlib.FilterEnum>, 'NOT_BASENAME': <enum PK_FILTER_ENUM_NOT_BASENAME of type PackageKitGlib.FilterEnum>, 'NEWEST': <enum PK_FILTER_ENUM_NEWEST of type PackageKitGlib.FilterEnum>, 'NOT_NEWEST': <enum PK_FILTER_ENUM_NOT_NEWEST of type PackageKitGlib.FilterEnum>, 'ARCH': <enum PK_FILTER_ENUM_ARCH of type PackageKitGlib.FilterEnum>, 'NOT_ARCH': <enum PK_FILTER_ENUM_NOT_ARCH of type PackageKitGlib.FilterEnum>, 'SOURCE': <enum PK_FILTER_ENUM_SOURCE of type PackageKitGlib.FilterEnum>, 'NOT_SOURCE': <enum PK_FILTER_ENUM_NOT_SOURCE of type PackageKitGlib.FilterEnum>, 'COLLECTIONS': <enum PK_FILTER_ENUM_COLLECTIONS of type PackageKitGlib.FilterEnum>, 'NOT_COLLECTIONS': <enum PK_FILTER_ENUM_NOT_COLLECTIONS of type PackageKitGlib.FilterEnum>, 'APPLICATION': <enum PK_FILTER_ENUM_APPLICATION of type PackageKitGlib.FilterEnum>, 'NOT_APPLICATION': <enum PK_FILTER_ENUM_NOT_APPLICATION of type PackageKitGlib.FilterEnum>, 'DOWNLOADED': <enum PK_FILTER_ENUM_DOWNLOADED of type PackageKitGlib.FilterEnum>, 'NOT_DOWNLOADED': <enum PK_FILTER_ENUM_NOT_DOWNLOADED of type PackageKitGlib.FilterEnum>, 'LAST': <enum PK_FILTER_ENUM_LAST of type PackageKitGlib.FilterEnum>, 'from_string': gi.FunctionInfo(from_string), 'to_string': gi.FunctionInfo(to_string)})"
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
    }
    __gtype__ = None # (!) real value is '<GType PkFilterEnum (94016447152640)>'
    __info__ = gi.EnumInfo(FilterEnum)


