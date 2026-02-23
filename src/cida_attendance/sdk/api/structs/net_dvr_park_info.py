from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PARK_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PARK_INFO, [
    ('sPlateNo', c_char * 32),
    ('sParkIndex', c_char * 32),
    ('byRes', BYTE * 64),
])

NET_DVR_PARK_INFO = struct_tagNET_DVR_PARK_INFO
LPNET_DVR_PARK_INFO = POINTER(struct_tagNET_DVR_PARK_INFO)
tagNET_DVR_PARK_INFO = struct_tagNET_DVR_PARK_INFO
