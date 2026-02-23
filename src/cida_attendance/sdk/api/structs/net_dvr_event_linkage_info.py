from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EVENT_LINKAGE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_EVENT_LINKAGE_INFO, [
    ('wMainEventType', WORD),
    ('wSubEventType', WORD),
    ('byRes', BYTE * 28),
])

NET_DVR_EVENT_LINKAGE_INFO = struct_tagNET_DVR_EVENT_LINKAGE_INFO
LPNET_DVR_EVENT_LINKAGE_INFO = POINTER(struct_tagNET_DVR_EVENT_LINKAGE_INFO)
tagNET_DVR_EVENT_LINKAGE_INFO = struct_tagNET_DVR_EVENT_LINKAGE_INFO
