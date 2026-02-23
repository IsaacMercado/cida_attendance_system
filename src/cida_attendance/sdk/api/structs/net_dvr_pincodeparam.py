from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PINCODEPARAM(Structure):
    pass

_S(struct_tagNET_DVR_PINCODEPARAM, [
    ('dwSize', DWORD),
    ('byPinCmd', BYTE),
    ('byRes1', BYTE * 3),
    ('byPinCode', BYTE * 12),
    ('byNewPinCode', BYTE * 12),
    ('byRes2', BYTE * 16),
])

NET_DVR_PINCODEPARAM = struct_tagNET_DVR_PINCODEPARAM
LPNET_DVR_PINCODEPARAM = POINTER(struct_tagNET_DVR_PINCODEPARAM)
tagNET_DVR_PINCODEPARAM = struct_tagNET_DVR_PINCODEPARAM
