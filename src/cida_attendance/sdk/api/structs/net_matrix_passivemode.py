from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_MATRIX_PASSIVEMODE(Structure):
    pass

_S(struct_tagNET_MATRIX_PASSIVEMODE, [
    ('wTransProtol', WORD),
    ('wPassivePort', WORD),
    ('struMcastIP', NET_DVR_IPADDR),
    ('byStreamType', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_MATRIX_PASSIVEMODE = struct_tagNET_MATRIX_PASSIVEMODE
LPNET_DVR_MATRIX_PASSIVEMODE = POINTER(struct_tagNET_MATRIX_PASSIVEMODE)
tagNET_MATRIX_PASSIVEMODE = struct_tagNET_MATRIX_PASSIVEMODE
