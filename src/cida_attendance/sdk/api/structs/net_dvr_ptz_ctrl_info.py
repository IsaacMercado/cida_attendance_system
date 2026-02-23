from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_CTRL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_CTRL_INFO, [
    ('dwSize', DWORD),
    ('dwCtrlDelayTime', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_PTZ_CTRL_INFO = struct_tagNET_DVR_PTZ_CTRL_INFO
LPNET_DVR_PTZ_CTRL_INFO = POINTER(struct_tagNET_DVR_PTZ_CTRL_INFO)
tagNET_DVR_PTZ_CTRL_INFO = struct_tagNET_DVR_PTZ_CTRL_INFO
