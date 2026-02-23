from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ADD_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_ADD_PARAM, [
    ('struIP', NET_DVR_IPADDR),
    ('szPassword', c_char * 16),
    ('byAddType', BYTE),
    ('byDisableBackup', BYTE),
])

NET_DVR_ADD_PARAM = struct_tagNET_DVR_ADD_PARAM
LPNET_DVR_ADD_PARAM = POINTER(struct_tagNET_DVR_ADD_PARAM)
tagNET_DVR_ADD_PARAM = struct_tagNET_DVR_ADD_PARAM
