from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SEND_CARD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SEND_CARD_INFO, [
    ('byCardNo', BYTE * 32),
    ('byRes', BYTE * 224),
])

NET_DVR_SEND_CARD_INFO = struct_tagNET_DVR_SEND_CARD_INFO
LPNET_DVR_SEND_CARD_INFO = POINTER(struct_tagNET_DVR_SEND_CARD_INFO)
tagNET_DVR_SEND_CARD_INFO = struct_tagNET_DVR_SEND_CARD_INFO
