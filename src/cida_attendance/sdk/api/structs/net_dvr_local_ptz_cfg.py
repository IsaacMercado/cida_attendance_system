from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_PTZ_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_PTZ_CFG, [
    ('byWithoutRecv', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_LOCAL_PTZ_CFG = struct_tagNET_DVR_LOCAL_PTZ_CFG
LPNET_DVR_LOCAL_PTZ_CFG = POINTER(struct_tagNET_DVR_LOCAL_PTZ_CFG)
tagNET_DVR_LOCAL_PTZ_CFG = struct_tagNET_DVR_LOCAL_PTZ_CFG
