from ctypes import Structure, c_float, c_int

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER


class struct_tagNET_SDK_NPQ_NOTIFY_PARAM(Structure):
    pass

_S(struct_tagNET_SDK_NPQ_NOTIFY_PARAM, [
    ('iVersion', LONG),
    ('dwBitRate', DWORD),
    ('bHaveBitrate', c_int),
    ('bHaveForceIframe', c_int),
    ('bForceIframe', c_int),
    ('bHaveScale', c_int),
    ('fScale', c_float),
    ('res', BYTE * 240),
])

NET_SDK_NPQ_NOTIFY_PARAM = struct_tagNET_SDK_NPQ_NOTIFY_PARAM
LPNET_SDK_NPQ_NOTIFY_PARAM = POINTER(struct_tagNET_SDK_NPQ_NOTIFY_PARAM)
tagNET_SDK_NPQ_NOTIFY_PARAM = struct_tagNET_SDK_NPQ_NOTIFY_PARAM
