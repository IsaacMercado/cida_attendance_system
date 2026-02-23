from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LED_CLOCK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_CLOCK_CFG, [
    ('dwDclkRate', DWORD),
    ('dwGclkRate', DWORD),
    ('dwGclkCountNum', DWORD),
    ('byDclkDutyRatio', BYTE),
    ('byDclkPhase', BYTE),
    ('byGclkNum', BYTE),
    ('byRes', BYTE * 17),
])

NET_DVR_LED_CLOCK_CFG = struct_tagNET_DVR_LED_CLOCK_CFG
LPNET_DVR_LED_CLOCK_CFG = POINTER(struct_tagNET_DVR_LED_CLOCK_CFG)
tagNET_DVR_LED_CLOCK_CFG = struct_tagNET_DVR_LED_CLOCK_CFG
