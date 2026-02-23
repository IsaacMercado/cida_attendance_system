from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_face_feature import NET_DVR_FACE_FEATURE


class struct_tagNET_DVR_CAPTURE_FACE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CAPTURE_FACE_CFG, [
    ('dwSize', DWORD),
    ('dwFaceTemplate1Size', DWORD),
    ('pFaceTemplate1Buffer', String),
    ('dwFaceTemplate2Size', DWORD),
    ('pFaceTemplate2Buffer', String),
    ('dwFacePicSize', DWORD),
    ('pFacePicBuffer', String),
    ('byFaceQuality1', BYTE),
    ('byFaceQuality2', BYTE),
    ('byCaptureProgress', BYTE),
    ('byFacePicQuality', BYTE),
    ('dwInfraredFacePicSize', DWORD),
    ('pInfraredFacePicBuffer', String),
    ('byInfraredFacePicQuality', BYTE),
    ('byRes1', BYTE * 3),
    ('struFeature', NET_DVR_FACE_FEATURE),
    ('byRes', BYTE * 56),
])

NET_DVR_CAPTURE_FACE_CFG = struct_tagNET_DVR_CAPTURE_FACE_CFG
LPNET_DVR_CAPTURE_FACE_CFG = POINTER(struct_tagNET_DVR_CAPTURE_FACE_CFG)
tagNET_DVR_CAPTURE_FACE_CFG = struct_tagNET_DVR_CAPTURE_FACE_CFG
