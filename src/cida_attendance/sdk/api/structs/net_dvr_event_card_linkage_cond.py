from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EVENT_CARD_LINKAGE_COND(Structure):
    pass

_S(struct_tagNET_DVR_EVENT_CARD_LINKAGE_COND, [
    ('dwSize', DWORD),
    ('dwEventID', DWORD),
    ('wLocalControllerID', WORD),
    ('byRes', BYTE * 106),
])

NET_DVR_EVENT_CARD_LINKAGE_COND = struct_tagNET_DVR_EVENT_CARD_LINKAGE_COND
LPNET_DVR_EVENT_CARD_LINKAGE_COND = POINTER(struct_tagNET_DVR_EVENT_CARD_LINKAGE_COND)
tagNET_DVR_EVENT_CARD_LINKAGE_COND = struct_tagNET_DVR_EVENT_CARD_LINKAGE_COND
