from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_calib_param import NET_DVR_CALIB_PARAM


class struct_tagNET_DVR_SLAVECAMERA_CALIB_V51(Structure):
    pass

_S(struct_tagNET_DVR_SLAVECAMERA_CALIB_V51, [
    ('dwSize', DWORD),
    ('byCalibMode', BYTE),
    ('byRes', BYTE * 3),
    ('struCalibParam', NET_DVR_CALIB_PARAM * 20),
    ('byRes1', BYTE * 512),
])

NET_DVR_SLAVECAMERA_CALIB_V51 = struct_tagNET_DVR_SLAVECAMERA_CALIB_V51
LPNET_DVR_SLAVECAMERA_CALIB_V51 = POINTER(struct_tagNET_DVR_SLAVECAMERA_CALIB_V51)
tagNET_DVR_SLAVECAMERA_CALIB_V51 = struct_tagNET_DVR_SLAVECAMERA_CALIB_V51
