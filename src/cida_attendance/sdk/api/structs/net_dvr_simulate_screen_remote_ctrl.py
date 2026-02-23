from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SIMULATE_SCREEN_REMOTE_CTRL(Structure):
    pass

_S(struct_tagNET_DVR_SIMULATE_SCREEN_REMOTE_CTRL, [
    ('dwSize', DWORD),
    ('byControlType', BYTE),
    ('byControlParam', BYTE),
    ('byRes', BYTE * 14),
])

NET_DVR_SIMULATE_SCREEN_REMOTE_CTRL = struct_tagNET_DVR_SIMULATE_SCREEN_REMOTE_CTRL
LPNET_DVR_SIMULATE_SCREEN_REMOTE_CTRL = POINTER(struct_tagNET_DVR_SIMULATE_SCREEN_REMOTE_CTRL)
tagNET_DVR_SIMULATE_SCREEN_REMOTE_CTRL = struct_tagNET_DVR_SIMULATE_SCREEN_REMOTE_CTRL
