from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_ptz_info import NET_PTZ_INFO


class struct_tagNET_DVR_BV_CALIB_POSITION(Structure):
    pass

_S(struct_tagNET_DVR_BV_CALIB_POSITION, [
    ('dwSize', DWORD),
    ('struInitialPos', NET_PTZ_INFO),
    ('struAdjustPos', NET_PTZ_INFO),
    ('byRes', BYTE * 300),
])

NET_DVR_BV_CALIB_POSITION = struct_tagNET_DVR_BV_CALIB_POSITION
LPNET_DVR_BV_CALIB_POSITION = POINTER(struct_tagNET_DVR_BV_CALIB_POSITION)
tagNET_DVR_BV_CALIB_POSITION = struct_tagNET_DVR_BV_CALIB_POSITION
