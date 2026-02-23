from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AGC_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_AGC_PARAM, [
    ('bySceneType', BYTE),
    ('byLightLevel', BYTE),
    ('byGainLevel', BYTE),
    ('byRes', BYTE * 5),
])

NET_DVR_AGC_PARAM = struct_tagNET_DVR_AGC_PARAM
LPNET_DVR_AGC_PARAM = POINTER(struct_tagNET_DVR_AGC_PARAM)
tagNET_DVR_AGC_PARAM = struct_tagNET_DVR_AGC_PARAM
