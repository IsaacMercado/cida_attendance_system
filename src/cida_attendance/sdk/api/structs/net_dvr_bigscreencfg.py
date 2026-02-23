from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_singlescreencfg import NET_DVR_SINGLESCREENCFG


class struct_tagNET_DVR_BIGSCREENCFG(Structure):
    pass

_S(struct_tagNET_DVR_BIGSCREENCFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byModeX', BYTE),
    ('byModeY', BYTE),
    ('byMainDecodeSystem', BYTE),
    ('byMainDecoderDispChan', BYTE),
    ('byVideoStandard', BYTE),
    ('byRes1', BYTE * 2),
    ('dwResolution', DWORD),
    ('struFollowSingleScreen', NET_DVR_SINGLESCREENCFG * 100),
    ('wBigScreenX', WORD),
    ('wBigScreenY', WORD),
    ('byRes2', BYTE * 12),
])

NET_DVR_BIGSCREENCFG = struct_tagNET_DVR_BIGSCREENCFG
LPNET_DVR_BIGSCREENCFG = POINTER(struct_tagNET_DVR_BIGSCREENCFG)
tagNET_DVR_BIGSCREENCFG = struct_tagNET_DVR_BIGSCREENCFG
