from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEN_VGA_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_VGA_CFG, [
    ('dwSize', DWORD),
    ('byEnableAutoAdjust', BYTE),
    ('byHorizontalPosition', BYTE),
    ('byVerticalPosition', BYTE),
    ('byClock', BYTE),
    ('byPhase', BYTE),
    ('byRes', BYTE * 11),
])

NET_DVR_SCREEN_VGA_CFG = struct_tagNET_DVR_SCREEN_VGA_CFG
LPNET_DVR_SCREEN_VGA_CFG = POINTER(struct_tagNET_DVR_SCREEN_VGA_CFG)
tagNET_DVR_SCREEN_VGA_CFG = struct_tagNET_DVR_SCREEN_VGA_CFG
