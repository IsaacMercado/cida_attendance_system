from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WDR(Structure):
    pass

_S(struct_tagNET_DVR_WDR, [
    ('byWDREnabled', BYTE),
    ('byWDRLevel1', BYTE),
    ('byWDRLevel2', BYTE),
    ('byWDRContrastLevel', BYTE),
    ('byRes', BYTE * 16),
])

NET_DVR_WDR = struct_tagNET_DVR_WDR
LPNET_DVR_WDR = POINTER(struct_tagNET_DVR_WDR)
tagNET_DVR_WDR = struct_tagNET_DVR_WDR
