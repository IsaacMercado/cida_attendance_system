from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEN_FAN_WORK_MODE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_FAN_WORK_MODE_CFG, [
    ('dwSize', DWORD),
    ('byWorkMode', BYTE),
    ('byTemperatureLimitValue', BYTE),
    ('byRes', BYTE * 14),
])

NET_DVR_SCREEN_FAN_WORK_MODE_CFG = struct_tagNET_DVR_SCREEN_FAN_WORK_MODE_CFG
LPNET_DVR_SCREEN_FAN_WORK_MODE_CFG = POINTER(struct_tagNET_DVR_SCREEN_FAN_WORK_MODE_CFG)
tagNET_DVR_SCREEN_FAN_WORK_MODE_CFG = struct_tagNET_DVR_SCREEN_FAN_WORK_MODE_CFG
