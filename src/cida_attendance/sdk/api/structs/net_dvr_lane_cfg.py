from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_one_lane import NET_DVR_ONE_LANE


class struct_tagNET_DVR_LANE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LANE_CFG, [
    ('dwSize', DWORD),
    ('struLane', NET_DVR_ONE_LANE * 8),
    ('byRes1', BYTE * 40),
])

NET_DVR_LANE_CFG = struct_tagNET_DVR_LANE_CFG
LPNET_DVR_LANE_CFG = POINTER(struct_tagNET_DVR_LANE_CFG)
tagNET_DVR_LANE_CFG = struct_tagNET_DVR_LANE_CFG
