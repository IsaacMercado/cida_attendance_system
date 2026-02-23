from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PLATE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_PLATE_PARAM, [
    ('byPlateRecoMode', BYTE),
    ('byBelive', BYTE),
    ('byRes', BYTE * 22),
])

NET_DVR_PALTE_PARAM = struct_tagNET_DVR_PLATE_PARAM
LPNET_DVR_PALTE_PARAM = POINTER(struct_tagNET_DVR_PLATE_PARAM)
tagNET_DVR_PLATE_PARAM = struct_tagNET_DVR_PLATE_PARAM
