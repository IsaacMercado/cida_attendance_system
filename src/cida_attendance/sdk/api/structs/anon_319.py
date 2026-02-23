from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_anon_319(Structure):
    pass

_S(struct_anon_319, [
    ('dwEnabled', DWORD),
    ('wInternalPort', WORD),
    ('wExternalPort', WORD),
    ('dwStatus', DWORD),
    ('struNatExternalIp', NET_DVR_IPADDR),
    ('struNatInternalIp', NET_DVR_IPADDR),
    ('byRes', BYTE * 16),
])

NET_DVR_UPNP_PORT_STATE = struct_anon_319
LPNET_DVR_UPNP_PORT_STATE = POINTER(struct_anon_319)
