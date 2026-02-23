from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DECCARD_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_DECCARD_ABILITY, [
    ('byCardType', BYTE),
    ('byDecNums', BYTE),
    ('byDispNums', BYTE),
    ('byDecStartIdx', BYTE),
    ('byDispStartIdx', BYTE),
    ('byDispResolution', BYTE * 80),
    ('byDispFormat', BYTE * 8),
    ('byWindowMode', (BYTE * 8) * 4),
    ('byRes', BYTE * 35),
])

NET_DVR_DECCARD_ABILITY = struct_tagNET_DVR_DECCARD_ABILITY
LPNET_DVR_DECCARD_ABILITY = POINTER(struct_tagNET_DVR_DECCARD_ABILITY)
tagNET_DVR_DECCARD_ABILITY = struct_tagNET_DVR_DECCARD_ABILITY
