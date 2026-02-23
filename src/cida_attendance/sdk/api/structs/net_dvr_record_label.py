from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_RECORD_LABEL(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_LABEL, [
    ('dwSize', DWORD),
    ('struTimeLabel', NET_DVR_TIME),
    ('byQuickAdd', BYTE),
    ('byRes1', BYTE * 3),
    ('sLabelName', BYTE * 40),
    ('byRes2', BYTE * 40),
])

NET_DVR_RECORD_LABEL = struct_tagNET_DVR_RECORD_LABEL
LPNET_DVR_RECORD_LABEL = POINTER(struct_tagNET_DVR_RECORD_LABEL)
tagNET_DVR_RECORD_LABEL = struct_tagNET_DVR_RECORD_LABEL
