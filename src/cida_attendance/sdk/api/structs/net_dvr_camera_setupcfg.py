from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CAMERA_SETUPCFG(Structure):
    pass

_S(struct_tagNET_DVR_CAMERA_SETUPCFG, [
    ('dwSize', DWORD),
    ('wSetupHeight', WORD),
    ('byLensType', BYTE),
    ('bySetupHeightUnit', BYTE),
    ('dwSceneDis', DWORD),
    ('fPitchAngle', c_float),
    ('fInclineAngle', c_float),
    ('fRotateAngle', c_float),
    ('wVideoDetCoefficient', WORD),
    ('byErectMethod', BYTE),
    ('byCameraViewAngle', BYTE),
    ('dwHorizontalDistance', DWORD),
    ('byDetailLensType', BYTE),
    ('byRes', BYTE * 3),
    ('fHorFieldAngle', c_float),
    ('fVerFieldAngle', c_float),
    ('fLableSetupHeight', c_float),
    ('fMaxViewRadius', c_float),
    ('byRes1', BYTE * 16),
])

NET_DVR_CAMERA_SETUPCFG = struct_tagNET_DVR_CAMERA_SETUPCFG
LPNET_DVR_CAMERA_SETUPCFG = POINTER(struct_tagNET_DVR_CAMERA_SETUPCFG)
tagNET_DVR_CAMERA_SETUPCFG = struct_tagNET_DVR_CAMERA_SETUPCFG
