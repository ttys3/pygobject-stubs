# encoding: utf-8
# module gi.repository.Libosinfo
# from /usr/lib64/girepository-1.0/Libosinfo-1.0.typelib
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


from .Product import Product

class Os(Product):
    """
    :Constructors:
    
    ::
    
        Os(**properties)
        new(id:str) -> Libosinfo.Os
    """
    def add_device(self, dev): # real signature unknown; restored from __doc__
        """ add_device(self, dev:Libosinfo.Device) -> Libosinfo.DeviceLink """
        pass

    def add_device_driver(self, driver): # real signature unknown; restored from __doc__
        """ add_device_driver(self, driver:Libosinfo.DeviceDriver) """
        pass

    def add_firmware(self, firmware): # real signature unknown; restored from __doc__
        """ add_firmware(self, firmware:Libosinfo.Firmware) """
        pass

    def add_image(self, image): # real signature unknown; restored from __doc__
        """ add_image(self, image:Libosinfo.Image) """
        pass

    def add_install_script(self, script): # real signature unknown; restored from __doc__
        """ add_install_script(self, script:Libosinfo.InstallScript) """
        pass

    def add_maximum_resources(self, resources): # real signature unknown; restored from __doc__
        """ add_maximum_resources(self, resources:Libosinfo.Resources) """
        pass

    def add_media(self, media): # real signature unknown; restored from __doc__
        """ add_media(self, media:Libosinfo.Media) """
        pass

    def add_minimum_resources(self, resources): # real signature unknown; restored from __doc__
        """ add_minimum_resources(self, resources:Libosinfo.Resources) """
        pass

    def add_network_install_resources(self, resources): # real signature unknown; restored from __doc__
        """ add_network_install_resources(self, resources:Libosinfo.Resources) """
        pass

    def add_param(self, key, value): # real signature unknown; restored from __doc__
        """ add_param(self, key:str, value:str) """
        pass

    def add_recommended_resources(self, resources): # real signature unknown; restored from __doc__
        """ add_recommended_resources(self, resources:Libosinfo.Resources) """
        pass

    def add_related(self, relshp, otherproduct): # real signature unknown; restored from __doc__
        """ add_related(self, relshp:Libosinfo.ProductRelationship, otherproduct:Libosinfo.Product) """
        pass

    def add_tree(self, tree): # real signature unknown; restored from __doc__
        """ add_tree(self, tree:Libosinfo.Tree) """
        pass

    def add_variant(self, variant): # real signature unknown; restored from __doc__
        """ add_variant(self, variant:Libosinfo.OsVariant) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_param(self, key): # real signature unknown; restored from __doc__
        """ clear_param(self, key:str) """
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

    def find_install_script(self, profile): # real signature unknown; restored from __doc__
        """ find_install_script(self, profile:str) -> Libosinfo.InstallScript """
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

    def get_all_devices(self, filter=None): # real signature unknown; restored from __doc__
        """ get_all_devices(self, filter:Libosinfo.Filter=None) -> Libosinfo.DeviceList """
        pass

    def get_all_device_links(self, filter=None): # real signature unknown; restored from __doc__
        """ get_all_device_links(self, filter:Libosinfo.Filter=None) -> Libosinfo.DeviceLinkList """
        pass

    def get_codename(self): # real signature unknown; restored from __doc__
        """ get_codename(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_devices(self, filter=None): # real signature unknown; restored from __doc__
        """ get_devices(self, filter:Libosinfo.Filter=None) -> Libosinfo.DeviceList """
        pass

    def get_devices_by_property(self, property, value, inherited): # real signature unknown; restored from __doc__
        """ get_devices_by_property(self, property:str, value:str, inherited:bool) -> Libosinfo.DeviceList """
        pass

    def get_device_drivers(self): # real signature unknown; restored from __doc__
        """ get_device_drivers(self) -> Libosinfo.DeviceDriverList """
        pass

    def get_device_drivers_prioritized(self): # real signature unknown; restored from __doc__
        """ get_device_drivers_prioritized(self) -> Libosinfo.DeviceDriverList """
        pass

    def get_device_links(self, filter=None): # real signature unknown; restored from __doc__
        """ get_device_links(self, filter:Libosinfo.Filter=None) -> Libosinfo.DeviceLinkList """
        pass

    def get_distro(self): # real signature unknown; restored from __doc__
        """ get_distro(self) -> str """
        return ""

    def get_eol_date(self): # real signature unknown; restored from __doc__
        """ get_eol_date(self) -> GLib.Date """
        pass

    def get_eol_date_string(self): # real signature unknown; restored from __doc__
        """ get_eol_date_string(self) -> str """
        return ""

    def get_family(self): # real signature unknown; restored from __doc__
        """ get_family(self) -> str """
        return ""

    def get_firmware_list(self, filter=None): # real signature unknown; restored from __doc__
        """ get_firmware_list(self, filter:Libosinfo.Filter=None) -> Libosinfo.FirmwareList """
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_image_list(self): # real signature unknown; restored from __doc__
        """ get_image_list(self) -> Libosinfo.ImageList """
        pass

    def get_install_script_list(self): # real signature unknown; restored from __doc__
        """ get_install_script_list(self) -> Libosinfo.InstallScriptList """
        pass

    def get_kernel_url_argument(self): # real signature unknown; restored from __doc__
        """ get_kernel_url_argument(self) -> str """
        return ""

    def get_logo(self): # real signature unknown; restored from __doc__
        """ get_logo(self) -> str """
        return ""

    def get_maximum_resources(self): # real signature unknown; restored from __doc__
        """ get_maximum_resources(self) -> Libosinfo.ResourcesList """
        pass

    def get_media_list(self): # real signature unknown; restored from __doc__
        """ get_media_list(self) -> Libosinfo.MediaList """
        pass

    def get_minimum_resources(self): # real signature unknown; restored from __doc__
        """ get_minimum_resources(self) -> Libosinfo.ResourcesList """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_network_install_resources(self): # real signature unknown; restored from __doc__
        """ get_network_install_resources(self) -> Libosinfo.ResourcesList """
        pass

    def get_param_keys(self): # real signature unknown; restored from __doc__
        """ get_param_keys(self) -> list """
        return []

    def get_param_value(self, key): # real signature unknown; restored from __doc__
        """ get_param_value(self, key:str) -> str """
        return ""

    def get_param_value_boolean(self, key): # real signature unknown; restored from __doc__
        """ get_param_value_boolean(self, key:str) -> bool """
        return False

    def get_param_value_boolean_with_default(self, key, default_value): # real signature unknown; restored from __doc__
        """ get_param_value_boolean_with_default(self, key:str, default_value:bool) -> bool """
        return False

    def get_param_value_enum(self, key, enum_type, default_value): # real signature unknown; restored from __doc__
        """ get_param_value_enum(self, key:str, enum_type:GType, default_value:int) -> int """
        return 0

    def get_param_value_int64(self, key): # real signature unknown; restored from __doc__
        """ get_param_value_int64(self, key:str) -> int """
        return 0

    def get_param_value_int64_with_default(self, key, default_value): # real signature unknown; restored from __doc__
        """ get_param_value_int64_with_default(self, key:str, default_value:int) -> int """
        return 0

    def get_param_value_list(self, key): # real signature unknown; restored from __doc__
        """ get_param_value_list(self, key:str) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_recommended_resources(self): # real signature unknown; restored from __doc__
        """ get_recommended_resources(self) -> Libosinfo.ResourcesList """
        pass

    def get_related(self, relshp): # real signature unknown; restored from __doc__
        """ get_related(self, relshp:Libosinfo.ProductRelationship) -> Libosinfo.ProductList """
        pass

    def get_release_date(self): # real signature unknown; restored from __doc__
        """ get_release_date(self) -> GLib.Date """
        pass

    def get_release_date_string(self): # real signature unknown; restored from __doc__
        """ get_release_date_string(self) -> str """
        return ""

    def get_release_status(self): # real signature unknown; restored from __doc__
        """ get_release_status(self) -> Libosinfo.ReleaseStatus """
        pass

    def get_short_id(self): # real signature unknown; restored from __doc__
        """ get_short_id(self) -> str """
        return ""

    def get_short_id_list(self): # real signature unknown; restored from __doc__
        """ get_short_id_list(self) -> list """
        return []

    def get_tree_list(self): # real signature unknown; restored from __doc__
        """ get_tree_list(self) -> Libosinfo.TreeList """
        pass

    def get_variant_list(self): # real signature unknown; restored from __doc__
        """ get_variant_list(self) -> Libosinfo.OsVariantList """
        pass

    def get_vendor(self): # real signature unknown; restored from __doc__
        """ get_vendor(self) -> str """
        return ""

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> str """
        return ""

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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, id): # real signature unknown; restored from __doc__
        """ new(id:str) -> Libosinfo.Os """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_param(self, key, value): # real signature unknown; restored from __doc__
        """ set_param(self, key:str, value:str) """
        pass

    def set_param_boolean(self, key, value): # real signature unknown; restored from __doc__
        """ set_param_boolean(self, key:str, value:bool) """
        pass

    def set_param_enum(self, key, value, enum_type): # real signature unknown; restored from __doc__
        """ set_param_enum(self, key:str, value:int, enum_type:GType) """
        pass

    def set_param_int64(self, key, value): # real signature unknown; restored from __doc__
        """ set_param_int64(self, key:str, value:int) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f7152fc45b0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Os), '__module__': 'gi.repository.Libosinfo', '__gtype__': <GType OsinfoOs (94407636386992)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_device': gi.FunctionInfo(add_device), 'add_device_driver': gi.FunctionInfo(add_device_driver), 'add_firmware': gi.FunctionInfo(add_firmware), 'add_image': gi.FunctionInfo(add_image), 'add_install_script': gi.FunctionInfo(add_install_script), 'add_maximum_resources': gi.FunctionInfo(add_maximum_resources), 'add_media': gi.FunctionInfo(add_media), 'add_minimum_resources': gi.FunctionInfo(add_minimum_resources), 'add_network_install_resources': gi.FunctionInfo(add_network_install_resources), 'add_recommended_resources': gi.FunctionInfo(add_recommended_resources), 'add_tree': gi.FunctionInfo(add_tree), 'add_variant': gi.FunctionInfo(add_variant), 'find_install_script': gi.FunctionInfo(find_install_script), 'get_all_device_links': gi.FunctionInfo(get_all_device_links), 'get_all_devices': gi.FunctionInfo(get_all_devices), 'get_device_drivers': gi.FunctionInfo(get_device_drivers), 'get_device_drivers_prioritized': gi.FunctionInfo(get_device_drivers_prioritized), 'get_device_links': gi.FunctionInfo(get_device_links), 'get_devices': gi.FunctionInfo(get_devices), 'get_devices_by_property': gi.FunctionInfo(get_devices_by_property), 'get_distro': gi.FunctionInfo(get_distro), 'get_family': gi.FunctionInfo(get_family), 'get_firmware_list': gi.FunctionInfo(get_firmware_list), 'get_image_list': gi.FunctionInfo(get_image_list), 'get_install_script_list': gi.FunctionInfo(get_install_script_list), 'get_kernel_url_argument': gi.FunctionInfo(get_kernel_url_argument), 'get_maximum_resources': gi.FunctionInfo(get_maximum_resources), 'get_media_list': gi.FunctionInfo(get_media_list), 'get_minimum_resources': gi.FunctionInfo(get_minimum_resources), 'get_network_install_resources': gi.FunctionInfo(get_network_install_resources), 'get_recommended_resources': gi.FunctionInfo(get_recommended_resources), 'get_release_status': gi.FunctionInfo(get_release_status), 'get_tree_list': gi.FunctionInfo(get_tree_list), 'get_variant_list': gi.FunctionInfo(get_variant_list), 'parent_instance': <property object at 0x7f715313f310>, 'priv': <property object at 0x7f715313f400>})"
    __gdoc__ = 'Object OsinfoOs\n\nProperties from OsinfoOs:\n  family -> gchararray: Family\n    Generic Family\n  distro -> gchararray: Distro\n    Generic Distro\n  kernel-url-argument -> gchararray: KernelURLArgument\n    Kernel URL Argument\n\nProperties from OsinfoProduct:\n  codename -> gchararray: Codename\n    Codename\n  name -> gchararray: Name\n    Name\n  short-id -> gchararray: ShortID\n    Short ID\n  vendor -> gchararray: Vendor\n    Vendor\n  version -> gchararray: Version\n    Version\n  logo -> gchararray: Logo\n    URI of the logo\n\nProperties from OsinfoEntity:\n  id -> gchararray: ID\n    Unique identifier\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType OsinfoOs (94407636386992)>'
    __info__ = ObjectInfo(Os)


