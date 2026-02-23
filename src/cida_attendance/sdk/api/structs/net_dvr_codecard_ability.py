from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CODECARD_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_CODECARD_ABILITY, [
    ('byCardType', BYTE),
    ('byCodeNums', BYTE),
    ('byDispNums', BYTE),
    ('byCodeStartIdx', BYTE),
    ('byDispStartIdx', BYTE),
    ('byRes1', BYTE * 3),
    ('dwVgaSupportResolution', DWORD * 32),
    ('dwHdmiSupportResolution', DWORD * 32),
    ('dwDviSupportResolution', DWORD * 32),
    ('dwYpbprSupportResolution', DWORD * 32),
    ('byDispFormat', BYTE * 8),
    ('byWindowMode', (BYTE * 12) * 8),
    ('byRes2', BYTE * 36),
])

NET_DVR_CODECARD_ABILITY = struct_tagNET_DVR_CODECARD_ABILITY
LPNET_DVR_CODECARD_ABILITY = POINTER(struct_tagNET_DVR_CODECARD_ABILITY)
tagNET_DVR_CODECARD_ABILITY = struct_tagNET_DVR_CODECARD_ABILITY
