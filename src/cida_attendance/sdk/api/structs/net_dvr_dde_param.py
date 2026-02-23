from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DDE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_DDE_PARAM, [
    ('byMode', BYTE),
    ('byNormalLevel', BYTE),
    ('byExpertLevel', BYTE),
    ('byRes', BYTE * 5),
])

NET_DVR_DDE_PARAM = struct_tagNET_DVR_DDE_PARAM
LPNET_DVR_DDE_PARAM = POINTER(struct_tagNET_DVR_DDE_PARAM)
tagNET_DVR_DDE_PARAM = struct_tagNET_DVR_DDE_PARAM
