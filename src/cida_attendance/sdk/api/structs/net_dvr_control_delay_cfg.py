from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CONTROL_DELAY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CONTROL_DELAY_CFG, [
    ('byUseDefine', BYTE),
    ('byRes1', BYTE),
    ('wDelayTime', WORD),
    ('byRes', BYTE * 128),
])

NET_DVR_CONTROL_DELAY_CFG = struct_tagNET_DVR_CONTROL_DELAY_CFG
LPNET_DVR_CONTROL_DELAY_CFG = POINTER(struct_tagNET_DVR_CONTROL_DELAY_CFG)
tagNET_DVR_CONTROL_DELAY_CFG = struct_tagNET_DVR_CONTROL_DELAY_CFG
