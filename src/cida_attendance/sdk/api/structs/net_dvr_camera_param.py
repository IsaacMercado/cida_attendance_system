from ctypes import Structure, c_float

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CAMERA_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_CAMERA_PARAM, [
    ('byEnableHeight', BYTE),
    ('byEnableAngle', BYTE),
    ('byEnableHorizon', BYTE),
    ('byRes', BYTE * 5),
    ('fCameraHeight', c_float),
    ('fCameraAngle', c_float),
    ('fHorizon', c_float),
])

NET_DVR_CAMERA_PARAM = struct_tagNET_DVR_CAMERA_PARAM
LPNET_DVR_CAMERA_PARAM = POINTER(struct_tagNET_DVR_CAMERA_PARAM)
tagNET_DVR_CAMERA_PARAM = struct_tagNET_DVR_CAMERA_PARAM
