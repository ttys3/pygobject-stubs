# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


from .Setting import Setting

class SettingIPConfig(Setting):
    """
    :Constructors:
    
    ::
    
        SettingIPConfig(**properties)
    """
    def add_address(self, address): # real signature unknown; restored from __doc__
        """ add_address(self, address:NM.IPAddress) -> bool """
        return False

    def add_dns(self, dns): # real signature unknown; restored from __doc__
        """ add_dns(self, dns:str) -> bool """
        return False

    def add_dns_option(self, dns_option): # real signature unknown; restored from __doc__
        """ add_dns_option(self, dns_option:str) -> bool """
        return False

    def add_dns_search(self, dns_search): # real signature unknown; restored from __doc__
        """ add_dns_search(self, dns_search:str) -> bool """
        return False

    def add_route(self, route): # real signature unknown; restored from __doc__
        """ add_route(self, route:NM.IPRoute) -> bool """
        return False

    def add_routing_rule(self, routing_rule): # real signature unknown; restored from __doc__
        """ add_routing_rule(self, routing_rule:NM.IPRoutingRule) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_addresses(self): # real signature unknown; restored from __doc__
        """ clear_addresses(self) """
        pass

    def clear_dns(self): # real signature unknown; restored from __doc__
        """ clear_dns(self) """
        pass

    def clear_dns_options(self, is_set): # real signature unknown; restored from __doc__
        """ clear_dns_options(self, is_set:bool) """
        pass

    def clear_dns_searches(self): # real signature unknown; restored from __doc__
        """ clear_dns_searches(self) """
        pass

    def clear_routes(self): # real signature unknown; restored from __doc__
        """ clear_routes(self) """
        pass

    def clear_routing_rules(self): # real signature unknown; restored from __doc__
        """ clear_routing_rules(self) """
        pass

    def compare(self, b, flags): # real signature unknown; restored from __doc__
        """ compare(self, b:NM.Setting, flags:NM.SettingCompareFlags) -> bool """
        return False

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

    def diff(self, b, flags, invert_results, results): # real signature unknown; restored from __doc__
        """ diff(self, b:NM.Setting, flags:NM.SettingCompareFlags, invert_results:bool, results:dict) -> bool, results:dict """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_aggregate(self, *args, **kwargs): # real signature unknown
        """ aggregate(self, type_i:int, arg=None) -> bool """
        pass

    def do_get_secret_flags(self, *args, **kwargs): # real signature unknown
        """ get_secret_flags(self, secret_name:str, out_flags:NM.SettingSecretFlags) -> bool """
        pass

    def do_init_from_dbus(self, *args, **kwargs): # real signature unknown
        """ init_from_dbus(self, keys:dict, setting_dict:GLib.Variant, connection_dict:GLib.Variant, parse_flags:int) -> bool """
        pass

    def do_set_secret_flags(self, *args, **kwargs): # real signature unknown
        """ set_secret_flags(self, secret_name:str, flags:NM.SettingSecretFlags) -> bool """
        pass

    def do_update_one_secret(self, *args, **kwargs): # real signature unknown
        """ update_one_secret(self, key:str, value:GLib.Variant) -> int """
        pass

    def do_verify(self, *args, **kwargs): # real signature unknown
        """ verify(self, connection:NM.Connection) -> int """
        pass

    def do_verify_secrets(self, *args, **kwargs): # real signature unknown
        """ verify_secrets(self, connection:NM.Connection=None) -> bool """
        pass

    def duplicate(self): # real signature unknown; restored from __doc__
        """ duplicate(self) -> NM.Setting """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def enumerate_values(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ enumerate_values(self, func:NM.SettingValueIterFn, user_data=None) """
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

    def get_address(self, idx): # real signature unknown; restored from __doc__
        """ get_address(self, idx:int) -> NM.IPAddress """
        pass

    def get_dad_timeout(self): # real signature unknown; restored from __doc__
        """ get_dad_timeout(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_dbus_property_type(self, property_name): # real signature unknown; restored from __doc__
        """ get_dbus_property_type(self, property_name:str) -> GLib.VariantType """
        pass

    def get_dhcp_hostname(self): # real signature unknown; restored from __doc__
        """ get_dhcp_hostname(self) -> str """
        return ""

    def get_dhcp_hostname_flags(self): # real signature unknown; restored from __doc__
        """ get_dhcp_hostname_flags(self) -> NM.DhcpHostnameFlags """
        pass

    def get_dhcp_iaid(self): # real signature unknown; restored from __doc__
        """ get_dhcp_iaid(self) -> str """
        return ""

    def get_dhcp_send_hostname(self): # real signature unknown; restored from __doc__
        """ get_dhcp_send_hostname(self) -> bool """
        return False

    def get_dhcp_timeout(self): # real signature unknown; restored from __doc__
        """ get_dhcp_timeout(self) -> int """
        return 0

    def get_dns(self, idx): # real signature unknown; restored from __doc__
        """ get_dns(self, idx:int) -> str """
        return ""

    def get_dns_option(self, idx): # real signature unknown; restored from __doc__
        """ get_dns_option(self, idx:int) -> str """
        return ""

    def get_dns_priority(self): # real signature unknown; restored from __doc__
        """ get_dns_priority(self) -> int """
        return 0

    def get_dns_search(self, idx): # real signature unknown; restored from __doc__
        """ get_dns_search(self, idx:int) -> str """
        return ""

    def get_gateway(self): # real signature unknown; restored from __doc__
        """ get_gateway(self) -> str """
        return ""

    def get_ignore_auto_dns(self): # real signature unknown; restored from __doc__
        """ get_ignore_auto_dns(self) -> bool """
        return False

    def get_ignore_auto_routes(self): # real signature unknown; restored from __doc__
        """ get_ignore_auto_routes(self) -> bool """
        return False

    def get_may_fail(self): # real signature unknown; restored from __doc__
        """ get_may_fail(self) -> bool """
        return False

    def get_method(self): # real signature unknown; restored from __doc__
        """ get_method(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_never_default(self): # real signature unknown; restored from __doc__
        """ get_never_default(self) -> bool """
        return False

    def get_num_addresses(self): # real signature unknown; restored from __doc__
        """ get_num_addresses(self) -> int """
        return 0

    def get_num_dns(self): # real signature unknown; restored from __doc__
        """ get_num_dns(self) -> int """
        return 0

    def get_num_dns_options(self): # real signature unknown; restored from __doc__
        """ get_num_dns_options(self) -> int """
        return 0

    def get_num_dns_searches(self): # real signature unknown; restored from __doc__
        """ get_num_dns_searches(self) -> int """
        return 0

    def get_num_routes(self): # real signature unknown; restored from __doc__
        """ get_num_routes(self) -> int """
        return 0

    def get_num_routing_rules(self): # real signature unknown; restored from __doc__
        """ get_num_routing_rules(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_route(self, idx): # real signature unknown; restored from __doc__
        """ get_route(self, idx:int) -> NM.IPRoute """
        pass

    def get_route_metric(self): # real signature unknown; restored from __doc__
        """ get_route_metric(self) -> int """
        return 0

    def get_route_table(self): # real signature unknown; restored from __doc__
        """ get_route_table(self) -> int """
        return 0

    def get_routing_rule(self, idx): # real signature unknown; restored from __doc__
        """ get_routing_rule(self, idx:int) -> NM.IPRoutingRule """
        pass

    def get_secret_flags(self, secret_name, out_flags): # real signature unknown; restored from __doc__
        """ get_secret_flags(self, secret_name:str, out_flags:NM.SettingSecretFlags) -> bool """
        return False

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

    def has_dns_options(self): # real signature unknown; restored from __doc__
        """ has_dns_options(self) -> bool """
        return False

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

    def lookup_type(self, name): # real signature unknown; restored from __doc__
        """ lookup_type(name:str) -> GType """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def next_valid_dns_option(self, idx): # real signature unknown; restored from __doc__
        """ next_valid_dns_option(self, idx:int) -> int """
        return 0

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

    def remove_address(self, idx): # real signature unknown; restored from __doc__
        """ remove_address(self, idx:int) """
        pass

    def remove_address_by_value(self, address): # real signature unknown; restored from __doc__
        """ remove_address_by_value(self, address:NM.IPAddress) -> bool """
        return False

    def remove_dns(self, idx): # real signature unknown; restored from __doc__
        """ remove_dns(self, idx:int) """
        pass

    def remove_dns_by_value(self, dns): # real signature unknown; restored from __doc__
        """ remove_dns_by_value(self, dns:str) -> bool """
        return False

    def remove_dns_option(self, idx): # real signature unknown; restored from __doc__
        """ remove_dns_option(self, idx:int) """
        pass

    def remove_dns_option_by_value(self, dns_option): # real signature unknown; restored from __doc__
        """ remove_dns_option_by_value(self, dns_option:str) -> bool """
        return False

    def remove_dns_search(self, idx): # real signature unknown; restored from __doc__
        """ remove_dns_search(self, idx:int) """
        pass

    def remove_dns_search_by_value(self, dns_search): # real signature unknown; restored from __doc__
        """ remove_dns_search_by_value(self, dns_search:str) -> bool """
        return False

    def remove_route(self, idx): # real signature unknown; restored from __doc__
        """ remove_route(self, idx:int) """
        pass

    def remove_route_by_value(self, route): # real signature unknown; restored from __doc__
        """ remove_route_by_value(self, route:NM.IPRoute) -> bool """
        return False

    def remove_routing_rule(self, idx): # real signature unknown; restored from __doc__
        """ remove_routing_rule(self, idx:int) """
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

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_secret_flags(self, secret_name, flags): # real signature unknown; restored from __doc__
        """ set_secret_flags(self, secret_name:str, flags:NM.SettingSecretFlags) -> bool """
        return False

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

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def verify(self, connection=None): # real signature unknown; restored from __doc__
        """ verify(self, connection:NM.Connection=None) -> bool """
        return False

    def verify_secrets(self, connection=None): # real signature unknown; restored from __doc__
        """ verify_secrets(self, connection:NM.Connection=None) -> bool """
        return False

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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb9b8283d60>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SettingIPConfig), '__module__': 'gi.repository.NM', '__gtype__': <GType NMSettingIPConfig (94741104465456)>, '__doc__': None, '__gsignals__': {}, 'add_address': gi.FunctionInfo(add_address), 'add_dns': gi.FunctionInfo(add_dns), 'add_dns_option': gi.FunctionInfo(add_dns_option), 'add_dns_search': gi.FunctionInfo(add_dns_search), 'add_route': gi.FunctionInfo(add_route), 'add_routing_rule': gi.FunctionInfo(add_routing_rule), 'clear_addresses': gi.FunctionInfo(clear_addresses), 'clear_dns': gi.FunctionInfo(clear_dns), 'clear_dns_options': gi.FunctionInfo(clear_dns_options), 'clear_dns_searches': gi.FunctionInfo(clear_dns_searches), 'clear_routes': gi.FunctionInfo(clear_routes), 'clear_routing_rules': gi.FunctionInfo(clear_routing_rules), 'get_address': gi.FunctionInfo(get_address), 'get_dad_timeout': gi.FunctionInfo(get_dad_timeout), 'get_dhcp_hostname': gi.FunctionInfo(get_dhcp_hostname), 'get_dhcp_hostname_flags': gi.FunctionInfo(get_dhcp_hostname_flags), 'get_dhcp_iaid': gi.FunctionInfo(get_dhcp_iaid), 'get_dhcp_send_hostname': gi.FunctionInfo(get_dhcp_send_hostname), 'get_dhcp_timeout': gi.FunctionInfo(get_dhcp_timeout), 'get_dns': gi.FunctionInfo(get_dns), 'get_dns_option': gi.FunctionInfo(get_dns_option), 'get_dns_priority': gi.FunctionInfo(get_dns_priority), 'get_dns_search': gi.FunctionInfo(get_dns_search), 'get_gateway': gi.FunctionInfo(get_gateway), 'get_ignore_auto_dns': gi.FunctionInfo(get_ignore_auto_dns), 'get_ignore_auto_routes': gi.FunctionInfo(get_ignore_auto_routes), 'get_may_fail': gi.FunctionInfo(get_may_fail), 'get_method': gi.FunctionInfo(get_method), 'get_never_default': gi.FunctionInfo(get_never_default), 'get_num_addresses': gi.FunctionInfo(get_num_addresses), 'get_num_dns': gi.FunctionInfo(get_num_dns), 'get_num_dns_options': gi.FunctionInfo(get_num_dns_options), 'get_num_dns_searches': gi.FunctionInfo(get_num_dns_searches), 'get_num_routes': gi.FunctionInfo(get_num_routes), 'get_num_routing_rules': gi.FunctionInfo(get_num_routing_rules), 'get_route': gi.FunctionInfo(get_route), 'get_route_metric': gi.FunctionInfo(get_route_metric), 'get_route_table': gi.FunctionInfo(get_route_table), 'get_routing_rule': gi.FunctionInfo(get_routing_rule), 'has_dns_options': gi.FunctionInfo(has_dns_options), 'next_valid_dns_option': gi.FunctionInfo(next_valid_dns_option), 'remove_address': gi.FunctionInfo(remove_address), 'remove_address_by_value': gi.FunctionInfo(remove_address_by_value), 'remove_dns': gi.FunctionInfo(remove_dns), 'remove_dns_by_value': gi.FunctionInfo(remove_dns_by_value), 'remove_dns_option': gi.FunctionInfo(remove_dns_option), 'remove_dns_option_by_value': gi.FunctionInfo(remove_dns_option_by_value), 'remove_dns_search': gi.FunctionInfo(remove_dns_search), 'remove_dns_search_by_value': gi.FunctionInfo(remove_dns_search_by_value), 'remove_route': gi.FunctionInfo(remove_route), 'remove_route_by_value': gi.FunctionInfo(remove_route_by_value), 'remove_routing_rule': gi.FunctionInfo(remove_routing_rule), 'parent': <property object at 0x7fb9b84f1b80>})"
    __gdoc__ = 'Object NMSettingIPConfig\n\nProperties from NMSettingIPConfig:\n  method -> gchararray: \n    \n  dns -> GStrv: \n    \n  dns-search -> GStrv: \n    \n  dns-options -> GStrv: \n    \n  dns-priority -> gint: \n    \n  addresses -> GPtrArray: \n    \n  gateway -> gchararray: \n    \n  routes -> GPtrArray: \n    \n  route-metric -> gint64: \n    \n  route-table -> guint: \n    \n  ignore-auto-routes -> gboolean: \n    \n  ignore-auto-dns -> gboolean: \n    \n  dhcp-hostname -> gchararray: \n    \n  dhcp-hostname-flags -> guint: \n    \n  dhcp-send-hostname -> gboolean: \n    \n  never-default -> gboolean: \n    \n  may-fail -> gboolean: \n    \n  dad-timeout -> gint: \n    \n  dhcp-timeout -> gint: \n    \n  dhcp-iaid -> gchararray: \n    \n\nProperties from NMSetting:\n  name -> gchararray: \n    \n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType NMSettingIPConfig (94741104465456)>'
    __info__ = ObjectInfo(SettingIPConfig)


