from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_TRAFFIC_DATA_QUERY_COND_(Structure):
    pass

_S(struct_tagNET_DVR_TRAFFIC_DATA_QUERY_COND_, [
    ('dwSize', DWORD),
    ('dwQueryCond', DWORD),
    ('dwChannel', DWORD),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('sLicense', c_char * 16),
    ('dwPlateType', DWORD),
    ('dwPlateColor', DWORD),
    ('dwVehicleColor', DWORD),
    ('dwVehicleType', DWORD),
    ('dwIllegalType', DWORD),
    ('dwEventType', DWORD),
    ('dwForensiceType', DWORD),
    ('wVehicleLogoRecog', WORD),
    ('byLaneNo', BYTE),
    ('byDirection', BYTE),
    ('wMinSpeed', WORD),
    ('wMaxSpeed', WORD),
    ('byDataType', BYTE),
    ('byExecuteCtrl', BYTE),
    ('byRes', BYTE * 254),
])

NET_DVR_TRAFFIC_DATA_QUERY_COND = struct_tagNET_DVR_TRAFFIC_DATA_QUERY_COND_
LPNET_DVR_TRAFFIC_DATA_QUERY_COND = POINTER(struct_tagNET_DVR_TRAFFIC_DATA_QUERY_COND_)
tagNET_DVR_TRAFFIC_DATA_QUERY_COND_ = struct_tagNET_DVR_TRAFFIC_DATA_QUERY_COND_
