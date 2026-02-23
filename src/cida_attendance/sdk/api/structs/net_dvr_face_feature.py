from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_FACE_FEATURE(Structure):
    pass

_S(struct_tagNET_DVR_FACE_FEATURE, [
    ('struFace', NET_VCA_RECT),
    ('struLeftEye', NET_VCA_POINT),
    ('struRightEye', NET_VCA_POINT),
    ('struLeftMouth', NET_VCA_POINT),
    ('struRightMouth', NET_VCA_POINT),
    ('struNoseTip', NET_VCA_POINT),
])

NET_DVR_FACE_FEATURE = struct_tagNET_DVR_FACE_FEATURE
LPNET_DVR_FACE_FEATURE = POINTER(struct_tagNET_DVR_FACE_FEATURE)
tagNET_DVR_FACE_FEATURE = struct_tagNET_DVR_FACE_FEATURE
