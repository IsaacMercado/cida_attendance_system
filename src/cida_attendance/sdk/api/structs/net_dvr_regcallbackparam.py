from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REGCALLBACKPARAM(Structure):
    pass

_S(struct_tagNET_DVR_REGCALLBACKPARAM, [
    ('sDeviceID', c_char * 32),
    ('sPassword', c_char * 16),
    ('sSerialNumber', BYTE * 48),
    ('dwDeviceType', DWORD),
    ('nStatus', BYTE),
    ('byNetType', BYTE),
    ('byRes', BYTE * 14),
])

NET_DVR_REGCALLBACKPARAM = struct_tagNET_DVR_REGCALLBACKPARAM
LPNET_DVR_REGCALLBACKPARAM = POINTER(struct_tagNET_DVR_REGCALLBACKPARAM)
tagNET_DVR_REGCALLBACKPARAM = struct_tagNET_DVR_REGCALLBACKPARAM
