from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DENSEFOGDETECTION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DENSEFOGDETECTION_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('bySensitivity', BYTE),
    ('byRes', BYTE * 258),
])

NET_DVR_DENSEFOGDETECTION_CFG = struct_tagNET_DVR_DENSEFOGDETECTION_CFG
LPNET_DVR_DENSEFOGDETECTION_CFG = POINTER(struct_tagNET_DVR_DENSEFOGDETECTION_CFG)
tagNET_DVR_DENSEFOGDETECTION_CFG = struct_tagNET_DVR_DENSEFOGDETECTION_CFG
