from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_FACEDETECTION_SEARCHCOND(Structure):
    pass

_S(struct_tagNET_DVR_FACEDETECTION_SEARCHCOND, [
    ('struFacePolygon', NET_VCA_POLYGON),
    ('dwPreTime', DWORD),
    ('dwDelayTime', DWORD),
    ('byRes', BYTE * 5972),
])

NET_DVR_FACEDETECTION_SEARCHCOND = struct_tagNET_DVR_FACEDETECTION_SEARCHCOND
LPNET_DVR_FACEDETECTION_SEARCHCOND = POINTER(struct_tagNET_DVR_FACEDETECTION_SEARCHCOND)
tagNET_DVR_FACEDETECTION_SEARCHCOND = struct_tagNET_DVR_FACEDETECTION_SEARCHCOND
