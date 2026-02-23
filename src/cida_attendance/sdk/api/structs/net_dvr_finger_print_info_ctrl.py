from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_del_finger_print_mode import NET_DVR_DEL_FINGER_PRINT_MODE


class struct_tagNET_DVR_FINGER_PRINT_INFO_CTRL(Structure):
    pass

_S(struct_tagNET_DVR_FINGER_PRINT_INFO_CTRL, [
    ('dwSize', DWORD),
    ('byMode', BYTE),
    ('byRes1', BYTE * 3),
    ('struProcessMode', NET_DVR_DEL_FINGER_PRINT_MODE),
    ('byRes', BYTE * 64),
])

NET_DVR_FINGER_PRINT_INFO_CTRL = struct_tagNET_DVR_FINGER_PRINT_INFO_CTRL
LPNET_DVR_FINGER_PRINT_INFO_CTRL = POINTER(struct_tagNET_DVR_FINGER_PRINT_INFO_CTRL)
tagNET_DVR_FINGER_PRINT_INFO_CTRL = struct_tagNET_DVR_FINGER_PRINT_INFO_CTRL
