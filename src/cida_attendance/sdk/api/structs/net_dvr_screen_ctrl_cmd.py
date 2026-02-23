from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_screen_ctrl_param import NET_DVR_SCREEN_CTRL_PARAM


class struct_tagNET_DVR_SCREEN_CTRL_CMD(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_CTRL_CMD, [
    ('dwSize', DWORD),
    ('byCmdType', BYTE),
    ('byRes1', BYTE * 3),
    ('struScreenCtrlParam', NET_DVR_SCREEN_CTRL_PARAM),
])

NET_DVR_SCREEN_CTRL_CMD = struct_tagNET_DVR_SCREEN_CTRL_CMD
LPNET_DVR_SCREEN_CTRL_CMD = POINTER(struct_tagNET_DVR_SCREEN_CTRL_CMD)
tagNET_DVR_SCREEN_CTRL_CMD = struct_tagNET_DVR_SCREEN_CTRL_CMD
