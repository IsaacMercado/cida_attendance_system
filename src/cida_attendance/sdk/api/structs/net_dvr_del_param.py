from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DEL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_DEL_PARAM, [
    ('struIP', NET_DVR_IPADDR),
    ('byDelType', BYTE),
])

NET_DVR_DEL_PARAM = struct_tagNET_DVR_DEL_PARAM
LPNET_DVR_DEL_PARAM = POINTER(struct_tagNET_DVR_DEL_PARAM)
tagNET_DVR_DEL_PARAM = struct_tagNET_DVR_DEL_PARAM
