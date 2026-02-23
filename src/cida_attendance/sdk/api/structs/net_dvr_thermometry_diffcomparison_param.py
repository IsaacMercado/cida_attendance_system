from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_THERMOMETRY_DIFFCOMPARISON_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_DIFFCOMPARISON_PARAM, [
    ('byEnable', BYTE),
    ('byRuleID', BYTE),
    ('byAlarmID1', BYTE),
    ('byAlarmID2', BYTE),
    ('byRule', BYTE),
    ('byRes', BYTE * 3),
    ('fTemperatureDiff', c_float),
    ('dwAlarmFilteringTime', DWORD),
    ('byRes1', BYTE * 28),
])

NET_DVR_THERMOMETRY_DIFFCOMPARISON_PARAM = struct_tagNET_DVR_THERMOMETRY_DIFFCOMPARISON_PARAM
LPNET_DVR_THERMOMETRY_DIFFCOMPARISON_PARAM = POINTER(struct_tagNET_DVR_THERMOMETRY_DIFFCOMPARISON_PARAM)
tagNET_DVR_THERMOMETRY_DIFFCOMPARISON_PARAM = struct_tagNET_DVR_THERMOMETRY_DIFFCOMPARISON_PARAM
