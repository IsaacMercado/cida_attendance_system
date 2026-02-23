from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MANAGE_UNIT_OPERATION_TIME_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MANAGE_UNIT_OPERATION_TIME_CFG, [
    ('dwMaxMonitoringTime', DWORD),
    ('dwMaxRingTime', DWORD),
    ('dwMaxTalkTime', DWORD),
    ('byRes', BYTE * 116),
])

NET_DVR_MANAGE_UNIT_OPERATION_TIME_CFG = struct_tagNET_DVR_MANAGE_UNIT_OPERATION_TIME_CFG
LPNET_DVR_MANAGE_UNIT_OPERATION_TIME_CFG = POINTER(struct_tagNET_DVR_MANAGE_UNIT_OPERATION_TIME_CFG)
tagNET_DVR_MANAGE_UNIT_OPERATION_TIME_CFG = struct_tagNET_DVR_MANAGE_UNIT_OPERATION_TIME_CFG
