from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TPS_LANE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_TPS_LANE_PARAM, [
    ('byLane', BYTE),
    ('bySpeed', BYTE),
    ('wArrivalFlow', WORD),
    ('dwLightVehicle', DWORD),
    ('dwMidVehicle', DWORD),
    ('dwHeavyVehicle', DWORD),
    ('dwTimeHeadway', DWORD),
    ('dwSpaceHeadway', DWORD),
    ('fSpaceOccupyRation', c_float),
    ('fTimeOccupyRation', c_float),
    ('byStoppingTimes', BYTE),
    ('byQueueLen', BYTE),
    ('byFlag', BYTE),
    ('byVehicelNum', BYTE),
    ('wDelay', WORD),
    ('byRes1', BYTE * 6),
    ('dwNonMotor', DWORD),
])

NET_DVR_TPS_LANE_PARAM = struct_tagNET_DVR_TPS_LANE_PARAM
LPNET_DVR_TPS_LANE_PARAM = POINTER(struct_tagNET_DVR_TPS_LANE_PARAM)
tagNET_DVR_TPS_LANE_PARAM = struct_tagNET_DVR_TPS_LANE_PARAM
