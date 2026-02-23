from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct_tagNET_DVR_CALIBRATION(Structure):
    pass

_S(struct_tagNET_DVR_CALIBRATION, [
    ('dwSize', DWORD),
    ('struRegion', NET_VCA_POLYGON),
    ('byRes', BYTE * 64),
])

NET_DVR_CALIBRATION = struct_tagNET_DVR_CALIBRATION
LPNET_DVR_CALIBRATION = POINTER(struct_tagNET_DVR_CALIBRATION)
tagNET_DVR_CALIBRATION = struct_tagNET_DVR_CALIBRATION
