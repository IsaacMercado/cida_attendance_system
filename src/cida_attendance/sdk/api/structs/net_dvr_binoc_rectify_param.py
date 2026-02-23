from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BINOC_RECTIFY_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_BINOC_RECTIFY_PARAM, [
    ('fCamInternalMatrix', (c_float * 3) * 3),
    ('fDistCoeffs', c_float * 8),
    ('fRotateMatrix', (c_float * 3) * 3),
    ('fProjectMatrix', (c_float * 4) * 3),
    ('byRes', BYTE * 64),
])

NET_DVR_BINOC_RECTIFY_PARAM = struct_tagNET_DVR_BINOC_RECTIFY_PARAM
LPNET_DVR_BINOC_RECTIFY_PARAM = POINTER(struct_tagNET_DVR_BINOC_RECTIFY_PARAM)
tagNET_DVR_BINOC_RECTIFY_PARAM = struct_tagNET_DVR_BINOC_RECTIFY_PARAM
