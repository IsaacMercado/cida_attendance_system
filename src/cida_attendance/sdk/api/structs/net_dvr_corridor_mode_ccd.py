from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CORRIDOR_MODE_CCD(Structure):
    pass

_S(struct_tagNET_DVR_CORRIDOR_MODE_CCD, [
    ('byEnableCorridorMode', BYTE),
    ('byRes', BYTE * 11),
])

NET_DVR_CORRIDOR_MODE_CCD = struct_tagNET_DVR_CORRIDOR_MODE_CCD
LPNET_DVR_CORRIDOR_MODE_CCD = POINTER(struct_tagNET_DVR_CORRIDOR_MODE_CCD)
tagNET_DVR_CORRIDOR_MODE_CCD = struct_tagNET_DVR_CORRIDOR_MODE_CCD
