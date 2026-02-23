from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_calib_param import NET_DVR_CALIB_PARAM


class struct_tagNET_DVR_SLAVECAMERA_CALIB_V50(Structure):
    pass

_S(struct_tagNET_DVR_SLAVECAMERA_CALIB_V50, [
    ('dwSize', DWORD),
    ('byCalibMode', BYTE),
    ('byRes', BYTE * 3),
    ('struCalibParam', NET_DVR_CALIB_PARAM * 20),
    ('byRes1', BYTE * 64),
])

NET_DVR_SLAVECAMERA_CALIB_V50 = struct_tagNET_DVR_SLAVECAMERA_CALIB_V50
LPNET_DVR_SLAVECAMERA_CALIB_V50 = POINTER(struct_tagNET_DVR_SLAVECAMERA_CALIB_V50)
tagNET_DVR_SLAVECAMERA_CALIB_V50 = struct_tagNET_DVR_SLAVECAMERA_CALIB_V50
