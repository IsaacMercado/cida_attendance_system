from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DECCARD_ABILITY_V41(Structure):
    pass

_S(struct_tagNET_DVR_DECCARD_ABILITY_V41, [
    ('byCardType', BYTE),
    ('byDecNums', BYTE),
    ('byDispNums', BYTE),
    ('byDecStartIdx', BYTE),
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

NET_DVR_DECCARD_ABILITY_V41 = struct_tagNET_DVR_DECCARD_ABILITY_V41
LPNET_DVR_DECCARD_ABILITY_V41 = POINTER(struct_tagNET_DVR_DECCARD_ABILITY_V41)
tagNET_DVR_DECCARD_ABILITY_V41 = struct_tagNET_DVR_DECCARD_ABILITY_V41
