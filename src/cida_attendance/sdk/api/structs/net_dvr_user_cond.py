from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_USER_COND(Structure):
    pass

_S(struct_tagNET_DVR_USER_COND, [
    ('szUserName', c_char * 32),
    ('byRes', BYTE * 48),
])

NET_DVR_USER_COND = struct_tagNET_DVR_USER_COND
LPNET_DVR_USER_COND = POINTER(struct_tagNET_DVR_USER_COND)
tagNET_DVR_USER_COND = struct_tagNET_DVR_USER_COND
