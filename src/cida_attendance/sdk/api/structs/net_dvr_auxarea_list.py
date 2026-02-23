from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_auxarea import NET_DVR_AUXAREA


class struct_tagNET_DVR_AUXAREA_LIST(Structure):
    pass

_S(struct_tagNET_DVR_AUXAREA_LIST, [
    ('dwSize', DWORD),
    ('struArea', NET_DVR_AUXAREA * 16),
    ('byRes2', BYTE * 64),
])

NET_DVR_AUXAREA_LIST = struct_tagNET_DVR_AUXAREA_LIST
LPNET_DVR_AUXAREA_LIST = POINTER(struct_tagNET_DVR_AUXAREA_LIST)
tagNET_DVR_AUXAREA_LIST = struct_tagNET_DVR_AUXAREA_LIST
