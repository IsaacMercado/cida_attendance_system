from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REALTIME_THERMOMETRY_COND(Structure):
    pass

_S(struct_tagNET_DVR_REALTIME_THERMOMETRY_COND, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('byRuleID', BYTE),
    ('byMode', BYTE),
    ('wInterval', WORD),
    ('fTemperatureDiff', c_float),
    ('byRes', BYTE * 56),
])

NET_DVR_REALTIME_THERMOMETRY_COND = struct_tagNET_DVR_REALTIME_THERMOMETRY_COND
LPNET_DVR_REALTIME_THERMOMETRY_COND = POINTER(struct_tagNET_DVR_REALTIME_THERMOMETRY_COND)
tagNET_DVR_REALTIME_THERMOMETRY_COND = struct_tagNET_DVR_REALTIME_THERMOMETRY_COND
