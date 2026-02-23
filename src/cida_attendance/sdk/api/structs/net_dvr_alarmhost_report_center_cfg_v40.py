from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_REPORT_CENTER_CFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_REPORT_CENTER_CFG_V40, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('byDataType', BYTE),
    ('byRes', BYTE * 2),
    ('byChanAlarmMode', BYTE * 4),
    ('byDealFailCenter', BYTE * 16),
    ('byZoneReport', BYTE * 512),
    ('byNonZoneReport', BYTE * 32),
    ('byAlarmNetCard', BYTE * 4),
    ('byRes2', BYTE * 252),
])

NET_DVR_ALARMHOST_REPORT_CENTER_CFG_V40 = struct_tagNET_DVR_ALARMHOST_REPORT_CENTER_CFG_V40
LPNET_DVR_ALARMHOST_REPORT_CENTER_CFG_V40 = POINTER(struct_tagNET_DVR_ALARMHOST_REPORT_CENTER_CFG_V40)
tagNET_DVR_ALARMHOST_REPORT_CENTER_CFG_V40 = struct_tagNET_DVR_ALARMHOST_REPORT_CENTER_CFG_V40
