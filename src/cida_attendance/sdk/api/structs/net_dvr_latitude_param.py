from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LATITUDE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_LATITUDE_PARAM, [
    ('byDegree', BYTE),
    ('byMinute', BYTE),
    ('bySec', BYTE),
    ('byRes', BYTE),
])

NET_DVR_LATITUDE_PARAM = struct_tagNET_DVR_LATITUDE_PARAM
LPNET_DVR_LATITUDE_PARAM = POINTER(struct_tagNET_DVR_LATITUDE_PARAM)
tagNET_DVR_LATITUDE_PARAM = struct_tagNET_DVR_LATITUDE_PARAM
