from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_SETUP_CALIB_COND(Structure):
    pass

_S(struct_tagNET_DVR_SETUP_CALIB_COND, [
    ('dwSize', DWORD),
    ('byCalibrateType', BYTE),
    ('byRes1', BYTE * 3),
    ('fTiltAngle', c_float),
    ('fHeelAngle', c_float),
    ('fHeight', c_float),
    ('struAutoCalibPolygon', NET_VCA_POLYGON),
    ('byIntelligentType', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_SETUP_CALIB_COND = struct_tagNET_DVR_SETUP_CALIB_COND
LPNET_DVR_SETUP_CALIB_COND = POINTER(struct_tagNET_DVR_SETUP_CALIB_COND)
tagNET_DVR_SETUP_CALIB_COND = struct_tagNET_DVR_SETUP_CALIB_COND
