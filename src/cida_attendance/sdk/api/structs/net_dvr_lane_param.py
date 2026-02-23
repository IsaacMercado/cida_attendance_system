from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_lane_queue import NET_DVR_LANE_QUEUE
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_LANE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_LANE_PARAM, [
    ('byRuleName', BYTE * 32),
    ('byRuleID', BYTE),
    ('byVaryType', BYTE),
    ('byLaneType', BYTE),
    ('byRes1', BYTE),
    ('dwLaneVolume', DWORD),
    ('dwLaneVelocity', DWORD),
    ('dwTimeHeadway', DWORD),
    ('dwSpaceHeadway', DWORD),
    ('fSpaceOccupyRation', c_float),
    ('struLaneQueue', NET_DVR_LANE_QUEUE),
    ('struRuleLocation', NET_VCA_POINT),
    ('byRes2', BYTE * 32),
])

NET_DVR_LANE_PARAM = struct_tagNET_DVR_LANE_PARAM
LPNET_DVR_LANE_PARAM = POINTER(struct_tagNET_DVR_LANE_PARAM)
tagNET_DVR_LANE_PARAM = struct_tagNET_DVR_LANE_PARAM
