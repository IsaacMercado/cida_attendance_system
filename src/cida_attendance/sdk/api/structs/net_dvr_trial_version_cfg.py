from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TRIAL_VERSION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_TRIAL_VERSION_CFG, [
    ('dwSize', DWORD),
    ('wReserveTime', WORD),
    ('byRes', BYTE * 62),
])

NET_DVR_TRIAL_VERSION_CFG = struct_tagNET_DVR_TRIAL_VERSION_CFG
LPNET_DVR_TRIAL_VERSION_CFG = POINTER(struct_tagNET_DVR_TRIAL_VERSION_CFG)
tagNET_DVR_TRIAL_VERSION_CFG = struct_tagNET_DVR_TRIAL_VERSION_CFG
