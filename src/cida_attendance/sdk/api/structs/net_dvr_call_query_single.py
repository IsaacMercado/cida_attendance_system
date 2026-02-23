from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_CALL_QUERY_SINGLE(Structure):
    pass

_S(struct_tagNET_DVR_CALL_QUERY_SINGLE, [
    ('dwSize', DWORD),
    ('byCallType', BYTE),
    ('byRes1', BYTE * 3),
    ('byTerminalName', BYTE * 64),
    ('byAddressURL', BYTE * 512),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('byRes2', BYTE * 32),
])

NET_DVR_CALL_QUERY_SINGLE = struct_tagNET_DVR_CALL_QUERY_SINGLE
LPNET_DVR_CALL_QUERY_SINGLE = POINTER(struct_tagNET_DVR_CALL_QUERY_SINGLE)
tagNET_DVR_CALL_QUERY_SINGLE = struct_tagNET_DVR_CALL_QUERY_SINGLE
