from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PLAN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PLAN_INFO, [
    ('byValid', BYTE),
    ('byType', BYTE),
    ('wLayoutNo', WORD),
    ('byScreenStyle', BYTE),
    ('byBaseMapType', BYTE),
    ('byRes1', BYTE * 2),
    ('dwDelayTime', DWORD),
    ('dwSerialNo', DWORD),
    ('dwBaseMapWndNo', DWORD),
    ('dwBaseMapNo', DWORD),
    ('byRes2', BYTE * 20),
])

NET_DVR_PLAN_INFO = struct_tagNET_DVR_PLAN_INFO
LPNET_DVR_PLAN_INFO = POINTER(struct_tagNET_DVR_PLAN_INFO)
tagNET_DVR_PLAN_INFO = struct_tagNET_DVR_PLAN_INFO
