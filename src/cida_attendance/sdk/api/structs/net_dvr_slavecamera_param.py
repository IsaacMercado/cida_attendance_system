from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SLAVECAMERA_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SLAVECAMERA_PARAM, [
    ('byLinkStatus', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_SLAVECAMERA_PARAM = struct_tagNET_DVR_SLAVECAMERA_PARAM
LPNET_DVR_SLAVECAMERA_PARAM = POINTER(struct_tagNET_DVR_SLAVECAMERA_PARAM)
tagNET_DVR_SLAVECAMERA_PARAM = struct_tagNET_DVR_SLAVECAMERA_PARAM
