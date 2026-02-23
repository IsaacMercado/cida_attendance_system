from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CORRECT_PARAMS(Structure):
    pass

_S(struct_tagNET_DVR_CORRECT_PARAMS, [
    ('byYellowIntervalTime', BYTE),
    ('byDigTrafficLight', BYTE),
    ('byRes', BYTE * 2),
])

NET_DVR_CORRECT_PARAMS = struct_tagNET_DVR_CORRECT_PARAMS
LPNET_DVR_CORRECT_PARAMS = POINTER(struct_tagNET_DVR_CORRECT_PARAMS)
tagNET_DVR_CORRECT_PARAMS = struct_tagNET_DVR_CORRECT_PARAMS
