from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CARD_READER_PLAN(Structure):
    pass

_S(struct_tagNET_DVR_CARD_READER_PLAN, [
    ('dwSize', DWORD),
    ('dwTemplateNo', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_CARD_READER_PLAN = struct_tagNET_DVR_CARD_READER_PLAN
LPNET_DVR_CARD_READER_PLAN = POINTER(struct_tagNET_DVR_CARD_READER_PLAN)
tagNET_DVR_CARD_READER_PLAN = struct_tagNET_DVR_CARD_READER_PLAN
