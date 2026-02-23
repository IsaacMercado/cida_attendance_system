from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from .net_dvr_buf_info import NET_DVR_BUF_INFO


class struct_tagNET_DVR_IN_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_IN_PARAM, [
    ('struCondBuf', NET_DVR_BUF_INFO),
    ('struInParamBuf', NET_DVR_BUF_INFO),
    ('dwRecvTimeout', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_IN_PARAM = struct_tagNET_DVR_IN_PARAM
LPNET_DVR_IN_PARAM = struct_tagNET_DVR_IN_PARAM
tagNET_DVR_IN_PARAM = struct_tagNET_DVR_IN_PARAM
