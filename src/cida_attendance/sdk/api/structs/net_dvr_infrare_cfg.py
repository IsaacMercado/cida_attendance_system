from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INFRARE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_INFRARE_CFG, [
    ('dwSize', DWORD),
    ('byIrControlMode', BYTE),
    ('byIrBrightness', BYTE),
    ('byIrSensitivity', BYTE),
    ('byIrTrigMode', BYTE),
    ('byIrBrightnessLimit', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_INFRARE_CFG = struct_tagNET_DVR_INFRARE_CFG
LPNET_DVR_INFRARE_CFG = POINTER(struct_tagNET_DVR_INFRARE_CFG)
tagNET_DVR_INFRARE_CFG = struct_tagNET_DVR_INFRARE_CFG
