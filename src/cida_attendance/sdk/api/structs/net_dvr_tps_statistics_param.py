from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30
from .net_dvr_tps_lane_param import NET_DVR_TPS_LANE_PARAM


class struct_tagNET_DVR_TPS_STATISTICS_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_TPS_STATISTICS_PARAM, [
    ('byStart', BYTE),
    ('byCMD', BYTE),
    ('byRes', BYTE * 2),
    ('wDeviceID', WORD),
    ('wDataLen', WORD),
    ('byTotalLaneNum', BYTE),
    ('byRes2', BYTE * 3),
    ('dwDeviceIDEx', DWORD),
    ('byRes1', BYTE * 8),
    ('struStartTime', NET_DVR_TIME_V30),
    ('dwSamplePeriod', DWORD),
    ('struLaneParam', NET_DVR_TPS_LANE_PARAM * 8),
])

NET_DVR_TPS_STATISTICS_PARAM = struct_tagNET_DVR_TPS_STATISTICS_PARAM
LPNET_DVR_TPS_STATISTICS_PARAM = POINTER(struct_tagNET_DVR_TPS_STATISTICS_PARAM)
tagNET_DVR_TPS_STATISTICS_PARAM = struct_tagNET_DVR_TPS_STATISTICS_PARAM
