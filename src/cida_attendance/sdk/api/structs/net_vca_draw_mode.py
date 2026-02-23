from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_DRAW_MODE(Structure):
    pass

_S(struct_tagNET_VCA_DRAW_MODE, [
    ('dwSize', DWORD),
    ('byDspAddTarget', BYTE),
    ('byDspAddRule', BYTE),
    ('byDspPicAddTarget', BYTE),
    ('byDspPicAddRule', BYTE),
    ('byRes', BYTE * 4),
])

NET_VCA_DRAW_MODE = struct_tagNET_VCA_DRAW_MODE
LPNET_VCA_DRAW_MODE = POINTER(struct_tagNET_VCA_DRAW_MODE)
tagNET_VCA_DRAW_MODE = struct_tagNET_VCA_DRAW_MODE
