from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct__NET_DVR_SEARCH_CONDITION(Structure):
    pass

_S(struct__NET_DVR_SEARCH_CONDITION, [
    ('dwSize', DWORD),
    ('byMajorType', BYTE),
    ('byMinorType', BYTE),
    ('byRes1', BYTE * 2),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('byChanType', BYTE),
    ('byRes2', BYTE * 3),
    ('dwChanNo', DWORD),
    ('dwSubChanNo', DWORD),
    ('dwVariableNo', DWORD),
    ('dwPointNo', DWORD),
    ('byDataType', BYTE),
    ('byRes3', BYTE * 31),
])

NET_DVR_SEARCH_CONDITION = struct__NET_DVR_SEARCH_CONDITION
LPNET_DVR_SEARCH_CONDITION = POINTER(struct__NET_DVR_SEARCH_CONDITION)
_NET_DVR_SEARCH_CONDITION = struct__NET_DVR_SEARCH_CONDITION
