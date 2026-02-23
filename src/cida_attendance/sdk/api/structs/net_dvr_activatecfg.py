from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACTIVATECFG(Structure):
    pass

_S(struct_tagNET_DVR_ACTIVATECFG, [
    ('dwSize', DWORD),
    ('sPassword', BYTE * 16),
    ('byLoginMode', BYTE),
    ('byHttps', BYTE),
    ('byRes', BYTE * 106),
])

NET_DVR_ACTIVATECFG = struct_tagNET_DVR_ACTIVATECFG
LPNET_DVR_ACTIVATECFG = POINTER(struct_tagNET_DVR_ACTIVATECFG)
tagNET_DVR_ACTIVATECFG = struct_tagNET_DVR_ACTIVATECFG
