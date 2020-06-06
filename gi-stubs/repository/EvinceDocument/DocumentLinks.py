# encoding: utf-8
# module gi.repository.EvinceDocument
# from /usr/lib64/girepository-1.0/EvinceDocument-3.0.typelib
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


class DocumentLinks(__gobject.GInterface):
    # no doc
    def find_link_dest(self, link_name): # real signature unknown; restored from __doc__
        """ find_link_dest(self, link_name:str) -> EvinceDocument.LinkDest """
        pass

    def find_link_page(self, link_name): # real signature unknown; restored from __doc__
        """ find_link_page(self, link_name:str) -> int """
        return 0

    def get_dest_page(self, dest): # real signature unknown; restored from __doc__
        """ get_dest_page(self, dest:EvinceDocument.LinkDest) -> int """
        return 0

    def get_dest_page_label(self, dest): # real signature unknown; restored from __doc__
        """ get_dest_page_label(self, dest:EvinceDocument.LinkDest) -> str """
        return ""

    def get_links(self, page): # real signature unknown; restored from __doc__
        """ get_links(self, page:EvinceDocument.Page) -> EvinceDocument.MappingList """
        pass

    def get_links_model(self): # real signature unknown; restored from __doc__
        """ get_links_model(self) -> Gtk.TreeModel """
        pass

    def get_link_page(self, link): # real signature unknown; restored from __doc__
        """ get_link_page(self, link:EvinceDocument.Link) -> int """
        return 0

    def get_link_page_label(self, link): # real signature unknown; restored from __doc__
        """ get_link_page_label(self, link:EvinceDocument.Link) -> str """
        return ""

    def has_document_links(self): # real signature unknown; restored from __doc__
        """ has_document_links(self) -> bool """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(DocumentLinks), '__module__': 'gi.repository.EvinceDocument', '__gtype__': <GType EvDocumentLinks (94742333856192)>, '__dict__': <attribute '__dict__' of 'DocumentLinks' objects>, '__weakref__': <attribute '__weakref__' of 'DocumentLinks' objects>, '__doc__': None, '__gsignals__': {}, 'find_link_dest': gi.FunctionInfo(find_link_dest), 'find_link_page': gi.FunctionInfo(find_link_page), 'get_dest_page': gi.FunctionInfo(get_dest_page), 'get_dest_page_label': gi.FunctionInfo(get_dest_page_label), 'get_link_page': gi.FunctionInfo(get_link_page), 'get_link_page_label': gi.FunctionInfo(get_link_page_label), 'get_links': gi.FunctionInfo(get_links), 'get_links_model': gi.FunctionInfo(get_links_model), 'has_document_links': gi.FunctionInfo(has_document_links)})"
    __gdoc__ = 'Interface EvDocumentLinks\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EvDocumentLinks (94742333856192)>'
    __info__ = InterfaceInfo(DocumentLinks)


