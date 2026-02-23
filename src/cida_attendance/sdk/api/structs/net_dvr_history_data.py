from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct__NET_DVR_HISTORY_DATA(Structure):
    pass

_S(struct__NET_DVR_HISTORY_DATA, [
    ('dwSize', DWORD),
    ('struTime', NET_DVR_TIME),
    ('byChanType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwChanNo', DWORD),
    ('dwSubChanNo', DWORD),
    ('dwVariableNo', DWORD),
    ('dwPointNo', DWORD),
    ('iData', c_int),
    ('byDataType', BYTE),
    ('byRes2', BYTE * 31),
])

NET_DVR_HISTORY_DATA = struct__NET_DVR_HISTORY_DATA
LPNET_DVR_HISTORY_DATA = POINTER(struct__NET_DVR_HISTORY_DATA)
_NET_DVR_HISTORY_DATA = struct__NET_DVR_HISTORY_DATA
