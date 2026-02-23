from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_ITS_CALIBRATION(Structure):
    pass

_S(struct_tagNET_DVR_ITS_CALIBRATION, [
    ('dwPointNum', DWORD),
    ('struPoint', NET_VCA_POINT * 4),
    ('fWidth', c_float),
    ('fHeight', c_float),
    ('byRes1', BYTE * 100),
])

NET_DVR_ITS_CALIBRATION = struct_tagNET_DVR_ITS_CALIBRATION
LPNET_DVR_ITS_CALIBRATION = POINTER(struct_tagNET_DVR_ITS_CALIBRATION)
tagNET_DVR_ITS_CALIBRATION = struct_tagNET_DVR_ITS_CALIBRATION
