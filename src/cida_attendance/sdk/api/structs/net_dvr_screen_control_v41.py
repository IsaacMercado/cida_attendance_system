from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX
from .net_dvr_screen_control_param import NET_DVR_SCREEN_CONTROL_PARAM


class struct_tagNET_DVR_SCREEN_CONTROL_V41(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_CONTROL_V41, [
    ('dwSize', DWORD),
    ('bySerialNo', BYTE),
    ('byRes', BYTE * 2),
    ('byProtocol', BYTE),
    ('dwCommand', DWORD),
    ('struControlParam', NET_DVR_SCREEN_CONTROL_PARAM),
    ('byWallNo', BYTE),
    ('byDevNo', BYTE),
    ('bySubboardNo', BYTE),
    ('byRes1', BYTE),
    ('struRect', NET_DVR_RECTCFG_EX),
    ('byRes2', BYTE * 28),
])

NET_DVR_SCREEN_CONTROL_V41 = struct_tagNET_DVR_SCREEN_CONTROL_V41
LPNET_DVR_SCREEN_CONTROL_V41 = POINTER(struct_tagNET_DVR_SCREEN_CONTROL_V41)
tagNET_DVR_SCREEN_CONTROL_V41 = struct_tagNET_DVR_SCREEN_CONTROL_V41
