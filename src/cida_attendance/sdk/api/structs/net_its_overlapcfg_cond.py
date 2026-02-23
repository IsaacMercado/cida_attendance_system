from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITS_OVERLAPCFG_COND(Structure):
    pass

_S(struct_tagNET_ITS_OVERLAPCFG_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwConfigMode', DWORD),
    ('byPicModeType', BYTE),
    ('byRelateType', BYTE),
    ('byRes', BYTE * 14),
])

NET_ITS_OVERLAPCFG_COND = struct_tagNET_ITS_OVERLAPCFG_COND
LPNET_ITS_OVERLAPCFG_COND = POINTER(struct_tagNET_ITS_OVERLAPCFG_COND)
tagNET_ITS_OVERLAPCFG_COND = struct_tagNET_ITS_OVERLAPCFG_COND
