from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PREVIEW_DELAY_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PREVIEW_DELAY_CFG, [
    ('dwSize', DWORD),
    ('wdelayTime', WORD),
    ('byRes', BYTE * 130),
])

NET_DVR_PREVIEW_DELAY_CFG = struct_tagNET_DVR_PREVIEW_DELAY_CFG
LPNET_DVR_PREVIEW_DELAY_CFG = POINTER(struct_tagNET_DVR_PREVIEW_DELAY_CFG)
tagNET_DVR_PREVIEW_DELAY_CFG = struct_tagNET_DVR_PREVIEW_DELAY_CFG
