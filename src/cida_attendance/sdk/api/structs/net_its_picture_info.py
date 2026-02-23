from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_ITS_PICTURE_INFO(Structure):
    pass

_S(struct_tagNET_ITS_PICTURE_INFO, [
    ('dwDataLen', DWORD),
    ('byType', BYTE),
    ('byDataType', BYTE),
    ('byCloseUpType', BYTE),
    ('byPicRecogMode', BYTE),
    ('dwRedLightTime', DWORD),
    ('byAbsTime', BYTE * 32),
    ('struPlateRect', NET_VCA_RECT),
    ('struPlateRecgRect', NET_VCA_RECT),
    ('pBuffer', POINTER(BYTE)),
    ('dwUTCTime', DWORD),
    ('byCompatibleAblity', BYTE),
    ('byTimeDiffFlag', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byRes2', BYTE * 4),
])

NET_ITS_PICTURE_INFO = struct_tagNET_ITS_PICTURE_INFO
LPNET_ITS_PICTURE_INFO = POINTER(struct_tagNET_ITS_PICTURE_INFO)
tagNET_ITS_PICTURE_INFO = struct_tagNET_ITS_PICTURE_INFO
