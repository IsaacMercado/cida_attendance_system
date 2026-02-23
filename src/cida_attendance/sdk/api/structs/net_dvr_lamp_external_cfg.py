from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_lamp_state import NET_DVR_LAMP_STATE


class struct_tagNET_DVR_LAMP_EXTERNAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LAMP_EXTERNAL_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struLampStateCtrl', NET_DVR_LAMP_STATE),
    ('byRes2', BYTE * 32),
])

NET_DVR_LAMP_EXTERNAL_CFG = struct_tagNET_DVR_LAMP_EXTERNAL_CFG
LPNET_DVR_LAMP_EXTERNAL_CFG = POINTER(struct_tagNET_DVR_LAMP_EXTERNAL_CFG)
tagNET_DVR_LAMP_EXTERNAL_CFG = struct_tagNET_DVR_LAMP_EXTERNAL_CFG
