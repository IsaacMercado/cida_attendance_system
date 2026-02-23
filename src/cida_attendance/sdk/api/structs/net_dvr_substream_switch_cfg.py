from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SUBSTREAM_SWITCH_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SUBSTREAM_SWITCH_CFG, [
    ('byAutoSwitchEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('wSubWndWidth', WORD),
    ('wSubWndHeight', WORD),
])

NET_DVR_SUBSTREAM_SWITCH_CFG = struct_tagNET_DVR_SUBSTREAM_SWITCH_CFG
LPNET_DVR_SUBSTREAM_SWITCH_CFG = POINTER(struct_tagNET_DVR_SUBSTREAM_SWITCH_CFG)
tagNET_DVR_SUBSTREAM_SWITCH_CFG = struct_tagNET_DVR_SUBSTREAM_SWITCH_CFG
