from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_430 import union_anon_430


class struct_tagNET_DVR_IOOUT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_IOOUT_CFG, [
    ('dwSize', DWORD),
    ('byWorkMode', BYTE),
    ('byRes1', BYTE * 3),
    ('uWorkModeInfo', union_anon_430),
    ('byRes2', BYTE * 128),
])

NET_DVR_IOOUT_CFG = struct_tagNET_DVR_IOOUT_CFG
LPNET_DVR_IOOUT_CFG = POINTER(struct_tagNET_DVR_IOOUT_CFG)
tagNET_DVR_IOOUT_CFG = struct_tagNET_DVR_IOOUT_CFG
