from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_buf_info import NET_DVR_BUF_INFO


class struct_tagNET_DVR_OUT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_OUT_PARAM, [
    ('struOutBuf', NET_DVR_BUF_INFO),
    ('lpStatusList', POINTER(None)),
    ('byRes', BYTE * 32),
])

NET_DVR_OUT_PARAM = struct_tagNET_DVR_OUT_PARAM
LPNET_DVR_OUT_PARAM = struct_tagNET_DVR_OUT_PARAM
tagNET_DVR_OUT_PARAM = struct_tagNET_DVR_OUT_PARAM
