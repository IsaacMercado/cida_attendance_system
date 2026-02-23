from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INDOOR_UNIT_OPERATION_TIME_CFG(Structure):
    pass

_S(struct_tagNET_DVR_INDOOR_UNIT_OPERATION_TIME_CFG, [
    ('dwMaxMonitoringTime', DWORD),
    ('dwMaxRingTime', DWORD),
    ('dwCallForwardingTime', DWORD),
    ('dwRingDurationTime', DWORD),
    ('byRes', BYTE * 112),
])

NET_DVR_INDOOR_UNIT_OPERATION_TIME_CFG = struct_tagNET_DVR_INDOOR_UNIT_OPERATION_TIME_CFG
LPNET_DVR_INDOOR_UNIT_OPERATION_TIME_CFG = POINTER(struct_tagNET_DVR_INDOOR_UNIT_OPERATION_TIME_CFG)
tagNET_DVR_INDOOR_UNIT_OPERATION_TIME_CFG = struct_tagNET_DVR_INDOOR_UNIT_OPERATION_TIME_CFG
