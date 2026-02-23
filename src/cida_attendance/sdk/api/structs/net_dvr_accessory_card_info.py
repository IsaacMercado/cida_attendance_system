from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACCESSORY_CARD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ACCESSORY_CARD_INFO, [
    ('dwSize', DWORD),
    ('szAccessoryCardInfo', BYTE * 256),
    ('byRes', BYTE * 512),
])

NET_DVR_ACCESSORY_CARD_INFO = struct_tagNET_DVR_ACCESSORY_CARD_INFO
LPNET_DVR_ACCESSORY_CARD_INFO = POINTER(struct_tagNET_DVR_ACCESSORY_CARD_INFO)
tagNET_DVR_ACCESSORY_CARD_INFO = struct_tagNET_DVR_ACCESSORY_CARD_INFO
