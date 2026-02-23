from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_LIMITCTRL(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_LIMITCTRL, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('byLimitMode', BYTE),
    ('byWorkMode', BYTE),
    ('byRes', BYTE * 122),
])

NET_DVR_PTZ_LIMITCTRL = struct_tagNET_DVR_PTZ_LIMITCTRL
LPNET_DVR_PTZ_LIMITCTRL = POINTER(struct_tagNET_DVR_PTZ_LIMITCTRL)
tagNET_DVR_PTZ_LIMITCTRL = struct_tagNET_DVR_PTZ_LIMITCTRL
