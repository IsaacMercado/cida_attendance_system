from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POSTRADARPARAM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_POSTRADARPARAM_CFG, [
    ('dwSize', DWORD),
    ('bySoftWareVersion', BYTE * 32),
    ('byID', BYTE),
    ('byWorkMode', BYTE),
    ('bySpeedType', BYTE),
    ('byDirectionFilter', BYTE),
    ('dwAngleCorrect', DWORD),
    ('dwSensitivity', DWORD),
    ('dwSpeedLowLimit', DWORD),
    ('dwTrigDistance', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_POSTRADARPARAM_CFG = struct_tagNET_DVR_POSTRADARPARAM_CFG
LPNET_DVR_POSTRADARPARAM_CFG = POINTER(struct_tagNET_DVR_POSTRADARPARAM_CFG)
tagNET_DVR_POSTRADARPARAM_CFG = struct_tagNET_DVR_POSTRADARPARAM_CFG
