from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_CALL_QUERY_COND(Structure):
    pass

_S(struct_tagNET_DVR_CALL_QUERY_COND, [
    ('dwSize', DWORD),
    ('bySearchID', BYTE * 36),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('byCallType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwMaxResults', DWORD),
    ('dwSearchPos', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_CALL_QUERY_COND = struct_tagNET_DVR_CALL_QUERY_COND
LPNET_DVR_CALL_QUERY_COND = POINTER(struct_tagNET_DVR_CALL_QUERY_COND)
tagNET_DVR_CALL_QUERY_COND = struct_tagNET_DVR_CALL_QUERY_COND
