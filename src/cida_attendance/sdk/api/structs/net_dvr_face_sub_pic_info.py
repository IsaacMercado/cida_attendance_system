from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_FACE_SUB_PIC_INFO(Structure):
    pass

_S(struct_tagNET_DVR_FACE_SUB_PIC_INFO, [
    ('dwSimilarity', DWORD),
    ('struVcaRect', NET_VCA_RECT),
    ('byRes2', BYTE * 236),
])

NET_DVR_FACE_SUB_PIC_INFO = struct_tagNET_DVR_FACE_SUB_PIC_INFO
LPNET_DVR_FACE_SUB_PIC_INFO = POINTER(struct_tagNET_DVR_FACE_SUB_PIC_INFO)
tagNET_DVR_FACE_SUB_PIC_INFO = struct_tagNET_DVR_FACE_SUB_PIC_INFO
