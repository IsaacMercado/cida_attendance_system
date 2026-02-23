from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_SDK_SCREEN_CHECK_RESPONSE_DATA(Structure):
    pass

_S(struct_tagNET_SDK_SCREEN_CHECK_RESPONSE_DATA, [
    ('dwSize', DWORD),
    ('byDataType', BYTE),
    ('byOperateType', BYTE),
    ('byProgress', BYTE),
    ('byStatus', BYTE),
    ('struRect', NET_DVR_RECTCFG_EX),
    ('byRes', BYTE * 64),
])

NET_SDK_SCREEN_CHECK_RESPONSE_DATA = struct_tagNET_SDK_SCREEN_CHECK_RESPONSE_DATA
LPNET_SDK_SCREEN_CHECK_RESPONSE_DATA = POINTER(struct_tagNET_SDK_SCREEN_CHECK_RESPONSE_DATA)
tagNET_SDK_SCREEN_CHECK_RESPONSE_DATA = struct_tagNET_SDK_SCREEN_CHECK_RESPONSE_DATA
