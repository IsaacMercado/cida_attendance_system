from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FFC_BACKCOMP_INFO(Structure):
    pass

_S(struct_tagNET_DVR_FFC_BACKCOMP_INFO, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_FFC_BACKCOMP_INFO = struct_tagNET_DVR_FFC_BACKCOMP_INFO
LPNET_DVR_FFC_BACKCOMP_INFO = POINTER(struct_tagNET_DVR_FFC_BACKCOMP_INFO)
tagNET_DVR_FFC_BACKCOMP_INFO = struct_tagNET_DVR_FFC_BACKCOMP_INFO
