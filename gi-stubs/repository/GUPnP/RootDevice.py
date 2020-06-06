# encoding: utf-8
# module gi.repository.GUPnP
# from /usr/lib64/girepository-1.0/GUPnP-1.0.typelib
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
import gi.repository.GSSDP as __gi_repository_GSSDP
import gobject as __gobject


from .Device import Device

class RootDevice(Device):
    """
    :Constructors:
    
    ::
    
        RootDevice(**properties)
        new(context:GUPnP.Context, description_path:str, description_dir:str) -> GUPnP.RootDevice
        new_full(context:GUPnP.Context, factory:GUPnP.ResourceFactory, description_doc:GUPnP.XMLDoc, description_path:str, description_dir:str) -> GUPnP.RootDevice
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_available(self): # real signature unknown; restored from __doc__
        """ get_available(self) -> bool """
        return False

    def get_context(self): # real signature unknown; restored from __doc__
        """ get_context(self) -> GUPnP.Context """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description_dir(self): # real signature unknown; restored from __doc__
        """ get_description_dir(self) -> str """
        return ""

    def get_description_path(self): # real signature unknown; restored from __doc__
        """ get_description_path(self) -> str """
        return ""

    def get_description_value(self, element): # real signature unknown; restored from __doc__
        """ get_description_value(self, element:str) -> str """
        return ""

    def get_device(self, type): # real signature unknown; restored from __doc__
        """ get_device(self, type:str) -> GUPnP.DeviceInfo or None """
        pass

    def get_device_type(self): # real signature unknown; restored from __doc__
        """ get_device_type(self) -> str """
        return ""

    def get_friendly_name(self): # real signature unknown; restored from __doc__
        """ get_friendly_name(self) -> str """
        return ""

    def get_icon_url(self, requested_mime_type=None, requested_depth, requested_width, requested_height, prefer_bigger): # real signature unknown; restored from __doc__
        """ get_icon_url(self, requested_mime_type:str=None, requested_depth:int, requested_width:int, requested_height:int, prefer_bigger:bool) -> str, mime_type:str, depth:int, width:int, height:int """
        return ""

    def get_location(self): # real signature unknown; restored from __doc__
        """ get_location(self) -> str """
        return ""

    def get_manufacturer(self): # real signature unknown; restored from __doc__
        """ get_manufacturer(self) -> str """
        return ""

    def get_manufacturer_url(self): # real signature unknown; restored from __doc__
        """ get_manufacturer_url(self) -> str """
        return ""

    def get_model_description(self): # real signature unknown; restored from __doc__
        """ get_model_description(self) -> str """
        return ""

    def get_model_name(self): # real signature unknown; restored from __doc__
        """ get_model_name(self) -> str """
        return ""

    def get_model_number(self): # real signature unknown; restored from __doc__
        """ get_model_number(self) -> str """
        return ""

    def get_model_url(self): # real signature unknown; restored from __doc__
        """ get_model_url(self) -> str """
        return ""

    def get_presentation_url(self): # real signature unknown; restored from __doc__
        """ get_presentation_url(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_relative_location(self): # real signature unknown; restored from __doc__
        """ get_relative_location(self) -> str """
        return ""

    def get_resource_factory(self): # real signature unknown; restored from __doc__
        """ get_resource_factory(self) -> GUPnP.ResourceFactory """
        pass

    def get_serial_number(self): # real signature unknown; restored from __doc__
        """ get_serial_number(self) -> str """
        return ""

    def get_service(self, type): # real signature unknown; restored from __doc__
        """ get_service(self, type:str) -> GUPnP.ServiceInfo """
        pass

    def get_ssdp_resource_group(self): # real signature unknown; restored from __doc__
        """ get_ssdp_resource_group(self) -> GSSDP.ResourceGroup """
        pass

    def get_udn(self): # real signature unknown; restored from __doc__
        """ get_udn(self) -> str """
        return ""

    def get_upc(self): # real signature unknown; restored from __doc__
        """ get_upc(self) -> str """
        return ""

    def get_url_base(self): # real signature unknown; restored from __doc__
        """ get_url_base(self) -> Soup.URI """
        pass

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_devices(self): # real signature unknown; restored from __doc__
        """ list_devices(self) -> list """
        return []

    def list_device_types(self): # real signature unknown; restored from __doc__
        """ list_device_types(self) -> list """
        return []

    def list_dlna_capabilities(self): # real signature unknown; restored from __doc__
        """ list_dlna_capabilities(self) -> list """
        return []

    def list_dlna_device_class_identifier(self): # real signature unknown; restored from __doc__
        """ list_dlna_device_class_identifier(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_services(self): # real signature unknown; restored from __doc__
        """ list_services(self) -> list """
        return []

    def list_service_types(self): # real signature unknown; restored from __doc__
        """ list_service_types(self) -> list """
        return []

    def new(self, context, description_path, description_dir): # real signature unknown; restored from __doc__
        """ new(context:GUPnP.Context, description_path:str, description_dir:str) -> GUPnP.RootDevice """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_full(self, context, factory, description_doc, description_path, description_dir): # real signature unknown; restored from __doc__
        """ new_full(context:GUPnP.Context, factory:GUPnP.ResourceFactory, description_doc:GUPnP.XMLDoc, description_path:str, description_dir:str) -> GUPnP.RootDevice """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_available(self, available): # real signature unknown; restored from __doc__
        """ set_available(self, available:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f24e9bfdb80>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(RootDevice), '__module__': 'gi.repository.GUPnP', '__gtype__': <GType GUPnPRootDevice (94417776042160)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_full': gi.FunctionInfo(new_full), 'get_available': gi.FunctionInfo(get_available), 'get_description_dir': gi.FunctionInfo(get_description_dir), 'get_description_path': gi.FunctionInfo(get_description_path), 'get_relative_location': gi.FunctionInfo(get_relative_location), 'get_ssdp_resource_group': gi.FunctionInfo(get_ssdp_resource_group), 'set_available': gi.FunctionInfo(set_available), 'parent': <property object at 0x7f24ea383360>, 'priv': <property object at 0x7f24ea383450>})"
    __gdoc__ = 'Object GUPnPRootDevice\n\nProperties from GUPnPRootDevice:\n  description-doc -> GUPnPXMLDoc: Description document\n    Device description document\n  description-path -> gchararray: Description Path\n    The path to device descrition document\n  description-dir -> gchararray: Description Directory\n    The path to directory where description documents are provided\n  available -> gboolean: Available\n    Whether this device is available\n\nProperties from GUPnPDevice:\n  root-device -> GUPnPRootDevice: Root device\n    The GUPnPRootDevice\n\nProperties from GUPnPDeviceInfo:\n  resource-factory -> GUPnPResourceFactory: Resource Factory\n    The resource factory to use\n  context -> GUPnPContext: Context\n    The GUPnPContext\n  location -> gchararray: Location\n    The location of the device description file\n  udn -> gchararray: UDN\n    The UDN\n  device-type -> gchararray: Device type\n    The device type\n  url-base -> SoupURI: URL base\n    The URL base\n  document -> GUPnPXMLDoc: Document\n    The XML document related to this device\n  element -> gpointer: Element\n    The XML element related to this device\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GUPnPRootDevice (94417776042160)>'
    __info__ = ObjectInfo(RootDevice)


