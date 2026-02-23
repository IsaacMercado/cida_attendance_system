from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_lane_queue import NET_DVR_LANE_QUEUE
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_LANE_PARAM_V41(Structure):
    pass

_S(struct_tagNET_DVR_LANE_PARAM_V41, [
    ('byRuleName', BYTE * 32),
    ('byRuleID', BYTE),
    ('byLaneType', BYTE),
    ('byTrafficState', BYTE),
    ('byLaneNo', BYTE),
    ('dwVaryType', DWORD),
    ('dwTpsType', DWORD),
    ('dwLaneVolume', DWORD),
    ('dwLaneVelocity', DWORD),
    ('dwTimeHeadway', DWORD),
    ('dwSpaceHeadway', DWORD),
    ('fSpaceOccupyRation', c_float),
    ('fTimeOccupyRation', c_float),
    ('dwLightVehicle', DWORD),
    ('dwMidVehicle', DWORD),
    ('dwHeavyVehicle', DWORD),
    ('struLaneQueue', NET_DVR_LANE_QUEUE),
    ('struRuleLocation', NET_VCA_POINT),
    ('dwOversizeVehicle', DWORD),
    ('byRes2', BYTE * 60),
])

NET_DVR_LANE_PARAM_V41 = struct_tagNET_DVR_LANE_PARAM_V41
LPNET_DVR_LANE_PARAM_V41 = POINTER(struct_tagNET_DVR_LANE_PARAM_V41)
tagNET_DVR_LANE_PARAM_V41 = struct_tagNET_DVR_LANE_PARAM_V41
