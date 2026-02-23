from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_VCA_SUB_PROCIMG_V50(Structure):
    pass

_S(struct_tagNET_VCA_SUB_PROCIMG_V50, [
    ('dwImageLen', DWORD),
    ('dwFaceScore', DWORD),
    ('struVcaRect', NET_VCA_RECT),
    ('struLeftEyePoint', NET_VCA_POINT),
    ('struRightEyePoint', NET_VCA_POINT),
    ('byDistance', BYTE),
    ('bySex', BYTE),
    ('byAgeGroup', BYTE),
    ('byEyeGlass', BYTE),
    ('struPosRect', NET_VCA_RECT),
    ('byRes', BYTE * 20),
    ('pImage', POINTER(BYTE)),
])

NET_VCA_SUB_PROCIMG_V50 = struct_tagNET_VCA_SUB_PROCIMG_V50
LPNET_VCA_SUB_PROCIMG_V50 = POINTER(struct_tagNET_VCA_SUB_PROCIMG_V50)
tagNET_VCA_SUB_PROCIMG_V50 = struct_tagNET_VCA_SUB_PROCIMG_V50
