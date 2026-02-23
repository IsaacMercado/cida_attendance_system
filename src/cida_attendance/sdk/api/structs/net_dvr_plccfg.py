from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PLCCFG(Structure):
    pass

_S(struct_tagNET_DVR_PLCCFG, [
    ('dwSize', DWORD),
    ('byPlcEnable', BYTE),
    ('byPlateExpectedBright', BYTE),
    ('byRes1', BYTE * 2),
    ('byTradeoffFlash', BYTE),
    ('byCorrectFactor', BYTE),
    ('wLoopStatsEn', WORD),
    ('byPlcBrightOffset', BYTE),
    ('byRes', BYTE * 19),
])

NET_DVR_PLCCFG = struct_tagNET_DVR_PLCCFG
LPNET_DVR_PLCCFG = POINTER(struct_tagNET_DVR_PLCCFG)
tagNET_DVR_PLCCFG = struct_tagNET_DVR_PLCCFG
