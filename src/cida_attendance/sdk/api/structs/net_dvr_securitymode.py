from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SECURITYMODE(Structure):
    pass

_S(struct_tagNET_DVR_SECURITYMODE, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwMode', DWORD),
    ('szRandCode', c_char * 6),
    ('byRes', BYTE * 6),
])

NET_DVR_SECURITYMODE = struct_tagNET_DVR_SECURITYMODE
LPNET_DVR_SECURITYMODE = POINTER(struct_tagNET_DVR_SECURITYMODE)
tagNET_DVR_SECURITYMODE = struct_tagNET_DVR_SECURITYMODE
