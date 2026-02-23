from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_VEHICLEFLOW_COND(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLEFLOW_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byLane', BYTE),
    ('byRes1', BYTE * 3),
    ('struStartTime', NET_DVR_TIME_V30),
    ('struEndTime', NET_DVR_TIME_V30),
    ('byRes', BYTE * 256),
])

NET_DVR_VEHICLEFLOW_COND = struct_tagNET_DVR_VEHICLEFLOW_COND
LPNET_DVR_VEHICLEFLOW_COND = POINTER(struct_tagNET_DVR_VEHICLEFLOW_COND)
tagNET_DVR_VEHICLEFLOW_COND = struct_tagNET_DVR_VEHICLEFLOW_COND
