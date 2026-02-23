from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BV_SAMPLE_CALIB_BEGIN_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_BV_SAMPLE_CALIB_BEGIN_PARAM, [
    ('dwCameraHeight', DWORD),
    ('dwHumanHeight', DWORD),
    ('byRes', BYTE * 248),
])

NET_DVR_BV_SAMPLE_CALIB_BEGIN_PARAM = struct_tagNET_DVR_BV_SAMPLE_CALIB_BEGIN_PARAM
LPNET_DVR_BV_SAMPLE_CALIB_BEGIN_PARAM = POINTER(struct_tagNET_DVR_BV_SAMPLE_CALIB_BEGIN_PARAM)
tagNET_DVR_BV_SAMPLE_CALIB_BEGIN_PARAM = struct_tagNET_DVR_BV_SAMPLE_CALIB_BEGIN_PARAM
