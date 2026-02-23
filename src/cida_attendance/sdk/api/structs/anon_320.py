from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_319 import NET_DVR_UPNP_PORT_STATE


class struct_anon_320(Structure):
    pass

_S(struct_anon_320, [
    ('strUpnpPort', NET_DVR_UPNP_PORT_STATE * 12),
    ('byRes', BYTE * 200),
])

NET_DVR_UPNP_NAT_STATE = struct_anon_320
LPNET_DVR_UPNP_NAT_STATE = POINTER(struct_anon_320)
