from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WINDOW_PLAYPLAN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WINDOW_PLAYPLAN_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 3),
    ('dwPlayPlanNo', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_WINDOW_PLAYPLAN_CFG = struct_tagNET_DVR_WINDOW_PLAYPLAN_CFG
LPNET_DVR_WINDOW_PLAYPLAN_CFG = POINTER(struct_tagNET_DVR_WINDOW_PLAYPLAN_CFG)
tagNET_DVR_WINDOW_PLAYPLAN_CFG = struct_tagNET_DVR_WINDOW_PLAYPLAN_CFG
