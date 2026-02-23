from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SMOKEDETECTION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SMOKEDETECTION_CFG, [
    ('byEnable', BYTE),
    ('bySensitivity', BYTE),
    ('byPatrolSensitivity', BYTE),
    ('byDoubleCheckSensitivity', BYTE),
    ('byRes', BYTE * 56),
])

NET_DVR_SMOKEDETECTION_CFG = struct_tagNET_DVR_SMOKEDETECTION_CFG
LPNET_DVR_SMOKEDETECTION_CFG = POINTER(struct_tagNET_DVR_SMOKEDETECTION_CFG)
tagNET_DVR_SMOKEDETECTION_CFG = struct_tagNET_DVR_SMOKEDETECTION_CFG
