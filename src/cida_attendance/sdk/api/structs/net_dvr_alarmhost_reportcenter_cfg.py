from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_REPORTCENTER_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_REPORTCENTER_CFG, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('byRes', BYTE * 3),
    ('byChanAlarmMode', BYTE * 4),
    ('byDealFailCenter', BYTE * 16),
    ('byDataType', BYTE),
    ('byRes2', BYTE * 15),
])

NET_DVR_ALARMHOST_REPORTCENTER_CFG = struct_tagNET_DVR_ALARMHOST_REPORTCENTER_CFG
LPNET_DVR_ALARMHOST_REPORTCENTER_CFG = POINTER(struct_tagNET_DVR_ALARMHOST_REPORTCENTER_CFG)
tagNET_DVR_ALARMHOST_REPORTCENTER_CFG = struct_tagNET_DVR_ALARMHOST_REPORTCENTER_CFG
