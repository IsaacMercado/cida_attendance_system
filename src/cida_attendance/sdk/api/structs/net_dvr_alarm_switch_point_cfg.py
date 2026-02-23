from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARM_SWITCH_POINT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_SWITCH_POINT_CFG, [
    ('dwIPCChanOsd', DWORD),
    ('byRes', BYTE * 60),
])

NET_DVR_ALARM_SWITCH_POINT_CFG = struct_tagNET_DVR_ALARM_SWITCH_POINT_CFG
LPNET_DVR_ALARM_SWITCH_POINT_CFG = POINTER(struct_tagNET_DVR_ALARM_SWITCH_POINT_CFG)
tagNET_DVR_ALARM_SWITCH_POINT_CFG = struct_tagNET_DVR_ALARM_SWITCH_POINT_CFG
