from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SMARTIR_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SMARTIR_PARAM, [
    ('byMode', BYTE),
    ('byIRDistance', BYTE),
    ('byShortIRDistance', BYTE),
    ('byLongIRDistance', BYTE),
])

NET_DVR_SMARTIR_PARAM = struct_tagNET_DVR_SMARTIR_PARAM
LPNET_DVR_SMARTIR_PARAM = POINTER(struct_tagNET_DVR_SMARTIR_PARAM)
tagNET_DVR_SMARTIR_PARAM = struct_tagNET_DVR_SMARTIR_PARAM
