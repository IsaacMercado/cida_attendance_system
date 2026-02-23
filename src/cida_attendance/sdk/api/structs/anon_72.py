from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_anon_72(Structure):
    pass

_S(struct_anon_72, [
    ('dwEnable', DWORD),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('struIP', NET_DVR_IPADDR),
    ('wDVRPort', WORD),
    ('byRes', BYTE * 34),
])

NET_DVR_IPDEVINFO = struct_anon_72
LPNET_DVR_IPDEVINFO = POINTER(struct_anon_72)
