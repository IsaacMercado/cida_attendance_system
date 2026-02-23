from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PREVIEW_SWITCH_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PREVIEW_SWITCH_CFG, [
    ('dwSize', DWORD),
    ('wSwitchSeq', WORD * 64),
    ('byPreviewNumber', BYTE),
    ('byEnableAudio', BYTE),
    ('bySwitchTime', BYTE),
    ('bySameSource', BYTE),
    ('byRes', BYTE * 32),
])

NET_DVR_PREVIEW_SWITCH_CFG = struct_tagNET_DVR_PREVIEW_SWITCH_CFG
LPNET_DVR_PREVIEW_SWITCH_CFG = POINTER(struct_tagNET_DVR_PREVIEW_SWITCH_CFG)
tagNET_DVR_PREVIEW_SWITCH_CFG = struct_tagNET_DVR_PREVIEW_SWITCH_CFG
