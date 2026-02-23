from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POOLPARAM(Structure):
    pass

_S(struct_tagNET_DVR_POOLPARAM, [
    ('dwPoolID', DWORD),
    ('byRes', BYTE * 4),
])

NET_DVR_POOLPARAM = struct_tagNET_DVR_POOLPARAM
LPNET_DVR_POOLPARAM = POINTER(struct_tagNET_DVR_POOLPARAM)
tagNET_DVR_POOLPARAM = struct_tagNET_DVR_POOLPARAM
