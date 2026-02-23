from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WIRELESSSERVER(Structure):
    pass

_S(struct_tagNET_DVR_WIRELESSSERVER, [
    ('dwSize', DWORD),
    ('byWLanShare', BYTE),
    ('byBroadcastSSID', BYTE),
    ('bySecurityMode', BYTE),
    ('byAlgorithmType', BYTE),
    ('szSSID', c_char * 32),
    ('szPassWord', c_char * 64),
    ('byDefaultPassword', BYTE),
    ('byWifiApModeType', BYTE),
    ('byRes', BYTE * 254),
])

NET_DVR_WIRELESSSERVER = struct_tagNET_DVR_WIRELESSSERVER
LPNET_DVR_WIRELESSSERVER = POINTER(struct_tagNET_DVR_WIRELESSSERVER)
tagNET_DVR_WIRELESSSERVER = struct_tagNET_DVR_WIRELESSSERVER
