from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ACCESS_DEVICE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ACCESS_DEVICE_INFO, [
    ('dwSize', DWORD),
    ('byGroup', BYTE),
    ('byProType', BYTE),
    ('byAccessMode', BYTE),
    ('byRes1', BYTE),
    ('szUserName', c_char * 32),
    ('szPassword', c_char * 16),
    ('szDomain', c_char * 64),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('szGB28181DevID', BYTE * 32),
    ('byRes2', BYTE * 2),
])

NET_DVR_ACCESS_DEVICE_INFO = struct_tagNET_DVR_ACCESS_DEVICE_INFO
LPNET_DVR_ACCESS_DEVICE_INFO = POINTER(struct_tagNET_DVR_ACCESS_DEVICE_INFO)
tagNET_DVR_ACCESS_DEVICE_INFO = struct_tagNET_DVR_ACCESS_DEVICE_INFO
