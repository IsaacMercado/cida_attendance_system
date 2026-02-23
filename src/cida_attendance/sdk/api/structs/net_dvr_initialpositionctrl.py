from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INITIALPOSITIONCTRL(Structure):
    pass

_S(struct_tagNET_DVR_INITIALPOSITIONCTRL, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('byWorkMode', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_INITIALPOSITIONCTRL = struct_tagNET_DVR_INITIALPOSITIONCTRL
LPNET_DVR_INITIALPOSITIONCTRL = POINTER(struct_tagNET_DVR_INITIALPOSITIONCTRL)
tagNET_DVR_INITIALPOSITIONCTRL = struct_tagNET_DVR_INITIALPOSITIONCTRL
