from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZ_PARKACTION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PTZ_PARKACTION_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byOneTouchSwitch', BYTE),
    ('byRes1', BYTE * 2),
    ('dwParkTime', DWORD),
    ('wActionType', WORD),
    ('wID', WORD),
    ('byRes', BYTE * 128),
])

NET_DVR_PTZ_PARKACTION_CFG = struct_tagNET_DVR_PTZ_PARKACTION_CFG
LPNET_DVR_PTZ_PARKACTION_CFG = POINTER(struct_tagNET_DVR_PTZ_PARKACTION_CFG)
tagNET_DVR_PTZ_PARKACTION_CFG = struct_tagNET_DVR_PTZ_PARKACTION_CFG
