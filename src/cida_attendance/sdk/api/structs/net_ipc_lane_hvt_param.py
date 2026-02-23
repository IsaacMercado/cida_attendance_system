from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_line import NET_ITC_LINE
from .net_itc_polygon import NET_ITC_POLYGON


class struct_tagNET_IPC_LANE_HVT_PARAM(Structure):
    pass

_S(struct_tagNET_IPC_LANE_HVT_PARAM, [
    ('byLaneNO', BYTE),
    ('byCarDriveDirect', BYTE),
    ('byRes', BYTE * 62),
    ('struLaneLine', NET_ITC_LINE),
    ('struPlateRecog', NET_ITC_POLYGON),
    ('byRes1', BYTE * 256),
])

NET_IPC_LANE_HVT_PARAM = struct_tagNET_IPC_LANE_HVT_PARAM
LPNET_IPC_LANE_HVT_PARAM = POINTER(struct_tagNET_IPC_LANE_HVT_PARAM)
tagNET_IPC_LANE_HVT_PARAM = struct_tagNET_IPC_LANE_HVT_PARAM
