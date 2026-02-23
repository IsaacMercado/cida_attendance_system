from ctypes import Structure, c_char

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LUN_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_LUN_PARAM, [
    ('dwHCapacity', DWORD),
    ('dwLCapacity', DWORD),
    ('szName', c_char * 16),
    ('dwBlockSize', DWORD),
    ('szArrayIDGroup', c_char * 32),
])

NET_DVR_LUN_PARAM = struct_tagNET_DVR_LUN_PARAM
LPNET_DVR_LUN_PARAM = POINTER(struct_tagNET_DVR_LUN_PARAM)
tagNET_DVR_LUN_PARAM = struct_tagNET_DVR_LUN_PARAM
