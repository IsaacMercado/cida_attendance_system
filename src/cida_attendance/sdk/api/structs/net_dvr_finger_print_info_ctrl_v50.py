from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_del_finger_print_mode_v50 import NET_DVR_DEL_FINGER_PRINT_MODE_V50


class struct_tagNET_DVR_FINGER_PRINT_INFO_CTRL_V50(Structure):
    pass

_S(struct_tagNET_DVR_FINGER_PRINT_INFO_CTRL_V50, [
    ('dwSize', DWORD),
    ('byMode', BYTE),
    ('byRes1', BYTE * 3),
    ('struProcessMode', NET_DVR_DEL_FINGER_PRINT_MODE_V50),
    ('byRes', BYTE * 64),
])

NET_DVR_FINGER_PRINT_INFO_CTRL_V50 = struct_tagNET_DVR_FINGER_PRINT_INFO_CTRL_V50
LPNET_DVR_FINGER_PRINT_INFO_CTRL_V50 = POINTER(struct_tagNET_DVR_FINGER_PRINT_INFO_CTRL_V50)
tagNET_DVR_FINGER_PRINT_INFO_CTRL_V50 = struct_tagNET_DVR_FINGER_PRINT_INFO_CTRL_V50
