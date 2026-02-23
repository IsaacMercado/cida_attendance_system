from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STOP_LINE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_STOP_LINE_PARAM, [
    ('byStatus', BYTE),
    ('byRes', BYTE * 39),
])

NET_DVR_STOP_LINE_PARAM = struct_tagNET_DVR_STOP_LINE_PARAM
LPNET_DVR_STOP_LINE_PARAM = POINTER(struct_tagNET_DVR_STOP_LINE_PARAM)
tagNET_DVR_STOP_LINE_PARAM = struct_tagNET_DVR_STOP_LINE_PARAM
