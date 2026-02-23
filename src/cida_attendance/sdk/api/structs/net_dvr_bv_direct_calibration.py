from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BV_DIRECT_CALIBRATION(Structure):
    pass

_S(struct_tagNET_DVR_BV_DIRECT_CALIBRATION, [
    ('dwCameraHeight', DWORD),
    ('fPitchAngle', c_float),
    ('fInclineAngle', c_float),
    ('byRes1', BYTE * 228),
])

NET_DVR_BV_DIRECT_CALIBRATION = struct_tagNET_DVR_BV_DIRECT_CALIBRATION
LPNET_DVR_BV_DIRECT_CALIBRATION = POINTER(struct_tagNET_DVR_BV_DIRECT_CALIBRATION)
tagNET_DVR_BV_DIRECT_CALIBRATION = struct_tagNET_DVR_BV_DIRECT_CALIBRATION
