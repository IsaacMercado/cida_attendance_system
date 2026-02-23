from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_lamp_ctrl_mode_union import NET_DVR_LAMP_CTRL_MODE_UNION


class struct_tagNET_DVR_LAMP_CTRL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_LAMP_CTRL_INFO, [
    ('dwSize', DWORD),
    ('byLampCtrlMode', BYTE),
    ('byCtrlChannelIndex', BYTE),
    ('byRes', BYTE * 2),
    ('uLampCtrlMode', NET_DVR_LAMP_CTRL_MODE_UNION),
    ('byRes2', BYTE * 32),
])

NET_DVR_LAMP_CTRL_INFO = struct_tagNET_DVR_LAMP_CTRL_INFO
LPNET_DVR_LAMP_CTRL_INFO = POINTER(struct_tagNET_DVR_LAMP_CTRL_INFO)
tagNET_DVR_LAMP_CTRL_INFO = struct_tagNET_DVR_LAMP_CTRL_INFO
