from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WIFIETHERNET(Structure):
    pass

_S(struct_tagNET_DVR_WIFIETHERNET, [
    ('sIpAddress', c_char * 16),
    ('sIpMask', c_char * 16),
    ('byMACAddr', BYTE * 6),
    ('byCloseWifi', BYTE),
    ('bRes', BYTE),
    ('dwEnableDhcp', DWORD),
    ('dwAutoDns', DWORD),
    ('sFirstDns', c_char * 16),
    ('sSecondDns', c_char * 16),
    ('sGatewayIpAddr', c_char * 16),
    ('bRes2', BYTE * 8),
])

NET_DVR_WIFIETHERNET = struct_tagNET_DVR_WIFIETHERNET
LPNET_DVR_WIFIETHERNET = POINTER(struct_tagNET_DVR_WIFIETHERNET)
tagNET_DVR_WIFIETHERNET = struct_tagNET_DVR_WIFIETHERNET
