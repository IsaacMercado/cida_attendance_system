from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_ASYNC_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_ASYNC_CFG, [
    ('bEnable', c_int),
    ('byRes', BYTE * 60),
])

NET_DVR_LOCAL_ASYNC_CFG = struct_tagNET_DVR_LOCAL_ASYNC_CFG
LPNET_DVR_LOCAL_ASYNC_CFG = POINTER(struct_tagNET_DVR_LOCAL_ASYNC_CFG)
tagNET_DVR_LOCAL_ASYNC_CFG = struct_tagNET_DVR_LOCAL_ASYNC_CFG
