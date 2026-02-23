from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_FACE_PIC_DATA_INFO(Structure):
    pass

_S(struct_tagNET_DVR_FACE_PIC_DATA_INFO, [
    ('dwImageLen', DWORD),
    ('struVcaRect', NET_VCA_RECT),
    ('dwFaceScore', DWORD),
    ('byVcaRectOnly', BYTE),
    ('byRes1', BYTE * 3),
    ('dwPID', DWORD),
    ('dwFaceSearchNum', DWORD),
    ('struMultiVcaRect', NET_VCA_RECT * 5),
    ('byRes', BYTE * 136),
    ('pImage', POINTER(BYTE)),
])

NET_DVR_FACE_PIC_DATA_INFO = struct_tagNET_DVR_FACE_PIC_DATA_INFO
LPNET_DVR_FACE_PIC_DATA_INFO = POINTER(struct_tagNET_DVR_FACE_PIC_DATA_INFO)
tagNET_DVR_FACE_PIC_DATA_INFO = struct_tagNET_DVR_FACE_PIC_DATA_INFO
