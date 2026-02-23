from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DEV_IP_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DEV_IP_INFO, [
    ('byUserName', BYTE * 32),
    ('byPassWord', BYTE * 16),
    ('struIPAddr', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes', BYTE * 24),
])

NET_DVR_DEV_IP_INFO = struct_tagNET_DVR_DEV_IP_INFO
LPNET_DVR_DEV_IP_INFO = POINTER(struct_tagNET_DVR_DEV_IP_INFO)
tagNET_DVR_DEV_IP_INFO = struct_tagNET_DVR_DEV_IP_INFO
