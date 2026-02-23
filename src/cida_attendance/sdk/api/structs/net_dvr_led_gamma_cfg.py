from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LED_GAMMA_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_GAMMA_CFG, [
    ('dwSize', DWORD),
    ('wGammaValue', WORD * 256),
    ('byGammaModel', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_LED_GAMMA_CFG = struct_tagNET_DVR_LED_GAMMA_CFG
LPNET_DVR_LED_GAMMA_CFG = POINTER(struct_tagNET_DVR_LED_GAMMA_CFG)
tagNET_DVR_LED_GAMMA_CFG = struct_tagNET_DVR_LED_GAMMA_CFG
