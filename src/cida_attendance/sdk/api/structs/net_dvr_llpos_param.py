from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_lli_param import NET_DVR_LLI_PARAM


class struct_tagNET_DVR_LLPOS_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_LLPOS_PARAM, [
    ('byLatitudeType', BYTE),
    ('byLongitudeType', BYTE),
    ('byRes1', BYTE * 2),
    ('struLatitude', NET_DVR_LLI_PARAM),
    ('struLongitude', NET_DVR_LLI_PARAM),
    ('byRes', BYTE * 16),
])

NET_DVR_LLPOS_PARAM = struct_tagNET_DVR_LLPOS_PARAM
LPNET_DVR_LLPOS_PARAM = POINTER(struct_tagNET_DVR_LLPOS_PARAM)
tagNET_DVR_LLPOS_PARAM = struct_tagNET_DVR_LLPOS_PARAM
