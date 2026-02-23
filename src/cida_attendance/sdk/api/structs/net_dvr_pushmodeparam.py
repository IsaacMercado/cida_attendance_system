from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PUSHMODEPARAM(Structure):
    pass

_S(struct_tagNET_DVR_PUSHMODEPARAM, [
    ('byUdpPreviewMode', BYTE),
    ('byVoiceWorkMode', BYTE),
    ('byRes', BYTE * 18),
])

NET_DVR_PUSHMODEPARAM = struct_tagNET_DVR_PUSHMODEPARAM
LPNET_DVR_PUSHMODEPARAM = POINTER(struct_tagNET_DVR_PUSHMODEPARAM)
tagNET_DVR_PUSHMODEPARAM = struct_tagNET_DVR_PUSHMODEPARAM
