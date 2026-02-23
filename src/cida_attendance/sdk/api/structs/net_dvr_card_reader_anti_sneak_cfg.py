from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CARD_READER_ANTI_SNEAK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CARD_READER_ANTI_SNEAK_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwFollowUpCardReader', DWORD * 8),
    ('byRes2', BYTE * 32),
])

NET_DVR_CARD_READER_ANTI_SNEAK_CFG = struct_tagNET_DVR_CARD_READER_ANTI_SNEAK_CFG
LPNET_DVR_CARD_READER_ANTI_SNEAK_CFG = POINTER(struct_tagNET_DVR_CARD_READER_ANTI_SNEAK_CFG)
tagNET_DVR_CARD_READER_ANTI_SNEAK_CFG = struct_tagNET_DVR_CARD_READER_ANTI_SNEAK_CFG
