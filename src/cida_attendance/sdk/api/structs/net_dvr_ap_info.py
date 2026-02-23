from ctypes import Structure, c_char

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AP_INFO(Structure):
    pass

_S(struct_tagNET_DVR_AP_INFO, [
    ('sSsid', c_char * 32),
    ('dwMode', DWORD),
    ('dwSecurity', DWORD),
    ('dwChannel', DWORD),
    ('dwSignalStrength', DWORD),
    ('dwSpeed', DWORD),
])

NET_DVR_AP_INFO = struct_tagNET_DVR_AP_INFO
LPNET_DVR_AP_INFO = POINTER(struct_tagNET_DVR_AP_INFO)
tagNET_DVR_AP_INFO = struct_tagNET_DVR_AP_INFO
