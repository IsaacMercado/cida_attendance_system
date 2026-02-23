from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_NET_DVR_UPLOAD_FACE_ANALYSIS_DATA_OUT(Structure):
    pass

_S(struct_NET_DVR_UPLOAD_FACE_ANALYSIS_DATA_OUT, [
    ('dwSize', DWORD),
    ('dwPID', DWORD),
    ('dwFaceAnalysisNum', DWORD),
    ('struVcaRect', NET_VCA_RECT * 32),
    ('byRes', BYTE * 128),
])

NET_DVR_UPLOAD_FACE_ANALYSIS_DATA_OUT = struct_NET_DVR_UPLOAD_FACE_ANALYSIS_DATA_OUT
LPNET_DVR_UPLOAD_FACE_ANALYSIS_DATA_OUT = POINTER(struct_NET_DVR_UPLOAD_FACE_ANALYSIS_DATA_OUT)
NET_DVR_UPLOAD_FACE_ANALYSIS_DATA_OUT = struct_NET_DVR_UPLOAD_FACE_ANALYSIS_DATA_OUT
