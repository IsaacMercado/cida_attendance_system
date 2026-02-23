from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_116 import NET_DVR_FRAMETYPECODE


class struct_tagNET_DVR_IDENTIFICAT(Structure):
    pass

_S(struct_tagNET_DVR_IDENTIFICAT, [
    ('byStartMode', BYTE),
    ('byEndMode', BYTE),
    ('byRes', BYTE * 2),
    ('struStartCode', NET_DVR_FRAMETYPECODE),
    ('struEndCode', NET_DVR_FRAMETYPECODE),
    ('byRes1', BYTE * 12),
])

NET_DVR_IDENTIFICAT = struct_tagNET_DVR_IDENTIFICAT
LPNET_DVR_IDENTIFICAT = POINTER(struct_tagNET_DVR_IDENTIFICAT)
tagNET_DVR_IDENTIFICAT = struct_tagNET_DVR_IDENTIFICAT
