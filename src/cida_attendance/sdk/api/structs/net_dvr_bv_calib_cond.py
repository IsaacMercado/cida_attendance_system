from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BV_CALIB_COND(Structure):
    pass

_S(struct_tagNET_DVR_BV_CALIB_COND, [
    ('dwSize', DWORD),
    ('dwChannels', DWORD),
    ('byRes', BYTE * 300),
])

NET_DVR_BV_CALIB_COND = struct_tagNET_DVR_BV_CALIB_COND
LPNET_DVR_BV_CALIB_COND = POINTER(struct_tagNET_DVR_BV_CALIB_COND)
tagNET_DVR_BV_CALIB_COND = struct_tagNET_DVR_BV_CALIB_COND
