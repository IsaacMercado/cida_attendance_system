from ctypes import Structure, c_char

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DVR_PARAM_(Structure):
    pass

_S(struct_tagNET_DVR_DVR_PARAM_, [
    ('dwHCapacity', DWORD),
    ('dwLCapacity', DWORD),
    ('szName', c_char * 16),
    ('dwBlockSize', DWORD),
    ('struWarrantIP', NET_DVR_IPADDR),
    ('szArrayIDGroup', c_char * 32),
])

NET_DVR_DVR_PARAM = struct_tagNET_DVR_DVR_PARAM_
LPNET_DVR_DVR_PARAM = POINTER(struct_tagNET_DVR_DVR_PARAM_)
tagNET_DVR_DVR_PARAM_ = struct_tagNET_DVR_DVR_PARAM_
