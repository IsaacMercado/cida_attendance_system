from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BV_CALIB_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_BV_CALIB_RESULT, [
    ('dwSize', DWORD),
    ('dwCameraHeight', DWORD),
    ('fPitchAngle', c_float),
    ('fInclineAngle', c_float),
    ('byRes', BYTE * 300),
])

NET_DVR_BV_CALIB_RESULT = struct_tagNET_DVR_BV_CALIB_RESULT
LPNET_DVR_BV_CALIB_RESULT = POINTER(struct_tagNET_DVR_BV_CALIB_RESULT)
tagNET_DVR_BV_CALIB_RESULT = struct_tagNET_DVR_BV_CALIB_RESULT
