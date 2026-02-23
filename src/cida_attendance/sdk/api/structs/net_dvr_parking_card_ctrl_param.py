from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PARKING_CARD_CTRL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_PARKING_CARD_CTRL_PARAM, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byCardType', BYTE),
    ('byDeleteALL', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_PARKING_CARD_CTRL_PARAM = struct_tagNET_DVR_PARKING_CARD_CTRL_PARAM
LPNET_DVR_PARKING_CARD_CTRL_PARAM = POINTER(struct_tagNET_DVR_PARKING_CARD_CTRL_PARAM)
tagNET_DVR_PARKING_CARD_CTRL_PARAM = struct_tagNET_DVR_PARKING_CARD_CTRL_PARAM
