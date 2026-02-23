from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_186 import NET_DVR_PTZPOS


class struct_tagNET_DVR_LIMIT_ANGLE(Structure):
    pass

_S(struct_tagNET_DVR_LIMIT_ANGLE, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struUp', NET_DVR_PTZPOS),
    ('struDown', NET_DVR_PTZPOS),
    ('struLeft', NET_DVR_PTZPOS),
    ('struRight', NET_DVR_PTZPOS),
    ('byRes2', BYTE * 20),
])

NET_DVR_LIMIT_ANGLE = struct_tagNET_DVR_LIMIT_ANGLE
LPNET_DVR_LIMIT_ANGLE = POINTER(struct_tagNET_DVR_LIMIT_ANGLE)
tagNET_DVR_LIMIT_ANGLE = struct_tagNET_DVR_LIMIT_ANGLE
