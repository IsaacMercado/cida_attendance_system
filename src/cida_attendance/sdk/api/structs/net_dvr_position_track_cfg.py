from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_position_index import NET_DVR_POSITION_INDEX


class struct_tagNET_DVR_POSITION_TRACK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_POSITION_TRACK_CFG, [
    ('dwSize', DWORD),
    ('byNum', BYTE),
    ('byRes1', BYTE * 3),
    ('struPositionIndex', NET_DVR_POSITION_INDEX * 10),
    ('byRes2', BYTE * 8),
])

NET_DVR_POSITION_TRACK_CFG = struct_tagNET_DVR_POSITION_TRACK_CFG
LPNET_DVR_POSITION_TRACK_CFG = POINTER(struct_tagNET_DVR_POSITION_TRACK_CFG)
tagNET_DVR_POSITION_TRACK_CFG = struct_tagNET_DVR_POSITION_TRACK_CFG
