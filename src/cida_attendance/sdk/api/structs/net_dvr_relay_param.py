from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RELAY_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_RELAY_PARAM, [
    ('byAccessDevInfo', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_RELAY_PARAM = struct_tagNET_DVR_RELAY_PARAM
LPNET_DVR_RELAY_PARAM = POINTER(struct_tagNET_DVR_RELAY_PARAM)
tagNET_DVR_RELAY_PARAM = struct_tagNET_DVR_RELAY_PARAM
