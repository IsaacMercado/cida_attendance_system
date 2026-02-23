from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_FIND_LABEL(Structure):
    pass

_S(struct_tagNET_DVR_FIND_LABEL, [
    ('dwSize', DWORD),
    ('lChannel', LONG),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('sLabelName', BYTE * 40),
    ('byDrawFrame', BYTE),
    ('byISO8601', BYTE),
    ('cStartTimeDifferenceH', c_char),
    ('cStartTimeDifferenceM', c_char),
    ('cStopTimeDifferenceH', c_char),
    ('cStopTimeDifferenceM', c_char),
    ('byRes', BYTE * 34),
])

NET_DVR_FIND_LABEL = struct_tagNET_DVR_FIND_LABEL
LPNET_DVR_FIND_LABEL = POINTER(struct_tagNET_DVR_FIND_LABEL)
tagNET_DVR_FIND_LABEL = struct_tagNET_DVR_FIND_LABEL
