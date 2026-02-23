from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_terminal_detail_ctrl_param import NET_DVR_TERMINAL_DETAIL_CTRL_PARAM


class struct_tagNET_DVR_TERMINAL_CTRL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_TERMINAL_CTRL_PARAM, [
    ('dwSize', DWORD),
    ('byOperateType', BYTE),
    ('byRes1', BYTE * 3),
    ('struCtrlParam', NET_DVR_TERMINAL_DETAIL_CTRL_PARAM),
    ('byRes2', BYTE * 32),
])

NET_DVR_TERMINAL_CTRL_PARAM = struct_tagNET_DVR_TERMINAL_CTRL_PARAM
LPNET_DVR_TERMINAL_CTRL_PARAM = POINTER(struct_tagNET_DVR_TERMINAL_CTRL_PARAM)
tagNET_DVR_TERMINAL_CTRL_PARAM = struct_tagNET_DVR_TERMINAL_CTRL_PARAM
