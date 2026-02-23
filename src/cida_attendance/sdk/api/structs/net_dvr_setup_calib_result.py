from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_pdc_enter_direction import NET_DVR_PDC_ENTER_DIRECTION
from .net_vca_line import NET_VCA_LINE
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_SETUP_CALIB_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_SETUP_CALIB_RESULT, [
    ('dwSize', DWORD),
    ('byCalibrateType', BYTE),
    ('byRes1', BYTE * 3),
    ('fTiltAngle', c_float),
    ('fHeelAngle', c_float),
    ('fHeight', c_float),
    ('struCountPolygon', NET_VCA_POLYGON),
    ('struEnterDirection', NET_DVR_PDC_ENTER_DIRECTION),
    ('struLine', NET_VCA_LINE),
    ('byRes', BYTE * 128),
])

NET_DVR_SETUP_CALIB_RESULT = struct_tagNET_DVR_SETUP_CALIB_RESULT
LPNET_DVR_SETUP_CALIB_RESULT = POINTER(struct_tagNET_DVR_SETUP_CALIB_RESULT)
tagNET_DVR_SETUP_CALIB_RESULT = struct_tagNET_DVR_SETUP_CALIB_RESULT
