from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_IPSAN_SERACH_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_IPSAN_SERACH_PARAM, [
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes', BYTE * 10),
])

NET_DVR_IPSAN_SERACH_PARAM = struct_tagNET_DVR_IPSAN_SERACH_PARAM
LPNET_DVR_IPSAN_SERACH_PARAM = POINTER(struct_tagNET_DVR_IPSAN_SERACH_PARAM)
tagNET_DVR_IPSAN_SERACH_PARAM = struct_tagNET_DVR_IPSAN_SERACH_PARAM
