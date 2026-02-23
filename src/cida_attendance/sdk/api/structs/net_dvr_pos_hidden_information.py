from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POS_HIDDEN_INFORMATION(Structure):
    pass

_S(struct_tagNET_DVR_POS_HIDDEN_INFORMATION, [
    ('szKeyWord', (c_char * 128) * 3),
    ('byRes', BYTE * 128),
])

NET_DVR_POS_HIDDEN_INFORMATION = struct_tagNET_DVR_POS_HIDDEN_INFORMATION
LPNET_DVR_POS_HIDDEN_INFORMATION = POINTER(struct_tagNET_DVR_POS_HIDDEN_INFORMATION)
tagNET_DVR_POS_HIDDEN_INFORMATION = struct_tagNET_DVR_POS_HIDDEN_INFORMATION
