from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_bv_calib_param import NET_DVR_BV_CALIB_PARAM


class struct_tagNET_DVR_BV_CALIB_INFO(Structure):
    pass

_S(struct_tagNET_DVR_BV_CALIB_INFO, [
    ('dwSize', DWORD),
    ('dwBVCalibNumber', DWORD),
    ('struBVCalibParam', NET_DVR_BV_CALIB_PARAM * 12),
    ('dwHumanHeight', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 300),
])

NET_DVR_BV_CALIB_INFO = struct_tagNET_DVR_BV_CALIB_INFO
LPNET_DVR_BV_CALIB_INFO = POINTER(struct_tagNET_DVR_BV_CALIB_INFO)
tagNET_DVR_BV_CALIB_INFO = struct_tagNET_DVR_BV_CALIB_INFO
