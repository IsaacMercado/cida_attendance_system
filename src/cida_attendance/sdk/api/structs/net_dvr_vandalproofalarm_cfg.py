from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VANDALPROOFALARM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VANDALPROOFALARM_CFG, [
    ('dwSize', DWORD),
    ('bySensitivity', BYTE),
    ('byUploadEnabled', BYTE),
    ('byVoiceWarningEnabled', BYTE),
    ('byEnable', BYTE),
    ('byRes', BYTE * 124),
])

NET_DVR_VANDALPROOFALARM_CFG = struct_tagNET_DVR_VANDALPROOFALARM_CFG
LPNET_DVR_VANDALPROOFALARM_CFG = POINTER(struct_tagNET_DVR_VANDALPROOFALARM_CFG)
tagNET_DVR_VANDALPROOFALARM_CFG = struct_tagNET_DVR_VANDALPROOFALARM_CFG
