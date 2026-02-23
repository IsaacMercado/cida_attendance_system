from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CONTROL_START_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CONTROL_START_CFG, [
    ('byUseDefine', BYTE),
    ('byRes1', BYTE),
    ('wCourseIndex', WORD),
    ('byRes', BYTE * 128),
])

NET_DVR_CONTROL_START_CFG = struct_tagNET_DVR_CONTROL_START_CFG
LPNET_DVR_CONTROL_START_CFG = POINTER(struct_tagNET_DVR_CONTROL_START_CFG)
tagNET_DVR_CONTROL_START_CFG = struct_tagNET_DVR_CONTROL_START_CFG
