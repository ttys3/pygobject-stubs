# encoding: utf-8
# module gi.repository.Champlain
# from /usr/lib64/girepository-1.0/Champlain-0.12.typelib
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
import gi.repository.Clutter as __gi_repository_Clutter
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


from .TileSource import TileSource

class FileTileSource(TileSource):
    """
    :Constructors:
    
    ::
    
        FileTileSource(**properties)
        new_full(id:str, name:str, license:str, license_uri:str, min_zoom:int, max_zoom:int, tile_size:int, projection:Champlain.MapProjection, renderer:Champlain.Renderer) -> Champlain.FileTileSource
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

    def do_fill_tile(self, *args, **kwargs): # real signature unknown
        """ fill_tile(self, tile:Champlain.Tile) """
        pass

    def do_get_id(self, *args, **kwargs): # real signature unknown
        """ get_id(self) -> str """
        pass

    def do_get_license(self, *args, **kwargs): # real signature unknown
        """ get_license(self) -> str """
        pass

    def do_get_license_uri(self, *args, **kwargs): # real signature unknown
        """ get_license_uri(self) -> str """
        pass

    def do_get_max_zoom_level(self, *args, **kwargs): # real signature unknown
        """ get_max_zoom_level(self) -> int """
        pass

    def do_get_min_zoom_level(self, *args, **kwargs): # real signature unknown
        """ get_min_zoom_level(self) -> int """
        pass

    def do_get_name(self, *args, **kwargs): # real signature unknown
        """ get_name(self) -> str """
        pass

    def do_get_projection(self, *args, **kwargs): # real signature unknown
        """ get_projection(self) -> Champlain.MapProjection """
        pass

    def do_get_tile_size(self, *args, **kwargs): # real signature unknown
        """ get_tile_size(self) -> int """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def fill_tile(self, tile): # real signature unknown; restored from __doc__
        """ fill_tile(self, tile:Champlain.Tile) """
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

    def get_cache(self): # real signature unknown; restored from __doc__
        """ get_cache(self) -> Champlain.TileCache """
        pass

    def get_column_count(self, zoom_level): # real signature unknown; restored from __doc__
        """ get_column_count(self, zoom_level:int) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_latitude(self, zoom_level, y): # real signature unknown; restored from __doc__
        """ get_latitude(self, zoom_level:int, y:float) -> float """
        return 0.0

    def get_license(self): # real signature unknown; restored from __doc__
        """ get_license(self) -> str """
        return ""

    def get_license_uri(self): # real signature unknown; restored from __doc__
        """ get_license_uri(self) -> str """
        return ""

    def get_longitude(self, zoom_level, x): # real signature unknown; restored from __doc__
        """ get_longitude(self, zoom_level:int, x:float) -> float """
        return 0.0

    def get_max_zoom_level(self): # real signature unknown; restored from __doc__
        """ get_max_zoom_level(self) -> int """
        return 0

    def get_meters_per_pixel(self, zoom_level, latitude, longitude): # real signature unknown; restored from __doc__
        """ get_meters_per_pixel(self, zoom_level:int, latitude:float, longitude:float) -> float """
        return 0.0

    def get_min_zoom_level(self): # real signature unknown; restored from __doc__
        """ get_min_zoom_level(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_next_source(self): # real signature unknown; restored from __doc__
        """ get_next_source(self) -> Champlain.MapSource """
        pass

    def get_projection(self): # real signature unknown; restored from __doc__
        """ get_projection(self) -> Champlain.MapProjection """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_renderer(self): # real signature unknown; restored from __doc__
        """ get_renderer(self) -> Champlain.Renderer """
        pass

    def get_row_count(self, zoom_level): # real signature unknown; restored from __doc__
        """ get_row_count(self, zoom_level:int) -> int """
        return 0

    def get_tile_size(self): # real signature unknown; restored from __doc__
        """ get_tile_size(self) -> int """
        return 0

    def get_x(self, zoom_level, longitude): # real signature unknown; restored from __doc__
        """ get_x(self, zoom_level:int, longitude:float) -> float """
        return 0.0

    def get_y(self, zoom_level, latitude): # real signature unknown; restored from __doc__
        """ get_y(self, zoom_level:int, latitude:float) -> float """
        return 0.0

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

    def load_map_data(self, map_path): # real signature unknown; restored from __doc__
        """ load_map_data(self, map_path:str) """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_full(self, id, name, license, license_uri, min_zoom, max_zoom, tile_size, projection, renderer): # real signature unknown; restored from __doc__
        """ new_full(id:str, name:str, license:str, license_uri:str, min_zoom:int, max_zoom:int, tile_size:int, projection:Champlain.MapProjection, renderer:Champlain.Renderer) -> Champlain.FileTileSource """
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

    def set_cache(self, cache): # real signature unknown; restored from __doc__
        """ set_cache(self, cache:Champlain.TileCache) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_id(self, id): # real signature unknown; restored from __doc__
        """ set_id(self, id:str) """
        pass

    def set_license(self, license): # real signature unknown; restored from __doc__
        """ set_license(self, license:str) """
        pass

    def set_license_uri(self, license_uri): # real signature unknown; restored from __doc__
        """ set_license_uri(self, license_uri:str) """
        pass

    def set_max_zoom_level(self, zoom_level): # real signature unknown; restored from __doc__
        """ set_max_zoom_level(self, zoom_level:int) """
        pass

    def set_min_zoom_level(self, zoom_level): # real signature unknown; restored from __doc__
        """ set_min_zoom_level(self, zoom_level:int) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_next_source(self, next_source): # real signature unknown; restored from __doc__
        """ set_next_source(self, next_source:Champlain.MapSource) """
        pass

    def set_projection(self, projection): # real signature unknown; restored from __doc__
        """ set_projection(self, projection:Champlain.MapProjection) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_renderer(self, renderer): # real signature unknown; restored from __doc__
        """ set_renderer(self, renderer:Champlain.Renderer) """
        pass

    def set_tile_size(self, tile_size): # real signature unknown; restored from __doc__
        """ set_tile_size(self, tile_size:int) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f2e2da06070>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(FileTileSource), '__module__': 'gi.repository.Champlain', '__gtype__': <GType ChamplainFileTileSource (94016588012880)>, '__doc__': None, '__gsignals__': {}, 'new_full': gi.FunctionInfo(new_full), 'load_map_data': gi.FunctionInfo(load_map_data), 'parent': <property object at 0x7f2e2ca8f450>})"
    __gdoc__ = "Object ChamplainFileTileSource\n\nProperties from ChamplainTileSource:\n  id -> gchararray: Id\n    The id of the tile source\n  name -> gchararray: Name\n    The name of the tile source\n  license -> gchararray: License\n    The usage license of the tile source\n  license-uri -> gchararray: License-uri\n    The usage license's uri for more information\n  min-zoom-level -> guint: Minimum Zoom Level\n    The minimum zoom level\n  max-zoom-level -> guint: Maximum Zoom Level\n    The maximum zoom level\n  tile-size -> guint: Tile Size\n    The tile size\n  projection -> ChamplainMapProjection: Projection\n    The map projection\n  cache -> ChamplainTileCache: Cache\n    Cache used for tile sorage\n\nProperties from ChamplainMapSource:\n  next-source -> ChamplainMapSource: Next Source\n    Next source in the loading chain\n  renderer -> ChamplainRenderer: Tile renderer\n    Tile renderer used to render tiles\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ChamplainFileTileSource (94016588012880)>'
    __info__ = ObjectInfo(FileTileSource)


