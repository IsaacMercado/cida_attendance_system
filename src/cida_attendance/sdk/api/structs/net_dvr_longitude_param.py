from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LONGITUDE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_LONGITUDE_PARAM, [
    ('byDegree', BYTE),
    ('byMinute', BYTE),
    ('bySec', BYTE),
    ('byRes', BYTE),
])

NET_DVR_LONGITUDE_PARAM = struct_tagNET_DVR_LONGITUDE_PARAM
LPNET_DVR_LONGITUDE_PARAM = POINTER(struct_tagNET_DVR_LONGITUDE_PARAM)
tagNET_DVR_LONGITUDE_PARAM = struct_tagNET_DVR_LONGITUDE_PARAM
