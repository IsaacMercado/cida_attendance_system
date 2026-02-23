from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOGO_OVERLAYCFG(Structure):
    pass

_S(struct_tagNET_DVR_LOGO_OVERLAYCFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwCoordinateX', DWORD),
    ('dwCoordinateY', DWORD),
    ('wPicWidth', WORD),
    ('wPicHeight', WORD),
    ('byLogoName', BYTE * 16),
])

NET_DVR_LOGO_OVERLAYCFG = struct_tagNET_DVR_LOGO_OVERLAYCFG
LPNET_DVR_LOGO_OVERLAYCFG = POINTER(struct_tagNET_DVR_LOGO_OVERLAYCFG)
tagNET_DVR_LOGO_OVERLAYCFG = struct_tagNET_DVR_LOGO_OVERLAYCFG
