from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEV_PLAYCTRL(Structure):
    pass

_S(struct_tagNET_DVR_DEV_PLAYCTRL, [
    ('dwSize', DWORD),
    ('byControlType', BYTE),
    ('byRes', BYTE * 131),
])

NET_DVR_DEV_PLAYCTRL = struct_tagNET_DVR_DEV_PLAYCTRL
LPNET_DVR_DEV_PLAYCTRL = POINTER(struct_tagNET_DVR_DEV_PLAYCTRL)
tagNET_DVR_DEV_PLAYCTRL = struct_tagNET_DVR_DEV_PLAYCTRL
