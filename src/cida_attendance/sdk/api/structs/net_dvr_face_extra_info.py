from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_FACE_EXTRA_INFO(Structure):
    pass

_S(struct_tagNET_DVR_FACE_EXTRA_INFO, [
    ('struVcaRect', NET_VCA_RECT * 30),
    ('byRes', BYTE * 64),
])

NET_DVR_FACE_EXTRA_INFO = struct_tagNET_DVR_FACE_EXTRA_INFO
LPNET_DVR_FACE_EXTRA_INFO = POINTER(struct_tagNET_DVR_FACE_EXTRA_INFO)
tagNET_DVR_FACE_EXTRA_INFO = struct_tagNET_DVR_FACE_EXTRA_INFO
