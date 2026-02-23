from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_POINT_VALUE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_POINT_VALUE, [
    ('byChanType', BYTE),
    ('byPointType', BYTE),
    ('byRes1', BYTE * 2),
    ('dwChanNo', DWORD),
    ('dwSubChanNo', DWORD),
    ('dwVariableNo', DWORD),
    ('dwPointNo', DWORD),
    ('iValue', c_int),
    ('iValueEx', c_int),
    ('byRes', BYTE * 12),
])

NET_DVR_ALARMHOST_POINT_VALUE = struct_tagNET_DVR_ALARMHOST_POINT_VALUE
LPNET_DVR_ALARMHOST_POINT_VALUE = POINTER(struct_tagNET_DVR_ALARMHOST_POINT_VALUE)
tagNET_DVR_ALARMHOST_POINT_VALUE = struct_tagNET_DVR_ALARMHOST_POINT_VALUE
