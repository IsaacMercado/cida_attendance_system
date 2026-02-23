from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OSDCFG(Structure):
    pass

_S(struct_tagNET_DVR_OSDCFG, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('byDispMode', BYTE),
    ('byFontColorY', BYTE),
    ('byFontColorU', BYTE),
    ('byFontColorV', BYTE),
    ('byBackColorY', BYTE),
    ('byBackColorU', BYTE),
    ('byBackColorV', BYTE),
    ('wXCoordinate', WORD),
    ('wYCoordinate', WORD),
    ('wWidth', WORD),
    ('wHeight', WORD),
    ('dwCharCnt', DWORD),
    ('wOSDChar', WORD * 256),
    ('byRes', BYTE * 32),
])

NET_DVR_OSDCFG = struct_tagNET_DVR_OSDCFG
LPNET_DVR_OSDCFG = POINTER(struct_tagNET_DVR_OSDCFG)
tagNET_DVR_OSDCFG = struct_tagNET_DVR_OSDCFG
