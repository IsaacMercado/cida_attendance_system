from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCKGATE_TIME_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCKGATE_TIME_CFG, [
    ('sBeginTime', c_char * 32),
    ('sEndTime', c_char * 32),
    ('byRes', BYTE * 64),
])

NET_DVR_LOCKGATE_TIME_CFG = struct_tagNET_DVR_LOCKGATE_TIME_CFG
LPNET_DVR_LOCKGATE_TIME_CFG = POINTER(struct_tagNET_DVR_LOCKGATE_TIME_CFG)
tagNET_DVR_LOCKGATE_TIME_CFG = struct_tagNET_DVR_LOCKGATE_TIME_CFG
